import requests 
import re
from time import sleep
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
def SendMess(UrlListTinNhan,cookie,headers):
    Tinnhan=requests.get(UrlListTinNhan,headers=headers).text
    UrlSend=re.findall('action="/messages/send?.*?"',Tinnhan)[0].replace('"','').replace('amp;','').replace('action=','')
    fb_dtsg = Tinnhan.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = Tinnhan.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    tids = Tinnhan.split('<input type="hidden" name="tids" value="')[1].split('"')[0]
    id=tids.split(':')[0].replace('cid.c.','')
    csid=re.findall('input type="hidden" name="csid" value=".*?"',Tinnhan)[0]
replace('input type="hidden" name="csid" value="','').replace('"','')
    data=(f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body=hhi&send=G%E1%BB%ADi&tids={tids}&wwwupp=C3&ids[{id}]={id}&referrer=&ctype=&cver=legacy&csid={csid}")
    hd={
        'authority':'mbasic.facebook.com',
        'method':'POST',
        'path':UrlSend,
        'secheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control':'max-age=0',
        'content-length':'303',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':cookie,
        'origin':'https://mbasic.facebook.com',
        'referer':'https://mbasic.facebook.com'+UrlSend,
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    b=requests.post('https://mbasic.facebook.com'+UrlSend,data=data,headers=hd)
    if b.status_code==200:
        return '1'
    else:
        return '0'

#vao tool#

cookie='sb=yC69Y0rf5sABJNh0EqDcyK1Q; datr=yC69Y1SWztuy8pGCP01mAfJQ; vpd=v1;724x384x1.875; c_user=100089801793694; xs=26:JGFGBkSVX542cA:2:1680175532:-1:6338; fr=02BImBWjyCSgQ8l67.AWWicnwVDnrGM4GxIhW8MNCzGlU.Bj92jR.HU.AAA.0.0.BkJXGs.AWXQysowcWQ; m_page_voice=100089801793694'


UrlHome='https://mbasic.facebook.com/home'
headers = {
        'authority': 'mbasic.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://mbasic.facebook.com',
        
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1186',
        'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
        'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
        'cookie': cookie
    }

DataHome=requests.get(UrlHome,headers=headers).text
UrlTinNhan='https://mbasic.facebook.com'+re.findall('"/messages/?.*?"',DataHome)[0].replace('"','').replace('amp;','')
DataTinNhan=requests.get(UrlTinNhan,headers=headers).text
UrlListTinNhans=re.findall('"/messages/read?.*?"',DataTinNhan)


for i in range(len(UrlListTinNhans)):
	UrlListTinNhan='https://mbasic.facebook.com'+re.findall('"/messages/read?.*?"',DataTinNhan)[i].replace('"','').replace('amp;','')
	Tinnhan=requests.get(UrlListTinNhan,headers=headers).text
	Name=re.findall('<title.*?</title>',Tinnhan)[0].replace('<title>','').replace('</title>','')
	print(f'{vang}[ {hong}{i+1}{vang} ] {do}=> {xnhac}{Name}')
dem=int(input(f'{vang}Nhập đoạn chát muốn spam: '))
UrlListTinNhan='https://mbasic.facebook.com'+re.findall('"/messages/read?.*?"',DataTinNhan)[0].replace('"','').replace('amp;','')
a=SendMess(UrlListTinNhan,cookie,headers)
print(a)
