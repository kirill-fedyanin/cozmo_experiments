import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
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

    def get_red_array(self):
        red = self.get_red()
        self.show(red.resize((320, 240)), False)
        pixels = list(red.getdata())
        reds = [pixel[0] for pixel in pixels]
        reds = np.resize(np.array(reds), (10, 10))

        return reds

    def show(self, image, block=True):
        plt.imshow(image)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show(block=block)

class Runner:
    degrees = 15

    def __init__(self, decider, robot, imager):
        self.decider = decider
        self.robot = robot
        self.imager = imager

    def guide(self):
        while True:
            reds = self.imager.get_red_array()
            action = self.decider.decide(reds)
            if action == 0:
                self._finish()
                break
            elif action == 1:
                self._right()
            elif action == 2:
                self._left()
            elif action == 3:
                self._right()
            elif action == 4:
                self._forward()
            else:
                raise RuntimeError("Unknow action")

    def _forward(self):
        self.robot.drive_straight(distance_mm(100), speed_mmps(100)).wait_for_completed()

    def _left(self):
        self.robot.turn_in_place(degrees(self.degrees)).wait_for_completed()

    def _right(self):
        self.robot.turn_in_place(degrees(-self.degrees)).wait_for_completed()

    def _finish(self):
        self.robot.turn_in_place(degrees(180)).wait_for_completed()
        self.robot.say_text("Based!").wait_for_completed()


class AlgoDecider:
    threshold = 65
    sum_threshold = 1500

    # def __init__(self, robot, imager=None):
    #     self.robot = robot
    #     self.imager = imager

    def decide(self, reds):
        if np.amax(reds) < self.threshold:
            return 1
        else:
            columns = reds.sum(axis=0)
            max_column = np.argmax(columns)
            print("Max column", max_column)
            print("Sum", columns.sum())

            if columns.sum() > self.sum_threshold:
                return 0
            elif max_column < 2:
                return 2
            elif max_column > 7:
                return 3
            else:
                return 4



def cozmo_program(robot: cozmo.robot.Robot):
    imager = Imager(robot)
    runner = Runner(AlgoDecider(), robot, imager)
    runner.guide()


cozmo.run_program(cozmo_program)
