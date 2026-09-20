import logging

logging.basicConfig(
    filename="chat_logs.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_interaction(prompt, response, latency, tokens_used):
    logging.info(
        f"PROMPT: {prompt} | RESPONSE: {response} | LATENCY: {latency:.2f}s | TOKENS: {tokens_used}"
    )
