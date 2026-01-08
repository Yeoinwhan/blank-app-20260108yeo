import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, time

# 제목과 간단한 설명
st.title("🎈 Streamlit 요소 데모 페이지")
st.write("이 페이지는 한 페이지에서 자주 쓰이는 Streamlit 요소들을 예시와 함께 보여줍니다.")

# -----------------------------
# Layout: columns / expander / sidebar
# -----------------------------
st.header("레이아웃 예시")
col1, col2 = st.columns(2)

with col1:
    st.subheader("컬럼 1: 텍스트, 버튼")
    # 버튼: 클릭하면 값을 반환
    if st.button("버튼 클릭 (컬럼1)"):
        st.write("버튼을 클릭했습니다!")

with col2:
    st.subheader("컬럼 2: 체크박스, 라디오")
    # 체크박스: True/False
    cb = st.checkbox("체크박스 켜기")
    st.write("체크박스 상태:", cb)
    # 라디오 버튼: 단일 선택
    color = st.radio("색 선택", ("빨강", "초록", "파랑"))
    st.write("선택한 색:", color)

with st.expander("더 보기: 설명 텍스트"):
    st.write("이곳은 숨김/보임 가능한 영역입니다. 공부할 때 긴 설명을 숨겨두기 편리합니다.")

st.sidebar.header("사이드바 예시")
st.sidebar.write("사이드바에는 보조 입력을 두기 좋습니다.")

# -----------------------------
# 입력 위젯들 (form 포함)
# -----------------------------
st.header("입력 위젯 예시")

# 간단한 텍스트 입력
name = st.text_input("이름을 입력하세요", value="홍길동")
st.write("입력한 이름:", name)

# 텍스트 영역
bio = st.text_area("자기소개", "여기에 소개를 적어주세요.")
st.write("자기소개 미리보기:")
st.write(bio)

# 숫자 입력 및 슬라이더
age = st.number_input("나이", min_value=0, max_value=120, value=30)
st.write("나이:", age)
score = st.slider("점수", 0, 100, 75)
st.write("점수:", score)

# 날짜, 시간
dob = st.date_input("생년월일", value=date(1990,1,1))
t = st.time_input("알람 시간", value=time(7,30))
st.write("생년월일:", dob, " / 알람:", t)

# 선택박스와 멀티셀렉트
option = st.selectbox("옵션 선택", ["옵션 A", "옵션 B", "옵션 C"])
choices = st.multiselect("여러 항목 선택", ["사과","바나나","체리"], default=["사과"])
st.write("선택:", option, choices)

# 파일 업로드
uploaded = st.file_uploader("파일 업로드 (이미지, csv 등)")
if uploaded is not None:
    st.write("업로드된 파일:", uploaded.name)

# 색상 선택
color = st.color_picker("색상 선택", "#00f900")
st.write("선택한 색상:", color)

# Form 사용 예시: 제출 버튼이 하나일 때 유용
with st.form("my_form"):
    st.write("폼 예시: 아래 값을 채우고 제출하세요")
    f_name = st.text_input("이름")
    f_age = st.number_input("나이", min_value=0, max_value=120, value=20)
    submitted = st.form_submit_button("제출")
    if submitted:
        st.success(f"폼이 제출되었습니다: {f_name} ({f_age})")

# -----------------------------
# 출력: 텍스트, 메시지, 코드, 수식
# -----------------------------
st.header("출력/표시 예시")
st.text("일반 텍스트: st.text() 사용")
st.markdown("**마크다운** 예시: *강조*와 [링크](https://docs.streamlit.io)")
st.code("print('Hello, Streamlit')", language="python")
st.latex(r"E = mc^2")

st.info("정보 메시지: st.info()")
st.success("성공 메시지: st.success()")
st.warning("경고 메시지: st.warning()")
st.error("오류 메시지: st.error()")

# -----------------------------
# 미디어: 이미지, 오디오, 비디오
# -----------------------------
st.header("미디어 예시")
st.write("이미지/오디오/비디오는 로컬 파일 또는 URL로 표시할 수 있습니다.")
st.image("https://static.streamlit.io/examples/dice.jpg", caption="샘플 이미지")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# -----------------------------
# 데이터와 차트
# -----------------------------
st.header("데이터프레임 및 차트")
df = pd.DataFrame(np.random.randn(20, 3), columns=["a","b","c"])
st.dataframe(df)  # 데이터프레임은 스크롤 가능
st.table(df.head())

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# 지도 (lat, lon 필요)
map_df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.56, 126.97],
    columns=["lat", "lon"],
)
st.map(map_df)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
df.cumsum().plot(ax=ax)
st.pyplot(fig)

import altair as alt
chart = alt.Chart(df.reset_index()).transform_fold(
    ['a','b','c'], as_=['variable','value']
).mark_line().encode(x='index:Q', y='value:Q', color='variable:N')
st.altair_chart(chart, use_container_width=True)

# -----------------------------
# 인터랙티브: 상태, 진행바, 스피너
# -----------------------------
st.header("상태 및 진행 표시")
with st.spinner("처리중..."):
    import time
    time.sleep(0.3)
st.success("완료")

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i+1)

# -----------------------------
# 다운로드 버튼, 카메라 입력, 세션 상태
# -----------------------------
st.header("기타 유용한 요소들")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("CSV 다운로드", data=csv, file_name='sample.csv', mime='text/csv')

if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("세션 카운트 증가"):
    st.session_state.count += 1
st.write("세션 카운트:", st.session_state.count)

# 카메라 입력 (브라우저가 지원하면 사용 가능)
try:
    cam = st.camera_input("카메라 촬영")
    if cam:
        st.image(cam)
except Exception:
    st.write("카메라 입력이 지원되지 않거나 권한이 필요합니다.")

# -----------------------------
# 마무리
# -----------------------------
st.write("---")
st.write("이 페이지의 코드를 읽으며 각 위젯의 사용법을 익혀보세요.")
