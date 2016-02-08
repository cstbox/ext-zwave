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

""" ZWAve devices sub-network management service.
"""

from pycstbox.hal.network import DeviceNetworkSvc

SERVICE_NAME = "ZWaveDriver"


class ZWaveSvc(DeviceNetworkSvc):
    """ This class implements the model of the service managing the sub-network
    built with ZWave products.
    """
    def __init__(self, conn):
        """ :param Connection conn: D-Bus connection (see service.ServiceObject.__init__())
        """
        super(ZWaveSvc, self).__init__(conn, SERVICE_NAME, coord_types=['zwave'])
