import cv2
import pyautogui
import time as t
import pickle
import os, sys

# 判断缓存文件夹是否存在
buffer_dir_path = os.path.join(os.getcwd(),"buffer")
if not os.path.exists(buffer_dir_path):
    os.makedirs(buffer_dir_path)

print_info = lambda l: print('当前的标准平方差值为：',l[0],'分辨率为：',l[1],' x ',l[2])
    
# 判断是否存在匹配数据
if not os.path.exists('variance.canyat'):
    Vari_list = [0.35,1920,1080]
    with open('variance.canyat','wb') as pickle_vari_List:
        pickle.dump(Vari_list,pickle_vari_List)
    print_info(Vari_list)
else:
    with open('variance.canyat','rb') as pickle_vari_List:
        Vari_list = pickle.load(pickle_vari_List)  # 读取
    print_info(Vari_list)

# 输入选择
while True:
    choose: str = str(input('输入对应数字执行操作:\n  1 -> 执行脚本\n  2 -> 修改标准平方差值及分辨率\n  3 -> 退出程序'))

    if choose == '2':
        Vari_list_revise = [float(input('想要修改的标准平方差值：')),int(input('想要修改的分辨率宽：')),int(input('想要修改的分辨率高：'))]
        with open('variance.canyat','wb') as pickle_vari_List:
            pickle.dump(Vari_list_revise,pickle_vari_List)
        print_info(Vari_list)
    elif choose == '1':
        # 自动钓鱼钓鱼本体循环
        print("进入循环, 如要关闭程序，请直接关闭窗口")
        while True:
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
    elif choose =="3":
        sys.exit()
    else:
        pass
