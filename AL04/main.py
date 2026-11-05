from console_style import print_color
from search_support import category_key, id_key, matches, compare_values
from ticket_data import TICKETS
from ticket_display import show_ticket, show_trace


def linear_search(records, target, key=id_key):
    # Returns a matching position and trace, or None and the trace if absent.
    trace = []
    for position, record in enumerate(records):
        value = key(record)
        trace.append((position, value))
        if matches(value, target):
            return position, trace
    return None, trace


def binary_search(records, target, key=id_key):
    # Searches an ascending view; equal keys may return any matching position.
    low, high, trace = 0, len(records) - 1, []
    while low <= high:
        middle = (low + high) // 2
        value = key(records[middle])
        trace.append((low, high, middle, value))
        comparison = compare_values(value, target)
        if comparison == 0:
            return middle, trace
        if comparison < 0:
            low = middle + 1
        else:
            high = middle - 1
    return None, trace


def show_result(records, position):
    # Displays the found ticket, or a clear message when it is absent.
    if position is None:
        show_ticket(None)
    else:
        show_ticket(records[position])


def main():
    rows = TICKETS
    print_color("Ticket search demonstrations", "heading")
    print("Input order:", [id_key(record) for record in rows])

    print_color("\n1. A key selects a value", "success")
    value = id_key(rows[0])
    print("The first ticket's ID is", value)
    print("Does that ID match T403?", value == "T403")
    
    print_color("\n2. Linear search in input order", "success")
    position, trace = linear_search(rows, "T403")
    print(f"T403 input position: {position}")
    show_result(rows, position)
    show_trace("Linear search for T403", trace)

    missing_position, _ = linear_search(rows, "T499")
    print(f"\nT499 input position: {missing_position}")
    show_result(rows, missing_position)
    
    print_color("\n3. Binary search in ascending ID order", "success")
    id_view = sorted(rows, key=id_key)
    print("ID search view:", [id_key(record) for record in id_view])
    binary_position, trace = binary_search(id_view, "T403")
    print(f"T403 search-view position: {binary_position}")
    show_result(id_view, binary_position)
    show_trace("Binary search for T403", trace)
    print("The same ticket is at input position 0 and search-view position 2.")

    missing_position, _ = binary_search(id_view, "T499")
    print(f"\nT499 search-view position: {missing_position}")
    show_result(id_view, missing_position)

    print_color("\n4. Deliberate binary-search precondition failure", "success")
    linear_position, _ = linear_search(rows, "T401")
    print(f"Linear search finds T401 at input position {linear_position}:")
    show_result(rows, linear_position)
    invalid_position, _ = binary_search(rows, "T401")
    print(f"Binary search on the unsorted input returns {invalid_position}:")
    show_result(rows, invalid_position)
    print("Reason: at index 0, T403 is greater than T401, so binary search discards index 1, where T401 actually sits.")

    print_color("\n5. Repeated category search", "success")
    account_position, _ = linear_search(rows, "account", key=category_key)
    category_view = sorted(rows, key=category_key)
    binary_account_position, _ = binary_search(category_view, "account", key=category_key)
    
    print("Category search view:", [category_key(record) for record in category_view])
    print(f"Linear account position: {account_position}")
    show_result(rows, account_position)
    print(f"Binary account position: {binary_account_position}")
    show_result(category_view, binary_account_position)
    print("Both returned records have category 'account'; duplicate positions may differ.")


if __name__ == "__main__":
    main()
