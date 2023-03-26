import subprocess
import json
import time

def load_model_config(file_name="model.config"):
    try:
        with open(file_name, "r") as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        config = {
            "cmd": ["/Users/jeremias/Downloads/Alpaca/chat_mac", "-m", "/Users/jeremias/Downloads/Alpaca/ggml-alpaca-13b-q4.bin"]
        }
        with open(file_name, "w") as f:
            json.dump(config, f, indent=2)

    return config

class SubConsciousnessChat:
    def __init__(self, cmd):
        # Start the chat.cpp process
        self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

    def send_message(self, message: str) -> str:
        # Send the message to the chat.cpp process
        print(message, file=self.process.stdin, flush=True)

        # Read the response from the chat.cpp process
        response = self.process.stdout.readline().strip()

        return response

    def close(self):
        # Terminate the chat.cpp process
        self.process.terminate()

def load_short_term_memory(file_name="short-term-memory.json"):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(file_name, "w") as f:
            json.dump([], f, indent=2)
        return []

def update_short_term_memory(conversation, file_name="short-term-memory.json"):
    with open(file_name, "w") as f:
        json.dump(conversation, f, indent=2)

def main():
    config = load_model_config()
    chat = SubConsciousnessChat(config["cmd"])
    conversation = load_short_term_memory()

    try:
        while True:
            conversation = load_short_term_memory()
            if conversation and "consciousness" in conversation[-1] and "sub_consciousness" not in conversation[-1]:
                consciousness_input = conversation[-1]["consciousness"]

                sub_consciousness_response = chat.send_message(consciousness_input)
                print("Sub_consciousness: ", sub_consciousness_response)

                conversation[-1]["sub_consciousness"] = sub_consciousness_response
                update_short_term_memory(conversation)

            time.sleep(1)  # Wait for 1 second before checking for new messages
    finally:
        chat.close()

if __name__ == "__main__":
    main()
