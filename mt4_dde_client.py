import win32com.client
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Create a DDE client
        dde = win32com.client.Dispatch("DDEClient.DDEClient")
        logger.info("DDE client created.")
    except Exception as e:
        logger.error(f"Error initializing DDE client: {e}")
        return

    try:
        # Connect to MT4's DDE server
        dde.Connect("MT4", "BID")
        logger.info("Connected to MT4 DDE server.")
    except Exception as e:
        logger.error(f"Error connecting to MT4 DDE server: {e}")
        return

    try:
        # Request data
        eurusd_bid = dde.Request("EURUSD")
        logger.info("Data requested from MT4 DDE server.")
        print("EURUSD Bid: ", eurusd_bid)
    except Exception as e:
        logger.error(f"Error requesting data from MT4 DDE server: {e}")

    try:
        # Disconnect
        dde.Disconnect()
        logger.info("Disconnected from MT4 DDE server.")
    except Exception as e:
        logger.error(f"Error disconnecting from MT4 DDE server: {e}")

if __name__ == "__main__":
    main()
