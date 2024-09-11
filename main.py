import datetime
from utils import get_holdings, get_market_data, rank_stocks, execute_trades
from config import TOP_N_SCRIPTS

# Main strategy execution
def trading_strategy():
    print("Starting trading strategy...")

    # Get current holdings
    holdings = get_holdings()

    # Extract stock symbols from holdings to pass to market feed
    stock_ids = [holding['securityId'] for holding in holdings['data']]

    # Fetch live prices and previous close data
    market_data = get_market_data(stock_ids)

    # Rank stocks
    ranked_stocks = rank_stocks(market_data)

    # Execute trades (sell top gainers, buy top losers)
    execute_trades(TOP_N_SCRIPTS, ranked_stocks, holdings, market_data)

    print("Strategy execution completed.")

# Run the strategy
if __name__ == "__main__":
    trading_strategy()
