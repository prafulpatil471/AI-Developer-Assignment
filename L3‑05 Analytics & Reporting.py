
import sqlite3
import re

def analyze_chat_logs(log_file="chat_logs.txt"):
    try:
        with open(log_file, "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        print("No chat_logs.txt found.")
        return

    total_chats = len(logs)
    latencies = []
    tokens = []

    for line in logs:
        
        if "LATENCY:" in line and "TOKENS:" in line:
            try:
                latency_match = re.search(r"LATENCY:\s*([\d\.]+)", line)
                tokens_match = re.search(r"TOKENS:\s*(\d+)", line)

                if latency_match:
                    latencies.append(float(latency_match.group(1)))
                if tokens_match:
                    tokens.append(int(tokens_match.group(1)))
            except Exception as e:
                print("Parse error:", e)

    print("\n--- Chat Log Analytics ---")
    print(f"Total chats: {total_chats}")
    if latencies:
        print(f"Average latency: {sum(latencies)/len(latencies):.3f} sec")
    if tokens:
        print(f"Average tokens used: {sum(tokens)/len(tokens):.1f}")

def analyze_sqlite(db_file="set2_L2-05.db"):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM patients;")
        count = cursor.fetchone()[0]

        print("\n--- SQLite Analytics ---")
        print(f"Total patients in DB: {count}")

        conn.close()
    except Exception as e:
        print("SQLite analysis failed:", e)

if __name__ == "__main__":
    analyze_chat_logs()
    analyze_sqlite()

