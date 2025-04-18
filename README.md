# 🧠 AI-Powered Journal

An intelligent journaling application built with **Streamlit**, **MySQL**, and **Groq LLM**, enabling users to write daily entries and query past records using natural language. The app allows you to reflect, analyze, and retrieve meaningful insights from your thoughts, powered by large language models.

---

## ✨ Features

- **New Journal Entries**: Write and save daily reflections with a clean notebook-style interface.
- **AI-Powered Querying**: Ask questions in natural language to retrieve relevant journal content.
- **Entry History Viewer**: Browse and revisit your past entries sorted by date.
- **Streamlit UI**: Intuitive, interactive interface for writing and querying.
- **SQL Integration**: Efficient storage and retrieval of entries using MySQL.

---

## 📁 Project Structure

```
.
├── app.py               # Streamlit app entry point
├── LLM_Func.py          # Handles Groq LLM-based query processing
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (MySQL & Groq API keys)
└── README.md            # Project documentation
```

---

## ⚙️ Requirements

- Python 3.8+
- Streamlit
- Groq LLM SDK or API wrapper
- MySQL Database
- `python-dotenv` (for environment variable management)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-journaling-app.git
cd ai-journaling-app
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory with the following:

```
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DATABASE=entries
GROQ_KEY=your_groq_api_key
```

### 3. Set Up MySQL Database

Run the following SQL to create the required table:

```sql
CREATE DATABASE entries;
USE entries;

CREATE TABLE entry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    text TEXT
);
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## ✍️ How to Use

1. Navigate to **"New Entry"** to write a journal entry.
2. Use **"Your Previous Entries"** to view your latest thoughts.
3. Head to **"Query"** to ask questions like:
   - *"What did I write about anxiety last month?"*
   - *"Show my happiest entries."*
4. Save responses and insights as needed.

---

## 🛠 Future Improvements

- **User Authentication** for private journals
- **Sentiment Analysis** and visualizations


---

## 📚 References

- Groq LLM Documentation: [groq.com](https://groq.com)
- Streamlit: [streamlit.io](https://streamlit.io)
