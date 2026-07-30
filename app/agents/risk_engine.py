class LeaveRiskEngine:


    def analyze(
        self,
        history,
        days_requested,
        leave_type,
        policies
    ):

        risk_score = 0
        risks = []


        # Check policy limit
        allowed_days = policies.get(
            leave_type,
            0
        )


        if allowed_days == 0:

            risk_score += 40

            risks.append(
                "Leave type not found in company policy"
            )


        elif days_requested > allowed_days:

            risk_score += 50

            risks.append(
                "Requested days exceed company policy limit"
            )



        # Large leave request
        if days_requested > 15:

            risk_score += 30

            risks.append(
                "Large leave duration requested"
            )



        # Pending requests
        pending_requests = [
            leave
            for leave in history
            if leave["status"] == "Pending"
        ]


        if len(pending_requests) > 1:

            risk_score += 20

            risks.append(
                "Employee has multiple pending leave requests"
            )



        # Previous rejected requests
        rejected_requests = [
            leave
            for leave in history
            if leave["status"] == "Reject"
        ]


        if len(rejected_requests) > 0:

            risk_score += 10

            risks.append(
                "Employee has previous rejected leave requests"
            )



        # Risk level

        if risk_score >= 60:

            level = "HIGH"


        elif risk_score >= 30:

            level = "MEDIUM"


        else:

            level = "LOW"



        return {

            "risk_score": risk_score,

            "risk_level": level,

            "risks": risks

        }