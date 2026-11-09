# AL05: Filter, Sort, and Search Pipeline

Name: Garrett Hickie

## Run

Keep main.py, test_assignment.py, search_algorithms.py, ticket_data.py,
search_support.py, pipeline_support.py, ticket_display.py, and console_style.py together.

## Pipeline and Work Notes

- Pipeline: Source: TICKETS -> Filter: minimum age -> Display/Search Views: age-display and ID-search -> Lookup
- One request: Filter TICKETS, then build the views needed for the requested display and lookup.
- Repeated requests: Reuse the selected records and ID-ordered view at the same threshold; rebuild views when the threshold or source records change.
- Issued change: Raising the threshold from 4 to 7 days removes T406; insertion sort and the search algorithms stay the same.
- Copying/stability: Sorting creates a new list but shares ticket dictionaries; equal-age tickets retain their input order.

Short bullets are enough; traces/counts can stay in the console.

## Assistance

For AI: tool/task and what you checked, changed, or rejected.

Supplied modules include: console_style.py, pipeline_support.py, search_algorithms.py, search_support.py, ticket_data.py, & ticket_display.py. 

The search_algorithms.py is coming from my AL04 assignment. 

AI use statement: 
I had Copilot's assistance with building and formatting my def main() function. I used it in a similar fashion to AL04, helping align the print statements and the trace with console styling. I also consulted Copilot for inspiration on assertions and tried some interesting new formatting with functions. 


## Instructor Comments

[Reserved for instructor feedback.]