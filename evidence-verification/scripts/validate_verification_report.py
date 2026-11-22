#!/usr/bin/env python3
"""Validate an evidence verification report, optionally checking file evidence."""

import argparse
import json
import sys
from pathlib import Path


STATUSES = {"passed", "failed", "blocked"}
EVIDENCE_TYPES = {"file", "command", "url", "observation"}


def nonempty_string(value, path, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path}: expected a non-empty string")


def string_list(value, path, errors, required=False):
    if not isinstance(value, list):
        errors.append(f"{path}: expected a list")
        return
    if required and not value:
        errors.append(f"{path}: expected at least one item")
    for index, item in enumerate(value):
        nonempty_string(item, f"{path}[{index}]", errors)


def validate(data, base_dir=None, check_files=False):
    errors = []
    if not isinstance(data, dict):
        return ["root: expected a JSON object"]

    version = data.get("version")
    if not isinstance(version, dict):
        errors.append("version: expected an object")
    else:
        for field in ("id", "environment", "target"):
            nonempty_string(version.get(field), f"version.{field}", errors)

    overall = data.get("overall")
    if overall not in STATUSES:
        errors.append("overall: expected passed, failed, or blocked")

    cases = data.get("cases")
    if not isinstance(cases, list):
        errors.append("cases: expected a list")
        return errors
    if not cases:
        errors.append("cases: expected at least one case")

    seen_ids = set()
    statuses = []
    for index, case in enumerate(cases):
        path = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{path}: expected an object")
            continue

        case_id = case.get("id")
        nonempty_string(case.get("id"), f"{path}.id", errors)
        if isinstance(case_id, str) and case_id:
            if case_id in seen_ids:
                errors.append(f"{path}.id: duplicate id {case_id!r}")
            seen_ids.add(case_id)

        nonempty_string(case.get("requirement"), f"{path}.requirement", errors)
        if "preconditions" in case:
            string_list(case["preconditions"], f"{path}.preconditions", errors)
        string_list(case.get("steps"), f"{path}.steps", errors, required=True)
        nonempty_string(case.get("expected"), f"{path}.expected", errors)
        nonempty_string(case.get("actual"), f"{path}.actual", errors)

        status = case.get("status")
        if status not in STATUSES:
            errors.append(f"{path}.status: expected passed, failed, or blocked")
        else:
            statuses.append(status)
        if status == "blocked":
            nonempty_string(case.get("blocker"), f"{path}.blocker", errors)

        evidence = case.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{path}.evidence: expected a list")
            continue
        if not evidence:
            errors.append(f"{path}.evidence: expected at least one evidence item")
        for evidence_index, item in enumerate(evidence):
            evidence_path = f"{path}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                errors.append(f"{evidence_path}: expected an object")
                continue
            evidence_type = item.get("type")
            if evidence_type not in EVIDENCE_TYPES:
                errors.append(f"{evidence_path}.type: expected file, command, url, or observation")
            value = item.get("value")
            nonempty_string(value, f"{evidence_path}.value", errors)
            if check_files and evidence_type == "file" and isinstance(value, str) and value.strip():
                evidence_file = Path(value)
                if not evidence_file.is_absolute() and base_dir is not None:
                    evidence_file = base_dir / evidence_file
                if not evidence_file.is_file():
                    errors.append(f"{evidence_path}.value: file does not exist: {evidence_file}")

    if "human_review" in data:
        string_list(data["human_review"], "human_review", errors)

    if statuses and overall in STATUSES:
        expected_overall = "failed" if "failed" in statuses else "blocked" if "blocked" in statuses else "passed"
        if overall != expected_overall:
            errors.append(f"overall: expected {expected_overall!r} from case statuses, got {overall!r}")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Path to verification report JSON")
    parser.add_argument("--check-files", action="store_true", help="Require file evidence to exist relative to the report")
    args = parser.parse_args()

    try:
        with args.path.open("r", encoding="utf-8-sig") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate(data, base_dir=args.path.resolve().parent, check_files=args.check_files)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    counts = {status: 0 for status in STATUSES}
    for case in data["cases"]:
        counts[case["status"]] += 1
    print(
        f"OK: {len(data['cases'])} case(s); {counts['passed']} passed; "
        f"{counts['failed']} failed; {counts['blocked']} blocked"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
