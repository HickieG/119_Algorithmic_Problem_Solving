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