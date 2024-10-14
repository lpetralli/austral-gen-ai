from langchain.tools.retriever import create_retriever_tool

def create_retriever_tool_from_vectorstore(vectorstore):
    retriever = vectorstore.as_retriever()
    return create_retriever_tool(
        retriever,
        "retrieve_company_docs",
        "Search and return information about AutoCare",
    )

from typing import Dict, Literal
from pydantic import BaseModel, Field
from langchain.tools import BaseTool

CarModelOptions = Literal["Model S", "Model 3", "Model X", "Model Y", "Cybertruck"]

class CarModelInput(BaseModel):
    model: CarModelOptions = Field(..., description="The model of the car")

class CarPriceOutput(BaseModel):
    model: CarModelOptions
    price: float

class GetCarPriceTool(BaseTool):
    name: str = "get_car_price"
    description: str = "Retrieves the price of a car based on its model"
    args_schema: type[CarModelInput] = CarModelInput

    def _run(self, model: CarModelOptions) -> Dict:
        # Mocked car price data
        car_prices = {
            "Model S": 79990.0,
            "Model 3": 39990.0,
            "Model X": 89990.0,
            "Model Y": 49990.0,
            "Cybertruck": 39900.0,
        }

        if model not in car_prices:
            available_models = ", ".join(car_prices.keys())
            raise ValueError(f"Invalid car model. Available models are: {available_models}")

        price = car_prices[model]
        return CarPriceOutput(model=model, price=price).dict()

def create_get_car_price_tool():
    return GetCarPriceTool()