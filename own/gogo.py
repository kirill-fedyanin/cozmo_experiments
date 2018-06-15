import cozmo
import time
import PIL
from PIL import Image, ImageTk

from matplotlib import pyplot as plt
import numpy as np


class CozmoTrainer:
    def __init__(self):
        pass

class Imager:
    def __init__(self, robot):
        robot.camera.image_stream_enabled = True
        robot.camera.color_image_enabled = True
        robot.set_head_angle(cozmo.util.radians(0))
        time.sleep(0.3)
        self.robot = robot

    def get_red(self):
        raw = self.robot.world.latest_image.raw_image
        pixels = list(raw.getdata())
        new_pixels = []
        # self.show(raw)

        # left red only
        for pixel in pixels:
            red = min(max((pixel[0] - (pixel[1]+pixel[2])//2 - 40) * 2, 0), 255)
            pixel = (red, 0, 0)
            new_pixels.append(pixel)

        modified = Image.new(raw.mode, (320, 240))
        modified.putdata(new_pixels)
        modified = modified.resize((10, 10))
        return modified

    def show(self, image, block=True):
        # image.show()
        # ImageTk.PhotoImage(image)
        # time.sleep(1)
        plt.imshow(image)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show(block=block)


class MarkerGuide:
    def __init__(self, robot, imager=None):
        self.robot = robot
        self.imager = imager

    def guide(self):
        red = self.imager.get_red()
        self.imager.show(red.resize((320, 240)))
        pixels = list(red.getdata())
        reds = [pixel[0] for pixel in pixels]
        reds = np.resize(np.array(reds), (10, 10))

        print(reds)





def cozmo_program(robot: cozmo.robot.Robot):
    imager = Imager(robot)
    guider = MarkerGuide(robot, imager)
    guider.guide()


cozmo.run_program(cozmo_program)
