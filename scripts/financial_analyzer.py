import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt
# from pypfopt.efficient_frontier import EfficientFrontier
# from pypfopt import risk_models
# from pypfopt import expected_returns



class FinancialAnalyzer:
    def __init__(self, df):
        self.df = df
       

    # def moving_average(self,df, period):
    #     return ta.SMA(df, timeperiod = period) 

    def indicators(self,df):
        df['SMA'] = ta.SMA(df['Close'], timeperiod = 20)
        df['RSI'] = ta.RSI(df['Close'], timeperiod = 14)
        df['EMA'] = ta.EMA(df['Close'], timeperiod = 20)
        df['MACD'], df['MACDsignal'], df['MACDhist'] = ta.MACD(df['Close'], fastperiod = 12, slowperiod = 26, signalperiod = 9)

        return df
    
    def plot_moving_average(self,df):
        plt.figure(figsize=(15, 6))
        plt.plot(df['Date'], df['Close'], label='Close Price', color='blue', linewidth=2)
        plt.plot(df['Date'], df['SMA'], label='Simple Moving Average', color='red', linewidth=2)
        plt.title('Stock Price Moving Average (SMA)')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
    

    def plot_rsi(self,df):
        plt.figure(figsize=(15, 6))
        plt.plot(df['Date'], df['RSI'], label = 'RSI', color='blue', linewidth=2)
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()
        plt.grid(True)
        plt.show()




    def plot_ema(self, data):
        plt.figure(figsize=(15, 6))
        plt.plot(data['Date'], data['Close'], label='Close Price', color='blue', linewidth=2)
        plt.plot(data['Date'], data['EMA'], label='EMA', color='red', linewidth=2)
        plt.title('Exponential Moving Average (EMA)')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_macd(self, data):
        plt.figure(figsize=(15, 6))
        plt.plot(data['Date'], data['MACD'], label='MACD', color='blue', linewidth=2)
        plt.plot(data['Date'], data['MACDsignal'], label='MACDsignal', color='red', linewidth=2)
        plt.title('Moving Average Convergence Divergence (MACD)')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
       

      
        