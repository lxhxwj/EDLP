#############################################################################
# Software Testing Automation Framework (STAF)                              #
# (C) Copyright IBM Corp. 2001                                              #
#                                                                           #
# This software is licensed under the Eclipse Public License (EPL) V1.0.    #
#############################################################################

import PySTAFMon

# STAFLogDoLog - This function logs a message to a log file

def STAFLogDoLog(handle, logType, name, level, msg, mask = [ "Fatal", "Error",
                 "Warning", "Start", "Stop", "Pass", "Fail" ], system = "local",
                 service = "Log"):

    logRequest = "LOG %s LOGNAME :%d:%s LEVEL %s MESSAGE :%d:%s" % \
                 (logType, len(name), name, level, len(msg), msg)

    result = handle.submit(system, service, logRequest)

    if (result.rc != 0):
        PySTAFMon.STAFMonitorDoLog(handle, "Logging failed, RC: %s, on message: %s" % \
                                   (result.rc, msg))
    elif (level in mask):
        result = PySTAFMon.STAFMonitorDoLog(handle, "%s:%s" % (level, msg))

    return result


# STAFLog - This class is a wrapper around the STAF logging service.
#           It provides a set of constants for log types and levels.
#           It provides a log() method to log a message.  It also interfaces
#           with the MONITOR service for a user defined set of levels.  For
#           these level STAFLog will also send the given message to the
#           monitor service.  If there is an error logging, STAFLog will
#           also try to send an error to the MONITOR service.

class STAFLog:

    # Log type constants

    Global  = "GLOBAL"
    Machine = "MACHINE"
    Handle  = "HANDLE"

    # Log level constants

    Fatal     = "Fatal"
    Error     = "Error"
    Warning   = "Warning"
    Info      = "Info"
    Trace     = "Trace"
    Trace2    = "Trace2"
    Trace3    = "Trace3"
    Debug     = "Debug"
    Debug2    = "Debug2"
    Debug3    = "Debug3"
    Start     = "Start"
    Stop      = "Stop"
    Pass      = "Pass"
    Fail      = "Fail"
    Status    = "Status"
    User1     = "User1"
    User2     = "User2"
    User3     = "User3"
    User4     = "User4"
    User5     = "User5"
    User6     = "User6"
    User7     = "User7"
    User8     = "User8"

    # Log service return codes

    InvalidLevel                = 4004
    InvalidLogFileFormat        = 4007
    PurgeFailure                = 4008

    # This mask enables Fatal, Error, Warning, Start, Stop, Pass, Fail,
    # and Status

    def __init__(self, handle, logType, name, monitorMask = [ "Fatal", "Error",
                 "Warning", "Start", "Stop", "Pass", "Fail" ], system = "local",
                 service = "Log"):
        self.name        = name
        self.handle      = handle
        self.logType     = logType
        self.monitorMask = monitorMask
        self.system      = system
        self.service     = service


    # Method to actually log a message with a given level

    def log(self, level, msg):
        return STAFLogDoLog(self.handle, self.logType, self.name, level, msg,
                            self.monitorMask, self.system, self.service)

