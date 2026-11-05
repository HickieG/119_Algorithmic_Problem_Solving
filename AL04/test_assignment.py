from main import binary_search, linear_search
from search_support import category_key, id_key
from ticket_data import TICKETS


def test_found_and_missing():
    id_view = sorted(TICKETS, key=id_key)

    linear_position, _ = linear_search(TICKETS, "T403")
    # Linear search finds T403 in the input.
    assert id_key(TICKETS[linear_position]) == "T403"

    binary_position, _ = binary_search(id_view, "T403")
    # Binary search finds T403 in the ascending-ID view.
    assert id_key(id_view[binary_position]) == "T403"

    linear_missing, _ = linear_search(TICKETS, "T499")
    # Linear search reports a missing ticket with None.
    assert linear_missing is None

    binary_missing, _ = binary_search(id_view, "T499")
    # Binary search reports a missing ticket with None.
    assert binary_missing is None


def test_empty_and_singleton():
    for search in (linear_search, binary_search):
        empty_position, _ = search([], "T403")
        # Searching an empty list returns None.
        assert empty_position is None

        one_ticket = [TICKETS[0]]
        found_position, _ = search(one_ticket, "T403")
        # Searching a one-ticket list finds its only ticket at position zero.
        assert found_position == 0

        missing_position, _ = search(one_ticket, "T499")
        # A missing ticket is not found in a one-ticket list.
        assert missing_position is None


def test_endpoints():
    id_view = sorted(TICKETS, key=id_key)

    first_linear, _ = linear_search(TICKETS, "T403")
    # Linear search finds the first input ticket at the first position.
    assert first_linear == 0

    last_linear, _ = linear_search(TICKETS, "T406")
    # Linear search finds the last input ticket at the last position.
    assert last_linear == len(TICKETS) - 1

    first_binary, _ = binary_search(id_view, "T401")
    # Binary search finds the smallest ID at the first sorted position.
    assert first_binary == 0

    last_binary, _ = binary_search(id_view, "T406")
    # Binary search finds the largest ID at the last sorted position.
    assert last_binary == len(id_view) - 1


def test_repeated_category():
    category_view = sorted(TICKETS, key=category_key)

    for search, records in (
        (linear_search, TICKETS),
        (binary_search, category_view),
    ):
        position, _ = search(records, "account", key=category_key)
        # Each search returns some ticket in the repeated account category.
        assert category_key(records[position]) == "account"


def test_input_order_is_unchanged():
    original_ids = [id_key(record) for record in TICKETS]

    linear_search(TICKETS, "T403")
    binary_search(sorted(TICKETS, key=id_key), "T403")
    binary_search(sorted(TICKETS, key=category_key), "account", key=category_key)

    # Searches and sorted views leave the source ticket order unchanged.
    assert [id_key(record) for record in TICKETS] == original_ids


def test_unsorted_binary_search_example():
    linear_position, _ = linear_search(TICKETS, "T401")
    # Linear search finds T401 in the original unsorted input.
    assert id_key(TICKETS[linear_position]) == "T401"

    binary_position, _ = binary_search(TICKETS, "T401")
    # Binary search deliberately misses T401 when given the unsorted input.
    assert binary_position is None


def run_tests():
    tests = (
        test_found_and_missing,
        test_empty_and_singleton,
        test_endpoints,
        test_repeated_category,
        test_input_order_is_unchanged,
        test_unsorted_binary_search_example,
    )
    for test in tests:
        test()
    print(f"{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()
