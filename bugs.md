
# Bug & Incident Tracker

**Project**: mcp_plugin
**Last Updated**: 2026-04-08

---

## Open Items

| ID | Type | Severity | Cycle | Summary | Reporter | Created | Status |
|----|------|----------|-------|---------|----------|---------|--------|
| BUG-4 | Bug | Medium | Cycle-2 | Login timeout on slow networks | DEV | 2026-04-08 | Open |
| INC-3 | Incident | P1 | Cycle-2 | API gateway 502 errors in prod | OPS | 2026-04-08 | Open |

---

## Resolved Items

| ID | Type | Severity | Cycle | Summary | Reporter | Created | Resolved | Resolution |
|----|------|----------|-------|---------|----------|---------|----------|------------|
| BUG-1 | Bug | Low | Cycle-1 | Typo in error message | DEV | 2026-04-07 | 2026-04-07 | Fixed |
| BUG-2 | Bug | Medium | Cycle-1 | CSS overflow on mobile | DEV | 2026-04-07 | 2026-04-08 | Fixed |
| BUG-3 | Bug | High | Cycle-1 | Auth token not refreshing | QA | 2026-04-07 | 2026-04-08 | Fixed |
| INC-1 | Incident | P2 | Cycle-1 | Memory spike during deploy | OPS | 2026-04-07 | 2026-04-07 | Mitigated |
| INC-2 | Incident | P1 | Cycle-1 | Database connection pool exhausted | OPS | 2026-04-07 | 2026-04-08 | Root cause fixed |

---

## Field Definitions

| Field | Required | Values | Purpose |
|-------|----------|--------|---------|
| **ID** | Yes | `BUG-N` or `INC-N` | Unique identifier |
| **Type** | Yes | `Bug` or `Incident` | Bug = defect found in testing/post-deploy; Incident = production P1/P2 event |
| **Severity** | Yes | `P1`, `P2`, `High`, `Medium`, `Low` | P1/P2 used for incident KPI tracking |
| **Cycle** | Yes | `Cycle-1`, `Cycle-2`, etc. | Must match the Cycle column in `status.md` Build Cycles table |
| **Summary** | Yes | Free text | Brief description |
| **Reporter** | Yes | Name or role | Who raised it |
| **Created** | Yes | `YYYY-MM-DD` | Date the item was raised |
| **Status** | Yes | `Open` or `Resolved` | Current state (move to Resolved table when done) |
| **Resolved** | On resolve | `YYYY-MM-DD` | Date the item was closed |
| **Resolution** | On resolve | `Fixed`, `Mitigated`, `Won't Fix`, `Duplicate` | How it was resolved |



