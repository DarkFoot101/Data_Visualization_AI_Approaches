import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Embed your Gemini API key here
API_KEY = "AIzaSyAqtK-XxakzUVVL3s0PaKaPwQeuB8HuJr0"

# Function to get column suggestions from Gemini API
def ask_gemini_for_columns_and_graph(api_key, df, user_query):
    """
    Use Gemini API to determine the best columns and graph type based on the user's query.
    """
    columns = df.columns.tolist()

    prompt = f"""
    You are analyzing a CSV file with the following columns: {columns}.
    Based on the user's query: "{user_query}",
    suggest two columns: one for the X-axis and one for the Y-axis, and the most suitable graph type (e.g., bar, scatter, line, histogram, pie). 
    Respond in JSON format like this:
    {{
        "x_column": "ColumnX",
        "y_column": "ColumnY",
        "graph_type": "graphType"
    }}
    """

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        content = response.json()
        reply = content['candidates'][0]['content']['parts'][0]['text'].strip()
        result = eval(reply.replace("json", "").replace("", "").strip())
        return result['x_column'], result['y_column'], result['graph_type']
    except Exception as e:
        st.error(f"Error interacting with the Gemini API: {e}")
        return None, None, None

# Function to plot the graph
def plot_graph(df, x_column, y_column, graph_type):
    plt.figure(figsize=(10, 6))
    try:
        if graph_type == "bar":
            plt.bar(df[x_column], df[y_column], color='skyblue')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Bar Graph: {y_column} vs {x_column}")
            plt.xticks(rotation=45)
        elif graph_type == "scatter":
            plt.scatter(df[x_column], df[y_column], color='skyblue')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Scatter Plot: {y_column} vs {x_column}")
        elif graph_type == "line":
            plt.plot(df[x_column], df[y_column], color='skyblue', marker='o')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f"Line Graph: {y_column} vs {x_column}")
        elif graph_type == "histogram":
            plt.hist(df[y_column], bins=20, color='skyblue', edgecolor='black')
            plt.xlabel(y_column)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {y_column}")
        elif graph_type == "pie":
            pie_data = df[x_column].value_counts()
            plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title(f"Pie Chart: Distribution of {x_column}")
        else:
            st.error(f"Unsupported graph type: {graph_type}")
            return
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error generating the plot: {e}")

# Streamlit Application
def main():
    st.title("Interactive Graph Generator")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        # User query input
        user_query = st.text_input("Describe the graph you'd like to generate:")

        if st.button("Generate Graph"):
            # Get graph suggestions from Gemini API
            x_column, y_column, graph_type = ask_gemini_for_columns_and_graph(API_KEY, df, user_query)

            if x_column and graph_type:
                plot_graph(df, x_column, y_column, graph_type)
            else:
                st.error("Could not determine columns or graph type.")

if __name__== "_main_":
    main()