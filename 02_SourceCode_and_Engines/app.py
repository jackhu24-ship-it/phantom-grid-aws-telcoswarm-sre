import json
import requests
import streamlit as st

OLLAMA_BASE = "http://localhost:11434"

st.set_page_layout = "wide"
st.title("🤖 本機 Ollama 智慧對話平台")

# 1. 取得本機現有模型清單
@st.cache_data(ttl=60)
def get_available_models():
    try:
        res = requests.get(f"{OLLAMA_BASE}/api/tags", timeout=3)
        if res.status_code == 200:
            return [m["name"] for m in res.json().get("models", [])]
    except Exception:
        pass
    return ["qwen3:8b", "commander:latest"]

available_models = get_available_models()

# 側邊欄配置
with st.sidebar:
    st.header("⚙️ 核心設定")
    selected_model = st.selectbox("選擇執行模型", available_models)
    
    system_prompt = st.text_area(
        "系統角色設定 (System Prompt)",
        value="你是一個專業、嚴謹且條理分明的高級助理，請一律使用繁體中文回答。"
    )
    
    if st.button("🗑️ 清除對話紀錄"):
        st.session_state.messages = []
        st.rerun()

# 2. 初始化對話紀錄
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. 渲染過往對話紀錄
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# 4. 串流生成函式
def stream_ollama(model: str, messages: list):
    url = f"{OLLAMA_BASE}/api/chat"
    payload = {
        "model": model,
        "messages": messages,
        "stream": True
    }
    try:
        response = requests.post(url, json=payload, stream=True, timeout=60)
        response.raise_for_status()
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                content = chunk.get("message", {}).get("content", "")
                yield content
    except Exception as e:
        yield f"\n\n❌ 連線錯誤: {str(e)}"

# 5. 處理使用者輸入與串流回應用戶端
if user_input := st.chat_input("請輸入問題..."):
    # 顯示並儲存使用者訊息
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 組合包含 System Prompt 的完整上下文傳遞給模型
    full_context = [{"role": "system", "content": system_prompt}] + [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    # 即時打字機串流輸出
    with st.chat_message("assistant"):
        response_placeholder = st.write_stream(stream_ollama(selected_model, full_context))

    # 儲存助手回答進歷史紀錄
    st.session_state.messages.append({"role": "assistant", "content": response_placeholder})