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


        # Normalize leave type matching
        allowed_days = 0

        for policy_name, days in policies.items():

            if (
                leave_type.lower() == policy_name.lower()
                or leave_type.lower() in policy_name.lower()
                or policy_name.lower() in leave_type.lower()
            ):
                allowed_days = days
                break



        # Check policy limit

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



        # Large leave duration

        if days_requested > 15:

            risk_score += 20

            risks.append(
                "Large leave duration requested"
            )



        # Pending requests

        pending_requests = [

            leave

            for leave in history

            if leave.get("status","").lower() == "pending"

        ]



        # Only consider excessive pending requests

        if len(pending_requests) > 2:

            risk_score += 20

            risks.append(
                "Employee has multiple pending leave requests"
            )



        # Previous rejected requests

        rejected_requests = [

            leave

            for leave in history

            if leave.get("status","").lower() in [
                "reject",
                "rejected"
            ]

        ]



        if rejected_requests:

            risk_score += 10

            risks.append(
                "Employee has previous rejected leave requests"
            )



        # Remove duplicate risks

        risks = list(
            dict.fromkeys(risks)
        )



        # Risk classification

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