from operator import truediv

from dotenv import load_dotenv
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from agents.classifier import classifier_agent, ClassificationState
from agents.fare_agent import fare_agent
from agents.fare_agent import fare_tools
from langchain_core.messages import HumanMessage

load_dotenv(override=True)

def classification_condition(state: ClassificationState):
    if state["is_valid"]:
        return "TRUE"
    return "FALSE"

graph_builder = StateGraph(MessagesState)

graph_builder.add_node("classifier_agent", classifier_agent)
graph_builder.add_node("fare_agent", fare_agent)
graph_builder.add_node("fare_tools", ToolNode(fare_tools))

graph_builder.add_edge(START, "classifier_agent")
graph_builder.add_conditional_edges("classifier_agent", classification_condition, {
    "TRUE": "fare_agent",
    "FALSE": END
})
graph_builder.add_conditional_edges("fare_agent", tools_condition, {
    "tools": "fare_tools",
    "__end__": END
})
graph_builder.add_edge("fare_tools", "fare_agent")
graph_builder.add_edge("fare_agent", END)

graph = graph_builder.compile()

def main():
    print("Hello from langgraph-course!")

    result = graph.invoke({
        "messages": [HumanMessage(content="What is the fare of a flight to Tokyo? My budget is USD 1200")]
        # "messages": [HumanMessage(content="How much does an iPhone 17 cost?")]
        })
    print(result["messages"][-1].content[0]['text'])

if __name__ == "__main__":
    main()
