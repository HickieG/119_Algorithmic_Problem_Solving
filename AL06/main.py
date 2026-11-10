"""Optional generic English-first scaffold for any one AL06 application."""

from scenario_data import SCENARIOS
from record_support import validate_node
from record_display import show_records, show_results

CHOICE = "fundraiser"

def recursive_total(node, included_status):
    """Return the selected entry amount or recursively combine a group's totals."""
    validate_node(node)
    if node["type"] == "entry":
        return node["amount"] if node["status"] == included_status else 0

    subtotal = 0
    for record in node["items"]:
        record_total = recursive_total(record, included_status)
        subtotal += record_total
    return subtotal


def iterative_total(node, included_status):
    """Total matching entries using an explicit stack without changing the source."""
    pending = [node]
    total = 0

    while pending:
        current = pending.pop()
        validate_node(current)
        if current["type"] == "entry":
            if current["status"] == included_status:
                total += current["amount"]
        else:
            pending.extend(current["items"])

    return total


def main():
    """Choose one context and present only the completed application stages."""
    scenario = SCENARIOS[CHOICE]
    data = scenario["data"]
    included_status = scenario["included_status"]

    show_records(data, scenario["unit"])
    recursive_result = recursive_total(data, included_status)
    iterative_result = iterative_total(data, included_status)
    show_results(scenario, recursive_result, iterative_result)


if __name__ == "__main__":
    main()