class DecisionAgent:


    def decide(
        self,
        context
    ):


        observations = context["observations"]

        risk = context["risk"]



        if risk["risk_level"] == "HIGH":


            decision = "REJECT"

            confidence = 0.90



        elif risk["risk_level"] == "MEDIUM":


            decision = "REVIEW"

            confidence = 0.75



        else:


            decision = "APPROVE"

            confidence = 0.85




        return {

            "decision": decision,

            "confidence": confidence,

            "risk_level": risk["risk_level"],

            "risk_score": risk["risk_score"],

            "reason": observations,

            "risk_factors": risk["risks"],

            "explanation":
                f"Decision made based on "
                f"{risk['risk_level']} risk assessment."

        }