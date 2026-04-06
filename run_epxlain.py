from typing import Dict, Any
from src.generator import generate_test_cases,format_test_case

workflow: Dict[str, Any] = {
    "actors": [
        "Customer",
        "Claims Processing System",
        "Claims Adjuster"
    ],
    "preconditions": [
        "Policy is active",
        "Customer is authenticated",
        "Claim has not been previously submitted"
    ],
    "workflow": [
        "Customer submits claim with amount",
        "System validates claim",
        "System routes to adjuster if threshold exceeded"
    ],
    "business_rules": [
        "Claims above threshold require manual review",
        "Duplicate claims must be flagged"
    ],
    "constraints": [
        "Regulatory audit logging required"
    ]
}

#explain_generation(workflow)

test_cases = generate_test_cases(workflow)

print("=== GENERATED TEST CASE CANDIDATES ===")
for tc in test_cases:
    print(format_test_case(tc))
    print("\n" + "=" * 50 + "\n")


