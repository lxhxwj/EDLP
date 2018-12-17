#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32gui
import win32api
import os, win32process
import win32con
import winnt
import win32com.client
import time
import shutil
from time import sleep
import os
import os.path
import random
import subprocess
import win32clipboard
import platform
import win32gui_struct
import struct
import array
import sys
sys.path.append("Adaptors-5.0.4\Adaptors\SafeUI")
import autoutil, autoinput, autogui
from ctypes import *

VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'pide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '//':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0}


class POINT(Structure):#鼠标位置二维数组对象
    _fields_ = [("x", c_ulong),("y", c_ulong)]
def get_mouse_point():#获取鼠标位置
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
def mouse_click(x=None,y=None):#单击（左键）
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)#按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)#弹起
def mouse_dclick(x=None,y=None):#双击
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):#移动鼠标
    windll.user32.SetCursorPos(x, y)
def put(str='',flag=0):#flag默认为0，则表示输入的字符串，为1：字符要表示的是快捷组合按键
    if flag==0:
        for c in str:
            if c == ' ':#处理空格
                win32api.keybd_event(VK_CODE['spacebar'],0,0,0)
                win32api.keybd_event(VK_CODE['spacebar'],0,win32con.KEYEVENTF_KEYUP,0)
            else:
                win32api.keybd_event(VK_CODE[c],0,0,0)
                win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
    else:
        cmd = str.split(' ')
        for i in cmd:
            win32api.keybd_event(VK_CODE[i],0,0,0)
        cmd.reverse()
        for i in cmd:#快捷键释放的时候要逆序释放
            win32api.keybd_event(VK_CODE[i],0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)


#函数功能:在x,y(屏幕坐标)处点击鼠标,button控制是左键还是邮件
#参数:x,y--屏幕坐标,button--鼠标的左键或右键
#备注:其中,cx,cy是我的屏幕的长和宽,按(0-65536)的比例在映射一下x,y的虚拟位置

def MouseClick(x, y, button = "LEFT"):
    SCREENRANGE = 65536
    cx = 1366
    cy = 768
    x = x * SCREENRANGE / cx
    y = y * SCREENRANGE / cy

    if "RIGHT" == button:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)


#函数功能:模拟鼠标移动到当前处于焦点的Popup菜单的某一项
#参数:idx--菜单项的序号
#备注:MN_GETHMENU = 0x01E1 这个消息在win32con中没有,自己定义了一下,见msdn
#备注2:菜单中有separator,不要漏数

def MouseHoverMenuItem(idx):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    if idx < 0:
        idx += icount
    rect = win32gui.GetMenuItemRect(hwnd, hmenu, idx)[1]
    x = (rect[2] - rect[0]) / 2 + rect[0]
    y = (rect[3] - rect[1]) / 2 + rect[1]
    DesktopCommon.MouseTo(x, y)


#函数功能:模拟鼠标点击当前处于焦点的Popup菜单的某一项
#参数:idx--菜单项的序号,button -- "LEFT", "RIGHT" 点击鼠标的左键或是右键
#备注:MN_GETHMENU = 0x01E1 这个消息在win32con中没有,自己定义了一下,见msdn

def ClickOnMenuItem(idx, button = "LEFT"):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    if idx < 0:
        idx += icount
    rect = win32gui.GetMenuItemRect(hwnd, hmenu, idx)[1]
    x = (rect[2] - rect[0]) / 2 + rect[0]
    y = (rect[3] - rect[1]) / 2 + rect[1]

    MouseClick(x, y, button)

#函数功能:点击菜单中文字内容为text的菜单项
#参数:text--要点击的菜单的内容, button -- 点击左键还是右键
#返回值:如果成功点击,则返回True,否则False

def ClickOnMenuItemByText(text, button = "LEFT"):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    for i in xrange(icount):
        t = GetMenuItemString(i).decode("gbk").encode("UTF-8")
        #        print text, t
        if text == t:
            rect = win32gui.GetMenuItemRect(hwnd, hmenu, i)[1]
            #print rect
            x = (rect[2] - rect[0]) / 2 + rect[0]
            y = (rect[3] - rect[1]) / 2 + rect[1]

            #print x
            #print y
            sleep(3)
            #MouseClick(x, y, button)
            get_mouse_point()
            sleep(3)
            mouse_move(x,y)
            sleep(3)
            mouse_click(x,y)
            return True

    return False

#函数功能:通过下标获得某个菜单项的内容文本
#参数:idx要操作的菜单项的index
#返回值:获得的菜单项的内容的文本

def GetMenuItemString(idx):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    mii, extra = win32gui_struct.EmptyMENUITEMINFO()
    win32gui.GetMenuItemInfo(hmenu, idx, True, mii)
    fType, fState, wID, hSubMenu, hbmpChecked, hbmpUnchecked,\
    dwItemData, text, hbmpItem = win32gui_struct.UnpackMENUITEMINFO(mii)
    print text
    return text


#函数功能:获得菜单中的菜单项的个数
#函数返回:菜单项的个数

def GetMenuItemCount():
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    return icount
def topWindow(hwnd):
    ret = win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE)
    if ret & win32con.WS_EX_TOPMOST:
        return True
    hwndList = [hwnd]
    while True:
        hwnd = getParentWindow(hwnd)
        if not hwnd:
            break
        hwndList.append(hwnd)
    topHwnd = None
    while len(hwndList) > 0:
        hwnd = hwndList.pop()
        if not isRawWindow(hwnd):
            topHwnd = hwnd
            break
    if not topHwnd:
        return False
    place = autoutil.tryExcept(win32gui.GetWindowPlacement, topHwnd)
    if autoutil.isExcept(place):
        return False
    if place[1] == win32con.SW_SHOWMINIMIZED and not showWindow(topHwnd):
        return False
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == topHwnd:
        return True
    rst = autoutil.tryExcept(win32gui.SetForegroundWindow, topHwnd)
    if not autoutil.isExcept(rst):
        return True
    return getWindowClass(hwnd) == 'Progman' and getWindowText(hwnd) == 'Program Manager'
def getWindowRect(hwnd):
    rect = autoutil.tryExcept(win32gui.GetWindowRect, hwnd)
    if not autoutil.isExcept(rect):
        return rect
def moveWindowByClick(hwnd, x, y):
    topWindow(hwnd)
    a = 10
    while a:
        left, top, right, bottom = getWindowRect(hwnd)
        if left == x and right == y:
            break
        pos = left+(right-left)/2, top+10
        autoinput.moveMouse(pos[0], pos[1])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        autoinput.moveMouse(x+(right-left)/2, y)
        time.sleep(0.1)
        a -= 1
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def MenuControl():
	#sleep几秒,可以有反应时间
    sleep(1)

    hwnds = autogui.findWindows('CabinetWClass')

    subprocess.Popen(r"explorer /select," + r"C:\www.txt")
    time.sleep(5)
    hwnds_2 = autogui.findWindows('CabinetWClass')

    hwnds_find = list(set(hwnds_2).difference(set(hwnds)))
    if len(hwnds_find) == 1:

        print 'right'
        target_wnd = hwnds_find[0]
        print target_wnd

        autogui.topWindow(target_wnd)
        autogui.clickWindow(target_wnd,(40,15))

        win32api.keybd_event(0xA0,0,0,0)
        win32api.keybd_event(0x79,0,0,0)
        time.sleep(0.05)

        win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x79, 0, win32con.KEYEVENTF_KEYUP, 0)
    '''
    hwnd = win32gui.GetDesktopWindow()
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0] + (rect[2] - rect[0]) * 2 / 3
    y = rect[1] + (rect[3] - rect[1]) * 2 / 3
    print x
    print y
    MouseClick(x-500, y-100, "RIGHT")
  	'''
    sleep(0.5)
    #print ClickOnMenuItemByText("新建(&W)",button = "LEFT")
    ClickOnMenuItemByText("数据防泄漏",button = "LEFT")
    sleep(3)

    ClickOnMenuItemByText("加密",button = "LEFT")
    sleep(3)

    hwnd = win32gui.FindWindow('CabinetWClass', None)
    sleep(3)
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    '''
    keymap = {'j': 0x4A, 'a': 0x41, 'c': 0x43, 'k': 0x4B, 'i': 0x49, 'e': 0x45, '\n': win32con.VK_RETURN}
    for key in 'jackie\n':
        win32api.keybd_event(keymap[key], 0, 0, 0)
        win32api.keybd_event(keymap[key], 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(1)
        #end
    '''

if __name__ == '__main__':
	'''
	computer = "10.95.27.118"
	user = "administrator"
	password = "www.360.cn"
	conn = wmi.WMI(computer, user, password)
	for sys in conn.Win32_OperatingSystem():
		print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber #系统信息
		print sys.OSArchitecture.encode("UTF8") # 系统的位数
		print sys.NumberOfProcesses # 系统的进程数
	'''
	MenuControl()