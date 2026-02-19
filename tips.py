def get_pricing_tips(scenario: str) -> str:
    """Get pricing psychology tips for different scenarios"""
    
    tips = {
        "free-to-paid": """
[bold]Transitioning from Free to Paid:[/bold]

• Start with a freemium model - keep basic features free
• Introduce paid tiers gradually (e.g., "Pro" features)
• Communicate value clearly: what problems does paid solve?
• Offer early-bird discounts to existing users (e.g., 50% off first year)
• Don't apologize for charging - you're providing value
• Example: "Free: 100 requests/month, Pro ($29/mo): unlimited + priority support"

[yellow]Key insight:[/yellow] Only 2-5% of free users typically convert. That's normal!
Your 5000 visitors could mean 100-250 paying customers = $2,900-$7,250/month at $29/user.
        """,
        
        "negotiation": """
[bold]Handling Price Negotiations:[/bold]

• Know your walk-away price (minimum acceptable)
• Never discount without getting something back (e.g., longer contract, referrals)
• Use anchoring: present highest price first
• Offer package deals instead of discounts
• Say "I can adjust scope to fit your budget" not "I can lower my price"
• Practice saying: "My price reflects the value and quality you'll receive"

[yellow]Key insight:[/yellow] Clients who push hardest on price often cause most problems.
Sometimes losing a deal is winning.
        """,
        
        "handmade": """
[bold]Pricing Handmade Products:[/bold]

• Formula: (Materials + Labor + Overhead) × 2 = Wholesale, × 4 = Retail
• Don't compete on price with mass production - compete on uniqueness
• Tell your story: handmade, custom, limited quantity
• Use psychological pricing: $47 feels cheaper than $50
• Bundle products: "Set of 3 for $120" (vs $50 each)
• Offer customization at premium prices

[yellow]Key insight:[/yellow] People who say "too expensive" aren't your customers.
Your customers value craftsmanship and uniqueness.
        """,
        
        "complex": """
[bold]Simplifying Complex Pricing:[/bold]

• Offer 3 clear tiers: Good, Better, Best
• Use comparison tables to show differences
• Name tiers by outcome, not features (e.g., "Starter", "Growth", "Enterprise")
• Hide complexity behind simple monthly prices
• Provide a pricing calculator for custom needs
• Lead with most popular option

[yellow]Key insight:[/yellow] Confused customers don't buy.
Make the decision easy with clear recommendations.
        """
    }
    
    return tips.get(scenario.lower(), "")
