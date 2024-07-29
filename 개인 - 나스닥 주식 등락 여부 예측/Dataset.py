import pandas as pd
from datetime import timedelta 
import streamlit as st

class DatasetMaker:
    def __init__(self, stock_code, stock_data, timeframe):
        self.stock_code = stock_code
        self.timeframe = timeframe
    
    # 메인 주식 데이터
        # 기존 데이터 불러오기
        try:
            self.old_df = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_{self.timeframe}_train.csv', index_col='날짜')
            self.old_df.index = pd.to_datetime(self.old_df.index)
            self.old_df.index = self.old_df.index.date
        except FileNotFoundError:
            st.write(f"데이터 파일을 찾을 수 없습니다")
        
        # API.PY에서 만든 새로운 데이터 불러오기
        self.new_df = pd.DataFrame(stock_data['output2'])
        self.new_df.index = pd.to_datetime(self.new_df['xymd'], format="%Y%m%d")
        self.new_df.index = self.new_df.index.date 

        self.new_df = self.new_df[['clos','diff','rate','tvol','tamt']].rename(columns={'clos': '종가','diff':'전일대비','rate':'등락률','tvol':'거래량','tamt':'거래대금'})
        self.new_df = self.new_df[['종가','전일대비','등락률','거래량','거래대금']].astype(float)
        
        # 기존 데이터에는 새로운 데이터에 없는 날짜들만 남겨두기
        self.old_df = self.old_df[~self.old_df.index.isin(self.new_df.index)]
                
        # 기존 데이터와 새로운 데이터 합치기
        self.df = pd.concat([self.new_df, self.old_df], ignore_index=False)
        self.df.index.rename("날짜", inplace=True)
        self.df.index = pd.to_datetime(self.df.index, format='%Y-%m-%d')

    # 기업 재무재표 데이터
        self.account_df = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}재무제표.csv')
        self.account_df['날짜'] = pd.to_datetime(self.account_df['날짜'])
        self.account_df = self.account_df.set_index('날짜')

    # 미국 경제 지표 데이터
        self.rate_df = pd.read_csv('C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\경제 지표.csv')
        self.rate_df['날짜'] = pd.to_datetime(self.rate_df['날짜'])
        self.rate_df = self.rate_df.set_index('날짜')

    # 메인 데이터에 합치기    
        self.df['매출액'] = self.df['매출액'].combine_first(self.account_df['매출액'])
        self.df['영업이익'] = self.df['영업이익'].combine_first(self.account_df['영업이익'])
        self.df['당기순이익'] = self.df['당기순이익'].combine_first(self.account_df['당기순이익'])
        self.df['부채비율'] = self.df['부채비율'].combine_first(self.account_df['부채비율'])
        self.df['주당순이익'] = self.df['주당순이익'].combine_first(self.account_df['주당순이익'])
        self.df['ROE'] = self.df['ROE'].combine_first(self.account_df['ROE'])
        self.df['연간매출액'] = self.df['연간매출액'].combine_first(self.account_df['연간매출액'])
        self.df['연간영업이익'] = self.df['연간영업이익'].combine_first(self.account_df['연간영업이익'])
        self.df['연간당기순이익'] = self.df['연간당기순이익'].combine_first(self.account_df['연간당기순이익'])
        self.df['연간부채비율'] = self.df['연간부채비율'].combine_first(self.account_df['연간부채비율'])
        self.df['연간주당순이익'] = self.df['연간주당순이익'].combine_first(self.account_df['연간주당순이익'])
        self.df['연간ROE'] = self.df['연간ROE'].combine_first(self.account_df['연간ROE'])

        self.df['실제 금리'] = self.df['실제 금리'].combine_first(self.rate_df['실제 금리'])
        self.df['예측 금리'] = self.df['예측 금리'].combine_first(self.rate_df['예측 금리'])  
        self.df['이전 금리'] = self.df['이전 금리'].combine_first(self.rate_df['이전 금리'])
        self.df['실제 GDP'] = self.df['실제 GDP'].combine_first(self.rate_df['실제 GDP'])
        self.df['예측 GDP'] = self.df['예측 GDP'].combine_first(self.rate_df['예측 GDP'])          
        self.df['이전 GDP'] = self.df['이전 GDP'].combine_first(self.rate_df['이전 GDP'])
        self.df['실제 GDP 물가지수'] = self.df['실제 GDP 물가지수'].combine_first(self.rate_df['실제 GDP 물가지수'])
        self.df['예측 GDP 물가지수'] = self.df['예측 GDP 물가지수'].combine_first(self.rate_df['예측 GDP 물가지수'])          
        self.df['이전 GDP 물가지수'] = self.df['이전 GDP 물가지수'].combine_first(self.rate_df['이전 GDP 물가지수'])     
        self.df['실제 생산자물가지수 전월 대비'] = self.df['실제 생산자물가지수 전월 대비'].combine_first(self.rate_df['실제 생산자물가지수 전월 대비'])
        self.df['예측 생산자물가지수 전월 대비'] = self.df['예측 생산자물가지수 전월 대비'].combine_first(self.rate_df['예측 생산자물가지수 전월 대비'])          
        self.df['이전 생산자물가지수 전월 대비'] = self.df['이전 생산자물가지수 전월 대비'].combine_first(self.rate_df['이전 생산자물가지수 전월 대비'])  
        self.df['실제 소비자물가지수 전월 대비'] = self.df['실제 소비자물가지수 전월 대비'].combine_first(self.rate_df['실제 소비자물가지수 전월 대비'])
        self.df['예측 소비자물가지수 전월 대비'] = self.df['예측 소비자물가지수 전월 대비'].combine_first(self.rate_df['예측 소비자물가지수 전월 대비'])          
        self.df['이전 소비자물가지수 전월 대비'] = self.df['이전 소비자물가지수 전월 대비'].combine_first(self.rate_df['이전 소비자물가지수 전월 대비'])
        self.df['실제 소비자물가지수 전년 대비'] = self.df['실제 소비자물가지수 전년 대비'].combine_first(self.rate_df['실제 소비자물가지수 전년 대비'])
        self.df['예측 소비자물가지수 전년 대비'] = self.df['예측 소비자물가지수 전년 대비'].combine_first(self.rate_df['예측 소비자물가지수 전년 대비'])          
        self.df['이전 소비자물가지수 전년 대비'] = self.df['이전 소비자물가지수 전년 대비'].combine_first(self.rate_df['이전 소비자물가지수 전년 대비'])
        self.df['실제 무역수지'] = self.df['실제 무역수지'].combine_first(self.rate_df['실제 무역수지'])
        self.df['예측 무역수지'] = self.df['예측 무역수지'].combine_first(self.rate_df['예측 무역수지'])          
        self.df['이전 무역수지'] = self.df['이전 무역수지'].combine_first(self.rate_df['이전 무역수지'])
        self.df['실제 실업률'] = self.df['실제 실업률'].combine_first(self.rate_df['실제 실업률'])
        self.df['예측 실업률'] = self.df['예측 실업률'].combine_first(self.rate_df['예측 실업률'])          
        self.df['이전 실업률'] = self.df['이전 실업률'].combine_first(self.rate_df['이전 실업률'])   
        self.df['실제 내구재 주문'] = self.df['실제 내구재 주문'].combine_first(self.rate_df['실제 내구재 주문'])
        self.df['예측 내구재 주문'] = self.df['예측 내구재 주문'].combine_first(self.rate_df['예측 내구재 주문'])          
        self.df['이전 내구재 주문'] = self.df['이전 내구재 주문'].combine_first(self.rate_df['이전 내구재 주문'])
        self.df['실제 소매판매'] = self.df['실제 소매판매'].combine_first(self.rate_df['실제 소매판매'])
        self.df['예측 소매판매'] = self.df['예측 소매판매'].combine_first(self.rate_df['예측 소매판매'])          
        self.df['이전 소매판매'] = self.df['이전 소매판매'].combine_first(self.rate_df['이전 소매판매'])  
        self.df['실제 ism제조업지수'] = self.df['실제 ism제조업지수'].combine_first(self.rate_df['실제 ism제조업지수'])
        self.df['예측 ism제조업지수'] = self.df['예측 ism제조업지수'].combine_first(self.rate_df['예측 ism제조업지수'])          
        self.df['이전 ism제조업지수'] = self.df['이전 ism제조업지수'].combine_first(self.rate_df['이전 ism제조업지수'])
        self.df['실제 시카고제조업지수'] = self.df['실제 시카고제조업지수'].combine_first(self.rate_df['실제 시카고제조업지수'])
        self.df['예측 시카고제조업지수'] = self.df['예측 시카고제조업지수'].combine_first(self.rate_df['예측 시카고제조업지수'])          
        self.df['이전 시카고제조업지수'] = self.df['이전 시카고제조업지수'].combine_first(self.rate_df['이전 시카고제조업지수'])    
        self.df['실제 건축승인건수'] = self.df['실제 건축승인건수'].combine_first(self.rate_df['실제 건축승인건수'])
        self.df['예측 건축승인건수'] = self.df['예측 건축승인건수'].combine_first(self.rate_df['예측 건축승인건수'])          
        self.df['이전 건축승인건수'] = self.df['이전 건축승인건수'].combine_first(self.rate_df['이전 건축승인건수'])
        self.df['실제 기존주택판매'] = self.df['실제 기존주택판매'].combine_first(self.rate_df['실제 기존주택판매'])
        self.df['예측 기존주택판매'] = self.df['예측 기존주택판매'].combine_first(self.rate_df['예측 기존주택판매'])          
        self.df['이전 기존주택판매'] = self.df['이전 기존주택판매'].combine_first(self.rate_df['이전 기존주택판매'])
        self.df['실제 신규주택판매'] = self.df['실제 신규주택판매'].combine_first(self.rate_df['실제 신규주택판매'])
        self.df['예측 신규주택판매'] = self.df['예측 신규주택판매'].combine_first(self.rate_df['예측 신규주택판매'])          
        self.df['이전 신규주택판매'] = self.df['이전 신규주택판매'].combine_first(self.rate_df['이전 신규주택판매'])
        self.df['실제 CB소비자신뢰지수'] = self.df['실제 CB소비자신뢰지수'].combine_first(self.rate_df['실제 CB소비자신뢰지수'])
        self.df['예측 CB소비자신뢰지수'] = self.df['예측 CB소비자신뢰지수'].combine_first(self.rate_df['예측 CB소비자신뢰지수'])          
        self.df['이전 CB소비자신뢰지수'] = self.df['이전 CB소비자신뢰지수'].combine_first(self.rate_df['이전 CB소비자신뢰지수'])
        self.df['실제 미시간소비자심리지수'] = self.df['실제 미시간소비자심리지수'].combine_first(self.rate_df['실제 미시간소비자심리지수'])
        self.df['예측 미시간소비자심리지수'] = self.df['예측 미시간소비자심리지수'].combine_first(self.rate_df['예측 미시간소비자심리지수'])          
        self.df['이전 미시간소비자심리지수'] = self.df['이전 미시간소비자심리지수'].combine_first(self.rate_df['이전 미시간소비자심리지수'])         
        self.df['실제 비농업고용지수'] = self.df['실제 비농업고용지수'].combine_first(self.rate_df['실제 비농업고용지수'])
        self.df['예측 비농업고용지수'] = self.df['예측 비농업고용지수'].combine_first(self.rate_df['예측 비농업고용지수'])
        self.df['이전 비농업고용지수'] = self.df['이전 비농업고용지수'].combine_first(self.rate_df['이전 비농업고용지수'])
        self.df['공포탐욕지수'] = self.df['공포탐욕지수'].combine_first(self.rate_df['공포탐욕지수'])
        self.df['공포탐욕지수 변동률'] = self.df['공포탐욕지수 변동률'].combine_first(self.rate_df['공포탐욕지수 변동률'])

        self.df['PER'] = round(self.df['종가'] / self.df['연간주당순이익'],2)

        for i, row in self.df.iterrows():
            if row['등락률'] > 0:
                self.df.at[i, '등락여부'] = 1
            else:
                self.df.at[i, '등락여부'] = 0

    # 저장  
        self.df.to_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_{self.timeframe}_train.csv')

    # 테스트 데이터셋 생성
        self.test_df = self.df.iloc[0:1].drop(['종가', '전일대비', '등락여부','등락률','PER'], axis=1)
        self.test_df.index= self.test_df.index + timedelta(days=7)

        self.test_df.to_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_{self.timeframe}_test.csv')    