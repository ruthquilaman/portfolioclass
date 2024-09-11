import datetime
from typing import List, Dict

class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def Price(self, date: datetime.date) -> float:
        # This is a placeholder. In a real implementation, this would fetch the actual price.
        return 100  # Dummy price for illustration

class Portfolio:
    def __init__(self):
        self.stocks: Dict[str, int] = {}  # symbol -> quantity

    def AddStock(self, stock: Stock, quantity: int):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity

    def Profit(self, start_date: datetime.date, end_date: datetime.date) -> float:
        start_value = sum(stock.Price(start_date) * quantity for stock, quantity in self.stocks.items())
        end_value = sum(stock.Price(end_date) * quantity for stock, quantity in self.stocks.items())
        return end_value - start_value

    def AnnualizedReturn(self, start_date: datetime.date, end_date: datetime.date) -> float:
        total_days = (end_date - start_date).days
        if total_days <= 0:
            return 0.0

        profit = self.Profit(start_date, end_date)
        start_value = sum(stock.Price(start_date) * quantity for stock, quantity in self.stocks.items())
        
        if start_value == 0:
            return 0.0

        total_return = profit / start_value
        annualized_return = (1 + total_return) ** (365.0 / total_days) - 1
        return annualized_return

# Example usage
portfolio = Portfolio()
apple_stock = Stock("AAPL")
google_stock = Stock("GOOGL")
portfolio.AddStock(apple_stock, 10)
portfolio.AddStock(google_stock, 5)

start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2023, 1, 1)

profit = portfolio.Profit(start_date, end_date)
annualized_return = portfolio.AnnualizedReturn(start_date, end_date)

print(f"Profit: ${profit:.2f}")
print(f"Annualized Return: {annualized_return:.2%}")