import os

def calculator(expression: str):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error in calculation: {e}"

def file_lookup(filename: str, keyword: str):
    try:
        with open(filename, "r") as f:
            content = f.read()
        if keyword in content:
            return f"Keyword '{keyword}' found in {filename}"
        else:
            return f"Keyword '{keyword}' not found"
    except FileNotFoundError:
        return f"File {filename} not found"

def agent(user_input: str):
    if any(word in user_input.lower() for word in ["add", "sum", "calculate", "multiply", "divide"]):
        expression = user_input.replace("calculate", "").strip()
        return calculator(expression)
    elif "search" in user_input.lower():
        parts = user_input.split()
        if len(parts) >= 3:
            filename, keyword = parts[1], parts[2]
            return file_lookup(filename, keyword)
        else:
            return "Usage: search <filename> <keyword>"
    else:
        return "Sorry, I don't know which tool to use for that."


if __name__ == "__main__":
    print(agent("calculate 5 + 10 * 2"))
    print(agent("search chat_logs.txt latency"))
    print(agent("search missing.txt hello"))
