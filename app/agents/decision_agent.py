class DecisionAgent:


    def decide(
        self,
        context
    ):


        observations = context["observations"]

        risk = context.get(
            "risk",
            {}
        )


        decision = "APPROVE"

        confidence = 0.85



        risk_level = risk.get(
            "risk_level",
            "LOW"
        )


        if risk_level == "HIGH":

            decision = "REVIEW"

            confidence = 0.9



        elif risk_level == "MEDIUM":

            decision = "REVIEW"

            confidence = 0.75



        for item in observations:

            if "exceeds the allowed" in item:

                decision = "REJECT"

                confidence = 0.95



        return {

            "decision": decision,

            "confidence": confidence,

            "risk_level": risk_level,

            "risk_score": risk.get(
                "risk_score",
                0
            ),

            "reason": observations,

            "risk_factors": risk.get(
                "risks",
                []
            )

        }