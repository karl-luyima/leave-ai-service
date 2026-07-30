class RiskAssessmentAgent:


    def __init__(
        self,
        risk_engine
    ):

        self.risk_engine = risk_engine



    def assess(
        self,
        context
    ):

        result = self.risk_engine.analyze(

            employee=context["employee"],

            attendance={
                "attendance_rate": 100
            },

            history=context["leave_history"],

            days_requested=context["leave_request"]["days_requested"]

        )


        risk_score = result["risk_score"]



        if risk_score >= 60:

            risk_level = "HIGH"


        elif risk_score >= 30:

            risk_level = "MEDIUM"


        else:

            risk_level = "LOW"



        return {

            "risk_score": risk_score,

            "risk_level": risk_level,

            "risks": result["risks"]

        }