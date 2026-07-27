class LeavePolicyEngine:


    def evaluate(
        self,
        employee,
        attendance,
        history,
        days_requested
    ):

        reasons = []


        score = 100


        # Leave balance check
        if days_requested > employee["leave_balance"]:
            score -= 50
            reasons.append(
                "Requested days exceed leave balance"
            )


        # Attendance check
        if attendance["attendance_rate"] < 80:
            score -= 20
            reasons.append(
                "Low attendance performance"
            )


        # Previous leave usage
        total_taken = sum(
            item["days_taken"]
            for item in history
        )


        if total_taken > 25:
            score -= 10
            reasons.append(
                "High previous leave usage"
            )


        approved = score >= 60


        return {
            "approved": approved,
            "score": score,
            "reasons": reasons
        }