"""Focused tests for AL06 nested-record totals."""

from copy import deepcopy
from main import iterative_total, recursive_total
from scenario_data import SCENARIOS, make_group


def test_scenario_totals():
    expected_totals = {
        "fundraiser": 80,
        "project": 13,
        "inventory": 25,
    }

    for name, expected in expected_totals.items():
        scenario = SCENARIOS[name]
        data = scenario["data"]
        included_status = scenario["included_status"]
        assert recursive_total(data, included_status) == expected
        assert iterative_total(data, included_status) == expected


def test_empty_group():
    empty_group = make_group("Empty group", [])
    assert recursive_total(empty_group, "received") == 0
    assert iterative_total(empty_group, "received") == 0


def test_input_is_unchanged():
    for scenario in SCENARIOS.values():
        data = scenario["data"]
        original = deepcopy(data)
        recursive_total(data, scenario["included_status"])
        iterative_total(data, scenario["included_status"])
        assert data == original


def test_invalid_nested_record_is_rejected():
    malformed_group = make_group("Malformed group", [{"type": "entry"}])
    for total in (recursive_total, iterative_total):
        try:
            total(malformed_group, "received")
        except ValueError:
            pass
        else:
            raise AssertionError(f"{total.__name__} accepted an invalid entry")


def run_tests():
    tests = (
        test_scenario_totals,
        test_empty_group,
        test_input_is_unchanged,
        test_invalid_nested_record_is_rejected,
    )
    for test in tests:
        test()
    print(f"{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()
