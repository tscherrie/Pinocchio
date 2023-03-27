import sys

def get_user_input():
    user_input = input("Enter your command: ").strip()
    return user_input

def run_input_layer():
    while True:
        command = get_user_input()

        if command.lower() == "quit":
            print("Exiting...")
            break
        else:
            print(f"Received command: {command}")
            # Send command to LLM Decision Center for processing.
            # For now, we're just printing the command.

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        print(f"Received command: {command}")
        # Send command to LLM Decision Center for processing.
        # For now, we're just printing the command.
    else:
        run_input_layer()
