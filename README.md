# cosmic-issue-labels

**A protocol and (forthcoming) dataset for sizing issue-tracker items with the COSMIC functional size measurement method (ISO/IEC 19761).**
Companion to [`storypoint-calibrated`](https://github.com/samgit126/storypoint-calibrated) and to a planned EASE 2027 paper on calibrated story-point estimation.
Author: Samuel Temesgen Yimer, ORCID 0009-0008-0834-6782. Trained COSMIC rater; co-author of the COSMIC-BERT line (IEEE Access 2025, ICT4DA 2023).

## Why size issues with COSMIC

Story points are a team-relative, ordinal guess. COSMIC function points (CFP) are an ISO standard measure of functional size: count the **data movements** (Entry, Exit, Read, Write) that a functional process performs. A CFP label for an issue is therefore (a) comparable across projects and (b) defined by rules, so two trained raters should agree. That makes CFP a candidate *property of the issue itself* that can be measured before any work starts, and a candidate predictor of what an LLM agent or a human will spend resolving the issue.

## What is here

| Path | Content |
|---|---|
| `protocol/COSMIC_issue_labelling_protocol.md` | The step-by-step rating procedure for Jira-style issues: triggering event, functional users, functional processes, data groups, data movements, the counting rules, and the "cannot be sized" exits |
| `protocol/rater_worksheet.md` | The per-issue worksheet a rater fills in |
| `data/labels_template.csv` | The column layout of the released dataset; one row per issue |
| `data/examples.csv` | Five fully worked example issues from the public GPT2SP corpus |
| `scripts/validate_labels.py` | Checks a labels file: schema, value ranges, CFP = E + X + R + W, inter-rater agreement when two raters are present |

## Release plan

1. Label 300 issues from three projects of the Choetkiertikul corpus (two raters, adjudication of disagreements; Cohen's κ and ICC reported).
2. Extend to 1,000 issues; measure how far an LLM annotator, following this protocol, agrees with the human labels (after Ahmed et al., MSR 2025).
3. Release labels (CSV, CC BY 4.0) with the EASE 2027 replication package.

Labels are released here as they pass adjudication. Issue texts are not copied; rows reference the public `issuekey` in the source corpus.

## Licence

Protocol and code: MIT. Labels: CC BY 4.0 when released. The COSMIC method itself is owned by the COSMIC consortium; the Measurement Manual v5.0 is free at cosmic-sizing.org.
