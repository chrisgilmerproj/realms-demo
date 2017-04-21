#! /usr/bin/env python

import logging
import math

from realms import RealmsRobot


def main():

    ROBOT_IP = '192.168.1.110'
    with RealmsRobot(ROBOT_IP) as robot:

        robot.center()
        
        # GO TO COMPASS POINTS
        for X in range(1,3):
            robot.up()
            robot.down()
            robot.left()
            robot.right()


if __name__ == "__main__":
    LOG_FILENAME = 'example.log'
    logging.basicConfig(filename=LOG_FILENAME,
                        log_level=logging.INFO)
    main()
