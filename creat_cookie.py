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
    cookie = '''
    Q8qA_2132_saltkey=NVyW437m; Q8qA_2132_lastvisit=1535858847; 
    Q8qA_2132_sid=FxIlN6; Q8qA_2132_sendmail=1; 
    Q8qA_2132_seccode=10354.599c10d54fe06ebcf1; 
    Q8qA_2132_ulastactivity=4ac2vBXVf7tH85DFAKky%2F3oefsWsJM6uI3vmLWx359YcD7xcRAaB; 
    Q8qA_2132_lastcheckfeed=301262%7C1535862490; 
    Q8qA_2132_checkfollow=1; 
    Q8qA_2132_lip=10.170.19.186%2C1535861086; 
    Q8qA_2132_myrepeat_rr=R0; 
    Q8qA_2132_auth=7eb6w1y31iagwjKG%2Bo%2BlUSpMu%2FmH3K7txjdAU5R9tp5H2HdQen%2BxLlJlyk4o2Dc%2BGTd6uZAmN%2FKaXItxJ%2F%2B%2FFTzHwyQ; 
    Q8qA_2132_checkpm=1; 
    Q8qA_2132_lastact=1535862494%09misc.php%09patch
    '''
    trans = TransCookie(cookie)
    with open("1.txt", "wb") as f:
        pprint.pprint(trans.string_to_dict())
        pickle.dump(trans.string_to_dict(), f)


