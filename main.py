import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from models import CostInput, PricingStrategy
from calculator import calculate_costs, generate_pricing_strategies
from tips import get_pricing_tips

app = typer.Typer(help="A CLI tool to help entrepreneurs make confident pricing decisions")
console = Console()

@app.command()
def calculate(
    time_hours: float = typer.Option(..., "--time", "-t", help="Time spent in hours"),
    material_cost: float = typer.Option(0.0, "--material", "-m", help="Material cost"),
    overhead_cost: float = typer.Option(0.0, "--overhead", "-o", help="Monthly overhead cost"),
    hourly_rate: float = typer.Option(50.0, "--rate", "-r", help="Desired hourly rate"),
    target_margin: float = typer.Option(30.0, "--margin", help="Target profit margin (%)"),
):
    """Calculate true costs and generate pricing strategies"""
    
    cost_input = CostInput(
        time_hours=time_hours,
        material_cost=material_cost,
        overhead_cost=overhead_cost,
        hourly_rate=hourly_rate,
        target_margin=target_margin
    )
    
    total_cost = calculate_costs(cost_input)
    strategies = generate_pricing_strategies(total_cost, cost_input.target_margin)
    
    # Display cost breakdown
    console.print("\n[bold cyan]Cost Breakdown[/bold cyan]")
    cost_table = Table(show_header=True)
    cost_table.add_column("Item", style="cyan")
    cost_table.add_column("Amount", justify="right", style="green")
    
    cost_table.add_row("Labor Cost", f"${cost_input.time_hours * cost_input.hourly_rate:.2f}")
    cost_table.add_row("Material Cost", f"${cost_input.material_cost:.2f}")
    cost_table.add_row("Overhead Cost", f"${cost_input.overhead_cost:.2f}")
    cost_table.add_row("[bold]Total Cost[/bold]", f"[bold]${total_cost:.2f}[/bold]")
    
    console.print(cost_table)
    
    # Display pricing strategies
    console.print("\n[bold cyan]Pricing Strategies[/bold cyan]")
    strategy_table = Table(show_header=True)
    strategy_table.add_column("Strategy", style="cyan")
    strategy_table.add_column("Price", justify="right", style="green")
    strategy_table.add_column("Profit", justify="right", style="yellow")
    strategy_table.add_column("Margin", justify="right", style="magenta")
    
    for strategy in strategies:
        strategy_table.add_row(
            strategy.name,
            f"${strategy.price:.2f}",
            f"${strategy.profit:.2f}",
            f"{strategy.margin:.1f}%"
        )
    
    console.print(strategy_table)

@app.command()
def tips(
    scenario: str = typer.Argument(..., help="Scenario: free-to-paid, negotiation, handmade, or complex")
):
    """Get pricing psychology tips for common scenarios"""
    
    tips_content = get_pricing_tips(scenario)
    
    if tips_content:
        console.print(Panel(tips_content, title=f"[bold cyan]Tips: {scenario.title()}[/bold cyan]", border_style="cyan"))
    else:
        console.print("[red]Unknown scenario. Available: free-to-paid, negotiation, handmade, complex[/red]")

@app.command()
def quick(
    cost: float = typer.Argument(..., help="Total cost of product/service"),
    margin: float = typer.Option(30.0, "--margin", "-m", help="Target profit margin (%)")
):
    """Quick pricing calculation from total cost"""
    
    strategies = generate_pricing_strategies(cost, margin)
    
    console.print(f"\n[bold cyan]Quick Pricing for ${cost:.2f} cost[/bold cyan]\n")
    
    for strategy in strategies:
        console.print(f"[bold]{strategy.name}:[/bold] ${strategy.price:.2f} (profit: ${strategy.profit:.2f}, margin: {strategy.margin:.1f}%)")

if __name__ == "__main__":
    app()
