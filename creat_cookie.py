import pickle
import pprint


class TransCookie:
    def __init__(self, cookie_str):
        self.cookie = cookie_str

    def string_to_dict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        item_dict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '').strip()
            value = item.split('=')[1].strip()
            item_dict[key] = value
        return item_dict


if __name__ == "__main__":
    cookie = '''你的cookie'''
    trans = TransCookie(cookie)
    with open("1.txt", "wb") as f:
        pprint.pprint(trans.string_to_dict())
        pickle.dump(trans.string_to_dict(), f)


