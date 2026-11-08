# AL05: Filter, Sort, and Search Pipeline

Name: Garrett Hickie

## Run

Keep main.py, test_assignment.py, search_algorithms.py, ticket_data.py,
search_support.py, pipeline_support.py, ticket_display.py, and console_style.py together.

## Pipeline and Work Notes

- Pipeline: [one line connecting source, filter, display/search views, and lookup]
- One request: [brief choice/reason, including setup]
- Repeated requests: [brief choice/reason, including reuse, storage, and rebuilding]
- Issued change: [what changed at 4 -> 7 days; what algorithms stayed the same]
- Copying/stability or debugging learning: [one brief observation; append as useful]

Short bullets are enough; traces/counts can stay in the console.

## AL05 Online Help

Function	Required Contract
insertion_sort(records, key)	Return (ordered, comparisons, moves, trace). ordered is a new shallow list, ascending under key. comparisons counts executed key comparisons in the shifting loop; moves counts right-shifts only, excluding final placements. trace contains the ID order after each insertion. Equal keys retain their relative input order.

build_views(records, minimum_days=4)	Return (selected, display_view, search_view). Use the supplied open/age filter, your insertion sort under days_key for display, and ordinary sorted(selected, key=id_key) for the ID search view.

Both functions leave the source list/order and record fields unchanged. Their new lists intentionally share record dictionaries. This is not a Week 3 independent snapshot: a new ordering is separate from a copied record. Do not silently add record.copy() or deep-copy machinery to change this contract. Treat records as read-only during each run and rebuild affected views after relevant changes.

The supplied filter includes all open tickets with days_open >= minimum_days. Inputs are valid, flat records; minimum_days is a nonnegative integer. No input validation framework, menu, parser, live edit interface, or persistence is required. The search functions retain AL04's (position, trace) and any-match contracts; only search an ID-ascending view for ID binary search.

Build Across the Week
Tuesday - Stable Ordering Baseline
1. Start your individual AL05 folder with the supplied modules and your local search_algorithms.py, or the instructor-released recovery copy. Keep AL04's submitted snapshot unchanged. Do not choose someone else's solution as a base.
2. Inspect the six tickets and the supplied filter. At minimum_days=4, selected IDs are T403, T405, T402, T406 in that order. T404 is completed and excluded.
3. Implement insertion_sort using a saved item, a sorted prefix, and right-shifts. Stop shifting on equality so T403 remains before T405, both age 7.
4. Show the age-ordered display: T406, T402, T403, T405. Capture one small trace and its counts: six key comparisons and five right-shifts for that selection. Label these as teaching evidence, not durations or universal costs.
5. Compare with sorted(records, key=days_key), then test empty/singleton, ordered, reverse, and shuffled inputs with ties. Verify input order/fields stay unchanged while returned lists share the record objects.
6. Commit the sort baseline. Briefly note one stability or copying observation; do not write a pre-code essay or another evidence file.

Thursday - Compose, Change, and Verify
1. Implement build_views. Keep the age-ordered display separate from the ascending-ID search view. Display readable ticket details using the supplied helpers.
2. Find T403 through a linear scan of selected and binary search of search_view. Resolve each returned position in its own view; both identify the same ticket. Also show absent T499 and a clear empty-selection result at minimum_days=8.
3. Demonstrate the wrong-view risk using this fixture: ID binary search for T406 on the age-ordered display misses a present ticket. Mark this as deliberate invalid use, not the correct workflow or an assertion every unsorted view fails.
4. Apply the issued change: raise minimum_days from 4 to 7. Rebuild from TICKETS; selected/display IDs become T403, T405, and T406 no longer qualifies. Do not rewrite the sort, search, equality, or key helpers. Rerun earlier checks.
5. Compare two workloads in brief README bullets: one request with only the source list ready, and repeated requests with a retained ID-ordered selection. Include filtering, sort setup, view storage, and rebuilding after the rule changes. No timings, measured winner, crossover claim, or multi-size experiment.
6. Finish the compact pipeline description, one changed/preserved observation, contribution/assistance notes, and tests. Run the complete independent copy in your own week_04/AL05 folder before committing/pushing and submitting.

Evidence and Checks
Keep evidence lean: console result, one tiny insertion trace/count display, focused tests in test_assignment.py, and the README's short pipeline/workload/ change/copy notes. A one-line flow such as source -> filter -> display/search views -> lookup is enough; no diagramming tool, separate report, or duplicated copy of every console trace is required.

Check boundary eligibility at days 4 and 7, completed-ticket exclusion, empty and singleton inputs, sort stability, sorted parity, input nonmutation, shared-record identity, found/missing lookup, view-relative positions, and rebuilding after change. For stability, equal keys keep the order in the particular input supplied, even if that input is reversed. No ID tie-break is added to the age sort.

Keep counts simple: small comparisons/right-shifts and optionally a selected search trace. Do not instrument library sorting or add cmp_to_key/nonlocal counters, timer/trial utilities, or retired AL02 measurement plumbing. Small counts do not include every setup cost or prove equal-duration operations.

## Assistance

[Identify supplied modules/starter and whether search_algorithms.py is your AL04
work or the instructor-released recovery copy. Identify other help, or none.
For AI: tool/task and what you checked, changed, or rejected.]

## Instructor Comments

[Reserved for instructor feedback.]