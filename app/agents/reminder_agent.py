from app.providers.checkinpro_provider import CheckinProProvider
from app.notifications.notification_service import NotificationService



class LeaveReminderAgent:


    def __init__(
        self,
        provider=None
    ):

        self.provider = provider or CheckinProProvider()

        self.notification = NotificationService()



    def analyze_leave_usage(
        self
    ):


        employee = self.provider.get_employee()



        if not employee:

            return {

                "status": "FAILED",

                "message": "Employee data not found."

            }



        policies = self.provider.get_policy()



        history = self.provider.get_leave_history()



        balances = []



        for leave_type, allowed_days in policies.items():


            used_days = 0



            for leave in history:


                leave_type_id = leave.get(
                    "leave_type_id"
                )


                status = leave.get(
                    "status",
                    ""
                )



                if status in [
                    "Approved",
                    "Approve"
                ]:


                    for policy in self.provider.get_leave_types():


                        if (
                            policy["id"]
                            == leave_type_id

                            and

                            policy["title"]
                            == leave_type
                        ):


                            used_days += int(
                                leave.get(
                                    "total_leave_days",
                                    0
                                )
                            )



            remaining_days = (
                allowed_days - used_days
            )



            if remaining_days > 0:


                message = (

                    f"Hi {employee['name']}, "

                    f"you still have "

                    f"{remaining_days} "

                    f"{leave_type} leave days "

                    "available. "

                    "Consider planning your leave "

                    "before the leave cycle ends."

                )



                reminder = {


                    "employee_id": employee["employee_id"],


                    "employee": employee["name"],


                    "leave_type": leave_type,


                    "allowed_days": allowed_days,


                    "used_days": used_days,


                    "remaining_days": remaining_days,


                    "action": "SEND_REMINDER",


                    "message": message


                }



                self.notification.send_notification(

                    employee["name"],

                    message

                )



                balances.append(
                    reminder
                )



        return {


            "employee": employee,


            "reminders": balances

        }