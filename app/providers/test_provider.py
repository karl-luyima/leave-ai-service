from app.providers.dummy_provider import DummyLeaveProvider


provider = DummyLeaveProvider()


employee = provider.get_employee(1001)

print(employee)


history = provider.get_leave_history(1001)

print(
    "Leave records:",
    len(history)
)


attendance = provider.get_attendance(1001)

print(attendance)


policy = provider.get_policy()

print(policy)