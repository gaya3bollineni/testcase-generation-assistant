# Workflow Input Format

This document defines the required structure for workflow descriptions
used as input to the test-case generation process.

The goal of this format is clarity and consistency, not exhaustiveness.
It is designed to make implicit business logic explicit and reviewable
before any test cases are generated.

## Actors
A list of entities that interact with the system.

Examples:
- Customer
- Internal user
- External system
- Automated process

## Preconditions
Conditions that must be true before the workflow begins.

Examples:
- Account is active
- User is authenticated
- Policy exists and is not expired

## Workflow Steps
An ordered list of actions and system responses.

Each step should describe what happens, not how it is implemented.

Include decision points explicitly.

Example:
1. User submits a claim
2. System validates claim amount
3. If the amount exceeds threshold, manual review is triggered

## Business Rules
Rules that influence behavior, validation, or decision-making.

Examples:
- Claims above threshold require manual approval
- Duplicate submissions must be flagged
- Payment must not exceed policy limit

## Constraints
External or system-level constraints that affect the workflow.

Examples:
- Regulatory logging is required
- Processing must complete within a fixed time window
- Certain actions are irreversible once executed
``
