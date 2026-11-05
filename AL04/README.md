# AL04: Search Contracts and Correctness

Name: Garrett Hickie

## Run

Keep main.py, test_assignment.py, ticket_data.py, search_support.py,
ticket_display.py, and console_style.py together.

## Contract and Work Notes

- Ordering precondition: Binary search needs ascending order. On the original list, index 0 is T403, which is greater than T401, so the search discards index 1, where T401 actually sits.
- Result agreement: The searches can return different positions because one searches the input order and the other searches an ordered view. With duplicate categories, either search may return any matching ticket.
- Reflection/debugging/learning:
  - Linear search works without sorting; binary search depends on the records being ordered by the search key.
  - A position is relative to the list being searched, so positions can differ even when both searches find the same ticket.
  - Sorting a copy before using `.sort()` keeps the original ticket order unchanged.

## Assistance

I brought over all assisting files from GitHub so that I could focus on my main functions. Everything except the test_assignment.py and the main.py is supplied from a learning resource. 

I was surprisingly aided most by the console style and ticket display functions. They made the console output much easier to read, even while troubleshooting, so that I could easily delineate which section I was in. While I appreciated following the trace, it did not seem to teach me much except for what my binary search was actually doing.

AI Use: 
I used AI primarily to assist with the content within the "def main()" function. I initially was building the print functions similar to how the demo file looked, but ended up asking AI to refactor some steps to make it more consistent with variables I was using (id_key instead of equipment_id, etc.) and generally clean up formatting. Then, when revisiting the assignment on Tuesday, I asked Copilot to help check over my category search. I approved changes it suggested and think the output looks clean, but truthfully I am not 100% on what the category search helps accomplish besides for showing that it can be done. My assumption is that categories will be more useful when we start filtering rather than searching. I also had AI help me write test assignments after the first few, since I was a little lost on where to go. I think it went a little overboard there but I had it add comments for me to better understand what/how its checking.

## Instructor Comments

[Reserved for instructor feedback.]