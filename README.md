AI Developer Assignment – Chatbot, SQLite, Analytics

This repository contains my submission for the AI Engineer Technical Evaluation Program.  
I have completed one task from each set (Set 1, Set 2, Set 3).

Set 1 – Chatbot with Logging
Files: `set1_L1-05chatbot.py`, `logger.py`, `chat_logs.txt`  
- Implements a simple chatbot.  
- Uses `logger.py` to log conversations.  
- Logs are stored in `chat_logs.txt`.

Run in PowerShell:
python set1_L1-05chatbot.py

Set 2 – SQLite Integration

Files: set2_L2-05_sqlite.py, set2_L2-05.db
This task demonstrates how to use SQLite for structured data storage.
The Python script connects to a local SQLite database, creates tables, and allows inserting and retrieving records.
The database file set2_L2-05.db is automatically created and updated when you run the script.

Expected Output:

A new SQLite database file (set2_L2-05.db) is generated.
Tables are created (e.g., patients, services, etc.).
Records can be inserted and queried successfully.

Set 3 – Analytics & Reporting

File : set3_L3-05_analytics.py
This task focuses on reporting and analytics.
The script reads chat_logs.txt to calculate metrics like total chats, average latency, and average tokens.
It also connects to set2_L2-05.db to run queries and report counts (e.g., number of patients)

Expected Output:

Displays analytics from chat logs:
Total chats
Average latency (seconds)
Average tokens used
Displays analytics from SQLite database:
Row counts from tables (e.g., patients)


