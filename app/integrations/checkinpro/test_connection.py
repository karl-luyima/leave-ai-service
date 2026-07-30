from app.integrations.checkinpro.leave_service import LeaveService


def main():

    service = LeaveService()

    data = service.get_leave_data()


    if data:

        print(" CheckinPro connection successful")

        print("\nEmployee:")
        print(data["name"])

        print("\nEmployee ID:")
        print(data["employee_id"])


        print("\nLeave History:")

        for leave in data["leaves"]:

            print(
                f"- {leave['leave_reason']} | "
                f"{leave['total_leave_days']} days | "
                f"{leave['status']}"
            )


        print("\nLeave Types:")

        for leave_type in data["leave_types"]:

            print(
                f"- {leave_type['title']}: "
                f"{leave_type['days']} days"
            )


    else:

        print(
            " Failed to retrieve CheckinPro data"
        )



if __name__ == "__main__":

    main()