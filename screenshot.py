import pyautogui
import numpy as np
import cv2
import pyHook
import win32api
import win32gui
import win32con
import tkinter as tk
import time

hwnd_title = []
hwnd_list = []
ix,iy = -1,-1
bx,by = -1,-1
i=1
win_name = 'screenshot'
img1 = np.zeros([10,10,1],np.uint8)


def init():
    ix,iy = -1,-1
    bx,by = -1,-1
    i=1

    # img = pyautogui.screenshot(region=[0,0,width,height])

def draw(event,x,y,flags,param):
    global ix,iy,bx,by,i
    if event == cv2.EVENT_LBUTTONDOWN:
        # print('按下鼠标')
        ix, iy = x,y
        # print('坐标1：',str(ix),str(iy))
    elif event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if i ==1:
            # print('鼠标滑动')
            i = i+1
        if i >1:
            pass
        img = img1.copy()#实时更新这一步很重要，如果没有这一步画出来会是一个方块
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        root = tk.Tk()
        cv2.imshow(win_name, img)
    elif event == cv2.EVENT_LBUTTONUP:
        # print('鼠标抬起')
        bx, by = x, y
        # print('坐标2：',str(bx),str(by))

def take_screenshot():
    global img1
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    img = pyautogui.screenshot(region=[0,0,width,height])
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    img1 = img.copy()#为了上面的实时更新方框，如果不更新，最后是一个实心方块
    hide()
    cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(win_name,img1)#第一次显示
    cv2.setMouseCallback(win_name,draw)#回调鼠标
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img2 = img[iy:by,ix:bx]
    # img2 = pyautogui.screenshot(region=[ix,iy,bx-ix,by-iy])
    # img2 = cv2.cvtColor(np.asarray(img2),cv2.COLOR_RGB2BGR)
    cv2.imwrite('workspace/1.png',img2)
    show()
    # cv2.waitKey()

def hide():
    win32api.keybd_event(win32con.VK_LWIN,0,0,0)
    win32api.keybd_event(77,0,0,0)
    win32api.keybd_event(win32con.VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(77,0,win32con.KEYEVENTF_KEYUP,0)

def show():
    win32api.keybd_event(win32con.VK_LWIN,0,0,0)
    win32api.keybd_event(win32con.VK_SHIFT,0,0,0)
    win32api.keybd_event(77,0,0,0)
    win32api.keybd_event(win32con.VK_LWIN,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(win32con.VK_SHIFT,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(77,0,win32con.KEYEVENTF_KEYUP,0)