AI Developer Assignment – Chatbot, SQLite, Analytics

This repository contains my submission for the AI Engineer Technical Evaluation Program.  
I have completed one task from each set (Set 1, Set 2, Set 3).

Set 1 – Task L1-05 : LLM Observability and Logging
Files: set1_L1-05chatbot.py, logger.py, chat_logs.txt  
- Implements a simple chatbot.  
- Uses logger.py to log conversations.  
- Logs are stored in `chat_logs.txt.

Expected Output:

Chatbot responds to user input with simple replies.
Each interaction is logged in chat_logs.txt with details such as:
Prompt text
Response text
Latency (seconds)
Approximate token usage
Example : [2026-09-20 22:30:15] Prompt: Hello
Response: Hi there! How can I help you?
Latency: 0.45s
Tokens: 12

-----------------------------------------------------------

Set 2 – Task L2‑02: AI Agent with Tool Calling
Files:set2_L2-02_tool_agent.py  
- Implements an AI Agent capable of selecting and invoking tools based on user intent.  
- Includes two tools:
  - Calculator Tool → evaluates math expressions.  
  - File Lookup Tool → searches a file for a keyword.  
- Agent (`agent()`) decides which tool to call by analyzing the user input.  
- Handles tool failures gracefully (e.g., missing file, invalid math expression).  

Expected Output:

Correct math result (e.g., 25)
Keyword search result (e.g., "Keyword 'latency' found in chat_logs.txt")
Graceful error handling (e.g., "File missing.txt not found")

----------------------------------------------

Set 3 – Task L3‑01: Multi-Agent System
Files: set3_L3-01_multi_agent.py

Implements a system where multiple AI agents collaborate to complete tasks.
Agents:
MathAgent → performs calculations.
SearchAgent → searches files for keywords.
SupervisorAgent coordinates tasks and delegates them to the correct agent.
Demonstrates task delegation, coordination, and clear role separation.
Handles errors gracefully (e.g., missing file, unknown task).

Expected Output:

MathAgent performs calculations (e.g., 20.0).
SearchAgent searches files for keywords (e.g., "Keyword 'latency' not found").
SupervisorAgent coordinates tasks and reports when no suitable agent is found.

