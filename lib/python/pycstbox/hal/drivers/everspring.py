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

""" HAL interface classes for EVERSPRING supported products. """

import logging

import pycstbox.hal.device as haldev
import pycstbox.everspring.sm103 as sm103
import pycstbox.everspring.st814 as st814
from pycstbox.hal import hal_device

_logger = logging.getLogger('everspring')

DEFAULT_PRECISION = 3


@hal_device(device_type="everspring.sm103", coordinator_type="zwave")
class SM103(haldev.PolledDevice):
    """ HAL device modeling the EVERSPRING SM103.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(SM103, self).__init__(coord, cfg)
        self._hwdev = sm103.SM103Instrument(coord.port, cfg.address)


@hal_device(device_type="everspring.st814", coordinator_type="zwave")
class ST814(haldev.PolledDevice):
    """ HAL device modeling the everspring st814.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(ST814, self).__init__(coord, cfg)
        self._hwdev = st814.ST814Instrument(coord.port, cfg.address)


