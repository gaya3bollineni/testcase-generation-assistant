from typing import List, Dict, Any

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