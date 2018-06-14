import cozmo
import time
from PIL import Image

def cozmo_program(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.set_head_angle(cozmo.util.radians(0))
    time.sleep(0.3)

    pic_filename = "picture1.jpeg"
    raw = robot.world.latest_image.raw_image
    pixels = list(raw.getdata())
    # print(pixels)
    # print(pixels)
    new_pixels = []

    # left red only
    for pixel in pixels:
        red = max((pixel[0] - (pixel[1]+pixel[2])//2 - 40) * 2, 0)
        pixel = (red, 0, 0)
        new_pixels.append(pixel)

    modified = Image.new(raw.mode, (320, 240))
    modified.putdata(new_pixels)
    modified = modified.resize((10, 10))
    modified = modified.resize((320, 240))
    # modified = raw.resize((10, 10))

    modified.show()
    # raw.show()
    time.sleep(1)

cozmo.run_program(cozmo_program)
