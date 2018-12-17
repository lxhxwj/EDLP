#!/usr/bin/python
#coding=gbk

import time,re,ctypes
import os,sys,subprocess,win32gui,win32con,win32api
import glob,time
import getopt

class BaseWindow:
    @staticmethod
    def parseClickConfig(self,clkCfg):
        if clkCfg == None:
            return None, None, False, 0
        if type(clkCfg) == bool:
            return None, None, clkCfg, 0
        if type(clkCfg) == int:
            return None, None, False, clkCfg
        if len(clkCfg) == 2:
            if type(clkCfg[0]) == int and type(clkCfg[1]) == int:
                return clkCfg[0], clkCfg[1], False, 0
            return None, None, clkCfg[0], clkCfg[1]
        if len(clkCfg) == 3:
            if type(clkCfg[2]) == bool:
                return clkCfg[0], clkCfg[1], clkCfg[2], 0
            return clkCfg[0], clkCfg[1], False, clkCfg[2]
        return clkCfg



def createProcess(cmd, wait = False):
    if wait:
        proc = tryExcept(subprocess.Popen, cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    else:
        proc = tryExcept(subprocess.Popen, cmd)
    if isExcept(proc):
        return
    if not wait:
        return proc.pid
    proc.communicate()


def tryExcept(func, *params, **paramMap):
    try:
        return func(*params, **paramMap)
    except Exception, e:
        return e
def isExcept(e, eType = Exception):
    return isinstance(e, eType)

#µã»÷´°¿Ú
#clkCfg:byDrv|mode|(x,y)|(byDrv,mode)|(x,y,byDrv)|(x,y,mode)|(x,y,byDrv,mode)
def clickWindow(hwnd, clkCfg = None):
    if isRawWindow(hwnd):
        return
    topWindow(hwnd)
    rect = getWindowRect(hwnd)
    if not rect:
        return
    x, y, byDrv, mode = BaseWindow.parseClickConfig(clkCfg)
    if x == None:
        x = (rect[0] + rect[2]) / 2
    elif x < 0:
        x += rect[2]
    else:
        x += rect[0]
    if y == None:
        y = (rect[1] + rect[3]) / 2
    elif y < 0:
        y += rect[3]
    else:
        y += rect[1]
    clickMouse(x, y, byDrv, mode)

#µã»÷Êó±ê
CLICK_MOUSE = 0
CLICK_MOUSE_DOUBLE = 1
CLICK_MOUSE_RIGHT = 2

def clickMouse(x, y, byDrv = False, mode = CLICK_MOUSE):
    moveMouse(x, y, byDrv)
    downMsg, upMsg = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    if mode == CLICK_MOUSE_RIGHT:
        downMsg, upMsg = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
    win32api.mouse_event(downMsg, 0, 0, 0, 0)
    win32api.mouse_event(upMsg, 0, 0, 0, 0)
    if mode == CLICK_MOUSE_DOUBLE:
        win32api.mouse_event(downMsg, 0, 0, 0, 0)
        win32api.mouse_event(upMsg, 0, 0, 0, 0)

#ÒÆ¶¯Êó±ê
def moveMouse(x, y, byDrv = False):
    w, h = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    x, y = int(float(x) / w * 65535), int(float(y) / h * 65535)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

def getWindowRect(hwnd):
    rect = tryExcept(win32gui.GetWindowRect, hwnd)
    if not isExcept(rect):
        return rect


def topWindow(hwnd):
    fgHwnd = win32gui.GetForegroundWindow()
    if fgHwnd == hwnd:
        return True
    rst = tryExcept(win32gui.SetForegroundWindow, hwnd)
    if not isExcept(rst):
        return True
    return getWindowClass(fgHwnd) == 'Progman' and getWindowText(fgHwnd) == 'Program Manager'


##»ñÈ¡´°¿ÚÎÄ×Ö
def getWindowText(hwnd, buf = ctypes.c_buffer(1024)):
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)
    tryExcept(win32gui.SendMessageTimeout, hwnd, win32con.WM_GETTEXT, size, buf, win32con.SMTO_ABORTIFHUNG, 10)
    return buf.value.strip()

#»ñÈ¡´°¿ÚÀàÃû
def getWindowClass(hwnd, buf = ctypes.c_buffer(1024)):
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)
    ctypes.windll.user32.GetClassNameA(hwnd, ctypes.addressof(buf), size)
    return buf.value.strip()


#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findWindow(title, parentTitle = None, isRaw = False):
    hwndList =findWindows(title, parentTitle, isRaw)
    if hwndList:
    	return hwndList[0]
def findRawWindows(title, parentTitle = None):
    return findWindows(title, parentTitle, True)


def isRawWindow(hwnd):
    return not win32gui.IsWindowVisible(hwnd) or not win32gui.IsWindowEnabled(hwnd) or ctypes.windll.user32.IsHungAppWindow(hwnd)

#²éÕÒ´°¿Ú
#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findWindows(title, parentTitle = None, isRaw = False):
    def __enumWindowHandler__(hwnd, wndList):
        text = re.split('[\r|\n]+', getWindowText(hwnd))[0].strip()
        clazz = getWindowClass(hwnd).strip()
        ctrlId = win32gui.GetDlgCtrlID(hwnd)
        wndList.append((hwnd, text, clazz, ctrlId))
    if not parentTitle:
        parentHwndList = [None]
    elif type(parentTitle) == int:
        parentHwndList = [parentTitle]
    else:
        parentHwndList = findRawWindows(parentTitle)
    hwndSet = set()
    for parentHwnd in parentHwndList:
        wndList = []
        #EnumWindows
        if parentHwnd:
            tryExcept(win32gui.EnumChildWindows, parentHwnd, __enumWindowHandler__, wndList)
        else:
            win32gui.EnumWindows(__enumWindowHandler__, wndList)
        #FindWindowEx
        hwnd, foundHwndList = None, []
        while True:
            hwnd = tryExcept(win32gui.FindWindowEx, parentHwnd, hwnd, None, None)
            if not hwnd or isExcept(hwnd) or hwnd in foundHwndList:
                break
            __enumWindowHandler__(hwnd, wndList)
            foundHwndList.append(hwnd)
        #GetWindow
        if parentHwnd:
            hwnd = tryExcept(win32gui.GetWindow, parentHwnd, win32con.GW_CHILD)
        else:
            hwnd = tryExcept(win32gui.GetWindow, win32gui.GetDesktopWindow(), win32con.GW_CHILD)
        while hwnd and not isExcept(hwnd):
            __enumWindowHandler__(hwnd, wndList)
            hwnd = tryExcept(win32gui.GetWindow, hwnd, win32con.GW_HWNDNEXT)
        #Combine
        for hwnd, text, clazz, ctrlId in set(wndList):
            if type(title) == int:
                if ctrlId == title:
                    hwndSet.add(hwnd)
            elif text == title or re.match('^' + title + '$', text, re.S) or clazz == title or re.match('^' + title + '$', clazz, re.S):
                hwndSet.add(hwnd)
            if parentHwnd:
                hwndSet.update(findRawWindows(title, hwnd))
    if isRaw:
        return list(hwndSet)
    hwndList = []
    for hwnd in hwndSet:
        if not isRawWindow(hwnd):
            hwndList.append(hwnd)
    return hwndList

#ÉèÖÃ´°¿ÚÎÄ×Ö
def setWindowText(hwnd, text):
    rst = tryExcept(win32gui.SendMessageTimeout, hwnd, win32con.WM_SETTEXT, 0, text, win32con.SMTO_ABORTIFHUNG, 10)
    return not isExcept(rst)

def killProcessByName(pname, user = None):
    killProcessByNames([pname], user)

def listFile(path, isDeep=True):
    _list = []
    if isDeep:
        try:
            for root, dirs, files in os.walk(path):
                for fl in files:
                    _list.append('%s\%s' % (root, fl))
        except:
            pass
    else:
        for fn in glob.glob( path + os.sep + '*' ):
            if not os.path.isdir(fn):
                _list.append('%s' % path + os.sep + fn[fn.rfind('\\')+1:])
    return _list


def killProcessByNames(pnameList, user = None):
    cmd = 'taskkill /F /T'
    if user:
        cmd += ' /FI "USERNAME eq %s"' % user
    for pname in pnameList:
        cmd += ' /IM %s' % pname
    createProcess(cmd, True)

#³¬Ê±ÉèÖÃ
def handleTimeout(func, timeout, *params, **paramMap):
    interval = 0.8
    if type(timeout) == tuple:
        timeout, interval = timeout
    while timeout > 0:
        t = time.time()
        rst = func(*params, **paramMap)
        if rst and not isExcept(rst):
            break
        time.sleep(interval)
        timeout -= time.time() - t
    return rst

def setFileData(filename, data, mode):
    f = open(filename, mode)
    f.write(data)
    f.close()

def Pass():
    hwnd = win32gui.FindWindow('#32770',r'���ݰ�ȫ')
    print hwnd
    title = win32gui.GetWindowText(hwnd)
    print title
    classname = win32gui.GetClassName(hwnd)
    print classname
    hwnd1 = win32gui.FindWindowEx(hwnd,None,classname,None)
    print hwnd1
    topWindow(hwnd)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print left
    print top
    print right
    print bottom

    #win32api.SetCursorPos([1300,700])
    win32api.SetCursorPos([right - 150,bottom - 23])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    #win32api.SetCursorPos([right - 61,bottom - 23])
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
def Refuse():
    hwnd = win32gui.FindWindow('#32770',r'���ݰ�ȫ')
    print hwnd
    title = win32gui.GetWindowText(hwnd)
    print title
    classname = win32gui.GetClassName(hwnd)
    print classname
    hwnd1 = win32gui.FindWindowEx(hwnd,None,classname,None)
    print hwnd1
    topWindow(hwnd)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print left
    print top
    print right
    print bottom

    #win32api.SetCursorPos([1300,700])
    #win32api.SetCursorPos([right - 150,bottom - 23])
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.SetCursorPos([right - 61,bottom - 23])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)


if __name__ == '__main__':
    def usage():
        print(u'\
            -h or --help\n\
            -p Pass\n\
            -r Refuse\n\
            -v or --version\
            ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hprv", ["help", "version"])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        elif cmd in ("-p", "1"):
            Pass()
        elif cmd in ("-r", "1"):
            Refuse()
        elif cmd in ("-v", "--version"):
            print("version 1.0")