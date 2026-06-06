"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student, passing_students, subjects_offered, top_scorer


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    avg = average_per_student(records)
    passing = passing_students(records)
    subjects = subjects_offered(records)
    top = top_scorer(records)
    report = {
        "total_records": len(records),
        "subjects": sorted(subjects),
        "averge": avg,
        "top_scorer": top,
        "passing_student": passing
    }
    return report