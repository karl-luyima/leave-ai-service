from app.agents.observation_agent import ObservationAgent
from app.agents.reasoning_agent import ReasoningAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.action_agent import ActionAgent


class LeaveAIService:


    def __init__(
        self,
        provider
    ):

        self.observation_agent = ObservationAgent(provider)

        self.reasoning_agent = ReasoningAgent()

        self.decision_agent = DecisionAgent()

        self.action_agent = ActionAgent()



    def process_leave(
        self,
        employee_id=None
    ):

        context = self.observation_agent.observe(
            employee_id
        )

        reasoning = self.reasoning_agent.analyze(
            context
        )

        decision = self.decision_agent.decide(
            reasoning
        )

        action = self.action_agent.execute(
            decision
        )


        return action