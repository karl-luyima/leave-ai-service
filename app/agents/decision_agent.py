class DecisionAgent:


    def decide(
        self,
        reasoning
    ):


        observations = reasoning["observations"]


        decision = "APPROVE"


        confidence = 0.8


        for item in observations:

            if "pending leave request" in item:

                decision = "REVIEW"

                confidence = 0.6



        return {

            "decision": decision,

            "confidence": confidence,

            "reason": observations

        }