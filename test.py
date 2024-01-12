import streamlit as st
import pandas as pd
import io

# Streamlit 앱의 제목 설정
st.title('데이터 전처리 및 검수 웹 애플리케이션')

# 파일 업로드 섹션
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    data = pd.read_csv(uploaded_file)

    # 데이터 표시
    st.write("원본 데이터:")
    st.write(data)

    # 데이터 전처리 옵션
    if st.checkbox('결측치 제거'):
        data = data.dropna()
        st.write("결측치 제거 후 데이터:")
        st.write(data)

    if st.checkbox('중복 행 제거'):
        data = data.drop_duplicates()
        st.write("중복 행 제거 후 데이터:")
        st.write(data)

    # 데이터 다운로드
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(data)
    st.download_button(
        label="처리된 데이터 다운로드",
        data=csv,
        file_name='processed_data.csv',
        mime='text/csv',
    )
