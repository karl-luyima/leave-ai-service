from app.providers.checkinpro_provider import CheckinProProvider

from app.agents.observation_agent import ObservationAgent

from app.agents.reasoning_agent import ReasoningAgent

from app.agents.decision_agent import DecisionAgent

from app.agents.action_agent import ActionAgent



provider = CheckinProProvider()


observation_agent = ObservationAgent(
    provider
)


reasoning_agent = ReasoningAgent()


decision_agent = DecisionAgent()


action_agent = ActionAgent()



context = observation_agent.observe()


reasoning = reasoning_agent.analyze(
    context
)


decision = decision_agent.decide(
    reasoning
)


result = action_agent.execute(
    decision
)



print(result)