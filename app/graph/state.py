from typing import TypedDict, Any


class LeaveState(TypedDict):

    employee_id: int | None

    observation: dict | None

    reasoning: dict | None

    decision: dict | None

    action: dict | None