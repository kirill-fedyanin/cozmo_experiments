import cozmo
import time


def cozmo_program(robot: cozmo.robot.Robot):
    # robot.say_text("Hello World").wait_for_completed()
    # robot.say_text("Fuck the police").wait_for_completed()
    # robot.say_text("Happy child day, Alice").wait_for_completed()
    # robot.say_text("Suka blyat").wait_for_completed()
    # robot.say_text("Hi, kristina, how do you do?").wait_for_completed()
    # robot.say_text("Have a nice day, Polina").wait_for_completed()
    # robot.set_head_angle(cozmo.util.radians(1)).wait_for_completed()
    time.sleep(3)
    # robot.set_head_angle(cozmo.util.radians(0.5)).wait_for_completed()
    robot.set_lift_height(1.0).wait_for_completed()
    robot.set_lift_height(-1.0).wait_for_completed()
    # robot.say_text("Have a nice day, Polina").wait_for_completed()
    # robot.say_text("Hi").wait_for_completed()
    # robot.move_lift(2)
    # robot.move_lift(-2)


cozmo.run_program(cozmo_program)