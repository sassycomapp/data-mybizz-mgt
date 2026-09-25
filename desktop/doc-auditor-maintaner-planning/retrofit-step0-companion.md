---
title: "retrofit-step0-companion"
doc-id: "retrofit-step0-companion"
---
# Step 0 Retrofit — PowerShell Script Companion

## 1. Purpose and plan alignment

`retrofit-step0.ps1` performs the Step 0 corpus retrofit from the **mb-doc-maintainer — Complete Consolidated Plan**. It prepares eligible Markdown documents and the six register files listed in `register-paths.md` before Phase 1 begins.

The result for each eligible document is frontmatter containing exactly:

```yaml
---
title: "<filename stem>"
doc-id: "<filename stem>"
---
```

The retrofit removes other frontmatter fields, adds the block when absent, and normalizes affected Markdown files to LF. Each register table is converted to `doc-id`, `title`, `state`, `superseded-by`, and `notes`; the `title` value is the bare filename, without its directory path. Empty placeholders also receive filename-derived frontmatter, as directed by the developer.

**Placeholder behavior:** current GBrain code accepts valid frontmatter even when the body is empty. It can import the page with zero body chunks; later content can be added and synced normally. The script records a warning so the operator knows the placeholder has no searchable body content yet.

The plan contains references to “both registers.” The supplied `register-paths.md` identifies **six physical register files**; this script processes all six for Step 0.

## 2. Inputs and scope

The script reads scope roots and quoted path exceptions from the live `mybizz-scope-list.md`; it does not keep a separate roots list. A quoted exception path is recognized even when the line has an explanatory note after it. The current authority supplies four roots:

- `C:\data-mybizz-mgt`
- `C:\dev`
- `C:\mybizz`
- `C:\pdlf`

The script also reads the six register paths from `register-paths.md`:

1. `C:\data-mybizz-mgt\register-local.md`
2. `C:\dev\dev-makepdlf\makepdlf-project-library\register-local\register-local.md`
3. `C:\dev\dev-mb-3-cs\mb-3-cs-project-library\register-local\register-local.md`
4. `C:\mybizz\mybizz-config-docs\register-local.md`
5. `C:\mybizz\mybizz-os-docs\register-local.md`
6. `C:\dev\project-library-global\register-global\register-global.md`

Before planning writes, it checks that the path list contains exactly six unique, existing Markdown files and that every register lies within a scope root and outside listed exceptions. The optional `-SkipPath` parameter excludes specified Markdown files from this invocation only; it does not change the scope authority or the six-register list.

## 3. Exclusions and file handling

The script applies the scope authority's explicit path exceptions and its named-folder rules. It also excludes the Step 0 treatment exemptions: `tmp-` paths, `stencils`, `quarantine`, `backup`, and `catalogue`.

Traversal stops at any directory containing `anvil.yaml`. The script does not read or write `anvil.yaml`. It skips dotfolders, version-control folders, filesystem links, and files passed through `-SkipPath`. Empty and whitespace-only Markdown placeholders are selected and receive filename-derived frontmatter; a warning records that they have no body chunks yet. Documents with malformed frontmatter, invalid UTF-8, or null bytes are reported as errors and are not rewritten.

For this run, `-SkipPath` excludes `C:\dev\dev-mb4ecom\mb4ecom-project-library\register-local\register-local.md` from ordinary Markdown processing. It is not added to the six-register list.

## 4. Frontmatter conversion

For each eligible Markdown document, the script replaces an existing frontmatter block with exactly two YAML string fields: `title` and `doc-id`, both set to the filename stem. Other existing frontmatter fields are removed. If frontmatter is absent, the block is added before the body.

Filename values are escaped as YAML double-quoted strings. A malformed opening fence or an unclosed frontmatter block causes a reported error rather than an attempt to guess where the body begins. A placeholder with no body gets the two-field frontmatter block only; no body text is invented.

## 5. Register conversion

The six current register files use different legacy headers, including `filename`, `folder`, `type`, and date columns. The script maps values by header name rather than fixed column positions:

- `doc-id` is preserved.
- `filename` (or an existing `title`) becomes `title`, reduced to the bare filename.
- `state`, `superseded-by`, and `notes` are preserved when present.
- Missing trailing cells are padded with blanks; missing optional `superseded-by` or `notes` cells are emitted as blank.
- Legacy folder, type, and date columns are removed as required by D4.

Every table row is retained. Existing escaped pipes and pipes inside inline code are parsed as cell content. Extra trailing empty cells are accepted; extra note fragments are retained in `notes`; rows lacking the two identity cells cause a reported error. Non-table register content is retained; comments and blank lines inside the table's row region are placed after the converted rows. Each register's own frontmatter is updated to the two-field rule.

If any eligible file or register fails preflight, **no corpus or register file is written**. The JSON report still records the errors. During apply, an operating-system write failure can occur after earlier files have been written; review the report before retrying.

## 6. Dry-run, report, and apply

Dry-run is the default. It reads and classifies targets, calculates proposed changes, and writes a JSON report. The report is an intentional output, including during dry-run; no corpus or register file is changed without `-Apply`. `WritesSuppressed` is `true` in dry-run mode and when apply-mode preflight errors prevent writes. The report records run-specific exclusions in `SkippedPaths`.

The default report is created beside the script with a timestamped filename. An explicit `-ReportPath` must point to a new file in an existing directory; the script refuses to overwrite an existing report or a retrofit target.

Run the dry-run from PowerShell:

```powershell
& 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\retrofit-step0.ps1' `
  -ScopeFile 'C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md' `
  -RegisterListFile 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\register-paths.md' `
  -SkipPath 'C:\dev\dev-mb4ecom\mb4ecom-project-library\register-local\register-local.md'
```

Review the report, including all six register changes and any errors. Only after the dry-run is acceptable, apply with:

```powershell
& 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\retrofit-step0.ps1' `
  -ScopeFile 'C:\mybizz\mybizz-os-docs\os-reference-docs\mybizz-scope-list.md' `
  -RegisterListFile 'C:\data-mybizz-mgt\desktop\doc-auditor-maintaner-planning\register-paths.md' `
  -SkipPath 'C:\dev\dev-mb4ecom\mb4ecom-project-library\register-local\register-local.md' `
  -Apply
```

There is no `-DryRun` switch; omitting `-Apply` selects dry-run mode.

## 7. Parent boundary and watcher

`-Parent` is an optional additional boundary. Every scope target, input, register, and report path must be under that parent. If any path falls outside it, the script records an error and suppresses corpus writes. For the full four-root retrofit and six registers, omit `-Parent`.

The consolidated plan requires the watcher to be offline during Step 0. The script does not detect, stop, or verify the watcher; confirm it is offline before running either mode.

## 8. Execution and verification

The script performs these operations:

1. Read and validate the scope authority and six-register path list.
2. Traverse scope roots while applying the explicit exclusions and Anvil-folder rule.
3. Calculate frontmatter and LF changes for eligible Markdown documents.
4. Convert each register table by its actual header and retain its rows.
5. Write a report; apply planned corpus changes only when `-Apply` is present and preflight has no errors.

After the apply run, verify from the JSON report and resulting files that:

- all six registers have the five required columns and their original rows remain;
- eligible documents have `title` and `doc-id` equal to their filename stem, with no other frontmatter fields;
- exempt paths and Anvil code repositories were not modified;
- affected Markdown files use LF line endings;
- the script reported no errors.

The script does not rewrite links, create or delete documents, infer semantic relationships, run the watcher, modify DocCycle, or modify `mb-doc-auditor`.
