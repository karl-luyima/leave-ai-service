from app.agents.leave_agent import LeaveAgent


agent = LeaveAgent()


result = agent.analyze_leave_request(
    employee_id=1,
    days_requested=10
)


print(result)