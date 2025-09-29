# frontend.py
import streamlit as st
import requests
from typing import Optional

st.set_page_config(page_title="PDF RAG Chatbot", page_icon="📄")
st.title("📄 PDF RAG Chatbot")


BACKEND_URL = st.text_input("Backend base URL", value="http://127.0.0.1:8000")


tab_upload, tab_chat = st.tabs(["📂 Upload PDF", "💬 Chat"])


with tab_upload:
    st.header("Upload PDF to Weaviate")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    project_id = st.text_input("Project ID (optional)")
    tags = st.text_input("Tags (comma-separated, optional)")

    if st.button("Upload PDF"):
        if not uploaded_file:
            st.warning("Please select a PDF first.")
        else:
            try:
          
                files = {
                
                    "file": (uploaded_file.name, uploaded_file.read(), "application/pdf")
                }
                data = {}
                if project_id.strip():
                    data["project_id"] = project_id.strip()
                if tags.strip():
                    data["tags"] = tags.strip()

                resp = requests.post(f"{BACKEND_URL}/upload-pdf", files=files, data=data, timeout=120)

                if resp.status_code == 200:
                    st.success("✅ PDF uploaded and processed successfully!")
                    try:
                        st.json(resp.json())
                    except Exception:
                        st.write("Response:", resp.text)
                else:
                    st.error(f"❌ Upload failed ({resp.status_code}): {resp.text}")

            except Exception as e:
                st.error(f"Request failed: {e}")

with tab_chat:
    st.header("Ask questions about your PDFs")
    question = st.text_area("Enter your question", height=120)
    top_k = st.slider("Documents to retrieve (top_k)", 1, 10, 3)
    project_id_q = st.text_input("Project ID filter (optional)")
    tags_q = st.text_input("Tags filter (comma-separated, optional)")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  

    if st.button("Send"):
        if not question.strip():
            st.warning("Please type a question.")
        else:
            payload = {
                "question": question,
                "top_k": top_k,
              
                "project_id": project_id_q.strip() or None,
                "tags": tags_q.strip() or None
            }
            try:
                resp = requests.post(f"{BACKEND_URL}/chat", json=payload, timeout=120)
                if resp.status_code == 200:
                    data = resp.json()
                
                    answer = data.get("answer") or data.get("result") or data.get("results") or data
                    retrieved = data.get("retrieved_docs") or data.get("retrieved") or data.get("retrieved_count") or None

                   
                    st.session_state.chat_history.insert(0, (question, answer))

             
                    st.success("Answer:")
                    st.write(answer)

                    if retrieved is not None:
                        st.info(f"Retrieved docs: {retrieved}")

                    docs = data.get("results") or data.get("docs") or data.get("retrieved_list") or data.get("retrieved_items") or None
                    if docs:
                        st.write("### Retrieved Documents / Context")
                        for i, d in enumerate(docs, 1):
                         
                            content = d.get("content") if isinstance(d, dict) else str(d)
                            src = d.get("source_uri") if isinstance(d, dict) else ""
                            page = d.get("page_number") if isinstance(d, dict) else ""
                            st.markdown(f"**{i}. Source:** `{src}`  | **Page:** `{page}`")
                            st.write(content[:1000])  
                            st.write("---")
                else:
                    st.error(f"❌ Backend error ({resp.status_code}): {resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")


    if st.session_state.chat_history:
        st.markdown("### Chat history")
        for q, a in st.session_state.chat_history:
            st.markdown(f"**Q:** {q}")
            st.write(f"**A:** {a}")
            st.write("---")
