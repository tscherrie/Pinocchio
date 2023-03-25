import subprocess
import json
import time
import configparser


def load_or_create_config(file_name="/Users/jeremias/Documents/pinocchio/model.config"):
    config = configparser.ConfigParser()

    if not config.read(file_name):
        config["DEFAULT"] = {
            "ModelPath": "/Users/jeremias/Downloads/Alpaca/chat_mac",
            "ModelName": "/Users/jeremias/Downloads/Alpaca/ggml-alpaca-13b-q4.bin",
            "StMemory": "/Users/jeremias/Documents/pinocchio/short-term-memory.json"
        }
        with open(file_name, "w") as f:
            config.write(f)

    return config


class ConsciousnessChat:
    def __init__(self, config):
        cmd = [config["DEFAULT"]["ModelPath"], '-m', config["DEFAULT"]["ModelName"]]
        self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

    def send_message(self, message: str) -> str:
        print(message, file=self.process.stdin, flush=True)
        response = self.process.stdout.readline().strip()
        return response

    def close(self):
        self.process.terminate()

def load_short_term_memory(config):
    file_name=config["DEFAULT"]["StMemory"]
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(json.JSONDecodeError)
        with open(file_name, "w") as f:
            json.dump([], f, indent=2)
        return []

def update_short_term_memory(conversation, config):
    file_name=config["DEFAULT"]["StMemory"]
    with open(file_name, "w") as f:
        json.dump(conversation, f, indent=2)

def main():
    config = load_or_create_config()
    chat = ConsciousnessChat(config)
    conversation = load_short_term_memory(config)

    try:
        while True:
            conversation = load_short_term_memory(config)
            if conversation and "sub_consciousness" in conversation[-1] and "consciousness" not in conversation[-1]:
                sub_consciousness_input = conversation[-1]["sub_consciousness"]
                response = chat.send_message(sub_consciousness_input)
                print("Consciousness: ", response)
                conversation[-1]["consciousness"] = response
                update_short_term_memory(conversation)
            time.sleep(1)
    finally:
        chat.close()

if __name__ == "__main__":
    main()
