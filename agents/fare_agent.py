from dotenv import load_dotenv

from schemas.fare_schemas import FareResponse
from tools.fare_tool import get_ticket_price
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage

load_dotenv()

fare_tools = [get_ticket_price]

SYSTEM_PROMPT = """
You are a helpful flight and trip booking and recommendation assistant. 
User will give you an input city and flight ticket budget and using tools you can calculate fare of
destination city and give a recommendation to user whether they can afford the flight or not.
Use get_ticket_price to retrieve the destination fare.

Compare the fare with the user's stated budget.
If fare <= budget, set possible to true and calculate
balance_amount = budget - fare.
Otherwise, set possible to false and balance_amount to null.

Return the final answer using the required FareResponse schema.

Keep the response polite, short and to the point.
"""

system_prompt = SystemMessage(content=SYSTEM_PROMPT)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
).bind_tools(fare_tools)


def fare_agent(state: MessagesState):
    response = llm.invoke([
        system_prompt
    ] + state['messages'])

    return {"messages": [response]}