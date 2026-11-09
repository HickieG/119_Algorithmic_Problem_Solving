"""Focused checks for AL05 sorting, views, and search behavior."""

from main import build_views, insertion_sort
from pipeline_support import select_open_tickets
from search_algorithms import binary_search, linear_search
from search_support import days_key, id_key
from ticket_data import TICKETS


def value_key(record):
    """Return the value used to order a test record."""
    return record["value"]


def copy_records(records):
    """Make shallow copies for checking whether input records changed."""
    copies = []
    for record in records:
        copies.append(record.copy())
    return copies


def get_ids(records):
    """Return the IDs from a list of records in their current order."""
    ids = []
    for record in records:
        ids.append(record["id"])
    return ids


def check_records_share_source(records, source_records):
    """Check that every record is one of the source record objects."""
    for record in records:
        found_in_source = False
        for source_record in source_records:
            if record is source_record:
                found_in_source = True
                break
        assert found_in_source


def check_insertion_sort():
    """Check ordering, stability, counts, trace, and shallow-copy behavior."""
    original_tickets = copy_records(TICKETS)
    selected = select_open_tickets(TICKETS, minimum_days=4)
    ordered, comparisons, moves, trace = insertion_sort(selected, days_key)

    assert ordered == sorted(selected, key=days_key)
    assert get_ids(ordered) == ["T406", "T402", "T403", "T405"]
    assert comparisons == 6
    assert moves == 5

    tied_ticket_ids = []
    for record in ordered:
        if days_key(record) == 7:
            tied_ticket_ids.append(record["id"])
    assert tied_ticket_ids == ["T403", "T405"]

    expected_trace = [
        ["T403", "T405", "T402", "T406"],
        ["T402", "T403", "T405", "T406"],
        ["T406", "T402", "T403", "T405"],
    ]
    assert trace == expected_trace
    assert TICKETS == original_tickets
    check_records_share_source(ordered, selected)

    tied_records = [
        {"id": "second", "value": 2},
        {"id": "first", "value": 1},
        {"id": "third", "value": 2},
    ]
    test_cases = [
        [],
        [{"id": "only", "value": 1}],
        [{"id": "a", "value": 1}, {"id": "b", "value": 2}],
        [
            {"id": "a", "value": 3},
            {"id": "b", "value": 2},
            {"id": "c", "value": 1},
        ],
        tied_records,
    ]

    for records in test_cases:
        original_records = copy_records(records)
        result, _, _, case_trace = insertion_sort(records, value_key)

        assert result == sorted(records, key=value_key)
        assert records == original_records
        check_records_share_source(result, records)

        expected_trace_length = len(records) - 1
        if expected_trace_length < 0:
            expected_trace_length = 0
        assert len(case_trace) == expected_trace_length

    tied_result, _, _, _ = insertion_sort(tied_records, value_key)
    assert get_ids(tied_result) == ["first", "second", "third"]


def check_build_views():
    """Check filtering, view order, searches, and rebuilds at new thresholds."""
    original_tickets = copy_records(TICKETS)
    selected, display_view, search_view = build_views(TICKETS)

    assert get_ids(selected) == ["T403", "T405", "T402", "T406"]
    assert get_ids(display_view) == ["T406", "T402", "T403", "T405"]
    assert get_ids(search_view) == ["T402", "T403", "T405", "T406"]

    for record in selected:
        assert record["status"] == "open"
        assert record["days_open"] >= 4

    for view in (selected, display_view, search_view):
        check_records_share_source(view, TICKETS)

    linear_position, _ = linear_search(selected, "T403", key=id_key)
    binary_position, _ = binary_search(search_view, "T403", key=id_key)
    assert linear_position is not None
    assert binary_position is not None
    assert selected[linear_position] is search_view[binary_position]

    missing_linear_position, _ = linear_search(selected, "T499", key=id_key)
    missing_binary_position, _ = binary_search(search_view, "T499", key=id_key)
    assert missing_linear_position is None
    assert missing_binary_position is None

    display_t406_position = None
    for index, record in enumerate(display_view):
        if id_key(record) == "T406":
            display_t406_position = index
            break
    assert display_t406_position == 0

    wrong_view_position, _ = binary_search(
        display_view, "T406", key=id_key
    )
    assert wrong_view_position is None

    selected_7, display_7, search_7 = build_views(TICKETS, minimum_days=7)
    assert get_ids(selected_7) == ["T403", "T405"]
    assert get_ids(display_7) == ["T403", "T405"]
    assert get_ids(search_7) == ["T403", "T405"]
    assert "T406" not in get_ids(display_7)

    selected_8, display_8, search_8 = build_views(TICKETS, minimum_days=8)
    assert selected_8 == []
    assert display_8 == []
    assert search_8 == []
    assert TICKETS == original_tickets


def self_check():
    """Run all focused AL05 checks."""
    check_insertion_sort()
    check_build_views()


if __name__ == "__main__":
    self_check()
    print("AL05 checks passed.")
