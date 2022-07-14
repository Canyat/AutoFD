import cv2
import pyautogui
import time as t
import pickle
import os
# 判断是否存在匹配数据
if os.path.exists('variance.canyat') is not True:
    Vari_list = [0.35,1920,1080]
    pickle_vari_List = open('variance.canyat','wb')
    pickle.dump(Vari_list,pickle_vari_List)
    pickle_vari_List.close()
    print('当前的标准平方差值为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])
else:
    # 读取
    pickle_vari_List = open('variance.canyat','rb')
    Vari_list = pickle.load(pickle_vari_List)
    pickle_vari_List.close()
    print('当前的标准平方差值为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])
# 让用户输入自己选择
a = input('1.执行脚本 2.修改标准平方差值及分辨率：')
if a == '2':
    v1_r = float(input('想要修改的标准平方差值：'))
    v2_r = int(input('想要修改的分辨率宽：'))
    v3_r = int(input('想要修改的分辨率高：'))
    Vari_list_revise = [v1_r,v2_r,v3_r]
    pickle_vari_List = open('variance.canyat','wb')
    pickle.dump(Vari_list_revise,pickle_vari_List)
    pickle_vari_List.close()
    print('当前的标准平方差值为：',Vari_list[0],'分辨率为：',Vari_list[1],' x ',Vari_list[2])
    quit()
elif a == '1':
    # 自动钓鱼钓鱼本体循环
    while 1:
        pyautogui.screenshot(region=(Vari_list[1]/2,Vari_list[2]/2,Vari_list[1]/2,Vari_list[2]/2)).save('./buffer/shot_2.png')
        mu_ban = cv2.imread('2.png')
        shot_ = cv2.imread('./buffer/shot_2.png')
        res = cv2.matchTemplate(shot_,mu_ban,cv2.TM_SQDIFF_NORMED)
        upper_ = cv2.minMaxLoc(res)[0]
        print(upper_)
        if upper_ < Vari_list[0]:
            pyautogui.click(button='right')
            t.sleep(3)
            pyautogui.click(button='right')
            t.sleep(2)
        else:
            print('no')
