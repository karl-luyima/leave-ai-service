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


        history = context["leave_history"]

        leave_request = context["leave_request"]

        policies = context["policies"]



        result = self.risk_engine.analyze(

            history,

            leave_request["days_requested"],

            leave_request["leave_type"],

            policies

        )


        return result