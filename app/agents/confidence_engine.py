class ConfidenceEngine:


    def calculate(
        self,
        policy_score,
        risk_score
    ):

        confidence = (
            policy_score - risk_score
        )


        if confidence < 0:
            confidence = 0


        if confidence > 100:
            confidence = 100


        if confidence >= 80:
            recommendation = "AUTO_APPROVE"

        elif confidence >= 50:
            recommendation = "REVIEW"

        else:
            recommendation = "REJECT"



        return {
            "confidence": confidence,
            "recommendation": recommendation
        }