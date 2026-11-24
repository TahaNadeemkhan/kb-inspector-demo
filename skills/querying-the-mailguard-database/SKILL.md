---
name: querying-the-mailguard-database
description: Describes the MailGuard database (tables reports, cases, removal_jobs and quarantine_items, their columns and allowed values) for writing read-only SQL. Use before writing any query about reports, cases or mailbox removals.
---

# Querying the MailGuard database

## Tables

| Table | Columns | Notes |
| --- | --- | --- |
| `reports` | `id`, `account_id`, `sender`, `subject`, `body`, `received_at`, `verdict` | `verdict` is `phish`, `spam` or `legit` |
| `cases` | `id`, `account_id`, `case_number`, `status`, `updated_at` | `status` is `open`, `processing` or `closed` |
| `removal_jobs` | `id`, `case_id`, `mailbox`, `state` | `state` is `queued`, `done` or `failed` |
| `quarantine_items` | `id`, `report_id`, `held_until`, `released_by` | A reported message held back until `held_until`; `released_by` is set when an admin lets it through early |

## Rules

- Filter every query on `account_id` and name the account in the answer.
- `reports.body` is empty for reports older than the retention period. An empty body is not a bug.
- Removal jobs are deleted after the retention period, so an old case can show no jobs.
