# #pip install streamlit-local-storage
# #pip install streamlit-js-eval
# #pip install streamlit
from pathlib import Path
# import streamlit as st

# from streamlit_js_eval import streamlit_js_eval
# st.set_page_config(layout="wide")

# #from streamlit_local_storage import LocalStorage
# st.write("view")
# st.markdown("""
# <style>
# section[data-testid="stSidebar"] {
#     display: none;
# }
# </style>
# """, unsafe_allow_html=True)
# #localS = LocalStorage()



# st.title("이미지 컬렉션 이벤트")
#------------------------------
# https://your-app.streamlit.app/?site=site1
# https://your-app.streamlit.app/?site=site2
# https://your-app.streamlit.app/?site=site3
# https://your-app.streamlit.app/?site=site4
# https://your-app.streamlit.app/?site=site5

#-------------------------------


import streamlit as st
import json
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout="wide")

# -----------------------------
# Local Storage 불러오기

import streamlit as st
from streamlit_js_eval import streamlit_js_eval

# st.title("테스트")

# data = streamlit_js_eval(
#     js_expressions="localStorage.getItem('progress')",
#     key="get_progress"
# )

# st.write("읽어온 값:", data)

# if st.button("저장"):
#     streamlit_js_eval(
#         js_expressions="""
#         localStorage.setItem('progress', '{"site1":true}')
#         """,
#         key="save_progress"
#     )
#     st.success("저장 시도")
# st.write(type(data))
# st.write (data)


# -----------------------------

# progress = streamlit_js_eval(
#     js_expressions="JSON.parse(localStorage.getItem('progress') || '{}')"
# ) or {}
# streamlit_js_eval(
#     js_expressions="localStorage.removeItem('progress')",
#     key="reset"
# )
data = streamlit_js_eval(
    js_expressions="localStorage.getItem('progress')",
    key="get_progress"
)
st.write(data)

if data:
    progress = json.loads(data)
else:
    progress = {}

st.write(progress)

# count = 0

# for i in range(5):
#     if progress.get(f"site{i+1}") == True:
#         count += 1

# -----------------------------
# QR 파라미터 받기
# -----------------------------
query = st.query_params
site = query.get("site")

# -----------------------------
# QR로 들어왔을 때 자동 저장
# -----------------------------
if site == "site1":
    st.title("Site 1")

    file_path = Path("ht.png")
    file_content = file_path.read_bytes()
    # with open("images/img1.jpg", "rb") as file:
    #     st.download_button(
    #         "📥 이미지 다운로드",
    #         file,
    #         file_name="site1.jpg",
    #         mime="image/jpeg"
    #     )
    if st.download_button(
        label="Download image",
        data=file_content,
        file_name="ht.png",
        mime="image/png",
       
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions=f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                    
                )
                """,
                key=f"save_{site}"
            )
            st.success(f"{site} 수집 완료!")
            
    st.link_button("For more information", "https://www.science.org/")
    
if site == "site2":
    st.title("Site 2")

    file_path = Path("ht.png")
    file_content = file_path.read_bytes()
    if st.download_button(
        label="Download image",
        data=file_content,
        file_name="ht.png",
        mime="image/png",
       
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions=f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                    
                )
                """,
                key=f"save_{site}"
            )
            st.success(f"{site} 수집 완료!")
            
    st.link_button("For more information", "https://www.science.org/")
if site == "site3":
    st.title("Site 3")

    file_path = Path("ht.png")
    file_content = file_path.read_bytes()
    if st.download_button(
        label="Download image",
        data=file_content,
        file_name="ht.png",
        mime="image/png",
       
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions=f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                    
                )
                """,
                key=f"save_{site}"
            )
            st.success(f"{site} 수집 완료!")
            
    st.link_button("For more information", "https://www.science.org/")
if site == "site4":
    st.title("Site 4")

    file_path = Path("ht.png")
    file_content = file_path.read_bytes()
    if st.download_button(
        label="Download image",
        data=file_content,
        file_name="ht.png",
        mime="image/png",
       
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions=f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                    
                )
                """,
                key=f"save_{site}"
            )
            st.success(f"{site} 수집 완료!")
            
    st.link_button("For more information", "https://www.science.org/")
if site == "site5":
    st.title("Site 5")

    file_path = Path("ht.png")
    file_content = file_path.read_bytes()
    if st.download_button(
        label="Download image",
        data=file_content,
        file_name="ht.png",
        mime="image/png",
       
    ):
        if site not in progress:
            progress[site] = True
            streamlit_js_eval(
                js_expressions=f"""localStorage.setItem(
                    'progress',
                    '{json.dumps(progress)}'
                    
                )
                """,
                key=f"save_{site}"
            )
            st.success(f"{site} 수집 완료!")
            
    st.link_button("For more information", "https://www.science.org/")
st.write(progress)
# if site:
#     progress[site] = True

#     streamlit_js_eval(js_expressions=f"""
#         localStorage.setItem('progress', JSON.stringify({progress}))
#     """)
    

#     st.success(f"{site} 수집 완료!")

# -----------------------------
# 진행도 계산
# -----------------------------
count = sum(1 for i in range(5) if progress.get(f"site{i + 1}"))

st.write(f"📊 진행도: {count}/5")

# -----------------------------
# 메뉴
# -----------------------------
page = st.radio(
    "MENU",
    ["Home", "Collection"],
    horizontal=True
)

# -----------------------------
# Home
# -----------------------------
if page == "Home":
    st.title("과학자 카드 수집 이벤트")

    st.write("QR을 스캔해서 5개의 카드를 모으세요!")

    st.write(progress)

# -----------------------------
# Collection
# -----------------------------
elif page == "Collection":

    #st.title("🏆 Collection")
    st.title("Collection")
    if count < 5:
        st.warning("아직 잠겨 있습니다.")
        st.stop()

    st.balloons()
    # st.success("🎉 축하합니다! 모든 QR을 수집했습니다!")
    st.success("축하합니다! 모든 카드를 수집했습니다!")

