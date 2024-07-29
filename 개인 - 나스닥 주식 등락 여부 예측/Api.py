import mojito

class KisApi:
    def __init__(self, stock_code):
        self.stock_code = stock_code

        self.broker = mojito.KoreaInvestment(
            api_key='your thing',
            api_secret='your thing',
            acc_no='your thing',
            exchange='나스닥'
        )

    def get_daily_stock_data(self,timeframe):
        self.timeframe = timeframe

        stock_data = self.broker.fetch_ohlcv(
            symbol=self.stock_code,
            timeframe=timeframe,
            adj_price=False)

        return stock_data