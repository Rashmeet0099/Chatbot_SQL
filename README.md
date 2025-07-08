# SQL Chatbot for Music Store using LangChain + Gemini + Streamlit

# 🎵 SQL Chatbot for Music Store using LangChain + Gemini + Streamlit

This project is an interactive **SQL-based chatbot** that lets users ask **natural language questions** about a music store database (`Chinook.db`). It uses **LangChain**, **Google Gemini**, and **Streamlit** to build a conversational interface for real-time SQL querying.

---

## 🚀 Features

- 🔍 Query an SQLite database using plain English
- 🧠 Powered by **Google Gemini (`chat-bison-001`)** LLM
- 🎨 Streamlit frontend with dropdown-based question suggestions
- ⚡ Optimized for low-latency response with caching
- ✅ Uses LangChain 0.2+ with SQL Agent Toolkit

---

## 📦 Technologies Used

| Tool             | Purpose                                 |
|------------------|-----------------------------------------|
| `LangChain`      | Framework for building LLM applications |
| `langchain-community` | SQL agent + database tools         |
| `Google Gemini`  | LLM API via `chat-bison-001`            |
| `Streamlit`      | Web frontend interface                  |
| `SQLite`         | Sample database (Chinook)               |
| `dotenv`         | Environment variable management         |

---

## 📁 Folder Structure

📦chatbot_sql
┣ 📄 app.py ← Main Streamlit app
┣ 📄 Chinook.db ← Sample SQLite database
┣ 📄 .env ← Your Gemini API key
┣ 📄 requirements.txt ← Required Python packages
┗ 📄 README.md ← You're reading this

yaml
Copy
Edit

---

## 📋 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/sql-chatbot-langchain.git
cd sql-chatbot-langchain
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env file
env
Copy
Edit
google_api_key=YOUR_GEMINI_API_KEY
🔑 Get your Gemini API key from: https://makersuite.google.com/app/apikey

4. Run the app
bash
Copy
Edit
streamlit run app.py
✅ Sample Questions You Can Ask
"Which artist has the most albums?"

"List the top 5 customers by total purchases."

"How many tracks are in the database?"

"Which genres are the most popular?"

"List all employees and their titles."

🔒 Environment Variables
google_api_key → Your Gemini API Key (stored in .env)

🧠 Future Enhancements
Add support for OpenAI models (optional)

Add SQL query explanation under the result

Enable voice input for queries

Save chat history

🧑‍💻 Author
Rashmeet Singh
BTech CSE | CGC Jhanjeri | AI & LangChain Enthusiast

🪪 License
This project is licensed under the MIT License.
