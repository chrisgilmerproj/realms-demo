#! /usr/bin/env python

import logging

from realms import RealmsRobot


def main():

    ROBOT_IP = '192.168.1.110'
    with RealmsRobot(ROBOT_IP) as robot:

        # OPEN AND CLOSE THE GRIPPER
        for X in range(1, 3):
            robot.open_gripper()
            robot.close_gripper()


if __name__ == "__main__":
    LOG_FILENAME = 'example.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        log_level=logging.INFO)
    main()
