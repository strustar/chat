from openai import OpenAI
import streamlit as st
import streamlit.components.v1 as components
import os

st.sidebar.title('Useful Links')

st.sidebar.markdown('')
st.sidebar.markdown("[:red[시스템 동바리 설계 자동화 보고서]](https://support.streamlit.app)")
st.sidebar.markdown("[:green[Beam Design (RC vs. FRP)]](https://beam-frp.streamlit.app)")
st.sidebar.markdown("[:blue[Column Design (RC vs. FRP)]](https://column.streamlit.app)")

# link = st.sidebar.radio("Go to", ["시스템 동바리 설계 자동화 보고서", "Beam Design (RC vs. FRP)", "Column Design (RC vs. FRP)"], index=None)
# # 라디오 버튼이 선택된 경우 해당 사이트로 이동
# if link:
#     if '동바리' in link:
#         url = "https://support.streamlit.app"
#     elif 'Beam' in link:
#         url = "https://beam-frp.streamlit.app"
#     elif 'Column' in link:
#         url = "https://column.streamlit.app"    
    
#     # JavaScript to open the URL in a new tab
#     js = f"""
#     <script type="text/javascript">
#         window.open("{url}", "_blank");
#     </script>
#     """
#     # Display the JavaScript in the app
#     components.html(js)

st.header("🦜 ChatGPT by 손병직")
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

if prompt := st.chat_input("What is up?"):
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


# import streamlit as st

# st.set_page_config(page_title='ChatGPT', page_icon='🦜')
# st.title('🦜 ChatGPT')

# # 세션 상태에 'messages' 키가 없으면 빈 리스트로 초기화합니다.
# if 'messages' not in st.session_state:
#     st.session_state['messages'] = []

# # 이전 대화를 출력해 주는 코드
# if 'messages' in st.session_state and len(st.session_state['messages']) > 0:
#     for role, msg, avatar in st.session_state['messages']:
#         st.chat_message(role, avatar=avatar).write(msg)

# if user_input := st.chat_input('메세지를 입력하세요'):
#     st.chat_message('user', avatar='🧑‍🤝‍🧑').write(user_input)
#     st.session_state['messages'].append(('user', user_input, '🧑‍🤝‍🧑'))

#     with st.chat_message('ai', avatar='🤖'):
#         msg = f'당신이 입력한 내용 : {user_input}'
#         st.write(msg)
#         st.session_state['messages'].append(('ai', msg, '🤖'))

