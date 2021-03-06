#! /usr/bin/env python

import logging

from realms import RealmsRobot


def main():

    ROBOT_IP = '192.168.1.110'
    with RealmsRobot(ROBOT_IP) as robot:

        # PRESS RED BUTTON
        robot.center()
        robot.close_gripper()
        robot.press_red_button()
        robot.center()


if __name__ == "__main__":
    LOG_FILENAME = 'example.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        log_level=logging.INFO)
    main()
