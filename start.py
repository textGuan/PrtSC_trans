import wx
import demo

class CalcFrame(demo.MyFrame1): 
   def __init__(self,parent): 
      demo.MyFrame1.__init__(self,parent)  
	#按键事件触发函数
 
def main():        
    app = wx.App(False) 
    frame = CalcFrame(None) 
    frame.Show(True) 
    #start the applications 
    app.MainLoop() 
 
if __name__ == '__main__':
    main()

# import cv2
# import os
# import numpy as np
# file_path = 'image/'
# filename = os.listdir(file_path)
# for i in filename:
#     path = file_path+i
#     img1 = cv2.imread(path,3)
#     img1 = cv2.resize(img1,(60,60))
#     cv2.imwrite(path,img1)
