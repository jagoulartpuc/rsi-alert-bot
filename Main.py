import time
from RSICalculator import RSICalculator
from binance.client import Client
from telegram import Bot
import asyncio
import requests

client = Client("YOUR_API_KEY", "YOUR_SECRET_KEY")
bot = Bot("5809309564:AAH48xv6FlP94MHcKG74T_P1pqFaSegQNm8")

# Create an instance of the RSICalculator class
calculator = RSICalculator("YOUR_API_KEY", "YOUR_SECRET_KEY")
assets = [symbol['symbol'] for symbol in client.get_exchange_info(
)['symbols'] if symbol['quoteAsset'] == 'USDT']


async def main():
    while True:
        for asset in assets[:100]:
            try:
                rsi = calculator.calculate(asset)
                #print(rsi, asset)
                if rsi < 33:
                    message = "Alert: " + asset + " RSI is lower than 33!"
                    print(message)
                    await bot.send_message(chat_id='-829755881', text=message)
            except requests.exceptions.ReadTimeout:
                print("Connection timeout, retrying in 5 seconds")
                time.sleep(5)
                continue
        await asyncio.sleep(60)

asyncio.run(main())
