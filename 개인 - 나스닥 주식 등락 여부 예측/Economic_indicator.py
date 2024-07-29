import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st
import re

class Economicindicatorcrawling:
    def __init__(self):
        self.rate_df = pd.read_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')
        self.rate_df['날짜'] = pd.to_datetime(self.rate_df['날짜'], format='%Y-%m-%d')
        self.rate_df = self.rate_df.set_index('날짜')

        self.Interest_Rate()
        self.gdp()
        self.gdp_price()
        self.ppi_month()
        self.cpi_month()
        self.cpi_year()
        self.trade_balance()
        self.building_permits()
        self.cb_consumerconfidence()
        self.chicago_manufacturing()
        self.durablegoods_orders()
        self.existing_homesales()
        self.ism_manufacturing()
        self.michigan_consumersentiment()
        self.new_homesales()
        self.nonfarm_payrolls()
        self.retail_sales()
        self.unemployment_rate()
        self.vix()
    
    def Interest_Rate(self):

        url = 'https://kr.investing.com/economic-calendar/interest-rate-decision-168'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 blackFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 금리": actual_value, "예측 금리": expected_value, "이전 금리": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 금리'] = df['실제 금리'].str.replace('%', '').astype(float)
        df['예측 금리'] = df['예측 금리'].str.replace('%', '').astype(float)
        df['이전 금리'] = df['이전 금리'].str.replace('%', '').astype(float)
        # 발표 이후 날짜에 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 금리'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 금리'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 금리'] = df.iloc[0, 2]
        
        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def gdp(self):

        url = 'https://kr.investing.com/economic-calendar/gdp-375'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 GDP": actual_value, "예측 GDP": expected_value, "이전 GDP": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 GDP'] = df['실제 GDP'].str.replace('%', '').astype(float)
        df['예측 GDP'] = df['예측 GDP'].str.replace('%', '').astype(float)
        df['이전 GDP'] = df['이전 GDP'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 GDP'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 GDP'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 GDP'] = df.iloc[0, 2]
        
        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def gdp_price(self):

        url = 'https://kr.investing.com/economic-calendar/gdp-price-index-343'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 blackFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 GDP 물가지수": actual_value, "예측 GDP 물가지수": expected_value, "이전 GDP 물가지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 GDP 물가지수'] = df['실제 GDP 물가지수'].str.replace('%', '').astype(float)
        df['예측 GDP 물가지수'] = df['예측 GDP 물가지수'].str.replace('%', '').astype(float)
        df['이전 GDP 물가지수'] = df['이전 GDP 물가지수'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 GDP 물가지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 GDP 물가지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 GDP 물가지수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def ppi_month(self):

        url = 'https://kr.investing.com/economic-calendar/ppi-238'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold greenFont").text.strip()
            data.append({"날짜": date, "실제 생산자물가지수 전월 대비": actual_value, "예측 생산자물가지수 전월 대비": expected_value, "이전 생산자물가지수 전월 대비": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 생산자물가지수 전월 대비'] = df['실제 생산자물가지수 전월 대비'].str.replace('%', '').astype(float)
        df['예측 생산자물가지수 전월 대비'] = df['예측 생산자물가지수 전월 대비'].str.replace('%', '').astype(float)
        df['이전 생산자물가지수 전월 대비'] = df['이전 생산자물가지수 전월 대비'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 생산자물가지수 전월 대비'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 생산자물가지수 전월 대비'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 생산자물가지수 전월 대비'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def cpi_month(self):

        url = 'https://kr.investing.com/economic-calendar/cpi-69'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 소비자물가지수 전월 대비": actual_value, "예측 소비자물가지수 전월 대비": expected_value, "이전 소비자물가지수 전월 대비": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 소비자물가지수 전월 대비'] = df['실제 소비자물가지수 전월 대비'].str.replace('%', '').astype(float)
        df['예측 소비자물가지수 전월 대비'] = df['예측 소비자물가지수 전월 대비'].str.replace('%', '').astype(float)
        df['이전 소비자물가지수 전월 대비'] = df['이전 소비자물가지수 전월 대비'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 소비자물가지수 전월 대비'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 소비자물가지수 전월 대비'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 소비자물가지수 전월 대비'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def cpi_year(self):

        url = 'https://kr.investing.com/economic-calendar/cpi-733'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 소비자물가지수 전년 대비": actual_value, "예측 소비자물가지수 전년 대비": expected_value, "이전 소비자물가지수 전년 대비": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 소비자물가지수 전년 대비'] = df['실제 소비자물가지수 전년 대비'].str.replace('%', '').astype(float)
        df['예측 소비자물가지수 전년 대비'] = df['예측 소비자물가지수 전년 대비'].str.replace('%', '').astype(float)
        df['이전 소비자물가지수 전년 대비'] = df['이전 소비자물가지수 전년 대비'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 소비자물가지수 전년 대비'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 소비자물가지수 전년 대비'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 소비자물가지수 전년 대비'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv') 

    def trade_balance(self):

        url = 'https://kr.investing.com/economic-calendar/trade-balance-286'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold greenFont").text.strip()
            data.append({"날짜": date, "실제 무역수지": actual_value, "예측 무역수지": expected_value, "이전 무역수지": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 무역수지'] = df['실제 무역수지'].str.replace('B', '').astype(float)*1000000000
        df['예측 무역수지'] = df['예측 무역수지'].str.replace('B', '').astype(float)*1000000000
        df['이전 무역수지'] = df['이전 무역수지'].str.replace('B', '').astype(float)*1000000000

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 무역수지'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 무역수지'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 무역수지'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')   

    def unemployment_rate(self):

        url = 'https://kr.investing.com/economic-calendar/unemployment-rate-300'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 실업률": actual_value, "예측 실업률": expected_value, "이전 실업률": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 실업률'] = df['실제 실업률'].str.replace('%', '').astype(float)
        df['예측 실업률'] = df['예측 실업률'].str.replace('%', '').astype(float)
        df['이전 실업률'] = df['이전 실업률'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 실업률'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 실업률'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 실업률'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv') 

    def durablegoods_orders(self):

        url = 'https://kr.investing.com/economic-calendar/durable-goods-orders-86'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold redFont").text.strip()
            data.append({"날짜": date, "실제 내구재 주문": actual_value, "예측 내구재 주문": expected_value, "이전 내구재 주문": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 내구재 주문'] = df['실제 내구재 주문'].str.replace('%', '').astype(float)
        df['예측 내구재 주문'] = df['예측 내구재 주문'].str.replace('%', '').astype(float)
        df['이전 내구재 주문'] = df['이전 내구재 주문'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 내구재 주문'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 내구재 주문'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 내구재 주문'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv') 

    def retail_sales(self):

        url = 'https://kr.investing.com/economic-calendar/retail-sales-256'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold greenFont").text.strip()
            data.append({"날짜": date, "실제 소매판매": actual_value, "예측 소매판매": expected_value, "이전 소매판매": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 소매판매'] = df['실제 소매판매'].str.replace('%', '').astype(float)
        df['예측 소매판매'] = df['예측 소매판매'].str.replace('%', '').astype(float)
        df['이전 소매판매'] = df['이전 소매판매'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 소매판매'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 소매판매'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 소매판매'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv') 

    def ism_manufacturing(self):

        url = 'https://kr.investing.com/economic-calendar/ism-manufacturing-pmi-173'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 ism제조업지수": actual_value, "예측 ism제조업지수": expected_value, "이전 ism제조업지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 ism제조업지수'] = df['실제 ism제조업지수'].str.replace('%', '').astype(float)
        df['예측 ism제조업지수'] = df['예측 ism제조업지수'].str.replace('%', '').astype(float)
        df['이전 ism제조업지수'] = df['이전 ism제조업지수'].str.replace('%', '').astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 ism제조업지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 ism제조업지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 ism제조업지수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv') 

    def chicago_manufacturing(self):
        url = 'https://kr.investing.com/economic-calendar/chicago-pmi-38'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 시카고제조업지수": actual_value, "예측 시카고제조업지수": expected_value, "이전 시카고제조업지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 시카고제조업지수'] = df['실제 시카고제조업지수'].astype(float)
        df['예측 시카고제조업지수'] = df['예측 시카고제조업지수'].astype(float)
        df['이전 시카고제조업지수'] = df['이전 시카고제조업지수'].astype(float)

        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 시카고제조업지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 시카고제조업지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 시카고제조업지수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def building_permits(self):

        url = 'https://kr.investing.com/economic-calendar/building-permits-25'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 건축승인건수": actual_value, "예측 건축승인건수": expected_value, "이전 건축승인건수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 건축승인건수'] = df['실제 건축승인건수'].str.replace('M', '').astype(float)*1000000
        df['예측 건축승인건수'] = df['예측 건축승인건수'].str.replace('M', '').astype(float)*1000000
        df['이전 건축승인건수'] = df['이전 건축승인건수'].str.replace('M', '').astype(float)*1000000
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 건축승인건수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 건축승인건수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 건축승인건수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def existing_homesales(self):

        url = 'https://kr.investing.com/economic-calendar/existing-home-sales-99'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 기존주택판매": actual_value, "예측 기존주택판매": expected_value, "이전 기존주택판매": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 기존주택판매'] = round(df['실제 기존주택판매'].str.replace('M', '').astype(float)*1000000,2)
        df['예측 기존주택판매'] = round(df['예측 기존주택판매'].str.replace('M', '').astype(float)*1000000,2)
        df['이전 기존주택판매'] = round(df['이전 기존주택판매'].str.replace('M', '').astype(float)*1000000,2)
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 기존주택판매'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 기존주택판매'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 기존주택판매'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def new_homesales(self):

        url = 'https://kr.investing.com/economic-calendar/new-home-sales-222'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold greenFont").text.strip()
            data.append({"날짜": date, "실제 신규주택판매": actual_value, "예측 신규주택판매": expected_value, "이전 신규주택판매": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 신규주택판매'] = df['실제 신규주택판매'].str.replace('K', '').astype(float)*1000
        df['예측 신규주택판매'] = df['예측 신규주택판매'].str.replace('K', '').astype(float)*1000
        df['이전 신규주택판매'] = df['이전 신규주택판매'].str.replace('K', '').astype(float)*1000
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 신규주택판매'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 신규주택판매'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 신규주택판매'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def cb_consumerconfidence(self):

        url = 'https://kr.investing.com/economic-calendar/cb-consumer-confidence-48'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold redFont").text.strip()
            data.append({"날짜": date, "실제 CB소비자신뢰지수": actual_value, "예측 CB소비자신뢰지수": expected_value, "이전 CB소비자신뢰지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 CB소비자신뢰지수'] = df['실제 CB소비자신뢰지수'].astype(float)
        df['예측 CB소비자신뢰지수'] = df['예측 CB소비자신뢰지수'].astype(float)
        df['이전 CB소비자신뢰지수'] = df['이전 CB소비자신뢰지수'].astype(float)
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 CB소비자신뢰지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 CB소비자신뢰지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 CB소비자신뢰지수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def michigan_consumersentiment(self):

        url = 'https://kr.investing.com/economic-calendar/michigan-consumer-sentiment-320'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 redFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold blackFont").text.strip()
            data.append({"날짜": date, "실제 미시간소비자심리지수": actual_value, "예측 미시간소비자심리지수": expected_value, "이전 미시간소비자심리지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 미시간소비자심리지수'] = df['실제 미시간소비자심리지수'].astype(float)
        df['예측 미시간소비자심리지수'] = df['예측 미시간소비자심리지수'].astype(float)
        df['이전 미시간소비자심리지수'] = df['이전 미시간소비자심리지수'].astype(float)
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 미시간소비자심리지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 미시간소비자심리지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 미시간소비자심리지수'] = df.iloc[0, 2]

        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')

    def nonfarm_payrolls(self):

        url = 'https://kr.investing.com/economic-calendar/nonfarm-payrolls-227'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        rows = soup.find_all("div", id="releaseInfo")
        for row in rows:
            date = row.find("div", class_="noBold").text.strip()
            actual_value = row.find("div", class_="arial_14 greenFont").text.strip()
            expected_value = row.find("div", class_="arial_14 noBold").text.strip()
            forecast_value = row.find("div", class_="arial_14 noBold redFont").text.strip()
            data.append({"날짜": date, "실제 비농업고용지수": actual_value, "예측 비농업고용지수": expected_value, "이전 비농업고용지수": forecast_value})
        
        df = pd.DataFrame(data)
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')
        df = df.set_index('날짜')
        df['실제 비농업고용지수'] = df['실제 비농업고용지수'].str.replace('K', '').astype(float)*1000
        df['예측 비농업고용지수'] = df['예측 비농업고용지수'].str.replace('K', '').astype(float)*1000
        df['이전 비농업고용지수'] = df['이전 비농업고용지수'].str.replace('K', '').astype(float)*1000
        
        # 발표 이후 날짜값은 최신값으로 덮어쓰기
        for date in self.rate_df.index:
            if date >= df.index[0]:
                self.rate_df.loc[date, '실제 비농업고용지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '예측 비농업고용지수'] = df.iloc[0, 1]
                self.rate_df.loc[date, '이전 비농업고용지수'] = df.iloc[0, 2]

    def vix(self):            

        url = 'https://kr.investing.com/indices/volatility-s-p-500-historical-data'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        data = []
        
        date = pd.Timestamp.today().date()
        actual_value = soup.find("div", class_="text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]").text.strip()
        actual_value_1 = soup.find("div", class_="flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-positive-main").text.strip()
        
        data.append({"날짜": date, "공포탐욕지수": actual_value, '공포탐욕지수 변동률': actual_value_1})

        def extract_number(s):
            match = re.search(r'\(([+-]?\d+\.\d+)%\)', s)
            if match:
                return float(match.group(1))
            else:
                return None
            
        df = pd.DataFrame(data)
        df = df.head(1)    
        df['공포탐욕지수 변동률'] = df['공포탐욕지수 변동률'].apply(extract_number)
        df['날짜'] = pd.to_datetime(df['날짜'])
        df = df.set_index('날짜')

        df['공포탐욕지수'] = df['공포탐욕지수'].astype(float)
        df['공포탐욕지수 변동률'] = df['공포탐욕지수 변동률'].astype(float)

        for date in self.rate_df.index:
            if date >= df.index:
                self.rate_df.loc[date, '공포탐욕지수'] = df.iloc[0, 0]
                self.rate_df.loc[date, '공포탐욕지수 변동률'] = df.iloc[0, 1]


        self.rate_df.to_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')
        st.write('⭕최신화 완료')