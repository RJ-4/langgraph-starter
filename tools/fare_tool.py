from langchain_core.tools import tool

@tool
def get_ticket_price(city: str) -> float:
    """
    Takes city name as input and returns the fare of flight ticket to the input city in USD
    :param city: Name of the city to which fare of flight ticket is to be retrieved
    :return: Fare of the flight ticket to the city in USD
    """
    fare_dict = {
        "Paris": 1000,
        "New York": 1200,
        "Tokyo": 2000,
        "New Delhi": 800,
        "Dubai": 400
    }

    return fare_dict[city]