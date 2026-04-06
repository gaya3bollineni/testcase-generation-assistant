
from typing import List, Dict, Any


def generate_test_cases(workflow: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Generate candidate test cases from a structured workflow description.

    This function intentionally produces test-case *candidates* that must
    be reviewed and approved by a human.
    """

    _validate_workflow(workflow)

    candidates = _generate_candidates(workflow)

    return candidates


def _generate_candidates(workflow: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Placeholder generation logic.

    This hard-coded output exists only to validate that the generator
    conforms to the documented output schema.
    """

    return [
        {
            "test_id": "TC-CLAIMS-001",
            "description": "Claim exceeding manual review threshold is not auto-approved",
            "preconditions": [
                "Policy is active",
                "Claim amount exceeds manual review threshold"
            ],
            "steps": [
                "Customer submits claim with amount above threshold",
                "System routes claim to claims adjuster"
            ],
            "expected_outcome": "Claim is flagged for manual review and not automatically approved",
            "risk_level": "High",
            "rationale": (
                "Claims exceeding the threshold carry financial and regulatory risk "
                "and must not be processed without human review."
            )
        }
    ]


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
