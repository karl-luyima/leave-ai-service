from app.workflow.leave_graph import build_leave_graph


graph = build_leave_graph()


result = graph.invoke(
    {
        "employee_id": 1,
        "days_requested": 10
    }
)


print("\nFINAL AI DECISION")
print("-----------------")

print(result["final_decision"])