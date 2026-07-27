class LeaveRiskEngine:


    def analyze(
        self,
        employee,
        attendance,
        history,
        days_requested
    ):

        risk_score = 0
        risks = []


        # Large leave request
        if days_requested > 15:
            risk_score += 30
            risks.append(
                "Large number of leave days requested"
            )


        # Poor attendance
        if attendance["attendance_rate"] < 80:
            risk_score += 30
            risks.append(
                "Low attendance rate"
            )


        # Frequent leave usage
        total_leave = sum(
            item["days_taken"]
            for item in history
        )


        if total_leave > 25:
            risk_score += 20
            risks.append(
                "High previous leave usage"
            )


        return {
            "risk_score": risk_score,
            "risks": risks
        }