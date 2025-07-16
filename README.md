# JU16-EduBot-AI
GEN AI

# 📚 EduBot AI – Interactive Study Guide & Quiz Generator

EduBot AI transforms any study material (PDF, DOCX, or TXT) into a smart study guide with summaries, quizzes, flashcards, and interactive practice.

---

## ✅ Features

- 📥 Upload study material (notes, textbooks, etc.)
- 🧠 Get summarized key concepts
- ❓ Generate multiple-choice quiz questions
- 🃏 Create flashcards (Q&A)
- 🎮 Practice mode for testing recall

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/edubot-ai.git
cd edubot-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py

📚 EduBot AI – Interactive Study Guide Generator for Students
🧠 What It Does
EduBot AI takes any uploaded textbook chapter, article, or lecture notes (PDF/DOCX/TXT), and automatically creates an interactive study guide including:

✅ Key concept summary

❓ Auto-generated quiz questions

💬 Flashcards (Q&A format)

📊 Difficulty rating

🔁 Practice mode with random Q&A

👩‍🏫 Who It’s For
Perfect for:

Students revising chapters

Teachers creating quick revision material

Self-learners studying articles or research papers

🔍 Features Overview
Feature	Description
📁 Upload Study Material	PDF, DOCX, TXT
🧠 AI Summary	Summarizes key topics
❓ Quiz Generator	Multiple-choice questions from content
🧾 Flashcards Generator	Key Q&A flashcards
🎮 Practice Mode	Try answering questions with feedback

🧑‍💻 Tech Stack
Component	Tool
Frontend	Streamlit
AI Agent	Ollama (LLaMA3 or Mistral)
Extraction	PyMuPDF, docx2txt
Quiz Logic	Prompt-based QA
Practice	Interactive with user inputs
