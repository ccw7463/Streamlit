import streamlit as st
import json

# Streamlit 앱의 제목 설정
st.title('JSON 데이터 전처리 및 검수 웹 애플리케이션')

# 파일 업로드 섹션
uploaded_file = st.file_uploader("JSON 파일 업로드",
                                 type=["json"],
                                 accept_multiple_files=True)

print('='*30)
print(uploaded_file)
# print(uploaded_file.upload_url)
print(uploaded_file._file_urls=file_id)
print('='*30)

if uploaded_file is not None:
    
    # JSON 파일 읽기
    data = json.load(uploaded_file.upload_url)
    # data = json.load(uploaded_file)

    # 데이터 요약 정보 표시
    st.write("데이터 요약:")
    st.write("Key의 종류:", list(data.keys()))
    st.write("전체 항목 수:", len(data))

    # 특정 인덱스의 데이터 보기
    st.write("특정 인덱스의 데이터 보기:")
    index = st.number_input("인덱스 입력", min_value=0, max_value=len(data)-1, step=1)
    if index in data:
        st.write(data[index])
    else:
        st.write("해당 인덱스의 데이터가 없습니다.")

    # 데이터 탐색 버튼
    next_button = st.button("다음")
    prev_button = st.button("이전")

    # 버튼 로직 (여기서는 예시로 간단한 로직만 제공합니다)
    if next_button:
        index = min(index + 1, len(data) - 1)
    if prev_button:
        index = max(index - 1, 0)

    # 현재 인덱스의 데이터 보기
    st.write("현재 인덱스의 데이터:")
    if index in data:
        st.write(data[index])
    else:
        st.write("해당 인덱스의 데이터가 없습니다.")