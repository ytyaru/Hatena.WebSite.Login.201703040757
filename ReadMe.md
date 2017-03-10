# このソフトウェアについて

はてなサイトにログインする。

# 開発環境

* Linux Mint 17.3 MATE
* Python 3.4.3
* SQLite 3.8.2
    
## WebSite

* [はてな](http://www.hatena.ne.jp/)

# 準備

* [はてなアカウントDBを作る](http://ytyaru.hatenablog.com/entry/2017/06/30/000000)

以下のようにmain.pyを変更する。

1. 上記の準備で作ったDBのファイルパスと、対象のはてなIDを以下のコードで設定する。

```python
if __name__ == '__main__':
    hatena_id = 'ytyaru'
    client = HatenaSite(
        path_hatena_accounts_sqlite3 = "meta_Hatena.Accounts.sqlite3"
    )
    client.login(hatena_id)
```

# 実行

```sh
python3 main.py
```

# 結果

フォトライフのRSSを`photo_life.xml`ファイルに書き出す。

対象は'Hatena Blog'フォルダ。はてなブログ編集画面でアップロードした画像が配置されるフォルダである。

```python
url = 'http://f.hatena.ne.jp/{0}/{1}/rss'.format(hatena_id, 'Hatena Blog')
```
```python
with open('photo_life.xml', 'wb') as f:
```

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)

