from app.workflow.leave_graph import build_leave_graph


graph = build_leave_graph()



def test_normal_leave_request():

    result = graph.invoke(
        {
            "employee_id": 1,
            "days_requested": 5
        }
    )


    print("\nNORMAL REQUEST")
    print("----------------")
    print(result["final_decision"])




def test_large_leave_request():

    result = graph.invoke(
        {
            "employee_id": 1,
            "days_requested": 25
        }
    )


    print("\nLARGE REQUEST")
    print("----------------")
    print(result["final_decision"])




def test_invalid_employee():

    result = graph.invoke(
        {
            "employee_id": 999,
            "days_requested": 10
        }
    )


    print("\nINVALID EMPLOYEE")
    print("----------------")
    print(result["final_decision"])




if __name__ == "__main__":

    test_normal_leave_request()

    test_large_leave_request()

    test_invalid_employee()