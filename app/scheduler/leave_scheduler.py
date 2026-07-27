from apscheduler.schedulers.background import BackgroundScheduler

from app.agents.reminder_agent import LeaveReminderAgent


reminder_agent = LeaveReminderAgent()


def run_leave_reminder():

    print("Running Leave Reminder Agent...")

    reminders = reminder_agent.analyze_leave_usage()

    print(
        f"Generated {len(reminders)} reminders"
    )

    for reminder in reminders:

        print(
            reminder
        )



scheduler = BackgroundScheduler()


scheduler.add_job(
    run_leave_reminder,
    "cron",
    day="last",
    hour=9
)