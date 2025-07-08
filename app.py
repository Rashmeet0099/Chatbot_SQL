import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("google_api_key")

# Caching
@st.cache_resource
def load_db():
    return SQLDatabase.from_uri("sqlite:///Chinook.db")

@st.cache_resource
def load_llm():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

@st.cache_resource
def load_agent():
    return create_sql_agent(
        llm=load_llm(),
        db=load_db(),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=False
    )

# Sample dropdown questions
sample_questions = [
    "How many artists are in the database?",
    "Who are the top 5 artists by number of albums?",
    "Which artist has the most tracks?",
    "What is the total number of tracks available?",
    "Which album contains the most tracks?",
    "What are the top 5 most popular genres?",
    "Which customer has spent the most money?",
    "What are the top 5 countries by total invoice amount?",
    "List the names of all employees and their job titles.",
    "How many customers are from Brazil?",
    "Which customer made the most purchases?",
    "What is the total revenue generated?",
    "What are the top 10 tracks by unit price?",
    "List all playlists and how many tracks they contain.",
    "Which genre has the most tracks?",
    "How many invoices were made in 2010?",
    "List all invoices over $20.",
    "Which media types are available in the database?",
    "Who is the employee with the most customers under them?",
    "List all albums and their respective artists."
]

# UI
st.title("💬 SQL Chatbot for Music Store")

selected_question = st.selectbox("Choose a sample question (or type your own below):", sample_questions)
custom_question = st.text_input("Or type your custom question:")

query = custom_question if custom_question.strip() else selected_question

if st.button("Submit") and query:
    with st.spinner("Querying the database..."):
        agent = load_agent()
        response = agent.invoke(query)
        st.success(response)
