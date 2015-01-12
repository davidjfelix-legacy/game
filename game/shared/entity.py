#!/usr/bin/env python
from uuid import UUID, uuid4


class EntityMotion(object):

    def __init__(self):
        self.location = [0.0, 0.0, 0.0]
        self.velocity = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]

    def move(self, time_delta):
        delta = EntityMotion.vel_to_displ_delta(time_delta, self.velocity)
        self.location = [a + b for a, b in zip(self.location, delta)]

    def accel_move(self, time_delta, acceleration):
        delta_d1 = EntityMotion.vel_to_displ_delta(time_delta, self.velocity)
        delta_v = EntityMotion.accel_to_vel_delta(time_delta, acceleration)
        self.velocity = [a + b for a, b in zip(self.velocity, delta_v)]
        delta_d2 = EntityMotion.vel_to_displ_delta(time_delta, self.velocity)
        delta_d = [(a + b)/2 for a, b in zip(delta_d1, delta_d2)]
        self.location = [a + b for a, b in zip(self.location, delta_d)]

    @staticmethod
    def timedelta_to_seconds(time_delta):
        days = time_delta.days
        seconds = time_delta.seconds
        microseconds = time_delta.microseconds
        return (days * 86400) + (seconds) + (microseconds * 0.000001)

    @staticmethod
    def accel_to_vel_delta(time_delta, acceleration):
        seconds = EntityMotion.timedelta_to_seconds(time_delta)
        return [each * seconds for each in acceleration]

    @staticmethod
    def vel_to_displ_delta(time_delta, velocity):
        seconds = EntityMotion.timedelta_to_seconds(time_delta)
        return [each * seconds for each in velocity]


class Entity(object):

    def __init__(self, uuid=None):
        if uuid:
            self.uuid = UUID(str(uuid))
        else:
            self.uuid = uuid4()

        self.display_name = ""
        self.movement = EntityMotion()
        self.address = ""
        self.is_name_visible = ""
        self.scale = 0

    def __repr__(self):
        return str(self.uuid)

    def __str__(self):
        return str(self.display_name)

    def tick(self, time_delta):
        self.movement.move(time_delta)
