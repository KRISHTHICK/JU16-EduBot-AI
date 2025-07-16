# app.py – EduBot AI: Study Guide Generator

import streamlit as st
import fitz  # PyMuPDF
import docx2txt
import ollama
import random

# --- Extract Text ---
def extract_text(file):
    if file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

# --- LLM Functions ---
def get_summary(text):
    prompt = f"""
You are a study assistant.
Summarize the following content into a list of 5-8 key points:

{text[:2000]}
"""
    return query_llm(prompt)

def get_flashcards(text):
    prompt = f"""
Create 5 flashcards from the content below. Format:
Q: <question>\nA: <answer>

Content:
{text[:2000]}
"""
    return query_llm(prompt)

def get_quiz(text):
    prompt = f"""
Generate 5 multiple choice quiz questions from the following text.
Each question should have 1 correct answer and 3 distractors:

{text[:2000]}
"""
    return query_llm(prompt)

def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Practice Mode ---
def parse_flashcards(text):
    cards = []
    blocks = text.strip().split("Q:")
    for block in blocks:
        if "A:" in block:
            q, a = block.split("A:", 1)
            cards.append((q.strip(), a.strip()))
    return cards

# --- Streamlit UI ---
st.set_page_config(page_title="EduBot AI", layout="wide")
st.title("📚 EduBot AI – Study Guide & Quiz Generator")

uploaded = st.file_uploader("📁 Upload Study Material (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded:
    with st.spinner("Reading and generating content..."):
        raw_text = extract_text(uploaded)
        summary = get_summary(raw_text)
        flashcard_text = get_flashcards(raw_text)
        quiz = get_quiz(raw_text)
        flashcards = parse_flashcards(flashcard_text)

    st.header("🧠 Key Concepts Summary")
    st.markdown(summary)

    st.header("📋 Quiz Questions")
    st.markdown(quiz)

    st.header("🃏 Flashcards")
    for i, (q, a) in enumerate(flashcards):
        with st.expander(f"Q{i+1}: {q}"):
            st.markdown(f"**A:** {a}")

    st.header("🎮 Practice Mode")
    card = random.choice(flashcards)
    user_input = st.text_input(f"❓ {card[0]}", key="practice")
    if user_input:
        st.markdown(f"✅ **Correct Answer:** {card[1]}")
else:
    st.info("Upload a file to generate your study guide.")
