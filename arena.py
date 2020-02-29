# Joel Coddington @ Friday Feb. 28, 2020
# Arena Minigame

from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint
import time

mc = Minecraft.create(address="localhost", port=4711)
mc.postToChat("GET YOUR WEAPONS READY!. . .")
time.sleep(8)

id_list = mc.getPlayerEntityIds()

# selecting random x and z coordinates
x_rand = randint(-10000, 10000)
z_rand = randint(-10000, 10000)

# .getPlayerEntityIds() to teleport everyone
for id in id_list:
    pos = mc.entity.getPos(id)

    start_x = pos.x
    start_y = pos.y
    start_z = pos.z

    # sets a random coordinate for the fight to occur at
    new_x = start_x + x_rand
    new_z = start_z + z_rand

    # sets player to random x and z coordinates while keeping the
    # y coordinate low enough they won't die of fall damage
    new_player_x = new_x + 15
    new_player_z = new_z + 15
    mc.entity.setPos(id, new_player_x, 85, new_player_z)

    # blocks are spawned in a hallowed square (sides a, b, c, & d, each with height h)
    for a in range(-20, 20):
        for h in range(0, 90):
            x = new_x + 20 + a
            y = h
            z = new_z
            mc.setBlock(x, y, z, block.FENCE.id, 1)
    for b in range(-20, 15):
        for h in range(0, 90):
            x = new_x
            y = h
            z = new_z + 20 + b
            mc.setBlock(x, y, z, block.FENCE.id, 1)
    for c in range(-20, 20):
        for h in range(0, 90):
            x = new_x + 20 + c
            y = h
            z = new_z + 35
            mc.setBlock(x, y, z, block.FENCE.id, 1)
    for d in range(-20, 16):
        for h in range(0, 90):
            x = new_x + 40
            y = h
            z = new_z + 20 + d
            mc.setBlock(x, y, z, block.FENCE.id, 1)

    # pauses for fight -- 60 seconds
    mc.postToChat("YOU HAVE 1 MINUTE TO FIGHT!")
    time.sleep(15)
    mc.postToChat("45 SECONDS LEFT!")
    time.sleep(15)
    mc.postToChat("30 SECONDS LEFT!")
    time.sleep(20)
    # countdown from 10 begins
    for x in range(10, 0, -1):
        second_count = str(x)
        time.sleep(1)
        mc.postToChat("{}!".format(second_count))

    # teleports each player back to original coordinates
    time.sleep(2)

    mc.entity.setPos(id, start_x, start_y, start_z)

    mc.postToChat("Thanks for playing!")
