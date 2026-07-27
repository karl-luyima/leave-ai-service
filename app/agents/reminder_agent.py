from app.providers.database_provider import DatabaseLeaveProvider
from app.notifications.notification_service import NotificationService



class LeaveReminderAgent:


    def __init__(self):

        self.provider = DatabaseLeaveProvider()

        self.notification = NotificationService()



    def analyze_leave_usage(self):

        employees = self.provider.get_all_employees()

        policy = self.provider.get_policy()

        reminders = []


        for employee in employees:


            leave_balance = employee["leave_balance"]


            history = self.provider.get_leave_history(
                employee["id"]
            )


            reasons = []


            # Check unused leave balance
            if leave_balance >= 15:

                reasons.append(
                    f"You have {leave_balance} unused leave days"
                )



            # Check leave usage history
            if not history:

                reasons.append(
                    "You have not taken any recorded leave yet"
                )



            elif len(history) > 0:

                total_taken = sum(
                    record["days_taken"]
                    for record in history
                )


                if total_taken < 5:

                    reasons.append(
                        "You have taken very little leave this cycle"
                    )



            if reasons:


                message = (
                    f"Hi {employee['name']}, "
                    "our leave management system recommends "
                    "that you plan your leave. "
                    + ". ".join(reasons)
                    + "."
                )


                reminder = {

                    "employee_id": employee["id"],

                    "employee": employee["name"],

                    "message": message,

                    "reasons": reasons

                }



                self.notification.send_notification(
                    employee["name"],
                    message
                )


                reminders.append(
                    reminder
                )


        return reminders