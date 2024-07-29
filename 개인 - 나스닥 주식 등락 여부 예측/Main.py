from Api import KisApi
from Dataset import DatasetMaker
from Economic_indicator import Economicindicatorcrawling
from Predict import Predict
from Virtual import Heatmap
import streamlit as st

# main 함수 설정
def main(timeframe):
    kis_api = KisApi(stock_code)
    stock_data = kis_api.get_daily_stock_data(timeframe)

    DatasetMaker(stock_code, stock_data,timeframe)

    Predict(stock_code, timeframe)

# 구분선 무지개색 설정
st.markdown("""<style>
hr {
    background-image: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
    border: none;
}
</style>
""", unsafe_allow_html=True)

# 웹 페이지 제목
st.header('💰AI로 하는 주식 예측')

# 데이터 최신화 버튼
if st.button('데이터 최신화하기'):
    Economicindicatorcrawling()

# 종목입력 칸
st.write("""---""")
st.subheader('🔍원하는 주식 종목을 입력하세요')
stock_code=st.text_input('',placeholder='예) AAPL')

# 종목 입력 후
if not stock_code:
    st.write("종목 코드를 입력해주세요.")

else:
    st.write("""---""")

    # 예측 칸
    st.subheader(f'🧠{stock_code} 예측')
    main(timeframe='D')
    main(timeframe='W')
    main(timeframe='M')

    if st.button('새로고침'):
        main(timeframe='D')
        main(timeframe='W')
        main(timeframe='M')

    # 분석 그래프 확인 칸
    st.write("""---""")
    st.subheader('📊 분석 그래프 확인')

    #분석 그래프 선택 사이드바
    st.sidebar.title('📊 분석 그래프')

    # 상관관계 히트맵   
    st.sidebar.subheader('상관 관계')

    if st.sidebar.button(f'{stock_code} 모든 지표'):
            visual = Heatmap(stock_code)
            visual.all_correct()

    if st.sidebar.button(f'{stock_code} 주식 정보'):
            visual = Heatmap(stock_code)
            visual.i_correct()

    if st.sidebar.button(f'{stock_code} 경제 지표'):
            visual = Heatmap(stock_code)
            visual.e_correct()

    if st.sidebar.button(f'{stock_code} 재무 정보'):
            visual = Heatmap(stock_code)
            visual.f_correct()

    if st.sidebar.button(f'{stock_code} 주식 정보 + 경제 지표'):
            visual = Heatmap(stock_code)
            visual.ie_correct()

    if st.sidebar.button(f'{stock_code} 주식 정보 + {stock_code} 재무 정보'):
            visual = Heatmap(stock_code)
            visual.if_correct()

    if st.sidebar.button(f'{stock_code} 재무 정보+ 경제 지표'):
            visual = Heatmap(stock_code)
            visual.ef_correct()

#streamlit run Main.py