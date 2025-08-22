# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOG": 140
}

# Take input from user
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("Stock not available in database!")

# Calculate total investment
total = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())
print("\nYour Portfolio:", portfolio)
print("Total Investment Value: $", total)

# Optionally save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Portfolio: {portfolio}\n")
    f.write(f"Total Investment Value: ${total}\n")
