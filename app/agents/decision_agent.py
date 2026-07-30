class DecisionAgent:


    def decide(
        self,
        reasoning
    ):


        observations = reasoning["observations"]


        decision = "APPROVE"

        confidence = 0.85


        for item in observations:


            # Policy violation
            if "exceeds the allowed" in item:

                decision = "REJECT"

                confidence = 0.9



            # Unknown leave type
            elif "was not found in company policy" in item:

                decision = "REVIEW"

                confidence = 0.7



            # Existing pending requests
            elif "pending leave request" in item:

                if decision != "REJECT":

                    decision = "REVIEW"

                    confidence = 0.6



        return {

            "decision": decision,

            "confidence": confidence,

            "reason": observations

        }