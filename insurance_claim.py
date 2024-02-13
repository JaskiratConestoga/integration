def calculate_claim_amount(student_name, insurance_type, total_claim_amount):
    if insurance_type == "premium":
        return total_claim_amount   # 100% claim
    else:
        return total_claim_amount * 0.7 #70% claim
