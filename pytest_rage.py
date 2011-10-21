import pytest

test_count = 0

def pytest_report_teststatus(report):
    global test_count
    if report.passed:
        letter = "."
    elif report.skipped:
        letter = "s"
    elif report.failed:
        test_count += 1
        if test_count > 7:
            letter = "U"
        else:
            letter = "F"
        if report.when != "call":
            if test_count > 7:
                letter = "u"
            else:
                letter = "f"
    return report.outcome, letter, report.outcome.upper()
