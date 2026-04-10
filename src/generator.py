import json
from typing import List, Dict, Any
from pathlib import Path


def explain_generation(workflow: Dict[str, Any]) -> None:
    """
    Dry-run mode: explains what would be sent to the AI
    and what structure is expected back.
    """
    print("=== DRY RUN MODE ===")
    print("Workflow received:")
    print(workflow)
    print("\nExpected output structure:")
    print({
        "id": "<string>",
        "description": "<string>",
        "preconditions": ["<string>"],
        "steps": ["<string>"],
        "expected_outcome": "<string>",
        "risk_level": "Low | Medium | High",
        "rationale": "<string>"
    })


def generate_test_cases(workflow: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Generate candidate test cases from a structured workflow description.

    This function intentionally produces test-case *candidates* that must
    be reviewed and approved by a human.
    """
    validate_acceptance_criteria(acceptance_criteria)
    _validate_workflow(workflow)
    return _generate_candidates(workflow)


def _generate_candidates(workflow: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Delegates generation to the AI-backed function.
    """
    return _call_ai_for_test_generation(workflow)


def _call_ai_for_test_generation(workflow: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Calls an AI model (currently mocked) to propose test case candidates.
    """

    # PSEUDO-AI OUTPUT (safe placeholder)
    ai_response = [
        {
            "id": "TC-CLAIMS-002",
            "description": "Duplicate claim submission is flagged",
            "preconditions": [
                "Policy is active",
                "An identical claim was previously submitted"
            ],
            "steps": [
                "Customer submits duplicate claim",
                "System detects matching claim data"
            ],
            "expected_outcome": "Claim is flagged and not processed automatically",
            "risk_level": "Medium",
            "rationale": "Duplicate claims present fraud risk and require investigation"
        }
    ]

    validated = []
    for candidate in ai_response:
        _validate_candidate_schema(candidate)
        validated.append(candidate)

    return validated


def _validate_workflow(workflow: Dict[str, Any]) -> None:
    """
    Minimal validation to ensure required workflow sections exist.
    """
    required_keys = [
        "actors",
        "preconditions",
        "workflow",
        "business_rules",
        "constraints"
    ]

    missing = [key for key in required_keys if key not in workflow]

    if missing:
        raise ValueError(f"Missing required workflow fields: {missing}")


def _validate_candidate_schema(candidate: Dict[str, Any]) -> None:
    """
    Ensures that a generated test case candidate strictly conforms
    to the defined output schema.
    """
    required_fields = [
        "id",
        "description",
        "preconditions",
        "steps",
        "expected_outcome",
        "risk_level",
        "rationale"
    ]

    missing = [field for field in required_fields if field not in candidate]

    if missing:
        raise ValueError(f"Generated test case missing fields: {missing}")

    if candidate["risk_level"] not in ["Low", "Medium", "High"]:
        raise ValueError("Invalid risk_level value")




def format_test_case(candidate: Dict[str, Any]) -> str:
    lines = [
        f"TEST CASE: {candidate['id']}",
        f"Description: {candidate['description']}",
        "",
        "Preconditions:"
    ]

    for p in candidate["preconditions"]:
        lines.append(f"- {p}")

    lines.append("")
    lines.append("Steps:")

    for i, step in enumerate(candidate["steps"], start=1):
        lines.append(f"{i}. {step}")

    lines.extend([
        "",
        "Expected Outcome:",
        candidate["expected_outcome"],
        "",
        "Risk Level:",
        candidate["risk_level"],
        "",
        "Why This Test Exists:",
        candidate["rationale"]
    ])

    return "\n".join(lines)



def save_test_cases_json(
    test_cases: List[Dict[str, Any]],
    output_path: str
) -> None:
    """
    Saves generated test-case candidates to a JSON file.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(test_cases, f, indent=2)

    print(f"Saved test cases to {path}")



def save_test_cases_markdown(
    test_cases: List[Dict[str, Any]],
    output_path: str
) -> None:
    """
    Saves generated test-case candidates to a Markdown file
    for easy human review.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        for tc in test_cases:
            f.write(format_test_case(tc))
            f.write("\n\n---\n\n")

    print(f"Saved test cases to {path}")

def validate_acceptance_criteria(acceptance_criteria):
    if not acceptance_criteria:
        raise ValueError("Acceptance criteria are required to generate test cases.")

    if not isinstance(acceptance_criteria, list):
        raise ValueError("Acceptance criteria must be a list.")

    seen_ids = set()

    for ac in acceptance_criteria:
        if not isinstance(ac, dict):
            raise ValueError("Each acceptance criterion must be an object.")

        ac_id = ac.get("id")
        statement = ac.get("statement")

        if not ac_id or not isinstance(ac_id, str):
            raise ValueError("Each acceptance criterion must have a non-empty 'id' field.")

        if ac_id in seen_ids:
            raise ValueError(f"Duplicate acceptance criterion id found: {ac_id}")

        seen_ids.add(ac_id)

        if not statement or not isinstance(statement, str):
            raise ValueError(
                f"Acceptance criterion '{ac_id}' must have a non-empty 'statement' field."
            )
