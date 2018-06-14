import cozmo
import time
# import PIL PI
from PIL import ImageEnhance

def cozmo_program(robot: cozmo.robot.Robot):
    # print(cozmo.__version__)
    # print(dir(robot.camera))
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.set_head_angle(cozmo.util.radians(0))
    time.sleep(0.3)
    # time.sleep(0.5)
    # # while True:
    # #     time.sleep(0.1)
    # #     image = robot.world.latest_image
    # #     if image is not None:
    # #         break
    # #     print("image = %s" % image)
    # # time.sleep(1)
    pic_filename = "picture1.jpeg"
    image = robot.world.latest_image
    raw = image.raw_image
    print(raw.size)
    modified = raw
    # modified = raw.resize((10, 10))


    modified.show()
    time.sleep(1)
    # # print(dir(image))
    # print(image)
    #
    # # robot.camera.image_stream_enabled = True
    # # while True:
    # #     time.sleep(0.2)

cozmo.run_program(cozmo_program)
# cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
# cozmo.run.connect_with_tkviewer(cozmo_program)
