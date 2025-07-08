from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
 
#Load from .env
load_dotenv()
api_key = os.getenv("google_api_key")
 
#Set Gemini API key from environment
os.environ["GOOGLE_API_KEY"] = api_key
 
#Connect to SQLite database
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
 
#Set up Gemini 1.5 Flash LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
 
#Create agent to work with SQL (fixed agent type)
agent_executor = create_sql_agent(
llm=llm,
db=db,
agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # Fixed to avoid compatibility error
verbose=True
)
 
#✅ Ask a question
query = "Which artist has the most albums?"
response = agent_executor.invoke(query)
print(response)