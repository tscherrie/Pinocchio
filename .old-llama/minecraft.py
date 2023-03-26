import gym
import minerl
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.ERROR) # reduce clutter, remove if something doesn't work to see the error logs.

#env = gym.make("MineRLBasaltBuildVillageHouse-v0")
env = gym.make("MineRLBasaltFindCave-v0")

obs = env.reset()
done = False

while not done:
    action = env.action_space.noop()
    keyboard_input = input("Enter action: ")
    if keyboard_input == "w":
        action["forward"] = 1
    elif keyboard_input == "a":
        action["left"] = 1
    elif keyboard_input == "s":
        action["back"] = 1
    elif keyboard_input == "d":
        action["right"] = 1
    elif keyboard_input == "space":
        action["jump"] = 1
    elif keyboard_input == "shift":
        action["sneak"] = 1
    elif keyboard_input == "f":
        action["attack"] = 1
    elif keyboard_input == "e":
        action["camera"] = [0, 1]
    elif keyboard_input == "q":
        action["camera"] = [0, -1]
    elif keyboard_input == "esc":
        break



    obs, reward, done, info = env.step(action)
    env.render()
env.close()