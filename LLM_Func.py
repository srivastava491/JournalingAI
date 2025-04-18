from groq import Groq
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLM_Func:
    KEY = os.getenv("GROQ_KEY")  # Define as a class variable

    @staticmethod
    def getQuery(text):  # Removed `self`
        current_date = datetime.now().strftime('%Y-%m-%d')

        client = Groq(
            api_key=LLM_Func.KEY,  # Use class variable
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Generate an SQL query as an SQL Expert. Only provide the SQL query in plain text with no additional information write query so that even if best answer is unvailable you can get some output. The message is: '{text}'. Today's date is {current_date}. The table name is 'Entry' with columns 'date' and 'text'."
                }
            ],
            model="llama-3.1-8b-instant",
        )

        query = chat_completion.choices[0].message.content
        return query

    @staticmethod
    def getResponse(query, text, cursor):  # Removed `self`
        client = Groq(
            api_key=LLM_Func.KEY,  # Use class variable
        )
        cursor.execute(query)
        entries = cursor.fetchall()

        context = ""
        if entries:
            for entry in entries:
                if len(entry) == 2:  # Standard format with date and text
                    context += f"**{entry[0]}**: {entry[1]}\n"
                elif len(entry) == 1:  # Only date or text available
                    context += f"**{entry[0]}**\n"
                elif len(entry) == 0:  # Empty entry
                    context += "**Empty Entry**\n"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"context: {context}, query: {text} answer with no technical information",
                }
            ],
            model="llama-3.1-8b-instant",
        )

        response = chat_completion.choices[0].message.content
        return response
