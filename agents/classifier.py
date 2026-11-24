from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import MessagesState

load_dotenv()

CLASSIFICATION_SYSTEM_PROMPT = """
You are a classifier for an airline aggregator application. Your role is to classify input user messages.
If the query is regarding booking an airline journey, then that request is valid can be answered.
Simply return the string "true" without adding anything else in the output.
E.g.:
Query: What is the fare of a flight to Paris? My budget is USD 1200.
Answer: true
Reason: The query is regarding the inquiry related to fare of a flight.

If the request is outside the scope of the flight booking, then that request is invalid.
Simply return the string "false" without adding anything else in the output.
E.g.:
Query: How is the weather today?
Answer: false
Reason: The query is a general query without a specific intent related to flight travel.
"""

classifier_system_prompt = SystemMessage(CLASSIFICATION_SYSTEM_PROMPT)

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

class ClassificationState(MessagesState):
    is_valid: bool

def classifier_agent(state: ClassificationState):
    response = llm.invoke([
        classifier_system_prompt
    ] + state["messages"])
    is_valid = response.content[0]["text"].strip().lower() == "true"

    if is_valid:
        return {"is_valid": is_valid}

    response_message = AIMessage([{"text": "Unsupported query. Please input a valid query related to flight booking"}])
    return {
        "is_valid": is_valid,
        "messages": state["messages"] + [response_message]
    }