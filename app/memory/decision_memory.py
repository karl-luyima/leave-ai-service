decisions = []


def save_decision(decision):

    decisions.append(decision)



def get_previous_decisions(employee_id):

    return [
        d for d in decisions
        if d["employee_id"] == employee_id
    ]