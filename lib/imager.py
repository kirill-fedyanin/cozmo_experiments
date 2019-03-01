import time
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


class Imager:
    def __init__(self, robot):
        robot.camera.image_stream_enabled = True
        robot.camera.color_image_enabled = True
        robot.set_head_angle(degrees(0)).wait_for_completed()
        self.robot = robot
        time.sleep(0.3)

    def get_red(self):
        raw = self.robot.world.latest_image.raw_image
        pixels = list(raw.getdata())
        new_pixels = []

        # left red only
        for pixel in pixels:
            red = min(max((pixel[0] - (pixel[1]+pixel[2])//2 - 40) * 2, 0), 255)
            pixel = (red, 0, 0)
            new_pixels.append(pixel)

        modified = Image.new(raw.mode, (320, 240))
        modified.putdata(new_pixels)
        modified = modified.resize((10, 10))
        return modified

    def get_red_array(self):
        red = self.get_red()
        pixels = list(red.getdata())
        reds = [pixel[0] for pixel in pixels]
        reds = np.resize(np.array(reds), (10, 10))

        return reds

    def show(self, image, block=True):
        plt.imshow(image)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show(block=block)

