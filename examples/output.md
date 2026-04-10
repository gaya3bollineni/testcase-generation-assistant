### TC-CLAIMS-001
**Acceptance Criterion:** AC-1 – Customer can submit a claim with a valid claim amount
**Intent:** Verify claim submission below the manual review threshold  

**Preconditions**
- Policy is active  
- Customer is authenticated  

**Steps**
1. Customer submits a claim with amount below threshold  

**Expected Outcome**
- Claim is accepted  
- Claim is not routed for manual review  

---

### TC-CLAIMS-002
**Acceptance Criterion:** AC-1 – Customer can submit a claim with a valid claim amount
**Intent:** Verify duplicate claims are flagged  

**Preconditions**
- Policy is active  
- Customer is authenticated  
- A claim with identical details already exists  

**Steps**
1. Customer submits a duplicate claim  

**Expected Outcome**
- Duplicate claim is flagged  
- Audit log entry is created  
