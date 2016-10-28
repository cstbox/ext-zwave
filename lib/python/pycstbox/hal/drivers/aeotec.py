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

""" HAL interface classes for AEOTEC supported products. """

import logging

import pycstbox.hal.device as haldev
import pycstbox.aeotec.dsb28 as dsb28
from pycstbox.hal import hal_device

_logger = logging.getLogger('aeotec')

DEFAULT_PRECISION = 3


@hal_device(device_type="aeotec.dsb28", coordinator_type="zwave")
class DSB28(haldev.PolledDevice):
    """ HAL device modeling the AEOTEC DSB28.

    The extension adds the support of polling requests and CSTBox events
    publishing on D-Bus.
    """

    def __init__(self, coord, cfg):
        super(DSB28, self).__init__(coord, cfg)
        self._hwdev = dsb28.DSB28Instrument(coord.port, cfg.address)
        



