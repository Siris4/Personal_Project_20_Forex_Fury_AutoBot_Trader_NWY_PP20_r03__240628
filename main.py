import metatrader as MT4
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Connect to MetaTrader 4
        mt4 = MT4()
        mt4.initialize()
        logger.info("Connected to MetaTrader 4.")
    except AttributeError as e:
        logger.error(f"Initialization error: {e}")
        return
    except Exception as e:
        logger.error(f"Unexpected error during initialization: {e}")
        return

    try:
        # Log in to your account
        mt4.login(account_number='your_account_number', password='your_password', server='your_broker_server')
        logger.info("Logged into account.")
    except Exception as e:
        logger.error(f"Login error: {e}")
        mt4.shutdown()
        return

    try:
        # Fetch trade history
        trades = mt4.get_trade_history()
        logger.info("Trade history fetched.")
    except Exception as e:
        logger.error(f"Error fetching trade history: {e}")
        mt4.shutdown()
        return

    try:
        # Convert to DataFrame
        df = pd.DataFrame(trades)
        # Display trade history
        print(df)
    except Exception as e:
        logger.error(f"Error converting trades to DataFrame: {e}")

    try:
        # Shutdown connection
        mt4.shutdown()
        logger.info("MetaTrader 4 connection closed.")
    except Exception as e:
        logger.error(f"Error shutting down connection: {e}")

if __name__ == "__main__":
    main()
