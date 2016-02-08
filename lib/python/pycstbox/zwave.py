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

""" Common definitions and helpers for ZWAVE devices support."""

from collections import namedtuple


class ZWaveRegister(namedtuple('ZWAveRegister', ['inst', 'cmd_cls', 'data'])):
    """ ZWAve value description.

    :var inst:  instance number
    :var cmd_cls: command class number
    :var data: data number
    """
    def __new__(cls, inst, cmd_cls, data):
        """ Overidded __new__ allowing default values for tuple attributes. """
        return cls.__bases__[0].__new__(cls, inst, cmd_cls, data)
