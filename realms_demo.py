#! /usr/bin/env python

import logging

from realms import RealmsRobot


def main():

    ROBOT_IP = '192.168.1.110'
    with RealmsRobot(ROBOT_IP) as robot:

        # OPEN THE GRIPPER
        robot.open_gripper()

        # MOVE AROUND
        robot.up()

        robot.upper_right()
        robot.right()
        robot.lower_right()

        robot.down()

        robot.lower_left()
        robot.left()
        robot.upper_left()

        robot.up()
        robot.center()

        # CLOSE THE GRIPPER
        robot.close_gripper()


if __name__ == "__main__":
    LOG_FILENAME = 'example.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        log_level=logging.INFO)
    main()
