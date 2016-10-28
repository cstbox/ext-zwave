#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CSTBox.
#
# CSTBox is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CSTBox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with CSTBox.  If not, see <http://www.gnu.org/licenses/>.

""" HAL interface classes for FIBARO supported products. """

import logging

import pycstbox.hal.device as haldev
import pycstbox.fibaro.wall_plug as wall_plug
import pycstbox.fibaro.motion_sensor as motion_sensor
import pycstbox.fibaro.door_sensor as door_sensor
from pycstbox.hal import hal_device

_logger = logging.getLogger('fibaro')

DEFAULT_PRECISION = 3


@hal_device(device_type="fibaro.wall_plug", coordinator_type="zwave")
class WALL_PLUG(haldev.PolledDevice):
    """ HAL device modeling the FIBARO wall plug.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(WALL_PLUG, self).__init__(coord, cfg)
        self._hwdev = wall_plug.WALL_PLUGInstrument(coord.port, cfg.address)


@hal_device(device_type="fibaro.motion_sensor", coordinator_type="zwave")
class MOTION_SENSOR(haldev.PolledDevice):
    """ HAL device modeling the FIBARO motion sensor.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(MOTION_SENSOR, self).__init__(coord, cfg)
        self._hwdev = motion_sensor.MOTION_SENSORInstrument(coord.port, cfg.address)
        
@hal_device(device_type="fibaro.door_sensor", coordinator_type="zwave")
class DOOR_SENSOR(haldev.PolledDevice):
    """ HAL device modeling the fibaro door sensor.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(DOOR_SENSOR, self).__init__(coord, cfg)
        self._hwdev = door_sensor.DOOR_SENSORInstrument(coord.port, cfg.address)


