from langgraph.graph import StateGraph, END

from app.graph.state import LeaveState

from app.agents.observation_agent import ObservationAgent
from app.agents.reasoning_agent import ReasoningAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.action_agent import ActionAgent



def build_leave_graph(provider):


    observation_agent = ObservationAgent(
        provider
    )

    reasoning_agent = ReasoningAgent()

    decision_agent = DecisionAgent()

    action_agent = ActionAgent()



    graph = StateGraph(
        LeaveState
    )


    def observation_node(state):

        result = observation_agent.observe(
            state["employee_id"]
        )

        return {
            "observation": result
        }



    def reasoning_node(state):

        result = reasoning_agent.analyze(
            state["observation"]
        )

        return {
            "reasoning": result
        }



    def decision_node(state):

        result = decision_agent.decide(
            state["reasoning"]
        )

        return {
            "decision": result
        }



    def action_node(state):

        result = action_agent.execute(
            state["decision"]
        )

        return {
            "action": result
        }



    graph.add_node(
        "observation",
        observation_node
    )

    graph.add_node(
        "reasoning",
        reasoning_node
    )

    graph.add_node(
        "decision",
        decision_node
    )

    graph.add_node(
        "action",
        action_node
    )



    graph.set_entry_point(
        "observation"
    )


    graph.add_edge(
        "observation",
        "reasoning"
    )

    graph.add_edge(
        "reasoning",
        "decision"
    )

    graph.add_edge(
        "decision",
        "action"
    )


    graph.add_edge(
        "action",
        END
    )


    return graph.compile()