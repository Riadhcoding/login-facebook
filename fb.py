import mechanize,os,sys,json
import requests
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/287.0.0.50.119;]')]
id = input('\033[1;32mENTER YOUR EMAIL/ID :')
pw1 = input('\033[1;31mENTER YOUR PASSWORD : ')

data = br.open(
    'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pw1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
q = json.load(data)
if 'access_token' in q:
    print('\033[1;32mLogin success')
    print('\033[1;31m'+id + '\033[1;35m | \033[1;32m' + pw1)
else:
    if 'www.facebook.com' in q['error_msg']:
        print('\033[1;33mAccount Has Been Checkpoint')
        print(id + ' | ' + pw1)




