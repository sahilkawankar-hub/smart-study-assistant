def study_agent(message):
    message = message.lower()

    if "plan" in message or "study" in message:
        return {
            "action": "create_plan",
            "output": "Study plan:\n1. Pick topic\n2. Study 45 minutes\n3. Break 10 minutes\n4. Review notes"
        }

    if "remind" in message:
        return {
            "action": "set_reminder",
            "output": "Reminder saved."
        }

    if "progress" in message:
        return {
            "action": "check_progress",
            "output": "You completed 60 percent of your weekly study goal."
        }

    return {
        "action": "respond",
        "output": "I support study plans, reminders and progress checks."
    }
