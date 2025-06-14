# Code Copilot - Streamlit App
# File: app.py

import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

st.set_page_config(page_title="Code Copilot", layout="wide")
st.title("🧑‍💻 Code Copilot - Your Mini Coding Assistant")

task = st.selectbox("Choose a Task", [
    "Explain Code",
    "Generate Code from Prompt",
    "Generate Docstrings",
    "Debug Code",
    "Optimize Code",
    "Convert Code Language",
    "Generate Unit Tests",
    "Clean / Lint Code",
    "Suggest Libraries",
    "Explain Error Message",
    "Generate Regex",
    "Generate README"
])

code = st.text_area("Paste your code or write a prompt:", height=250)
lang_target = st.text_input("If converting language, enter target language (e.g., JavaScript)")

def run_copilot(task, code, lang_target):
    prompt_map = {
        "Explain Code": f"Explain what this code does in simple terms:\n{code}",
        "Generate Code from Prompt": f"Write Python code for the following task:\n{code}",
        "Generate Docstrings": f"Add clear docstrings to this Python code:\n{code}",
        "Debug Code": f"Find and fix bugs in the following code:\n{code}",
        "Optimize Code": f"Optimize the performance and readability of this code:\n{code}",
        "Convert Code Language": f"Convert this code to {lang_target}:\n{code}",
        "Generate Unit Tests": f"Write unit tests using unittest for this code:\n{code}",
        "Clean / Lint Code": f"Clean and lint the following code:\n{code}",
        "Suggest Libraries": f"Suggest Python libraries that simplify or enhance this code:\n{code}",
        "Explain Error Message": f"Explain and suggest a fix for this error:\n{code}",
        "Generate Regex": f"Generate a regex for this requirement and explain it:\n{code}",
        "Generate README": f"Create a README.md for a GitHub project with this code:\n{code}"
    }
    return ask_llm(prompt_map[task])

if st.button("Run Copilot"):
    if code.strip():
        with st.spinner("Thinking..."):
            result = run_copilot(task, code, lang_target)
            st.subheader("📄 Output")
            st.code(result)
    else:
        st.warning("Please paste some code or write a prompt above.")
