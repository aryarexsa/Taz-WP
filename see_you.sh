# Develop By: DemonX
# Team: TazManianDevil
# Post Date: 7/12/2020

clear
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'

figlet Taz-WP | lolcat

trap ctrl_c INT
ctrl_c() {
clear
echo "Keluar Dari Galaxy Xploit Tools" | lolcat
sleep 1
echo "" 
figlet Taz-WP | lolcat
exit
}

tazmanian_devil=1
while [ $tazmanian_devil -lt 6 ]; 
do 

echo ""
echo ""

echo -e "---------------------------------------------------------" | lolcat
echo -e "#  Tipe Tools               : WP => MBF                 #" | lolcat
echo -e "#  Team                     : TazManianDevil            #" | lolcat
echo -e "#  Code By                  : DemonX                    #" | lolcat
echo -e "#  Post Date                : 7/12/2020                 #" | lolcat
echo -e "#  Version                  : v1.18                     #" | lolcat
echo -e "---------------------------------------------------------" | lolcat
echo ""
echo "Untuk pertama kali, silahkan update & install dependencies" | lolcat
echo "        Dengan mengetikan perintah ( u ) / ( i )" | lolcat
echo ""
echo ""
sleep 3

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"  | lolcat
echo "#       Tools sedang proses, selesai dalam 3 detik      |" | lolcat
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"  | lolcat
echo ""
echo "
"
echo "[1] Wordpress-Crack" | lolcat
echo ""
echo "[2] About Me" | lolcat
echo ""
echo "[3] Pesan" | lolcat
echo ""
echo "[u] Update & Upgrade" | lolcat
echo ""
echo "[i] Install Dependencies" | lolcat
echo ""
echo "[0] Keluar" | lolcat
echo ""
echo ""
echo -e "╭─Pilih [0-3] / [u-i]"
read -p "  ╰─root@tazmanan:~# " te_em_de;

case $te_em_de in

1|01) cd source
echo ''
read -p "Masukkan List Website ( .txt ): " multi_web;
python mbf.py --multi_web $multi_web 
;;

2|02) xdg-open https://demonxtechnoit.blogspot.com
;;
3|03) echo ""
echo "Tetaplah merendah sampai musuh kalian paham siapa anda sebenarnya" | lolcat
echo ""
;;
u|U) cd source
bash u_u.sh
;;
i|I) cd source
bash depen.sh
;;
0|00) echo "Left...."
figlet Taz-WP | lolcat
exit
;;
*) echo "Inputan anda tidak ada di system Demon!"
esac
done
done