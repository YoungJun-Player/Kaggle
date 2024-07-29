import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
import streamlit as st

class Heatmap:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    # 모든 상관 관계
    def all_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv').drop(['날짜'], axis = 1)
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv').drop(['날짜'], axis = 1)
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv').drop(['날짜'], axis = 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 주식 정보들의 상관 관계
    def i_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금','등락여부'])
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금','등락여부'])
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금','등락여부'])

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(5, 5))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(5, 5))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(5, 5))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 경제 지표들의 상관 관계
    def e_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv').drop(['날짜','등락여부','종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'],axis=1)
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv').drop(['날짜','등락여부','종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'],axis=1)
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv').drop(['날짜','등락여부','종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'],axis=1)

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 재무 정보들의 상관 관계
    def f_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv', usecols=['매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv', usecols=['매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv', usecols=['매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(10, 10))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(10, 10))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(10, 10))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 주식 정보와 경제 지표의 상관 관계
    def ie_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv').drop(['날짜','매출액','영업이익','당기순이익','부채비율','주당순이익','ROE','연간매출액','연간영업이익','연간당기순이익','연간부채비율','연간주당순이익','연간ROE'], axis = 1)
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv').drop(['날짜','매출액','영업이익','당기순이익','부채비율','주당순이익','ROE','연간매출액','연간영업이익','연간당기순이익','연간부채비율','연간주당순이익','연간ROE'], axis = 1)
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv').drop(['날짜','매출액','영업이익','당기순이익','부채비율','주당순이익','ROE','연간매출액','연간영업이익','연간당기순이익','연간부채비율','연간주당순이익','연간ROE'], axis = 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 주식정보와 재무정보의 상관 관계
    def if_correct(self):
        
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv', usecols=['종가', '전일대비', '등락률', '거래량', '거래대금', '매출액', '영업이익', '당기순이익', '부채비율', '주당순이익', 'ROE', '연간매출액', '연간영업이익', '연간당기순이익', '연간부채비율', '연간주당순이익', '연간ROE'])

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(15, 15))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=True,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)

    # 경제 지표와 재무 정보의 상관관계
    def ef_correct(self):
        self.df_d = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_D_train.csv').drop(['날짜','종가','전일대비','등락률','등락여부','거래량','거래대금'], axis = 1)
        self.df_w = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_W_train.csv').drop(['날짜','종가','전일대비','등락률','등락여부','거래량','거래대금'], axis = 1)
        self.df_m = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_M_train.csv').drop(['날짜','종가','전일대비','등락률','등락여부','거래량','거래대금'], axis = 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            mask = np.triu(np.ones_like(self.df_d.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_d.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)

            st.write('일')
            st.pyplot(fig)
        
        with col2:
            mask = np.triu(np.ones_like(self.df_w.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_w.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('주')
            st.pyplot(fig)

        with col3:
            mask = np.triu(np.ones_like(self.df_m.corr(), dtype=bool))

            fig, ax = plt.subplots(figsize=(20, 20))

            sns.heatmap(self.df_m.corr(),
                        mask=mask,
                        annot=False,
                        cmap='coolwarm',
                        vmin=-1, vmax=1,
                        ax=ax)
            
            st.write('월')
            st.pyplot(fig)