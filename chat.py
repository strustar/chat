from openai import OpenAI
import streamlit as st
import streamlit.components.v1 as components
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
    "CFD 유동해석에 의한 항력계수 산정  Ⅱ": "CFD 유동해석에 의한 항력계수 산정(건양대 손병직, 20240613).pdf",    
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


# 발표자료 ###############################################################################################
# 왼쪽 사이드바 인쇄하지 않기 설정 등, # 페이지 간 구분을 위한 CSS 스타일 정의
st.markdown("""
<style>
    @media print {
        [data-testid=stSidebar], header, footer, .no-print {
            display: none;
        }
        @page {
            size: A4;
            margin-left: 50px; /* 왼쪽 여백 설정 */
        }
        body {
            width: 100%; /* 전체 너비 사용 */
        }
    }
    /* 페이지 브레이크 스타일 */
    .page-break {
        page-break-before: always;
    }
</style> """, unsafe_allow_html=True)

st.write('## :blue[CFD 유동해석에 의한 항력계수 산정 Ⅲ]')

'---'
st.write('### :blue[[2차 회의 논의사항]]')
'- #### 1. 음압의 의미'
'- #### 2. 유동장 크기 확대 해석'

'---'
'### :orange[1. 음압의 의미]'
st.markdown("""
- #### 양압
  - ##### :green[대기압 보다 높은 압력]
  - ##### :green[미는 압력]
- #### 음압
  - ##### :green[대기압 보다 낮은 압력]
  - ##### :green[잡아 당기는 압력]
  - ##### :green[압력은 높은 쪽에서 낮은 쪽으로 흐름]
""")

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
'---'
'### :orange[2. 유동장 크기 확대 해석]'

'---'
st.markdown("""
- #### :orange[A. 토공부 방음벽]
  - ##### :green[항력계수 : 0.962 ⇒ 0.613]
""")
st.image('case1_model.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
''
st.markdown("""- #### :blue[속도 분포 [m/s]]""")
st.image('case1_velocity.png')
st.image('case11_vel.png')

''
st.markdown("""- #### :blue[압력 분포 [Pa]]""")
st.image('case1_pressure.png')
st.image('case11_pre.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
'---'
st.markdown("""
- #### :orange[B. 교량부 방음벽]
  - ##### :green[항력계수 : 1.705 ⇒ 1.511 ⇒ 1.737]
""")
st.image('case2_model.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
''
st.markdown("""- #### :blue[속도 분포 [m/s]]""")
st.image('case2_velocity.png')
st.image('case22_vel.png')
st.image('case22_velB.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
''
st.markdown("""- #### :blue[압력 분포 [Pa]]""")
st.image('case2_pressure.png')
st.image('case22_pre.png')
st.image('case22_preB.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
'---'
'- #### :orange[C. Transient Analysis]'

st.markdown("""- #### :blue[Velocity [m/s]]""")

video_file = open('case11_vel.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, autoplay=True, loop=True)

video_file = open('case22_vel.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, autoplay=True, loop=True)

video_file = open('case22_velB.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes, autoplay=True, loop=True)

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
st.markdown("""- #### :blue[Drag Coefficient]""")
st.image('case11_cd.png')
st.image('case22_cd.png')
st.image('case22_cdB.png')

st.markdown('<div class="page-break"></div>', unsafe_allow_html=True)    ############ 인쇄할 때, 페이지 나누기 ###################
'---'
'### :orange[감사합니다]'

# 발표자료 ###############################################################################################


'---'
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

