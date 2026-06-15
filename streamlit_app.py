import streamlit as st

# 앱 제목 설정
st.title("🧪 지시약 액성 판별 프로그램")
st.write("지시약 종류와 관찰된 색상을 선택하면 수용액의 액성을 판별해 드립니다.")

st.divider() # 시각적 분리선

# 1. 입력 위젯 정의 (사용자가 오타를 내지 않도록 selectbox 활용)
indicators = ["리트머스", "페놀프탈레인", "BTB"]
colors = ["붉은색", "푸른색", "무색", "노란색", "초록색"]

search_ind = st.selectbox("1. 지시약 이름을 선택하세요:", indicators)
search_col = st.selectbox("2. 관찰된 색상을 선택하세요:", colors)

# 판별 결과를 저장할 변수
result_text = ""
check = 0

# 2. 핵심 판별 로직 (기존 로직 유지)
if st.button("액성 판별하기", type="primary"):
    for i in range(3):
        if search_ind == indicators[i]:
            if i == 0:  # 리트머스
                if search_col == "붉은색":
                    result_text = "해당 수용액은 [산성] 입니다."
                    check = 1
                elif search_col == "푸른색":
                    result_text = "해당 수용액은 [염기성] 입니다."
                    check = 1
            
            elif i == 1:  # 페놀프탈레인
                if search_col == "무색":
                    result_text = "해당 수용액은 [산성 또는 중성] 입니다."
                    check = 1
                elif search_col == "붉은색":
                    result_text = "해당 수용액은 [염기성] 입니다."
                    check = 1
            
            elif i == 2:  # BTB
                if search_col == "노란색":
                    result_text = "해당 수용액은 [산성] 입니다."
                    check = 1
                elif search_col == "초록색":
                    result_text = "해당 수용액은 [중성] 입니다."
                    check = 1
                elif search_col == "푸른색":
                    result_text = "해당 수용액은 [염기성] 입니다."
                    check = 1

    # 3. 결과 웹 화면 출력
    st.subheader("📋 판별 결과")
    if check == 1:
        # 조건에 맞는 액성이 나왔을 때 알림 스타일 적용
        if "산성" in result_text and "중성" in result_text:
            st.info(result_text)  # 정보 알림 (파란색)
        elif "산성" in result_text:
            st.warning(result_text)  # 경고/산성 느낌 (주황색)
        elif "염기성" in result_text:
            st.success(result_text)  # 성공/안정적 느낌 (초록색)
        else:
            st.write(result_text)
    else:
        # 지시약과 색상 조합이 맞지 않는 경우
        st.error("❌ 입력된 지시약 및 색상의 조합이 올바르지 않습니다. 다시 선택해 주세요.")