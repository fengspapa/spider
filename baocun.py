import keyboard
import time
from  PIL import ImageGrab,Image
import sys
from baidu import BaiDuapi
from getText import GetText
def screenShot():
    #监听按压事件
    if keyboard.wait(hotkey='shift+a') == None:
        time.sleep(0.01)
        if keyboard.wait(hotkey='esc') == None:
            im = ImageGrab.grabclipboard()
            if isinstance(im,Image.Image):
                im.save('图片.jpg')
                #print('图片保存完成')
            else:
                print('请重新截图')
if __name__ == "__main__":
    a = BaiDuapi('api.ini')
    for i in range(sys.maxsize):

        screenShot()

        cc = a.pictureText('图片.jpg')
        print(cc)
        GetText.setText(cc)
        GetText.getText()
