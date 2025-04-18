import streamlit as st
from datetime import datetime
import pandas as pd
import mysql.connector
import os
from LLM_Func import LLM_Func
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
if 'entries' not in st.session_state:
    st.session_state.entries = []

page = st.sidebar.radio("Navigation", ["Your Previous Entries", "Query", "New Entry"])

if page == "Your Previous Entries":
    st.title("📜 Your Previous Entries")

    cursor.execute("SELECT * FROM entry ORDER BY date DESC LIMIT 50;")
    entries = cursor.fetchall()

    if entries:
        for entry in entries:
            st.markdown(f"**{entry[1]}**")  # Assuming entry[1] is the 'date' column
            st.write(entry[2])              # Assuming entry[2] is the 'text' column
            st.markdown("---")
    else:
        st.write("No entries found.")

elif page == "Query":
    st.title("🔍 Query Your Entries")
    inp = st.text_input("Enter your query:")
    if inp:
        query=LLM_Func.getQuery(inp)
        st.write(query)
        # print(query)
        results=LLM_Func.getResponse(query,inp,cursor)
        if results:
            st.write(results)
            # for entry in results:
            #     st.markdown(f"**{entry['date']}**")
            #     st.write(entry['content'])
            #     st.markdown("---")
        else:
            st.write("No matching entries found.")

elif page == "New Entry":
    st.title("📔 New Entry")
    new_entry = st.text_area("Write your entry here:", height=300)
    if st.button("Save Entry"):
        current_date = datetime.now().strftime('%Y-%m-%d')
        if new_entry.strip():
            cursor.execute("INSERT INTO entry (date, text) VALUES (%s, %s)", (current_date, new_entry))
            conn.commit()

            st.success("Entry saved successfully!")
        else:
            st.warning("Please write something before saving.")
