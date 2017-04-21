#! /usr/bin/env python

import math

import urx
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

# Defaults for movement
DEFAULT_ACC = 1.5
DEFAULT_VEL = 0.5

DEFAULT_SPEED = 255
DEFAULT_FORCE = 50

ROT_LIMIT = 180.0


def limit_rotation(rotation):
    """
    Limit the rotation to values to within ROT_LIMIT
    """
    if abs(rotation) > ROT_LIMIT:
        if rotation <= 0:
            rot = -1 * ROT_LIMIT
        else:
            rot = ROT_LIMIT
    else:
        rot = rotation
    return math.radians(rot)


RIGHT = math.radians(-40)
CENTER = math.radians(-80)
LEFT = math.radians(-120)

GRIPPER = -3.14166


class RealmsRobot(urx.Robot):

    def __init__(self, robot_ip, payload=0.95):
        super(RealmsRobot, self).__init__(robot_ip)
        self.set_payload(payload)
        self.gripper = Robotiq_Two_Finger_Gripper(self,
                                                  payload=payload,
                                                  speed=DEFAULT_SPEED,
                                                  force=DEFAULT_FORCE)

    def go_to_waypoint(self, waypoint, acc=DEFAULT_ACC, vel=DEFAULT_VEL):
        # print([round(math.degrees(w), 3) for w in waypoint])
        self.movej(waypoint, acc=acc, vel=vel)

    def rotate(self, angle,
               acc=DEFAULT_ACC, vel=DEFAULT_VEL):
        print('rotate {}'.format(angle))

        # Ensure we don't send in bad values and convert to radians
        rot = limit_rotation(angle)

        # Get the current position
        # Modify the last joint to the desired rotation
        joints = self.getj()
        joints = joints[:5] + [rot]

        # Move the robot to the desired position
        self.go_to_waypoint(joints)

    def up(self):
        print('up')
        waypoint = [CENTER, -1.1781, -1.77325, -0.13963, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def down(self):
        print('down')
        waypoint = [CENTER, -2.58322, -2.0003, 1.47119, 1.57095, GRIPPER]
        self.go_to_waypoint(waypoint)

    def left(self):
        print('left')
        waypoint = [LEFT, -1.83085, -2.20784, 0.89884, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def right(self):
        print('right')
        waypoint = [RIGHT, -1.83085, -2.20784, 0.89884, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def center(self):
        print('center')
        waypoint = [CENTER, -1.83085, -2.20784, 0.89884, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def upper_left(self):
        print('upper_left')
        waypoint = [LEFT, -1.1781, -1.77325, -0.13963, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def upper_right(self):
        print('upper_right')
        waypoint = [RIGHT, -1.1781, -1.77325, -0.13963, 1.53414, GRIPPER]
        self.go_to_waypoint(waypoint)

    def lower_left(self):
        print('lower_left')
        waypoint = [LEFT, -2.58322, -2.0003, 1.47119, 1.57095, GRIPPER]
        self.go_to_waypoint(waypoint)

    def lower_right(self):
        print('lower_right')
        waypoint = [RIGHT, -2.58322, -2.0003, 1.47119, 1.57095, GRIPPER]
        self.go_to_waypoint(waypoint)

    def open_gripper(self):
        print('open gripper')
        self.gripper.open_gripper()

    def close_gripper(self):
        print('close gripper')
        self.gripper.close_gripper()

    def press_red_button(self):
        print('press red button')
        waypoint_list = [
            [-1.36413, -1.59541, -1.98985, 0.65372, 1.59265, -3.19592],
            [-0.36352, -2.21603, -1.07701, -1.40518, 1.59142, -3.19591],
            [-0.35618, -2.31777, -1.08357, -1.32479, 1.59186, -3.19596],
            [-0.36352, -2.21603, -1.07701, -1.40518, 1.59142, -3.19591],
            [-1.36413, -1.59541, -1.98985, 0.65372, 1.59265, -3.19592],
        ]
        for waypoint in waypoint_list:
            self.go_to_waypoint(waypoint)
