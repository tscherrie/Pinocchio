import asyncio
import minedojo
from functools import partial

class EnvInteraction:
    def __init__(self):
        self.minecraft_env = minedojo.make(
            task_id="open-ended",
            image_size=(160, 256)
        )

    async def execute_action(self, action):
        loop = asyncio.get_event_loop()
        step_func = partial(self.minecraft_env.step, action)
        obs, reward, done, info = await loop.run_in_executor(None, step_func)
        return obs, reward, done, info

    async def reset(self):
        loop = asyncio.get_event_loop()
        obs = await loop.run_in_executor(None, self.minecraft_env.reset)
        return obs

    async def close(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.minecraft_env.close)

async def main():
    env_interaction = EnvInteraction()
    obs = await env_interaction.reset()

    for i in range(50):
        act = env_interaction.minecraft_env.action_space.no_op()
        act[0] = 1  # forward/backward
        if i % 10 == 0:
            act[2] = 1  # jump

        print(f"Executing action: {act}")
        obs, reward, done, info = await env_interaction.execute_action(act)
        print(f"Result of action: obs: {obs}, reward: {reward}, done: {done}, info: {info}")

    await env_interaction.close()

if __name__ == "__main__":
    asyncio.run(main())
