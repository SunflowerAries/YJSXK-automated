from time import sleep, time
from requests import session
import shutil, os, json, traceback, sys
from des import o as des_encrypt
from config import *
from bs4 import BeautifulSoup
from filelock import FileLock
from crnn import ocr

def get_timestamp():
    return str(int(time()*1000))

class Fudan:
    """
    建立与复旦服务器的会话，执行登录/登出操作
    """

    UA = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"

    # 初始化会话
    def __init__(self, uid, psw, url_vcode_get, url_vcode_post, url_image_get):
        """
        初始化一个session，及登录信息
        :param uid: 学号
        :param psw: 密码
        :param url_vcode: 登录页，默认服务为空
        """
        self.session = session()
        self.session.headers['User-Agent'] = self.UA
        self.url_vcode_get = url_vcode_get
        self.url_vcode_post = url_vcode_post
        self.url_image_get = url_image_get

        self.uid = uid
        self.psw = des_encrypt(psw)
        self.timestamp = get_timestamp()
        self.headers_login = {
            "Host"      : "yjsxk.fudan.edu.cn",
            "Origin"    : "https://yjsxk.fudan.edu.cn",
            "Referer"   : "http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/*default/index.do",
            "User-Agent": self.UA
        }
        self.headers_get_cls = {
            "Host"      : "yjsxk.fudan.edu.cn",
            "Origin"    : "https://yjsxk.fudan.edu.cn",
            "Referer"   : "http://yjsxk.fudan.edu.cn/yjsxkapp/sys/xsxkappfudan/xsxkHome/gotoChooseCourse.do",
            "User-Agent": self.UA
        }

    def login(self):
        if not os.path.exists('./dataset'):
            os.makedirs('./dataset')
        os.chdir('./dataset')
        while True:
            timestamp = get_timestamp()
            vcode_get = self.session.get(self.url_vcode_get + timestamp)
            self.vtoken = vcode_get.json()["data"]["token"]

            r = self.session.get(self.url_image_get + self.vtoken, stream=True)
            if r.status_code == 200:
                with FileLock(timestamp + '.jpg.lock'):
                    with open(timestamp + '.jpg', 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                code = ocr(os.path.join(os.getcwd(), timestamp + '.jpg'))
                if sys.platform == 'linux':
                    os.remove(timestamp + '.jpg.lock')
                if code != None and len(code) == 4:
                    data = {
                        "loginName": self.uid,
                        "loginPwd": self.psw,
                        "verifyCode" : code,
                        "vtoken": self.vtoken
                    }
                    post = self.session.post(
                        self.url_vcode_post + timestamp,
                        data=data,
                        headers=self.headers_login,
                        allow_redirects=False
                    )
                    resp = json.loads(post.text)
                    # print(post.text)
                    if resp["code"] != "3":
                        if resp["code"] != "1":
                            print(resp)
                        os.chdir('../')
                        return

class Yjsxk(Fudan):
    def __init__(self, uid, psw, url_vcode_get, url_vcode_post, url_image_get, 
                url_class_get, yjsxk_wanted_class, url_class_validate, url_class_chs, url_class_res, url_csrf):
        super().__init__(uid, psw, url_vcode_get, url_vcode_post, url_image_get)
        self.url_class_get = url_class_get
        self.yjsxk_wanted_class = yjsxk_wanted_class
        self.url_class_validate = url_class_validate
        self.url_class_chs = url_class_chs
        self.url_class_res = url_class_res
        self.url_csrf = url_csrf
    
    def work(self):
        print("已进入选课模式")
        while True:
            wanted = []
            for key in self.yjsxk_wanted_class:
                if len(self.yjsxk_wanted_class[key]) == 0:
                    continue
                payload = yjsxk_map[key]
                url_class_post = self.url_class_get.replace("DTHBF", payload[0])
                self.session.post(
                    self.url_class_validate,
                    data={ 'bqdm': payload[1] },
                    headers=self.headers_get_cls,
                    allow_redirects=False
                )
                post = self.session.post(
                    url_class_post + get_timestamp(),
                    data=payload[3],
                    headers=self.headers_get_cls,
                    allow_redirects=False
                )
                clss = json.loads(post.text)
                
                for cls in self.yjsxk_wanted_class[key]:
                    wanted = wanted + list(filter(lambda get_cls: get_cls['KCMC'] == cls and get_cls["DQRS"] < get_cls["KXRS"] and get_cls["XQMC"] in xqmc and get_cls["IS_CONFLICT"] == 0, clss["datas"]))
            for wted in wanted:
                KCLBMC = wted['KCLBMC']
                if wted['KCLBMC'] == "第一外国语课":
                    KCLBMC = "第一外国语"
                elif wted['KCLBMC'] == "其他选修课":
                    KCLBMC = "其他可选课"
                # print(wted, wted['BJDM'], yjsxk_map[KCLBMC][2], KCLBMC)
                resp = self.session.get(
                    self.url_csrf
                )
                soup = BeautifulSoup(resp.text, 'lxml')
                csrf = soup.find(id="csrfToken")['value']
                # print(csrf)
                post = self.session.post(
                    self.url_class_chs + get_timestamp(),
                    data = {
                        'bjdm': wted['BJDM'],
                        'lx': yjsxk_map[KCLBMC][2],
                        'bqmc': wted['KCLBMC'],
                        'csrfToken': csrf
                    },
                    headers=self.headers_get_cls,
                    allow_redirects=False
                )
                # print(post, post.text, post.status_code)
                post = json.loads(post.text)
                if post["code"] == 0:
                    print(post["msg"])
                    continue
                res = self.session.post(
                    self.url_class_res + get_timestamp(),
                    data={
                        'xid': post['msg'],
                        'sfhqdqxkqqs': 1
                    },
                    headers=self.headers_get_cls,
                    allow_redirects=False
                )
                # print(res.text)
                res = json.loads(res.text)
                res = json.loads(res['msg'])
                if res['code'] == 1:
                    print("成功选上 {}".format(wted['KCMC']))
            
            sleep(sleep_time)
            print("wake again")

if __name__ == '__main__':
    yjsxk_fudan = Yjsxk(uid, psw, url_vcode_get, url_vcode_post, url_image_get, 
                        url_class_get, yjsxk_wanted_class, url_class_validate, url_class_chs, url_class_res, url_csrf)
    yjsxk_fudan.login()
    while True:
        try:
            yjsxk_fudan.work()
        except Exception as e:
            print(traceback.format_exc())
            print(e)