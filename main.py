import yfinance as yf
import matplotlib.pyplot as plt

ticker = input("Name of Stock: ")
data = yf.download(ticker, start="2021-01-01", end="2023-03-03")

plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(f"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()