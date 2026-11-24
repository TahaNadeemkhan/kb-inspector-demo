---
name: knowing-mailguard-business-rules
description: States MailGuard's business rules that decide whether something is a bug - how long report data is kept, when a case counts as stuck, and when a case closes on its own. Use when judging whether what a customer reports is expected behaviour.
---

# MailGuard business rules

| Rule | Value | Where it lives |
| --- | --- | --- |
| Report bodies kept for | 7 days after `received_at` | `src/retention.py` |
| Removal jobs kept for | 7 days after they finish | `src/retention.py` |
| A case is stuck when | `processing` for more than 2 hours | `src/case_status.py` |
| A case closes on its own after | 30 days with no activity | `src/case_status.py` |

A customer asking why an 8-day-old report has no body is seeing the retention rule, not a bug.
