import gzip
import struct
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

level_to_read = input("Enter level you want to view (make sure it ends with .lvl): ")

with gzip.open(level_to_read, 'rb') as f:
  data = f.read()

  # Read the header
(identifier, width, length, height, spawn_x, spawn_z, spawn_y, spawn_yaw, spawn_pitch, min_access, min_build) = struct.unpack('<HHHHHHHHBBB', data[:18])


def get_block(x, y, z):
  if identifier != 1874:
    print('Invalid lvl file')
    return

  # Read the blocks
  blocks = data[18:]

  # Calculate the block index
  index = (y * length + z) * width + x
  
  block_id = blocks[index]

  return block_id

app = Ursina()

def place_invalid_block(x, y, z):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/invalid.png"
    )

def place_block(x, y, z, block):
  if (block == 1):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/stone.png"
    )
  if (block == 2):
    Entity(
    model="cube", color=color.green, collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/grass.png"
    )

  if (block == 0 or block > 2):
    place_invalid_block(x, y, z)

for x in range(width):
  for y in range(height):
    for z in range(length):
      block = get_block(x, y, z)

      if (block != 0):
        place_block(x, y, z, block)


player = FirstPersonController()


player.x = 0
player.y = 0
player.z = 0


app.run()



