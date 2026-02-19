from pydantic import BaseModel, Field

class CostInput(BaseModel):
    time_hours: float = Field(gt=0, description="Time spent in hours")
    material_cost: float = Field(ge=0, description="Material cost")
    overhead_cost: float = Field(ge=0, description="Overhead cost")
    hourly_rate: float = Field(gt=0, description="Desired hourly rate")
    target_margin: float = Field(gt=0, le=100, description="Target profit margin percentage")

class PricingStrategy(BaseModel):
    name: str
    price: float
    profit: float
    margin: float
    description: str
