import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

import numpy as np
from lib.algo_decider import AlgoDecider
from lib.neural_decider import NeuralDecider
from lib.imager import Imager


class Runner:
    degrees = 3
    distance = 30

    def __init__(self, robot, decider, logger):
        self.decider = decider
        self.robot = robot
        self.imager = Imager(robot)
        self.logger = logger

    def guide(self):
        actions = ['_finish', '_right', '_left', '_right', '_forward']
        while True:
            reds = self.imager.get_red_array()
            action = self.decider.decide(reds)
            self.logger.log(reds, action)
            getattr(self, actions[action])()

    def _forward(self):
        self.robot.drive_straight(distance_mm(self.distance), speed_mmps(150), should_play_anim=False)\
            .wait_for_completed()

    def _left(self):
        self.robot.turn_in_place(degrees(self.degrees)).wait_for_completed()

    def _right(self):
        self.robot.turn_in_place(degrees(-self.degrees)).wait_for_completed()

    def _finish(self):
        self.robot.turn_in_place(degrees(180)).wait_for_completed()
        self.robot.say_text("Based!").wait_for_completed()


class Logger:
    def __init__(self, filename):
        self.file = open(filename, "a")

    def log(self, input_, output_):
        input_ = np.resize(input_, (1, 100))
        self.file.write(' '.join(str(el) for el in input_[0]))
        self.file.write("\n")
        self.file.write(str(output_))
        self.file.write("\n")


def cozmo_program(robot: cozmo.robot.Robot):
    generate_training = False

    if generate_training:
        decider = AlgoDecider()
        logger = Logger("data/action_data.txt")
    else:
        decider = NeuralDecider()
        logger = Logger("data/neuro_log.txt")
    runner = Runner(robot, decider, logger)

    runner.guide()


cozmo.run_program(cozmo_program)
