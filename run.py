import tweepy, os
from tweepy import Cursor
cwd = os.getcwd()
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the screen_name of the targeted user
def main():
    print("[*] Twitter Followers Scrapper")
    screen_name = input("[*] Input username target (without @): ")
    # printing the latest 20 followers of the user
    count = 1
    api = tweepy.API(auth, wait_on_rate_limit= True)
 
    for follower in Cursor(api.get_followers, screen_name=screen_name, count=200).items():
        print(f"[+] {follower.screen_name}")
        with open('success.txt','a') as f:
            f.write(f"{follower.screen_name}\n")
    print(f"[+] Scrapping Done!")
    file_list_akun = "success.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split("\n")
    print(f"[+] {len(list_accountsplit)} Successfully Scrapped!")
   
main()
