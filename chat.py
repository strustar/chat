from openai import OpenAI
import streamlit as st
import os

st.set_page_config(page_title = "AI Chatbot by 손병직", page_icon = "🦜", layout = "centered",    # centered, wide
                    initial_sidebar_state="expanded",
                    # runOnSave = True,
                    menu_items = {        #   initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                        # 'Get Help': 'https://www.extremelycoolapp.com/help',
                        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
                        # 'About': "# This is a header. This is an *extremely* cool app!"
                    })


st.sidebar.title('[My Websites]')
st.sidebar.markdown('')
st.sidebar.markdown("[:red[시스템 동바리 설계 자동화 보고서]](https://support.streamlit.app)")
st.sidebar.markdown("[:green[Beam Design (RC vs. FRP)]](https://beam-frp.streamlit.app)")
st.sidebar.markdown("[:blue[Column Design (RC vs. FRP)]](https://column.streamlit.app)")

st.sidebar.title(':orange[[Chatbot Links]]')
col = st.sidebar.columns(2)
with col[0]:
    st.markdown("[:orange[ChatGPT]](https://chatgpt.com/)")
with col[1]:
    st.markdown("[:orange[Claude]](https://claude.ai/)")

# GitHub 저장소 정보
github_repo = "strustar/chat"
github_branch = "main"

# PDF 파일 목록 (저장소에서 확인한 실제 파일들)
pdf_files = {
    "AI Chatbot 특강자료": "Chatbot 특강자료.pdf",
    "CFD 유동해석에 의한 항력계수 산정 Ⅰ": "CFD 유동해석에 의한 항력계수 산정(건양대 손병직, 20240613).pdf",
    "CFD 유동해석에 의한 항력계수 산정 Ⅱ": "CFD 유동해석에 의한 항력계수 산정 2 (건양대 손병직, 20240702).pdf",
}

# 사이드바에 PDF 파일 링크 추가
st.sidebar.markdown('')
st.sidebar.title("[PDF Files]")
for title, filename in pdf_files.items():
    # GitHub raw content URL 생성
    github_url = f"https://github.com/{github_repo}/raw/{github_branch}/{filename}"
    # URL 인코딩 처리
    encoded_url = github_url.replace(" ", "%20")
    st.sidebar.markdown(f"[{title}]({encoded_url})")

st.sidebar.markdown("[:blue[CFD 유동해석에 의한 항력계수 산정 Ⅲ & Ⅳ]](https://pptpdf.streamlit.app/)")



st.header("🦜 AI Chatbot by 손병직")
'';  ''

# api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("손병직에 의해 만들어진 개인 챗봇입니다. 질문을 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

