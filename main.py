import gzip
import struct
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

level_to_read = input("Enter level you want to view (make sure it ends with .lvl): ")

with gzip.open(level_to_read, 'rb') as f:
  data = f.read()

  # Read the header
(identifier, width, length, height, spawn_x, spawn_z, spawn_y, spawn_yaw, spawn_pitch, min_access, min_build) = struct.unpack('<HHHHHHHHBBB', data[:19])


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

def place_block(x, y, z, block):
  if (block == -1):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/invalid.png"
    )
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
  if (block == 3):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/dirt.png"
    )
  if (block == 4):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/cobblestone.png"
    )

  if (block == 5):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/wood.png"
    )

  if (block == 6):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/sapling.png"
    )

  if (block == 7):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/bedrock.png"
    )

  if (block == 8 or block == 9):
    Entity(
    model="cube", color=color.blue, collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "white_cube"
    )

  if (block == 10 or block == 11):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/lava.png"
    )

  if (block == 12):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/sand.png"
    )

  if (block == 13):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/gravel.png"
    )

  if (block == 14):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/gold_ore.png"
    )

  if (block == 15):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/iron_ore.png"
    )

  if (block == 16):
    Entity(
    model="cube", collider="box", ignore = True,
    position = (x, y, z),
    parent = scene,
    texture = "textures/coal_ore.png"
    )

  if (block > 16):
    place_block(x, y, z, -1)

for x in range(width):
  for y in range(height):
    for z in range(length):
      block = get_block(x, y, z)

      if (block != 0):
        place_block(x, y, z, block)


player = FirstPersonController()

scene.fog_color = color.rgb(201, 201, 201)
scene.fog_density = 0.2

player.x = 0
player.y = 0
player.z = 0


app.run()
