from pydantic import BaseModel, Field

class FareResponse(BaseModel):
    """
    Class representing template of an instance of the response by flight fare planner agent/
    """
    possible: bool = Field(description="True if the ticket fare is less than or equal to the budget.")
    message: str = Field(description="A concise explanation of whether the flight is affordable.")
    balance_amount: float | None = Field(description="Budget minus ticket fare when affordable; otherwise None")