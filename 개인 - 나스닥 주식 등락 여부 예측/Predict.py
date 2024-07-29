import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import lightgbm as lgb
from sklearn.metrics import f1_score
import streamlit as st
from streamlit.components.v1 import html

class Predict:
    def __init__(self,stock_code, timeframe):
        self.stock_code = stock_code
        self.timeframe = timeframe

        df = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_{self.timeframe}_train.csv')
        test_df = pd.read_csv(f'C:\\Users\\yjpak\\OneDrive\\바탕 화면\\investing\\Data\\{self.stock_code}_{self.timeframe}_test.csv')

        df['날짜'] = pd.to_datetime(df['날짜'])
        df['날짜'] = df['날짜'].dt.strftime('%Y%m%d').astype(int)
        df.set_index('날짜', inplace=True)

        test_df['날짜'] = pd.to_datetime(test_df['날짜'])
        test_df['날짜'] = test_df['날짜'].dt.strftime('%Y%m%d').astype(int)
        test_df.set_index('날짜', inplace=True)

        X = df.drop(['종가','전일대비','등락여부','등락률','PER'], axis = 1)
        y = df['등락여부']

        X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.9, random_state=None)

        scaler = MinMaxScaler()

        X_train = scaler.fit_transform(X_train)
        X_val= scaler.transform(X_val)
        test = scaler.fit_transform(test_df)

        model = lgb.LGBMClassifier(verbose=-1,
                            colsample_bytree = 0.5,
                            feature_fraction = 0.5,
                            is_unbalance = True,
                            learning_rate = 0.01916053217071907,
                            max_bin = 300,
                            max_depth = 50,
                            min_child_samples = 24,
                            min_split_gain = 0.04118318861314671,
                            n_estimators = 300,
                            num_leaves = 2,
                            objective = 'binary',
                            reg_alpha = 1,
                            reg_lambda = 0.6,
                            subsample = 0.5,
                            subsample_freq = 4)

        model.fit(X_train, y_train)


        preds = model.predict(X_val)

        f1 = round(f1_score(y_val, preds) *100,0).astype(int)

        preds = model.predict(test)

        # 예측 결과 출력
        col1, col2,col3 = st.columns(3)

        # 시간 정보 출력
        with col1:
            if self.timeframe == 'D':
                time = '내일'
            elif self.timeframe == 'W':
                time = '다음주'
            else:
                time = '다음달'

            st.success(f'{time}')

        # 예측 결과 출력
        with col2:
            if preds.item() == 1:
                icon = '🔺'
                st.error(f'{icon} 상승')
            else:
                icon = '🔻'
                st.info(f'{icon} 하락')

        # 확률 출력
        with col3:
            st.warning(f"정확도: {f1}%")