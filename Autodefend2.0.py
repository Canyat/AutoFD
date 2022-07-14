import cv2
import pyautogui
import time as t
import pickle
import os
if os.path.exists('Dvariance.canyat') is not True:
    command_input = 'This is a test'
    Vari_list = [command_input,1920,1080]
    pickle_vari_List = open('Dvariance.canyat','wb')
    pickle.dump(Vari_list,pickle_vari_List)
    pickle_vari_List.close()
    print('当前输入的命令为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])
else:
    # 读取
    pickle_vari_List = open('Dvariance.canyat','rb')
    Vari_list = pickle.load(pickle_vari_List)
    pickle_vari_List.close()
    print('当前输入命令为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])

a = input('1.执行脚本 2.修改输入命令及分辨率：')
if a == '2':
    v1_r = input('想要修改的命令：')
    v2_r = int(input('想要修改的分辨率宽：'))
    v3_r = int(input('想要修改的分辨率高：'))
    Vari_list_revise = [v1_r,v2_r,v3_r]
    pickle_vari_List = open('Dvariance.canyat','wb')
    pickle.dump(Vari_list_revise,pickle_vari_List)
    pickle_vari_List.close()
    print('当前输入命令为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])
    quit()

elif a == '1':
    while 1:
        pyautogui.screenshot(region=(Vari_list[1]/2,Vari_list[2]/2,Vari_list[1]/2,Vari_list[2]/2)).save('./buffer/shot_.png')
        mu_ban = cv2.imread('1.png')
        shot_ = cv2.imread('./buffer/shot_.png')
        # height,width,mode = qwq.shape
        res = cv2.matchTemplate(shot_,mu_ban,cv2.TM_SQDIFF_NORMED)
        upper_ = cv2.minMaxLoc(res)[0]
        # print(upper_)
        if upper_ < 0.5:
            pyautogui.keyDown('f3')
            pyautogui.press('c')
            pyautogui.keyUp('f3')
            pyautogui.press('t')
            pyautogui.typewrite(Vari_list[0])
            pyautogui.press('enter')
            t.sleep(3)
        else:
            print('搜寻中')
