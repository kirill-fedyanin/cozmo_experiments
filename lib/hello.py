import cozmo
import time


def cozmo_program(robot: cozmo.robot.Robot):
    robot.set_lift_height(1.0).wait_for_completed()
    robot.set_lift_height(-1.0).wait_for_completed()
    robot.say_text("Have a nice day, Polina").wait_for_completed()
    robot.move_lift(2)
    robot.move_lift(-2)


cozmo.run_program(cozmo_program)