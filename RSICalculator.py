from binance.client import Client

class RSICalculator:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def calculate(self, symbol):
        # Retrieve historical price data for BTCUSDT
        candSticks = self.client._klines(symbol=symbol, interval=Client.KLINE_INTERVAL_15MINUTE)
        # Initialize variables for RSI calculation
        gain_sum = 0
        loss_sum = 0
        previous_close = 0
        for candStick in candSticks:
            close = float(candStick[4])
            if previous_close != 0:
                change = close - previous_close
                if change > 0:
                    gain_sum += change
                else:
                    loss_sum += abs(change)
            previous_close = close

        # Calculate average gain and average loss
        period = 14
        avg_gain = gain_sum / period
        avg_loss = loss_sum / period
        
        # Calculate RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi