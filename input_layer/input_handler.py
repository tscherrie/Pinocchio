import asyncio
import sys

async def get_user_input():
    user_input = input("Enter your command: ").strip()
    return user_input

async def run_input_layer():
    while True:
        command = await get_user_input()

        if command.lower() == "quit":
            print("Exiting...")
            break
        else:
            print(f"Received command: {command}")
            # Eventually, send command to LLM Decision Center for processing.
            # For now, we're just printing the command.

async def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        print(f"Received command: {command}")
        # Eventually, send command to LLM Decision Center for processing.
        # For now, we're just printing the command.
    else:
        await run_input_layer()

if __name__ == "__main__":
    asyncio.run(main())
