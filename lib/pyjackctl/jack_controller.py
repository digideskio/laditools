# pyjackctl - The python jackdbus controller suite
# Copyright (C) 2007, Marc-Olivier Barre and Nedko Arnaudov.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import dbus

name_base = 'org.jackaudio'
controller_interface_name = name_base + '.JackController'
service_name = name_base + '.service'

class jack_controller:
        def __init__(self):
                 self.bus = dbus.SessionBus()
                 self.controller = self.bus.get_object(service_name, "/DefaultController")
                 self.iface = dbus.Interface(self.controller, controller_interface_name)

        def is_started(self):
                return self.iface.IsStarted()

        def is_realtime(self):
                return self.iface.IsRealtime()

        def get_load(self):
                return self.iface.GetLoad()

        def get_xruns(self):
                return self.iface.GetXruns()

        def get_sample_rate(self):
                return self.iface.GetSampleRate()

        def get_latency(self):
                return self.iface.GetLatency()

        def reset_xruns(self):
                return self.iface.ResetXruns()

        def start(self):
                self.iface.StartServer()

        def stop(self):
                self.iface.StopServer()

        def kill(self):
                self.iface.Exit()