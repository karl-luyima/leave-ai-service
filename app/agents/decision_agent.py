class DecisionAgent:


    def decide(
        self,
        context
    ):

        observations = context.get(
            "observations",
            []
        )


        risk = context.get(
            "risk",
            {}
        )


        risk_level = risk.get(
            "risk_level",
            "LOW"
        )


        risk_score = risk.get(
            "risk_score",
            0
        )


        confidence = 0.85



        if risk_level == "HIGH":

            decision = "REJECT"

            confidence = 0.90



        elif risk_level == "MEDIUM":

            decision = "REVIEW"

            confidence = 0.75



        elif risk_score >= 20:

            decision = "REVIEW"

            confidence = 0.80



        else:

            decision = "APPROVE"

            confidence = 0.85




        return {


            "decision": decision,


            "confidence": confidence,


            "risk_level": risk_level,


            "risk_score": risk_score,


            "reason": observations,


            "risk_factors": risk.get(
                "risks",
                []
            ),


            "explanation": (

                f"Decision made based on "

                f"{risk_level} risk assessment."

            )

        }