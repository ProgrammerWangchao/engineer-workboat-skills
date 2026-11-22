#!/usr/bin/env python3
"""Validate an evidence-backed feature_list.json without external packages."""

import argparse
import json
import re
import sys
from pathlib import Path


ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def nonempty_string(value, path, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path}: expected a non-empty string")


def string_list(value, path, errors, allow_empty=False):
    if not isinstance(value, list):
        errors.append(f"{path}: expected a list")
        return
    if not allow_empty and not value:
        errors.append(f"{path}: expected at least one item")
    for index, item in enumerate(value):
        nonempty_string(item, f"{path}[{index}]", errors)


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["root: expected a JSON object"]

    if type(data.get("version")) is not int or data.get("version") != 1:
        errors.append("version: expected integer 1")

    features = data.get("features")
    if not isinstance(features, list):
        errors.append("features: expected a list")
        return errors
    if not features:
        errors.append("features: expected at least one feature")

    seen_ids = set()
    for index, feature in enumerate(features):
        path = f"features[{index}]"
        if not isinstance(feature, dict):
            errors.append(f"{path}: expected an object")
            continue

        feature_id = feature.get("id")
        nonempty_string(feature_id, f"{path}.id", errors)
        if isinstance(feature_id, str) and feature_id:
            if not ID_PATTERN.fullmatch(feature_id):
                errors.append(f"{path}.id: use lowercase letters, digits, and hyphens")
            if feature_id in seen_ids:
                errors.append(f"{path}.id: duplicate id {feature_id!r}")
            seen_ids.add(feature_id)

        nonempty_string(feature.get("category"), f"{path}.category", errors)
        nonempty_string(feature.get("description"), f"{path}.description", errors)
        string_list(feature.get("steps"), f"{path}.steps", errors)

        passes = feature.get("passes")
        if type(passes) is not bool:
            errors.append(f"{path}.passes: expected true or false")

        evidence = feature.get("evidence")
        string_list(evidence, f"{path}.evidence", errors, allow_empty=True)
        if passes is True and isinstance(evidence, list) and not evidence:
            errors.append(f"{path}.evidence: a passed feature requires evidence")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Path to feature_list.json")
    args = parser.parse_args()

    try:
        with args.path.open("r", encoding="utf-8-sig") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    features = data["features"]
    passed = sum(feature["passes"] is True for feature in features)
    print(f"OK: {len(features)} feature(s); {passed} passed; {len(features) - passed} not passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
