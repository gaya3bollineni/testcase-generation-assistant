TEST CASE: TC-CLAIMS-002
Description: Duplicate claim submission is flagged

Preconditions:
- Policy is active
- An identical claim was previously submitted

Steps:
1. Customer submits duplicate claim
2. System detects matching claim data

Expected Outcome:
Claim is flagged and not processed automatically

Risk Level:
Medium

Why This Test Exists:
Duplicate claims present fraud risk and require investigation

---

