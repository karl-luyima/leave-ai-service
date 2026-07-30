from typing import TypedDict


class LeaveState(TypedDict):

    employee_id: int | None

    leave_request: dict | None

    observation: dict | None

    reasoning: dict | None

    decision: dict | None

    action: dict | None