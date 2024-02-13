import candidate_selection

def test_candidate_selection():
    candidate_name = "Judith Evans"
    score = 85

    selected = candidate_selection.select_candidate(candidate_name, score)

    assert selected is True
