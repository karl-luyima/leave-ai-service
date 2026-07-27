from app.agents.reminder_agent import LeaveReminderAgent


def test_leave_reminders():

    agent = LeaveReminderAgent()


    reminders = agent.analyze_leave_usage()


    print("\nLEAVE REMINDERS")
    print("----------------")


    if not reminders:

        print("No reminders generated")


    for reminder in reminders:

        print(reminder)



if __name__ == "__main__":

    test_leave_reminders()