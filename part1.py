__author__ = "theblackrose"
version = 1.0

import os 
import socket
from threading import Thread
import datetime
from time import sleep

os.system('clear')

#Globals
global username

def start():
  print('     --- Welcome ---')
  print('')
  username = "Player1"
  print("Your Username : ", username)
  print('')
  changeuser = input('If you want to change username press(1) : ')
  if changeuser == "1":
    newuser = input('Enter New Username : ')
    username = newuser
    os.system('clear')
    print('Welcome : ', newuser)
    sleep(2)
    print('')
    print('Logged ON')
    an = datetime.datetime.now()
    tarih = datetime.datetime.ctime(an)
    print(tarih)
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    print('')
    while True:
      soru1 = input('Bu Oyunda Otorite Kim ? :')
      if soru1 ==newuser:
        os.system('clear')
        print('Güzel Başlangıç ' ,newuser)
        break
      else:
        print('Yanlış!')
        continue
    print('')
    soru2 = input("yakın(1) mı uzak(2) mı ? : ")
    print('Hmmm..')
    soru2_neden = input('Peki Neden : ')
    print('')
    print('Pekala')
    while True:
      soru3 = input('Sevdiğin birine zarar veren birisi kaşında ve elleri kolları bağlı (1) - Kafasına RPG Göm, (2) - Katanayla Taşaklarını Dilimle : ')
      if soru3 =="1" and soru2 =="2":
        os.system('clear')
        print("Sen bu işi biliyorsun birdahaki sefere götünde patlat bence", newuser)
        break
      elif soru3 =="2" and soru2 =="1":
        os.system('clear')
        print("Ahhhhh bu çok acıtmış olmalı taşaklar iyi fikir değildi sanki ha ", newuser)
        break
      else:
        print('Mantıksız hareket ediyorsun')
        continue
    print('')
    print('Unutma Oyunda otorite sensin ve senin verdiğin cevaplara göre şekilleniyor oyunun!!!')
    print('')
    while True:
      soru4 = input('Suikast mı ?(1) , Düello mu ?(2) : ')
      if soru4=="1" and soru3=="2" and soru2=="1":
        os.system('clear')
        print('İstikrarını hiç bozmuyorsun ', newuser)
        break
      elif soru4=="2" and soru3=="1" and soru2=="2":
        os.system('clear')
        print('Asabisin bu aralar galiba ', newuser)
        break
      else:
        print('Unutma verdiğin kararları iyi düşün!')
        continue
    print('')
    print('Galiba bu aralar ne yapacağımı şaşırdım.')
    sleep(2)
    print('Saat şuan 05.35, ve tarihte bugün 13.05.2020')
    sleep(2)
    print('YKS Sınavıma : 45 GÜN 04 SAAT 38 DAKİKA 13 SANİYE KALDI')
    sleep(2)
    print('Birkaç gündür çok düzenli ve iyi ders çalışıyordum')
    sleep(2)
    print('Çok da verimli geçti')
    sleep(2)
    print('Ama bu gece çalışamadım nedenini hiç bilmiyorum')
    sleep(2)
    print('Neyse kafamı dağıtmak için kod yazmak istedim biraz bu gece')
    sleep(2)
    print('Çok olmasa da biraz iyi geldi')
    sleep(2)
    print('Ama eksik olan bir şey var')
    sleep(2)
    print('Bu Gece Bana ne engel oldu ????')
    sleep(2)
    os.system('clear')
    final1 = input('(1) - UYU , (2) - KOD YAZMAYA DEVAM ET : ')
    if final1 =="1":
      print('PART 1 COMPLETED')
    elif final1 =="2":
      print('Kaybettin')
    else:
      exit()

start()
