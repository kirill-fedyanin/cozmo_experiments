import cozmo
import time
# import PIL PI
from PIL import ImageEnhance

def cozmo_program(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.set_head_angle(cozmo.util.radians(0))
    time.sleep(0.3)

    image = robot.world.latest_image
    raw = image.raw_image
    print(raw.size)
    raw.show()
    time.sleep(1)
    robot.camera.image_stream_enabled = True
    while True:
        time.sleep(0.2)


cozmo.run.connect_with_tkviewer(cozmo_program)
