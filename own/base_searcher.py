import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import numpy as np
from algo_decider import AlgoDecider
from neural_decider import NeuralDecider
from imager import Imager


class Runner:
    degrees = 5

    def __init__(self, robot, decider, logger):
        self.decider = decider
        self.robot = robot
        self.imager = Imager(robot)
        self.logger = logger

    def guide(self):
        # reds = self.imager.get_red_array()
        # action = self.decider.decide(reds)
        while True:
            reds = self.imager.get_red_array()
            action = self.decider.decide(reds)
            self.logger.log(reds, action)
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
        self.robot.drive_straight(distance_mm(30), speed_mmps(150)).wait_for_completed()

    def _left(self):
        self.robot.turn_in_place(degrees(self.degrees)).wait_for_completed()

    def _right(self):
        self.robot.turn_in_place(degrees(-self.degrees)).wait_for_completed()

    def _finish(self):
        self.robot.turn_in_place(degrees(180)).wait_for_completed()
        # self.robot.say_text("Based!").wait_for_completed()


class Logger:
    def __init__(self, filename):
        self.file = open(filename, "a")

    def log(self, input_, output_):
        print(input_)
        print(output_)
        input_ = np.resize(input_, (1, 100))
        self.file.write(' '.join(str(el) for el in input_[0]))
        self.file.write("\n")
        self.file.write(str(output_))
        self.file.write("\n")


def cozmo_program(robot: cozmo.robot.Robot):
    generate_training = True
    if generate_training:
        decider = AlgoDecider()
        logger = Logger("action_data.txt")
    else:
        decider = NeuralDecider()
        logger = Logger("neuro_log.txt")
    runner = Runner(robot, decider, logger)
    runner.guide()


cozmo.run_program(cozmo_program)
