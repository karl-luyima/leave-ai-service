def requires_human_review(decision):

    if decision["recommendation"] == "REVIEW":
        return True

    return False