<#
.SYNOPSIS
    Step 0 documentation retrofit for the MyBizz documentation corpus.

.DESCRIPTION
    Reads roots and path-based exceptions from the live scope authority, then
    plans frontmatter/LF changes for eligible Markdown files and register-table
    changes for every path listed in register-paths.md.

    The six register paths are read from the path-list file. Register conversion
    maps values by column name, preserves every row and all non-table content,
    and fails closed if a table cannot be parsed safely. The complete operation
    is preflighted before any corpus file is written.

    Dry-run is the default. A JSON report is written in both modes; without
    -ReportPath it is written beside this script.

.PARAMETER ScopeFile
    Full path to mybizz-scope-list.md.

.PARAMETER RegisterListFile
    Full path to register-paths.md, containing the six quoted register paths.

.PARAMETER SkipPath
    Optional Markdown file paths to omit from this invocation only. This does
    not add them to or remove them from the six-register list or scope authority.

.PARAMETER Parent
    Optional additional safety boundary. Every scope target, register, input,
    and report path must be under Parent or the run stops before applying.
    Omit this for the complete four-root retrofit.

.PARAMETER Apply
    Actually write planned changes. Without -Apply the script is dry-run only.

.PARAMETER ReportPath
    Optional path for a machine-readable JSON report. The report is written in
    dry-run and apply modes; it is not a corpus target.

.EXAMPLE
    .\retrofit-step0.ps1 `
      -ScopeFile 'C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md' `
      -RegisterListFile 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\register-paths.md'

.EXAMPLE
    .\retrofit-step0.ps1 `
      -ScopeFile 'C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md' `
      -RegisterListFile 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\register-paths.md' `
      -Apply
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ScopeFile,

    [Parameter(Mandatory = $true)]
    [string]$RegisterListFile,

    [string[]]$SkipPath,

    [string]$Parent,

    [switch]$Apply,

    [string]$ReportPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Changes = [System.Collections.Generic.List[object]]::new()
$script:Errors = [System.Collections.Generic.List[object]]::new()
$script:Warnings = [System.Collections.Generic.List[object]]::new()
$script:PendingWrites = [System.Collections.Generic.List[object]]::new()

function Normalize-Path([string]$Path) {
    $full = [System.IO.Path]::GetFullPath($Path)
    $root = [System.IO.Path]::GetPathRoot($full)
    if ($full.Length -gt $root.Length) {
        return $full.TrimEnd([char[]]@([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar))
    }
    return $full
}

function Is-UnderPath([string]$Candidate, [string]$Root) {
    $candidateFull = Normalize-Path $Candidate
    $rootFull = Normalize-Path $Root
    if ($candidateFull.Equals($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $true
    }
    $separator = [System.IO.Path]::DirectorySeparatorChar
    $prefix = if ($rootFull.EndsWith([string]$separator)) { $rootFull } else { $rootFull + $separator }
    return $candidateFull.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)
}

function Assert-ParentBoundary([string]$Path) {
    if (-not [string]::IsNullOrWhiteSpace($Parent) -and -not (Is-UnderPath $Path $Parent)) {
        throw "SAFETY STOP: path is outside -Parent '$Parent': $Path"
    }
}

function Assert-NoReparseAncestor([string]$Path) {
    $current = Normalize-Path $Path
    while ($current) {
        if (Test-Path -LiteralPath $current) {
            $item = Get-Item -LiteralPath $current -Force
            if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "Filesystem link in path; refusing to read or write through it: $current"
            }
        }
        $parentPath = Split-Path -Parent $current
        if (-not $parentPath -or $parentPath -eq $current) { break }
        $current = Normalize-Path $parentPath
    }
}

function Convert-ToLf([string]$Text) {
    return $Text.Replace("`r`n", "`n").Replace("`r", "`n")
}

function Read-TextStrict([string]$Path) {
    $bytes = [System.IO.File]::ReadAllBytes($Path)
    $encoding = [System.Text.UTF8Encoding]::new($false, $true)
    $text = $encoding.GetString($bytes)
    if ($text.Length -gt 0 -and $text[0] -eq [char]0xFEFF) {
        $text = $text.Substring(1)
    }
    if ($text.IndexOf([char]0) -ge 0) {
        throw "Null byte found; refusing to treat this as a Markdown document: $Path"
    }
    return $text
}

function Get-Utf8NoBom([string]$Text) {
    return [System.Text.UTF8Encoding]::new($false, $true).GetBytes($Text)
}

function Escape-YamlString([string]$Value) {
    return '"' + $Value.Replace('\', '\\').Replace('"', '\"') + '"'
}

function Get-FrontmatterReplacement([string]$Path, [string]$Text) {
    $normalized = Convert-ToLf $Text
    $lines = @($normalized -split "`n")
    $firstContent = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if (-not [string]::IsNullOrWhiteSpace($lines[$i])) {
            $firstContent = $i
            break
        }
    }
    $bodyLines = if ($firstContent -lt 0) { @() } else { $lines }
    if ($firstContent -ge 0 -and $lines[$firstContent].Trim() -eq '---') {
        $close = -1
        for ($i = $firstContent + 1; $i -lt $lines.Count; $i++) {
            if ($lines[$i].Trim() -eq '---') {
                $close = $i
                break
            }
        }
        if ($close -lt 0) {
            throw "Frontmatter opens but has no closing fence: $Path"
        }
        $bodyLines = if ($close + 1 -lt $lines.Count) { @($lines[($close + 1)..($lines.Count - 1)]) } else { @() }
    }
    elseif ($firstContent -ge 0 -and $lines[$firstContent] -match '^\s*---') {
        throw "Malformed frontmatter opening fence: $Path"
    }

    $body = Convert-ToLf (($bodyLines -join "`n") -replace '^\n+', '')
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($Path)
    $frontmatter = "---`n" +
                   'title: ' + (Escape-YamlString $stem) + "`n" +
                   'doc-id: ' + (Escape-YamlString $stem) + "`n" +
                   "---`n"
    return $frontmatter + $body
}

function Is-TreatmentExempt([string]$Path) {
    $parts = (Normalize-Path $Path).Split([System.IO.Path]::DirectorySeparatorChar)
    foreach ($part in $parts) {
        $lower = $part.ToLowerInvariant()
        if ($lower -eq 'stencils' -or $lower -eq 'quarantine' -or
            $lower -eq 'backup' -or $lower -eq 'catalogue' -or
            $lower.StartsWith('tmp-')) {
            return $true
        }
    }
    return $false
}

function Is-ScopeException([string]$Path, $Scope) {
    $full = Normalize-Path $Path
    foreach ($exception in $Scope.ExplicitExceptions) {
        if (Is-UnderPath $full $exception) {
            return $true
        }
    }

    $parts = @($full.Split([System.IO.Path]::DirectorySeparatorChar))
    if (Test-Path -LiteralPath $full -PathType Leaf) {
        $parts = if ($parts.Count -gt 1) { @($parts[0..($parts.Count - 2)]) } else { @() }
    }
    foreach ($part in $parts) {
        $name = $part.ToLowerInvariant()
        foreach ($pattern in $Scope.DynamicFolderPatterns) {
            if ($name -eq $pattern) { return $true }
            if ($pattern.Contains('*')) {
                $escapedPattern = [System.Text.RegularExpressions.Regex]::Escape($pattern)
                $regex = '^' + $escapedPattern.Replace('\*', '.*') + '$'
                if ($name -match $regex) { return $true }
            }
        }
    }
    return $false
}

function Parse-ScopeFile([string]$Path) {
    $text = Convert-ToLf (Read-TextStrict $Path)
    $lines = $text -split "`n"
    $roots = [System.Collections.Generic.List[string]]::new()
    $exceptions = [System.Collections.Generic.List[string]]::new()
    $inRoots = $false
    $inExceptions = $false

    foreach ($line in $lines) {
        $trim = $line.Trim()
        if ($trim -eq '**In scope:**') {
            $inRoots = $true
            $inExceptions = $false
            continue
        }
        if ($trim -like '**Exceptions*') {
            $inRoots = $false
            $inExceptions = $true
            continue
        }
        if ($trim -match '^"([^"]+)"(?:\s+.*)?$') {
            if ($inRoots) { $roots.Add($Matches[1].Replace('\\', '\')) }
            elseif ($inExceptions) { $exceptions.Add($Matches[1].Replace('\\', '\')) }
        }
    }

    if ($roots.Count -eq 0) {
        throw "No quoted scope roots found in scope authority: $Path"
    }

    $normalizedText = [System.Text.RegularExpressions.Regex]::Replace($text, '\s+', ' ')
    $dynamicPatterns = [System.Collections.Generic.List[string]]::new()
    foreach ($match in [System.Text.RegularExpressions.Regex]::Matches($normalizedText, '(?i)any folder named (.+?), at any depth')) {
        $names = $match.Groups[1].Value -split '\s*,\s*|\s+or\s+'
        foreach ($name in $names) {
            $pattern = $name.Trim().TrimEnd('.').ToLowerInvariant()
            if ($pattern -and -not $dynamicPatterns.Contains($pattern)) {
                $dynamicPatterns.Add($pattern)
            }
        }
    }
    if ($dynamicPatterns.Count -eq 0) {
        throw "Could not read the named-folder scope exceptions from: $Path"
    }

    return [pscustomobject]@{
        Roots = @($roots | ForEach-Object { Normalize-Path $_ } | Sort-Object -Unique)
        ExplicitExceptions = @($exceptions | ForEach-Object { Normalize-Path $_ } | Sort-Object -Unique)
        DynamicFolderPatterns = @($dynamicPatterns)
    }
}

function Test-IsDotFolder([string]$Path) {
    foreach ($part in (Normalize-Path $Path).Split([System.IO.Path]::DirectorySeparatorChar)) {
        if ($part.Length -gt 1 -and $part.StartsWith('.')) { return $true }
    }
    return $false
}

function Test-IsVersionControlFolder([string]$Path) {
    foreach ($part in (Normalize-Path $Path).Split([System.IO.Path]::DirectorySeparatorChar)) {
        if ($part -in @('.git', '.svn', '.hg', '.bzr')) { return $true }
    }
    return $false
}

function Has-AnvilYaml([string]$Directory) {
    return Test-Path -LiteralPath (Join-Path $Directory 'anvil.yaml') -PathType Leaf
}

function Assert-NoAnvilAncestor([string]$Path) {
    $current = if (Test-Path -LiteralPath $Path -PathType Container) { Normalize-Path $Path } else { Split-Path -Parent (Normalize-Path $Path) }
    while ($current) {
        if (Has-AnvilYaml $current) {
            throw "Path is inside a directory containing anvil.yaml; refusing to process it: $Path"
        }
        $parentPath = Split-Path -Parent $current
        if (-not $parentPath -or $parentPath -eq $current) { break }
        $current = Normalize-Path $parentPath
    }
}

function Get-EligibleMarkdownFiles($Scope, [string[]]$RegisterPaths, [string[]]$SkipPaths) {
    $files = [System.Collections.Generic.List[string]]::new()
    $registerSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $skipSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    foreach ($registerPath in $RegisterPaths) { [void]$registerSet.Add((Normalize-Path $registerPath)) }
    foreach ($skipPath in $SkipPaths) { [void]$skipSet.Add((Normalize-Path $skipPath)) }

    foreach ($root in $Scope.Roots) {
        if (-not (Test-Path -LiteralPath $root -PathType Container)) {
            throw "Scope root does not exist or is not a directory: $root"
        }
        $rootItem = Get-Item -LiteralPath $root -Force
        if (($rootItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Scope root is a filesystem link; refusing to traverse it: $root"
        }

        $stack = [System.Collections.Generic.Stack[string]]::new()
        $stack.Push((Normalize-Path $root))
        while ($stack.Count -gt 0) {
            $directory = $stack.Pop()
            if ((Is-ScopeException $directory $Scope) -or
                (Is-TreatmentExempt $directory) -or
                (Test-IsDotFolder $directory) -or
                (Test-IsVersionControlFolder $directory) -or
                (Has-AnvilYaml $directory)) {
                continue
            }

            foreach ($file in Get-ChildItem -LiteralPath $directory -File -Force) {
                $fullPath = Normalize-Path $file.FullName
                if (($file.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { continue }
                if ((Is-ScopeException $fullPath $Scope) -or
                    (Is-TreatmentExempt $fullPath) -or
                    $registerSet.Contains($fullPath) -or
                    $skipSet.Contains($fullPath)) {
                    continue
                }
                if ($file.Extension -ieq '.md') {
                    $files.Add($fullPath)
                }
            }

            foreach ($child in Get-ChildItem -LiteralPath $directory -Directory -Force) {
                $childPath = Normalize-Path $child.FullName
                if (($child.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { continue }
                if ((Is-ScopeException $childPath $Scope) -or
                    (Is-TreatmentExempt $childPath) -or
                    (Test-IsDotFolder $childPath) -or
                    (Test-IsVersionControlFolder $childPath) -or
                    (Has-AnvilYaml $childPath)) {
                    continue
                }
                $stack.Push($childPath)
            }
        }
    }
    return @($files | Sort-Object -Unique)
}

function Read-RegisterPaths([string]$Path, $Scope) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Register path list does not exist: $Path"
    }
    $paths = [System.Collections.Generic.List[string]]::new()
    $registerListText = Convert-ToLf (Read-TextStrict $Path)
    foreach ($line in ($registerListText -split "`n")) {
        if ($line -match '^\s*"([^"]+)"\s*$') {
            $value = $Matches[1].Replace('\\', '\')
            $paths.Add((Normalize-Path $value))
        }
    }
    if ($paths.Count -ne 6) {
        throw "Expected exactly six quoted register paths in '$Path'; found $($paths.Count)."
    }
    $unique = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    foreach ($register in $paths) {
        if (-not $unique.Add($register)) { throw "Duplicate register path in '$Path': $register" }
        if (-not (Test-Path -LiteralPath $register -PathType Leaf)) { throw "Register does not exist: $register" }
        Assert-NoReparseAncestor $register
        Assert-NoAnvilAncestor $register
        if ([System.IO.Path]::GetExtension($register) -ine '.md') { throw "Register is not a Markdown file: $register" }
        if (-not (@($Scope.Roots | Where-Object { Is-UnderPath $register $_ }).Count -gt 0)) {
            throw "Register is outside every scope root: $register"
        }
        if ((Is-ScopeException $register $Scope) -or (Is-TreatmentExempt $register)) {
            throw "Register path falls under a scope or Step 0 exemption: $register"
        }
        $item = Get-Item -LiteralPath $register -Force
        if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Register is a filesystem link; refusing to write it: $register"
        }
    }
    return @($paths)
}

function Split-MarkdownRow([string]$Line) {
    $row = $Line.Trim()
    if ($row.StartsWith('|')) { $row = $row.Substring(1) }
    if ($row.EndsWith('|')) {
        $slashCount = 0
        for ($index = $row.Length - 2; $index -ge 0 -and $row[$index] -eq [char]'\'; $index--) { $slashCount++ }
        if (($slashCount % 2) -eq 0) { $row = $row.Substring(0, $row.Length - 1) }
    }

    $cells = [System.Collections.Generic.List[string]]::new()
    $cell = [System.Text.StringBuilder]::new()
    $inCode = $false
    for ($index = 0; $index -lt $row.Length; $index++) {
        $character = $row[$index]
        if ($character -eq [char]'`') {
            $inCode = -not $inCode
            [void]$cell.Append($character)
            continue
        }
        if ($character -eq [char]'\' -and $index + 1 -lt $row.Length) {
            $next = $row[$index + 1]
            if ($next -eq [char]'|' -or $next -eq [char]'\') {
                [void]$cell.Append($next)
                $index++
                continue
            }
        }
        if ($character -eq [char]'|' -and -not $inCode) {
            $cells.Add($cell.ToString().Trim())
            [void]$cell.Clear()
            continue
        }
        [void]$cell.Append($character)
    }
    $cells.Add($cell.ToString().Trim())
    return $cells.ToArray()
}

function Escape-MarkdownCell([string]$Value) {
    if ($null -eq $Value) { return '' }
    if ($Value.Contains("`n") -or $Value.Contains("`r")) {
        throw 'Multiline register cells cannot be represented safely in a Markdown table.'
    }
    $escaped = [System.Text.StringBuilder]::new()
    foreach ($character in $Value.Trim().ToCharArray()) {
        if ($character -eq [char]'\' -or $character -eq [char]'|') { [void]$escaped.Append([char]'\') }
        [void]$escaped.Append($character)
    }
    return $escaped.ToString()
}

function Get-BareFilename([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { return '' }
    $normalized = $Value.Replace('/', '\').TrimEnd([char]'\')
    $parts = $normalized.Split([char]'\')
    return $parts[$parts.Length - 1]
}

function Get-RegisterReplacement([string]$Path, [string]$Text) {
    $normalized = Get-FrontmatterReplacement $Path (Convert-ToLf $Text)
    $lines = @($normalized -split "`n")
    $headerIndex = -1
    $headers = @()
    $separatorIndex = -1

    for ($lineIndex = 0; $lineIndex -lt $lines.Count - 1; $lineIndex++) {
        if (-not $lines[$lineIndex].Trim().StartsWith('|')) { continue }
        $candidateHeaders = @(Split-MarkdownRow $lines[$lineIndex])
        if ($candidateHeaders.Count -lt 2) { continue }
        $names = @($candidateHeaders | ForEach-Object { $_.Trim().ToLowerInvariant() })
        if ($names -notcontains 'doc-id' -or ($names -notcontains 'filename' -and $names -notcontains 'title')) { continue }

        $candidateSeparator = @(Split-MarkdownRow $lines[$lineIndex + 1])
        if ($candidateSeparator.Count -ne $names.Count -or
            @($candidateSeparator | Where-Object { $_ -notmatch '^:?-{3,}:?$' }).Count -gt 0) {
            throw "Register table has an invalid separator row: $Path (line $($lineIndex + 2))"
        }
        $headerIndex = $lineIndex
        $separatorIndex = $lineIndex + 1
        $headers = $names
        break
    }
    if ($headerIndex -lt 0) { throw "No supported doc-id/filename register table found: $Path" }

    $column = @{}
    for ($i = 0; $i -lt $headers.Count; $i++) {
        if ($column.ContainsKey($headers[$i])) { throw "Duplicate register column '$($headers[$i])': $Path" }
        $column[$headers[$i]] = $i
    }
    if (-not $column.ContainsKey('state')) { throw "Register has no state column: $Path" }
    $titleKey = if ($column.ContainsKey('filename')) { 'filename' } else { 'title' }
    $notesIndex = if ($column.ContainsKey('notes')) { $column['notes'] } else { -1 }
    $rows = [System.Collections.Generic.List[object]]::new()
    $between = [System.Collections.Generic.List[string]]::new()
    $suffixIndex = $lines.Count

    for ($lineIndex = $separatorIndex + 1; $lineIndex -lt $lines.Count; $lineIndex++) {
        $trimmed = $lines[$lineIndex].Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed) -or $trimmed.StartsWith('<!--')) {
            $between.Add($lines[$lineIndex])
            continue
        }
        if (-not $trimmed.StartsWith('|')) {
            $suffixIndex = $lineIndex
            break
        }

        $cells = @(Split-MarkdownRow $lines[$lineIndex])
        if ($cells.Count -eq $headers.Count + 1 -and [string]::IsNullOrWhiteSpace($cells[$cells.Count - 1])) {
            $cells = @($cells[0..($cells.Count - 2)])
        }
        if ($cells.Count -lt 2) {
            throw "Register row has fewer than doc-id and filename/title cells: $Path (line $($lineIndex + 1))"
        }
        if ($cells.Count -lt $headers.Count) {
            $paddedCells = [System.Collections.Generic.List[string]]::new()
            foreach ($cell in $cells) { $paddedCells.Add($cell) }
            while ($paddedCells.Count -lt $headers.Count) { $paddedCells.Add('') }
            $cells = $paddedCells.ToArray()
        }
        if ($cells.Count -gt $headers.Count) {
            if ($notesIndex -ne $headers.Count - 1) { throw "Register row has extra cells but notes is not the final column: $Path (line $($lineIndex + 1))" }
            $notesParts = @($cells[$notesIndex..($cells.Count - 1)])
            $cells = @($cells[0..($notesIndex - 1)]) + @(($notesParts -join '|'))
        }

        $docId = $cells[$column['doc-id']]
        $filename = Get-BareFilename $cells[$column[$titleKey]]
        if ([string]::IsNullOrWhiteSpace($filename)) {
            throw "Register row has no filename/title value: $Path (line $($lineIndex + 1))"
        }
        $state = $cells[$column['state']]
        $supersededBy = if ($column.ContainsKey('superseded-by')) { $cells[$column['superseded-by']] } else { '' }
        $notes = if ($notesIndex -ge 0) { $cells[$notesIndex] } else { '' }
        $rows.Add([pscustomobject]@{
            DocId = $docId
            Title = $filename
            State = $state
            SupersededBy = $supersededBy
            Notes = $notes
        })
    }

    if ($rows.Count -eq 0) { throw "Register table contains no data rows: $Path" }

    $output = [System.Collections.Generic.List[string]]::new()
    for ($i = 0; $i -lt $headerIndex; $i++) { $output.Add($lines[$i]) }
    $output.Add('| doc-id | title | state | superseded-by | notes |')
    $output.Add('| --- | --- | --- | --- | --- |')
    foreach ($row in $rows) {
        $escapedCells = [string[]]@('', '', '', '', '')
        $escapedCells[0] = [string](Escape-MarkdownCell $row.DocId)
        $escapedCells[1] = [string](Escape-MarkdownCell $row.Title)
        $escapedCells[2] = [string](Escape-MarkdownCell $row.State)
        $escapedCells[3] = [string](Escape-MarkdownCell $row.SupersededBy)
        $escapedCells[4] = [string](Escape-MarkdownCell $row.Notes)
        $output.Add('| ' + [string]::Join(' | ', $escapedCells) + ' |')
    }
    foreach ($line in $between) { $output.Add($line) }
    for ($i = $suffixIndex; $i -lt $lines.Count; $i++) { $output.Add($lines[$i]) }
    $result = $output -join "`n"
    while ($result.EndsWith("`n")) { $result = $result.Substring(0, $result.Length - 1) }
    return (Convert-ToLf $result) + "`n"
}

function Add-Error([string]$Path, [string]$Message) {
    $script:Errors.Add([pscustomobject]@{ Path = $Path; Error = $Message })
}

function Add-PlannedWrite([string]$Path, [string]$OldText, [string]$NewText, [string]$Reason) {
    $oldBytes = [System.IO.File]::ReadAllBytes($Path)
    $newBytes = Get-Utf8NoBom $NewText
    if (-not [System.Linq.Enumerable]::SequenceEqual([byte[]]$oldBytes, [byte[]]$newBytes)) {
        $script:Changes.Add([pscustomobject]@{ Path = $Path; Action = 'UPDATE'; Reason = $Reason })
        $script:PendingWrites.Add([pscustomobject]@{ Path = $Path; Bytes = $newBytes })
    }
}

$scopeFull = Normalize-Path $ScopeFile
$registerListFull = Normalize-Path $RegisterListFile
if (-not (Test-Path -LiteralPath $scopeFull -PathType Leaf)) { throw "Scope file does not exist: $scopeFull" }
if (-not (Test-Path -LiteralPath $registerListFull -PathType Leaf)) { throw "Register path list does not exist: $registerListFull" }
Assert-ParentBoundary $scopeFull
Assert-ParentBoundary $registerListFull
Assert-NoReparseAncestor $scopeFull
Assert-NoReparseAncestor $registerListFull

$scope = Parse-ScopeFile $scopeFull
$registerPaths = Read-RegisterPaths $registerListFull $scope
$skipPaths = [System.Collections.Generic.List[string]]::new()
$skipPathSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
foreach ($requestedSkipPath in $SkipPath) {
    $skipFull = Normalize-Path $requestedSkipPath
    if (-not (Test-Path -LiteralPath $skipFull -PathType Leaf)) {
        throw "SkipPath does not exist or is not a file: $skipFull"
    }
    if ([System.IO.Path]::GetExtension($skipFull) -ine '.md') {
        throw "SkipPath must identify a Markdown file: $skipFull"
    }
    Assert-ParentBoundary $skipFull
    Assert-NoReparseAncestor $skipFull
    if (-not (@($scope.Roots | Where-Object { Is-UnderPath $skipFull $_ }).Count -gt 0)) {
        throw "SkipPath is outside every scope root: $skipFull"
    }
    if (@($registerPaths | Where-Object { (Normalize-Path $_).Equals($skipFull, [System.StringComparison]::OrdinalIgnoreCase) }).Count -gt 0) {
        throw "SkipPath cannot also be one of the six register paths: $skipFull"
    }
    if (-not $skipPathSet.Add($skipFull)) { throw "Duplicate SkipPath: $skipFull" }
    $skipPaths.Add($skipFull)
}
$markdownFiles = Get-EligibleMarkdownFiles $scope $registerPaths @($skipPaths)

foreach ($file in $markdownFiles) {
    try {
        Assert-ParentBoundary $file
        Assert-NoReparseAncestor $file
        $oldText = Read-TextStrict $file
        $newText = Get-FrontmatterReplacement $file $oldText
        $closingFence = $newText.IndexOf("`n---`n", 3)
        $bodyAfterFrontmatter = if ($closingFence -ge 0) { $newText.Substring($closingFence + 5) } else { '' }
        if ([string]::IsNullOrWhiteSpace($bodyAfterFrontmatter)) {
            $script:Warnings.Add([pscustomobject]@{
                Path = $file
                Warning = 'Empty placeholder received filename-derived frontmatter only; GBrain will have no body chunks until content is added.'
            })
        }
        Add-PlannedWrite $file $oldText $newText 'Set exact two-field frontmatter and LF line endings'
    }
    catch {
        Add-Error $file $_.Exception.Message
    }
}

foreach ($register in $registerPaths) {
    try {
        Assert-ParentBoundary $register
        Assert-NoReparseAncestor $register
        $oldText = Read-TextStrict $register
        $newText = Get-RegisterReplacement $register $oldText
        Add-PlannedWrite $register $oldText $newText 'Set exact frontmatter, convert register to five columns, and normalize LF'
    }
    catch {
        Add-Error $register $_.Exception.Message
    }
}

if (-not $ReportPath) {
    $ReportPath = Join-Path $PSScriptRoot ("retrofit-report-{0}.json" -f (Get-Date -Format 'yyyyMMdd-HHmmss'))
}
$reportFull = Normalize-Path $ReportPath
Assert-ParentBoundary $reportFull
Assert-NoReparseAncestor $reportFull
if (-not (Test-Path -LiteralPath (Split-Path -Parent $reportFull) -PathType Container)) {
    throw "Report directory does not exist: $(Split-Path -Parent $reportFull)"
}
if (Test-Path -LiteralPath $reportFull) {
    throw "Report file already exists; choose a new -ReportPath to avoid overwriting it: $reportFull"
}
foreach ($targetPath in @($scopeFull, $registerListFull) + @($markdownFiles) + @($registerPaths) + @($skipPaths)) {
    if ((Normalize-Path $targetPath).Equals($reportFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Report path collides with a scope input or retrofit target: $reportFull"
    }
}

$mode = if ($Apply) { 'APPLY' } else { 'DRY-RUN' }
$writeErrors = [System.Collections.Generic.List[object]]::new()
if ($Apply -and $script:Errors.Count -eq 0) {
    foreach ($plan in $script:PendingWrites) {
        try {
            [System.IO.File]::WriteAllBytes($plan.Path, [byte[]]$plan.Bytes)
        }
        catch {
            $writeErrors.Add([pscustomobject]@{ Path = $plan.Path; Error = $_.Exception.Message })
        }
    }
}

$allErrors = @($script:Errors) + @($writeErrors)
$report = [pscustomobject]@{
    Timestamp = (Get-Date).ToString('o')
    Mode = $mode
    ScopeFile = $scopeFull
    RegisterListFile = $registerListFull
    RegisterCount = $registerPaths.Count
    SkippedPaths = $skipPaths
    MarkdownFilesExamined = $markdownFiles.Count
    ChangesPlanned = $script:Changes.Count
    Changes = $script:Changes
    Warnings = $script:Warnings
    Errors = $allErrors
    WritesSuppressed = [bool](-not $Apply -or $script:Errors.Count -gt 0)
}

$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportFull -Encoding UTF8

Write-Host ''
Write-Host "MODE: $mode"
Write-Host "Markdown documents examined: $($markdownFiles.Count)"
Write-Host "Registers processed: $($registerPaths.Count)"
Write-Host "Changes planned: $($script:Changes.Count)"
Write-Host "Errors: $($allErrors.Count)"
Write-Host "Report: $reportFull"

if ($allErrors.Count -gt 0) {
    Write-Host ''
    Write-Host 'ERRORS:' -ForegroundColor Red
    $allErrors | Format-Table -AutoSize
    exit 2
}

if (-not $Apply) {
    Write-Host ''
    Write-Host 'DRY-RUN ONLY: corpus files were not modified; the JSON report was written.'
}
else {
    Write-Host ''
    Write-Host 'APPLY COMPLETE.'
}
