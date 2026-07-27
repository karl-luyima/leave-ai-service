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


        # Get reminder threshold from company policy
        unused_leave_threshold = policy.get(
            "unused_leave_threshold",
            15
        )


        for employee in employees:


            leave_balance = employee["leave_balance"]


            history = self.provider.get_leave_history(
                employee["id"]
            )


            reasons = []


            confidence = 0



            # Analyze unused leave balance
            if leave_balance >= unused_leave_threshold:

                reasons.append(
                    f"You have {leave_balance} unused leave days"
                )

                confidence += 0.5



            # Analyze leave history
            if not history:

                reasons.append(
                    "You have not taken any recorded leave yet"
                )

                confidence += 0.3



            else:

                total_taken = sum(
                    record["days_taken"]
                    for record in history
                )


                if total_taken < 5:

                    reasons.append(
                        "You have taken very little leave this cycle"
                    )

                    confidence += 0.2



            # Decide whether action is needed
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

                    "action": "SEND_REMINDER",

                    "confidence": round(
                        confidence,
                        2
                    ),

                    "message": message,

                    "reasons": reasons

                }



                # Send notification
                self.notification.send_notification(
                    employee["name"],
                    message
                )


                reminders.append(
                    reminder
                )



        return reminders