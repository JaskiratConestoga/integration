import insurance_claim

def test_normal_insurance_claim():
    student_name = "Judith Evans"
    insurance_type = "standard"
    total_claim_amount = 1000

    claim_amount = insurance_claim.calculate_claim_amount(student_name, insurance_type, total_claim_amount)

    assert claim_amount = 700
