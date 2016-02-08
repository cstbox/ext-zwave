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

""" aeotec dsb28 low-level interface.


"""

import urllib2
import base64
import struct
import math
from collections import namedtuple

from pycstbox.zwave import ZWaveRegister
from pycstbox.log import Loggable

__author__ = 'Patrick Pollet - CSTB (patrick.pollet@cstb.fr)'
__copyright__ = 'Copyright (c) 2016 CSTB'
__vcs_id__ = '$Id$'
__version__ = '1.0.0'


# registers

REG_ENERGY1 = ZWaveRegister(1,50,0)
REG_POWER1 = ZWaveRegister(1,50,2)
REG_VOLTAGE1 = ZWaveRegister(1,50,4)
REG_CURRENT1 = ZWaveRegister(1,50,5)
REG_ENERGY2 = ZWaveRegister(2,50,0)
REG_POWER2 = ZWaveRegister(2,50,2)
REG_VOLTAGE2 = ZWaveRegister(2,50,4)
REG_CURRENT2 = ZWaveRegister(2,50,5)
REG_ENERGY3 = ZWaveRegister(3,50,0)
REG_POWER3 = ZWaveRegister(3,50,2)
REG_VOLTAGE3 = ZWaveRegister(3,50,4)
REG_CURRENT3 = ZWaveRegister(3,50,5)


class DSB28Instrument(Loggable):


    # Definition of the type of the poll() method result

    # VERY IMPORTANT :
    # The name of its items MUST match the name of the outputs described
    # in the metadata stored in devcfg.d directory, since the notification
    # events generation process is based on this.
    # (see pycstbox.hyal.device.PolledDevice.poll() method for details)
    OutputValues = namedtuple('OutputValues', [
                        'energy1',
                        'power1',
                        'voltage1',
                        'current1',
                        'energy2',
                        'power2',
                        'voltage2',
                        'current2',
                        'energy3',
                        'power3',
                        'voltage3',
                        'current3'
    ])

    def __init__(self, port, unit_id):
        self._first_poll = True
        self.url = port
        self.address = int(unit_id)
        Loggable.__init__(self, logname='zwave%03d' % self.address)

    @property
    def unit_id(self):
        """ The id of the device """
        return self.address

    def reset(self):
        """ Resets operational mode """
        pass
        
    def read_reg(self, reg):
       url =  'http://'+self.url+'/ZWaveAPI/Run/devices['+str(self.address)+'].instances['+str(reg.inst)+'].commandClasses['+str(reg.cmd_cls)+'].data['+str(reg.data)+'].val.value'
       req = urllib2.Request(url)
       b64string = base64.b64encode('%s:%s' % ('admin','admin'))
       authheader = "Basic %s" % b64string
       req.add_header("Authorization", authheader)
       c = urllib2.urlopen(req).read()
       return float(c)

    def poll(self):
        """ Reads the registers operational mode and returns the
        values as a named tuple.  """
        
        raw_energy1 = self.read_reg(REG_ENERGY1)
        raw_power1 = self.read_reg(REG_POWER1)
        raw_voltage1 = self.read_reg(REG_VOLTAGE1)
        raw_current1 = self.read_reg(REG_CURRENT1)
        raw_energy2 = self.read_reg(REG_ENERGY2)
        raw_power2 = self.read_reg(REG_POWER2)
        raw_voltage2 = self.read_reg(REG_VOLTAGE2)
        raw_current2 = self.read_reg(REG_CURRENT2)
        raw_energy3 = self.read_reg(REG_ENERGY3)
        raw_power3 = self.read_reg(REG_POWER3)
        raw_voltage3 = self.read_reg(REG_VOLTAGE3)
        raw_current3 = self.read_reg(REG_CURRENT3)

        return self.OutputValues(
                energy1 = raw_energy1,
                power1 = raw_power1,
                voltage1 = raw_voltage1,
                current1 = raw_current1,
                energy2 = raw_energy2,
                power2 = raw_power2,
                voltage2 = raw_voltage2,
                current2 = raw_current2,
                energy3 = raw_energy3,
                power3 = raw_power3,
                voltage3 = raw_voltage3,
                current3 = raw_current3
        )
