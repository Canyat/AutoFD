import os
from sys import platform as PLF
from time import sleep

import cv2
import numpy
import pyautogui


def get_screen_size() -> tuple[int, int]:
    '''
    注意：由于Windows系统缩放功能的存在，实际分辨率 = 显示器分辨率 / 缩放倍数
    '''
    import ctypes
    return ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)


def get_sqrd_diff() -> float:
    DEFAULT_CRITICAL_SQRD_DIFF: float = 0.5

    # 获取用于判断是否匹配的平方差临界值
    while True:
        os.system('cls' if PLF.startswith('win') else 'clear')  # 清屏

        print('[归一化平方差匹配]')
        print('请输入判断图像匹配是否匹配的平方差临界值（0~1），完全匹配为0，')
        content: str = input(f'不输入则使用默认值（{DEFAULT_CRITICAL_SQRD_DIFF}）：')

        if content == '':  # 输入为空
            return DEFAULT_CRITICAL_SQRD_DIFF
        else:
            try:
                sqrd_diff: float = float(content)
                if not (0 < sqrd_diff <= 1):
                    raise ValueError
            except ValueError:
                print('请输入正确的数字！')
                os.system('pause' if PLF.startswith('win') else 'echo "Press any key to continue...";read -n 1')
            else:
                return sqrd_diff


if __name__ == '__main__':
    # 获取屏幕分辨率
    scr_size = get_screen_size()
    # 获取平方差临界值
    critical_sqrd_diff: float = get_sqrd_diff()

    # 清屏
    os.system('cls' if PLF.startswith('win') else 'clear')

    # 获取图片文件夹路径
    img_dir_path: str = os.path.join(os.getcwd(), 'img')

    # 显示参数信息
    print(f'屏幕分辨率：{scr_size[0]} x {scr_size[1]}')
    print(f'图像匹配程度临界值（标准平方差匹配）：{critical_sqrd_diff}')
    print('')

    # 程序主循环
    while True:
        # 为避免名称混淆：模板文件使用template，暂存文件使用tmp(temporary)。
        template_img = cv2.imread(os.path.join(img_dir_path, 'AutoDefending_template.png'))
        tmp_img = cv2.cvtColor(numpy.asarray(pyautogui.screenshot(region=(0, 0, *scr_size))), cv2.COLOR_RGB2BGR)

        # 进行匹配
        result = cv2.matchTemplate(tmp_img, template_img, cv2.TM_SQDIFF_NORMED)
        # 完全匹配 ---> 0
        # 完全不匹配 ---> 1
        best_sqrd_diff: float = cv2.minMaxLoc(result)[0]

        # 处理匹配结果
        print('\r当前最佳匹配程度：%.2f，' % best_sqrd_diff, end='')
        if best_sqrd_diff <= critical_sqrd_diff:
            print('检测到威胁！', end='')

            pyautogui.keyDown('F3')
            pyautogui.press('C')
            pyautogui.keyUp('F3')

            print()
            print('程序已结束。')
            # 按任意键退出
            os.system('pause' if PLF.startswith('win') else 'echo "Press any key to continue...";read -n 1')
            break  # 此处换成 exit() / quit() 效果相同
        else:
            print('搜寻中...', end='')

        # 短暂停顿，便于查看匹配数据
        sleep(0.1)
