from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandasai import Agent

# Configure the Local LLM model
model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)

# Initialize Streamlit
st.title("Data Analysis with PandasAI Agent")

# Sidebar for file upload
uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

# Initialize session state for memory retention
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Process the uploaded file
if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data (Preview)")
    st.write(data.head(6))

    # Initialize PandasAI Agent
    agent = Agent(data, config={"llm": model})

    # Input for user prompts
    prompt = st.text_input("Ask me what you want to analyze?")

    if st.button("Analyze Now!"):
        if prompt:
            with st.spinner("Generating response..."):
                try:
                    # Get the response from the agent
                    response = agent.chat(prompt)

                    # Display response text
                    st.write("Analyzed Response: ")
                    st.write(response)

                    # Add to chat history
                    st.session_state["chat_history"].append((prompt, response))

                    # Check if visualization is included in the response
                    if hasattr(agent, "last_plot") and agent.last_plot is not None:
                        st.write("Visualization Made: ")
                        st.pyplot(agent.last_plot)
                except Exception as e:
                    st.error(f"Error: Couldn't generate teh code. Please specify the chracterstics clearly for a satisfactory response")

    # Display chat history
    if st.session_state["chat_history"]:
        st.write(" Chat History")
        for i, (q, r) in enumerate(st.session_state["chat_history"]):
            st.write(f"Prompt {i+1}: {q}")
            st.write(f"Response {i+1}:{r}")