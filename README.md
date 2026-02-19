# Pricing Compass

A CLI tool to help entrepreneurs make confident pricing decisions.

## Installation


## Usage

### Calculate costs and generate pricing strategies


Options:
- `--time, -t`: Time spent in hours (required)
- `--material, -m`: Material cost (default: 0)
- `--overhead, -o`: Overhead cost (default: 0)
- `--rate, -r`: Desired hourly rate (default: 50)
- `--margin`: Target profit margin in % (default: 30)

### Quick pricing from total cost


### Get pricing psychology tips


## Examples

**Freelance service pricing:**

**Handmade product pricing:**

**Get advice on transitioning from free to paid:**

## Features

- **Cost Calculator**: Calculate true costs including time, materials, and overhead
- **Pricing Strategies**: Generate 3 pricing tiers (Budget, Standard, Premium)
- **Psychology Tips**: Practical advice for common pricing scenarios
- **Simple CLI**: Easy-to-use command-line interface with rich formatting
python main.py calculate --time 10 --material 50 --rate 75 --margin 40
python main.py quick 500 --margin 35
python main.py tips free-to-paid
python main.py tips negotiation
python main.py tips handmade
python main.py tips complex
pip install -r requirements.txt
python main.py --help