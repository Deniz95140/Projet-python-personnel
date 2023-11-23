import nmap
import os
print("Bienvenue dans le logiciel.")


def network_scanner():
    print("***************Bienvenue dans le Network Scanner***************")
    print("***************************************************************")
    adresse_ip = input("\nEntrez votre adresse IP: ")
    sc.scan(adresse_ip, '1-1024')
    print(sc.scaninfo())
    print(sc[adresse_ip]['tcp'].keys())

def vulnerabilities_detection():
    print("***************Bienvenue dans le Vulnerabilities Detection***************")
    print("*************************************************************************")
    adresse_ip = input("\nEntrez votre adresse IP: ")
    print(os.system('nmap -sV --script=vulscan.nse'))

def main():
    while True:
        try:
            choix = input("1- Network Scanner\n2- Vulnerabilities Detection\n3- Exploit\nEntrez un nombre: ")
            if choix == '1':
                network_scanner()
            if choix == '2':
                vulnerabilities_detection()
        except ValueError:
            print("Erreur, choisissez un nombre entre 1, 2 et 3.")



if __name__ == '__main__':
    main()
