#############################################################################
# Software Testing Automation Framework (STAF)                              #
# (C) Copyright IBM Corp. 2001                                              #
#                                                                           #
# This software is licensed under the Eclipse Public License (EPL) V1.0.    #
#############################################################################

# STAFMonitorDoLog - This function simply provides a function wrapper around
#                    the LOG request of the Monitor service

def STAFMonitorDoLog(stafHandle, message, system = "local", service = "Monitor"):
    return stafHandle.submit(system, service, "LOG MESSAGE :%d:%s" % \
                             (len(message), message))

# STAFMonitor - This class is a wrapper around the STAF monitor service.
#               It currently only provides a means to monitor locally.

class STAFMonitor:

    def __init__(self, stafHandle, system = "local", service = "Monitor"):
        self.handle  = stafHandle
        self.system  = system
        self.service = service

    def log(self, message):
        return STAFMonitorDoLog(self.handle, message, self.system, self.service)
