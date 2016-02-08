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

""" fortrezz mimolite low-level interface.


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

REG_BINARY = ZWaveRegister(0,48,1)
REG_ANALOG = ZWaveRegister(0,49,2)
REG_COUNTER = ZWaveRegister(0,53,0)



class MIMOLITEInstrument(Loggable):


    # Definition of the type of the poll() method result

    # VERY IMPORTANT :
    # The name of its items MUST match the name of the outputs described
    # in the metadata stored in devcfg.d directory, since the notification
    # events generation process is based on this.
    # (see pycstbox.hyal.device.PolledDevice.poll() method for details)
    OutputValues = namedtuple('OutputValues', [
                        'binary',
                        'analog',
                        'counter'

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
        
    def read_freg(self, reg):
        url = 'http://'+self.url+'/ZWaveAPI/Run/devices['+str(self.address)+'].instances['+str(reg.inst)+'].commandClasses['+str(reg.cmd_cls)+'].data['+str(reg.data)+'].val.value'
        req = urllib2.Request(url)
        b64string = base64.b64encode('%s:%s' % ('admin','admin'))
        authheader = "Basic %s" % b64string
        req.add_header("Authorization", authheader)
        c = urllib2.urlopen(req).read()
        return float(c)

    def read_counter_reg (self, reg):
        url = 'http://'+self.url+'/ZWaveAPI/Run/devices['+str(self.address)+'].instances['+str(reg.inst)+'].commandClasses['+str(reg.cmd_cls)+'].data.val.value'
        req = urllib2.Request(url)
        b64string = base64.b64encode('%s:%s' % ('admin','admin'))
        authheader = "Basic %s" % b64string
        req.add_header("Authorization", authheader)
        c = urllib2.urlopen(req).read()
        return float(c)
            
    def read_binary_reg (self, reg):
        url = 'http://'+self.url+'/ZWaveAPI/Run/devices['+str(self.address)+'].instances['+str(reg.inst)+'].commandClasses['+str(reg.cmd_cls)+'].data['+str(reg.data)+'].level.value'
        req = urllib2.Request(url)
        b64string = base64.b64encode('%s:%s' % ('admin','admin'))
        authheader = "Basic %s" % b64string
        req.add_header("Authorization", authheader)
        c = urllib2.urlopen(req).read()
        if c == 'true':
            return True
        else:
            return False       

    def poll(self):
        """ Reads the registers operational mode and returns the
        values as a named tuple.  """
        
        raw_analog = self.read_freg(REG_ANALOG)
        raw_binary = self.read_binary_reg(REG_BINARY)
        raw_counter = self.read_counter_reg(REG_COUNTER)
       

        return self.OutputValues(
                analog = raw_analog,
                binary = raw_binary,
                counter = raw_counter
        )
