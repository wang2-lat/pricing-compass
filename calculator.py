from models import CostInput, PricingStrategy

def calculate_costs(cost_input: CostInput) -> float:
    """Calculate total cost"""
    labor_cost = cost_input.time_hours * cost_input.hourly_rate
    total_cost = labor_cost + cost_input.material_cost + cost_input.overhead_cost
    return total_cost

def generate_pricing_strategies(total_cost: float, target_margin: float) -> list[PricingStrategy]:
    """Generate three pricing strategies"""
    
    # Budget strategy: lower margin for volume
    budget_margin = target_margin * 0.6
    budget_price = total_cost * (1 + budget_margin / 100)
    
    # Standard strategy: target margin
    standard_price = total_cost * (1 + target_margin / 100)
    
    # Premium strategy: higher margin for value
    premium_margin = target_margin * 1.5
    premium_price = total_cost * (1 + premium_margin / 100)
    
    strategies = [
        PricingStrategy(
            name="Budget",
            price=budget_price,
            profit=budget_price - total_cost,
            margin=budget_margin,
            description="Lower price for volume sales"
        ),
        PricingStrategy(
            name="Standard",
            price=standard_price,
            profit=standard_price - total_cost,
            margin=target_margin,
            description="Target margin pricing"
        ),
        PricingStrategy(
            name="Premium",
            price=premium_price,
            profit=premium_price - total_cost,
            margin=premium_margin,
            description="Higher price for premium positioning"
        )
    ]
    
    return strategies
