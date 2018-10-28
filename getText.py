import win32con
import win32clipboard as w


class GetText:
    #把识别内容贴到剪贴板
    @staticmethod
    def getText():
        #获取剪贴板内容
        try:
            w.OpenClipboard()
            d = w.GetClipboardData(win32con.CF_UNICODETEXT)
            w.CloseClipboard()
            return d
        except:
            pass



    @staticmethod
    def setText(String):
        #传递一个参数用于赋值到剪贴板

        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, String)
        w.CloseClipboard()


if __name__ == '__main__':
    GetText.setText('666667788887')
    GetText.getText()

