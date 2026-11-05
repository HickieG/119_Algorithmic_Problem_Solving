# AL03: Ticket Registry, Queue, and Undo

Name: [Garrett Hickie]
Partners: [Aiden Canon]
Shared repository: [can't find where to access shared repo URL]
My contribution: [Tuesday's functions, print statements, assertions and main.py]

## Operation Comparison

One short reason per row is enough. Compare list and dictionary behavior;
do not implement every operation twice or maintain two live stores.

| Operation | Representation fit / reason |
| --- | --- |
| Find one ticket by ID | A list must be scanned; a dictionary retrieves the ticket directly by ID. |
| Update one ticket's priority | A dictionary finds the ticket by ID before updating it; a list must first be searched for that ID. |
| Select tickets in a category | Both require checking every ticket; the dictionary's ID index does not speed up a category scan. |

## Work Notes and Reflections

Append brief observations, debugging challenges, changes, and learnings.

- Processing and undo: T301 and then T302 were processed in queue order, regardless of priority; undo restored only T302 to the front and left T301 completed.
- Contract or snapshot learning: Copying records for the registry and filtered reports, and returning a new queue from repair, keeps those results independent of their inputs.

These can be short bullets, not an essay or separate evidence document.

## Assistance

An AI assistant was used to help create `enqueue_ticket` and write terminal output statements. I provided our `Main.py` work and a portion of Cash's `main2.py` from Tuesday's demo, then checked the enqueue behavior against AL03's rules. I kept AL03's stricter rule that completed tickets are rejected before enqueueing, rather than copying the demo's unavailable-item behavior. `TicketData.py` and `Ticket_Display.py` were supplied modules.

## Instructor Comments

[Reserved for instructor feedback.]