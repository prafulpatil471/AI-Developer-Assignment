import os

class MathAgent:
    def handle(self, task: str):
        try:
            return eval(task)
        except Exception as e:
            return f"MathAgent error: {e}"

class SearchAgent:
    def handle(self, filename: str, keyword: str):
        try:
            with open(filename, "r") as f:
                content = f.read()
            if keyword in content:
                return f"Keyword '{keyword}' found in {filename}"
            else:
                return f"Keyword '{keyword}' not found"
        except FileNotFoundError:
            return f"SearchAgent error: File {filename} not found"


class SupervisorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.search_agent = SearchAgent()

    def delegate(self, user_input: str):
        if any(word in user_input.lower() for word in ["add", "sum", "calculate", "multiply", "divide"]):
            expression = user_input.replace("calculate", "").strip()
            return self.math_agent.handle(expression)
        elif "search" in user_input.lower():
            parts = user_input.split()
            if len(parts) >= 3:
                filename, keyword = parts[1], parts[2]
                return self.search_agent.handle(filename, keyword)
            else:
                return "Usage: search <filename> <keyword>"
        else:
            return "SupervisorAgent: No suitable agent found for this task."


if __name__ == "__main__":
    supervisor = SupervisorAgent()
    print(supervisor.delegate("calculate 10 + 20 / 2"))
    print(supervisor.delegate("search chat_logs.txt latency"))
    print(supervisor.delegate("search missing.txt hello"))
    print(supervisor.delegate("unknown task"))
