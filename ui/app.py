import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Knowledge Base Agent",
    layout="wide"
)

st.title("🤖 AI Knowledge Base Agent")

# ------------------------
# SIDEBAR NAVIGATION
# ------------------------

page = st.sidebar.radio(
    "Navigation",
    ["Chat", "Upload Knowledge", "Analytics"]
)

# ------------------------
# CHAT HISTORY
# ------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------
# CHAT PAGE
# ------------------------

if page == "Chat":

    st.header("Chat with AI")

    email = st.text_input("Your Email")

    question = st.text_area("Ask a question")

    if st.button("Ask AI"):

        payload = {
            "email": email,
            "question": question
        }

        try:

            response = requests.post(
                f"{API_URL}/ask",
                json=payload
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

                st.session_state.chat_history.append(
                    (question, answer)
                )

            else:
                st.error("API Error")

        except:
            st.error("Backend not running")

    st.subheader("Conversation")

    for q, a in st.session_state.chat_history:

        st.markdown(f"**You:** {q}")
        st.markdown(f"**AI:** {a}")
        st.markdown("---")

# ------------------------
# UPLOAD PAGE
# ------------------------

elif page == "Upload Knowledge":

    st.header("Upload Knowledge Base")

    file = st.file_uploader(
        "Upload TXT File",
        type=["txt"]
    )

    if st.button("Upload"):

        if file is None:
            st.warning("Upload a file first")

        else:

            files = {
                "file": (file.name, file.getvalue())
            }

            try:

                response = requests.post(
                    f"{API_URL}/upload-knowledge",
                    files=files
                )

                if response.status_code == 200:

                    st.success("Knowledge uploaded")

                else:

                    st.error("Upload failed")

            except:

                st.error("Backend not running")

# ------------------------
# ANALYTICS PAGE
# ------------------------

elif page == "Analytics":

    st.header("Analytics Dashboard")

    if st.button("Load Analytics"):

        try:

            response = requests.get(
                f"{API_URL}/analytics"
            )

            if response.status_code == 200:

                data = response.json()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Total Conversations",
                        data["total_conversations"]
                    )

                with col2:
                    st.metric(
                        "Total Leads",
                        data["total_leads"]
                    )

                st.subheader("Lead Intent Breakdown")

                df = pd.DataFrame(
                    data["lead_intents"].items(),
                    columns=["Intent","Count"]
                )

                st.bar_chart(
                    df.set_index("Intent")
                )

            else:

                st.error("Analytics API error")

        except:

            st.error("Backend not running")