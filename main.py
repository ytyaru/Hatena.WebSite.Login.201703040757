#!python3
#encoding:utf-8
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import pprint
import dataset

class HatenaSite(object):
    def __init__(self, path_hatena_accounts_sqlite3):
        self.path_hatena_accounts_sqlite3 = path_hatena_accounts_sqlite3
        self.db_accounts = dataset.connect('sqlite:///' + path_hatena_accounts_sqlite3)

    def login(self, hatena_id):
        account = self.db_accounts['Accounts'].find_one(HatenaId=hatena_id)
        if (None == account):
            print('{0} のはてなIDを持ったアカウント情報は次のDBに存在しません。: {1}'.format(hatena, self.path_hatena_accounts_sqlite3))
            return
        print(account['Password'])

        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        post = {
            'name': hatena_id,
            'password': account['Password']
        }
        data = urlencode(post).encode('utf-8')
        res = opener.open('https://www.hatena.ne.jp/login', data)
        pprint.pprint(res.getheaders())
        res.close()

        url = 'http://f.hatena.ne.jp/{0}/{1}/rss'.format(hatena_id, 'Hatena Blog')
        res = opener.open(url)
        with open('photo_life.xml', 'wb') as f:
            f.write(res.read())
        res.close()
        
        
if __name__ == '__main__':
    hatena_id = 'ytyaru'
    client = HatenaSite(
        path_hatena_accounts_sqlite3 = "meta_Hatena.Accounts.sqlite3"
    )
    client.login(hatena_id)

