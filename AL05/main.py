"""Optional English-first starter for stable sorting and a key-correct pipeline."""

from ticket_data import TICKETS
from search_support import id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets, show_trace
from search_algorithms import linear_search, binary_search

def insertion_sort(records, key):
    """Return a stable shallow ordered list, comparison/shift counts, and ID trace."""
    ordered = list(records)
    comparisons = 0
    moves = 0
    trace = []

    for index in range(1, len(ordered)):
        item = ordered[index]
        item_key = key(item)
        position = index - 1
        # Shifting position to look at where the current item should be inserted

        while position >= 0:
            comparisons += 1
            if key(ordered[position]) <= item_key:
                # The earlier item is already less than or equal to the saved item.
                break
            # Otherwise shift this larger item right to open a spot.
            ordered[position + 1] = ordered[position]
            moves += 1
            position -= 1

        ordered[position + 1] = item
        # Place the current item at its correct position and record the ID order.
        trace.append([record["id"] for record in ordered])

    return ordered, comparisons, moves, trace


def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists sharing eligible records."""
    selected = select_open_tickets(records, minimum_days)
    display_view, _, _, _ = insertion_sort(selected, days_key)
    search_view = sorted(selected, key=id_key)
    return selected, display_view, search_view


def main():
    """Present completed daily stages and explain the issued threshold change."""
    selected = select_open_tickets(TICKETS, minimum_days=4)
    ordered, comparisons, moves, trace = insertion_sort(selected, days_key)

    show_tickets("Tuesday: open tickets aged at least 4 days, ascending age", ordered)
    print("\nTeaching trace: ID order after each insertion")
    for insertion, ids in enumerate(trace, start=1):
        print(f"  {insertion}: {', '.join(ids)}")
    print(
        "Teaching counts: "
        f"{comparisons} key comparisons, {moves} right-shifts."
    )
    
    selected, display_view, search_view = build_views(TICKETS)
    show_tickets("Thursday: age-ordered display (minimum 4 days)", display_view)

    print("\nFind T403 with linear search in the selected list:")
    position, search_trace = linear_search(selected, "T403", key=id_key)
    print(f"  Selected-list position: {position}")
    show_ticket(selected[position] if position is not None else None)
    show_trace("linear search for T403", search_trace)

    print("\nFind T403 with binary search in the ID-ordered view:")
    position, search_trace = binary_search(search_view, "T403", key=id_key)
    print(f"  Search-view position: {position}")
    show_ticket(search_view[position] if position is not None else None)
    show_trace("binary search for T403", search_trace)

    print("\nLook for absent T499:")
    position, search_trace = linear_search(selected, "T499", key=id_key)
    print(f"  Selected-list position: {position}")
    show_ticket(selected[position] if position is not None else None)
    show_trace("linear search for T499", search_trace)
    position, search_trace = binary_search(search_view, "T499", key=id_key)
    print(f"  Search-view position: {position}")
    show_ticket(search_view[position] if position is not None else None)
    show_trace("binary search for T499", search_trace)

    print("\nDeliberate wrong-view example: binary-search for T406 by ID")
    display_position = None
    for index, record in enumerate(display_view):
        if id_key(record) == "T406":
            display_position = index
            break
    position, search_trace = binary_search(display_view, "T406", key=id_key)
    print(f"  T406 is present at age-display position {display_position}.")
    print(f"  Binary-search result on this non-ID-ordered view: {position}")
    print("  The age view is not sorted by ID, so binary search is not valid here.")
    show_trace("deliberate binary search on the age-ordered view", search_trace)

    _, changed_display, changed_search = build_views(TICKETS, minimum_days=7)
    show_tickets("Rebuilt views after the minimum changes to 7 days", changed_display)
    show_tickets("Rebuilt ID search view at 7 days", changed_search)

    _, empty_display, empty_search = build_views(TICKETS, minimum_days=8)
    show_tickets("Rebuilt views at 8 days", empty_display)
    show_tickets("Rebuilt ID search view at 8 days", empty_search)


if __name__ == "__main__":
    main()