from aip import AipOcr
import configparser
class BaiDuapi():
    '''调用百度API'''
    def __init__(self,filePath = None):
        target = configparser.ConfigParser()
        target.read(filePath,encoding='utf-8')
        app_id = target.get('工单信息','APP_ID')
        app_key = target.get('工单信息','APP_KEY')
        app_passwd = target.get('工单信息','Secret Key')
        self.client = AipOcr(app_id, app_key, app_passwd)

    def pictureText(self,filePath):
        #图像转文字
        image = self.getPicture(filePath)
        text = self.client.basicGeneral(image)
        w = text['words_result']
        w = str(w)
        w = w.replace("[{'words': ",'').replace("'}, ",'\n').replace("'",'').replace('{words: ','').replace('}]','')
        return w

    def getPicture(self,filePath):
        with open(filePath,'rb')as f:
            return f.read()

if __name__ == "__main__":


    a = BaiDuapi('api.ini')
    print(a.pictureText('图片.jpg'))