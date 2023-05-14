from tkinter import *
import tkinter.scrolledtext as sc
import threading
from bs4 import BeautifulSoup as bc
from tkinter import ttk
import requests
import time
root = Tk()
root.geometry('970x560+200+100')
root.title("taha cherlock")
root.configure(background='whitesmoke')
root.iconbitmap('download.ico')
root.resizable(False, FALSE)
# ============================================
title = Label(root, text='cyber security tools',
              font=('Courier', 18), bg='black', fg='white')
title.pack(fill=X)
photo = PhotoImage(file='download.png')
photos = PhotoImage(file='images1.png')
panel1 = Label(root, image=photos)
panel1.place(x=2, y=35, width='200', height='440')
l1 = Label(root, text='USER:')
l1.place(x=5, y=360)
en1 = Entry(root, font=('Arial', '12'), justify=CENTER)
en1.place(x=40, y=360, width=150, height=24)


def go():

    threading.Thread(target=data).start()


def data():
    username = en1.get()

    def face():
        facebook_url = 'https://www.facebook.com/'
        r = requests.get(facebook_url+username)
        soup = bc(r.content, 'html.parser')
        title1 = soup.find('title')
        a1 = title.__str__
        if a1 == 'facebook':
            text1.insert('end', '[+]facebook:', 'blue')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', facebook_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="facebook acc", index=0, values=(
                'facebook', facebook_url, username, 'FOUND'))

    def instagram():
        insta_url = 'https://www.instagram.com/'
        r = requests.get(insta_url+username)
        soup = bc(r.content, 'html.parser')
        title2 = soup.find('title')
        a1 = title.__str__
        if a1 == 'instagram':
            text1.insert('end', '[+]instagram:', 'pink')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', insta_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="instagram acc", index=0, values=(
                'instagram', insta_url, username, 'FOUND'))

    def github():
        github_url = 'https://www.github.com/'
        r = requests.get(github_url+username)
        soup = bc(r.content, 'html.parser')
        title3 = soup.find('title')
        a1 = title.__str__
        if a1 == 'github':
            text1.insert('end', '[+]github:', 'blue')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', github_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="github acc", index=0, values=(
                'github', github_url, username, 'FOUND'))

    def snapchat():
        snap_url = 'https://www.snapchat.com/'
        r = requests.get(snap_url+username)
        soup = bc(r.content, 'html.parser')
        title4 = soup.find('title')
        a1 = title.__str__
        if a1 == 'snapchat':
            text1.insert('end', '[+]snapchat:', 'yellow')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', snap_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="snapchat acc", index=0, values=(
                'snapchat', snap_url, username, 'FOUND'))

    def google():
        google_url = 'https://www.google.com/'
        r = requests.get(google_url+username)
        soup = bc(r.content, 'html.parser')
        title5 = soup.find('title')
        a1 = title.__str__
        if a1 == 'google':
            text1.insert('end', '[+]google:', 'red')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', google_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="google acc", index=0, values=(
                'google', google_url, username, 'FOUND'))

    def youtube():
        youtube_url = 'https://www.youtube.com/'
        r = requests.get(youtube_url+username)
        soup = bc(r.content, 'html.parser')
        title6 = soup.find('title')
        a1 = title.__str__
        if a1 == 'youtube':
            text1.insert('end', '[+]youtube:', 'red')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', youtube_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="youtube acc", index=0, values=(
                'youtube', youtube_url, username, 'FOUND'))

    def amazon():
        amazon_url = 'https://www.amazon.com/'
        r = requests.get(amazon_url+username)
        soup = bc(r.content, 'html.parser')
        title7 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amazon':
            text1.insert('end', '[+]amazon:', '#333')
            text1.insert('end', username, 'gray')
            text1.insert('end', '\n')
            text1.insert('end', amazon_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="amazon acc", index=0, values=(
                'amazon', amazon_url, username, 'FOUND'))

    def netflix():
        netflix_url = 'https://www.netflix.com/'
        r = requests.get(netflix_url+username)
        soup = bc(r.content, 'html.parser')
        title8 = soup.find('title')
        a1 = title.__str__
        if a1 == 'Netflix':
            text1.insert('end', '[+]Netflix:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', netflix_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="Netflix acc", index=0, values=(
                'Netflix', netflix_url, username, 'FOUND'))

    def linkedin():
        linkedin_url = 'https://www.linkedin.com/'
        r = requests.get(linkedin_url+username)
        soup = bc(r.content, 'html.parser')
        title9 = soup.find('title')
        a1 = title.__str__
        if a1 == 'LinkedIn':
            text1.insert('end', '[+]LinkedIn:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', linkedin_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="linkedin acc", index=0, values=(
                'LinkedIn', linkedin_url, username, 'FOUND'))

    def twitter():
        twitter_url = 'https://www.twitter.com/'
        r = requests.get(twitter_url+username)
        soup = bc(r.content, 'html.parser')
        title10 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitter':
            text1.insert('end', '[+]twitter:', '#333')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', twitter_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitter acc", index=0, values=(
                'twitter', twitter_url, username, 'FOUND'))

    def fiverr():
        fiverr_url = 'https://www.fiverr.com/'
        r = requests.get(fiverr_url+username)
        soup = bc(r.content, 'html.parser')
        title11 = soup.find('title')
        a1 = title.__str__
        if a1 == 'fiverr':
            text1.insert('end', '[+]fiverr:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', fiverr_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="fiverr acc", index=0, values=(
                'fiverr', fiverr_url, username, 'FOUND'))

    def chatgpt():
        chat_url = 'https://chat.openai.com/'
        r = requests.get(chat_url+username)
        soup = bc(r.content, 'html.parser')
        title12 = soup.find('title')
        a1 = title.__str__
        if a1 == 'chatgpt':
            text1.insert('end', '[+]chatgpt:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', chat_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="chatgpt acc", index=0, values=(
                'chatgpt', chat_url, username, 'FOUND'))

    def reddit():
        reddit_url = 'https://www.reddit.com/'
        r = requests.get(reddit_url+username)
        soup = bc(r.content, 'html.parser')
        title12 = soup.find('title')
        a1 = title.__str__
        if a1 == 'reddit':
            text1.insert('end', '[+]reddit:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', reddit_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="reddit acc", index=0, values=(
                'reddit', reddit_url, username, 'FOUND'))

    def pinterest():
        pinterest_url = 'https://www.pinterest.com/'
        r = requests.get(pinterest_url+username)
        soup = bc(r.content, 'html.parser')
        title13 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pinterest':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pinterest_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pinterest acc", index=0, values=(
                'pinterest', pinterest_url, username, 'FOUND'))

    def canva():
        canva_url = 'https://www.canva.com/'
        r = requests.get(canva_url+username)
        soup = bc(r.content, 'html.parser')
        title14 = soup.find('title')
        a1 = title.__str__
        if a1 == 'canva':
            text1.insert('end', '[+]canva:', 'royalblue')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', canva_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="canva acc", index=0, values=(
                'canva', canva_url, username, 'FOUND'))
    # ====================finding all account of all design website===============

    def pinterest():
        pinterst_url = 'https://www.pinterest.com/'
        r = requests.get(pinterst_url+username)
        soup = bc(r.content, 'html.parser')
        title13 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pinterest':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pinterst_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pinterest acc", index=0, values=(
                'pinterest', pinterst_url, username, 'FOUND'))

    def designevo():
        designevo_url = 'https://www.designevo.com/'
        r = requests.get(designevo_url+username)
        soup = bc(r.content, 'html.parser')
        title14 = soup.find('title')
        a1 = title.__str__
        if a1 == 'desginevo':
            text1.insert('end', '[+]desginevo:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', designevo_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="designevo acc", index=0, values=(
                'designevo', designevo_url, username, 'FOUND'))

    def logojoy():
        logojoy_url = 'https://www.logojoy.com/'
        r = requests.get(logojoy_url+username)
        soup = bc(r.content, 'html.parser')
        title15 = soup.find('title')
        a1 = title.__str__
        if a1 == 'logojoy':
            text1.insert('end', '[+]pinterest:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', logojoy_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="logojoy acc", index=0, values=(
                'pinterest', logojoy_url, username, 'FOUND'))

    def tinkercad():
        tinker_url = 'https://www.tinkercad.com/'
        r = requests.get(tinker_url+username)
        soup = bc(r.content, 'html.parser')
        title15 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tinkercad':
            text1.insert('end', '[+]tinkercad:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tinker_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tinkercad acc", index=0, values=(
                'tinkercad', tinker_url, username, 'FOUND'))

    def freelancer():
        freelancer_url = 'https://www.freelancer.com/'
        r = requests.get(freelancer_url+username)
        soup = bc(r.content, 'html.parser')
        title16 = soup.find('title')
        a1 = title.__str__
        if a1 == 'freelancer':
            text1.insert('end', '[+]freelancer:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', freelancer_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="freelancer acc", index=0, values=(
                'freelancer', freelancer_url, username, 'FOUND'))

    def tesla():
        tesla_url = 'https://www.tesla.com/'
        r = requests.get(tesla_url+username)
        soup = bc(r.content, 'html.parser')
        title17 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tesla':
            text1.insert('end', '[+]tesla:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tesla_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tesla acc", index=0, values=(
                'tesla', tesla_url, username, 'FOUND'))

    def spacex():
        spacex_url = 'https://www.spacex.com/'
        r = requests.get(spacex_url+username)
        soup = bc(r.content, 'html.parser')
        title17 = soup.find('title')
        a1 = title.__str__
        if a1 == 'space x ':
            text1.insert('end', '[+]space x:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', spacex_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="spacex acc", index=0, values=(
                'space ', spacex_url, username, 'FOUND'))

    def twicth():
        twitch_url = 'https://www.twitch.tv/'
        r = requests.get(twitch_url+username)
        soup = bc(r.content, 'html.parser')
        title18 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitch tv':
            text1.insert('end', '[+]twitch tv :', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', twitch_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitch acc", index=0, values=(
                'twitch ', twitch_url, username, 'FOUND'))

    def dropbox():
        dropbox_url = 'https://www.dropbox.com/'
        r = requests.get(dropbox_url+username)
        soup = bc(r.content, 'html.parser')
        title19 = soup.find('title')
        a1 = title.__str__
        if a1 == 'twitch tv':
            text1.insert('end', '[+]twitch tv :', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', dropbox_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="twitch acc", index=0, values=(
                'twitch ', dropbox_url, username, 'FOUND'))

    def discord():
        discord_url = 'https://www.discord.com/'
        r = requests.get(discord_url+username)
        soup = bc(r.content, 'html.parser')
        title20 = soup.find('title')
        a1 = title.__str__
        if a1 == 'discord':
            text1.insert('end', '[+]discord:', 'orange')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', discord_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="discord acc", index=0, values=(
                'discord', discord_url, username, 'FOUND'))

    def liu():
        liu_url = 'https://www.liu.edu.lb/'
        r = requests.get(liu_url+username)
        soup = bc(r.content, 'html.parser')
        title21 = soup.find('title')
        a1 = title.__str__
        if a1 == 'liu':
            text1.insert('end', '[+]liu:', 'dodgerblue')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', liu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="liu acc", index=0, values=(
                'liu ', liu_url, username, 'FOUND'))

    def jinan():
        jinan_url = 'https://www.jinan.edu.lb/'
        r = requests.get(jinan_url+username)
        soup = bc(r.content, 'html.parser')
        title22 = soup.find('title')
        a1 = title.__str__
        if a1 == 'jinan':
            text1.insert('end', '[+]jinane:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', jinan_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="jinan acc", index=0, values=(
                'jinan', jinan_url, username, 'FOUND'))

    def aub():
        aub_url = 'https://www.aub.edu.lb/'
        r = requests.get(aub_url+username)
        soup = bc(r.content, 'html.parser')
        title23 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aub':
            text1.insert('end', '[+]aub:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aub_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aub acc", index=0, values=(
                'aub', aub_url, username, 'FOUND'))

    def aut():
        aut_url = 'https://www.aut.edu.lb/'
        r = requests.get(aut_url+username)
        soup = bc(r.content, 'html.parser')
        title24 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aut':
            text1.insert('end', '[+]aut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aut_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aut acc", index=0, values=(
                'aut', aut_url, username, 'FOUND'))

    def balamand():
        balamand_url = 'https://www.balamand.edu.lb/'
        r = requests.get(balamand_url+username)
        soup = bc(r.content, 'html.parser')
        title25 = soup.find('title')
        a1 = title.__str__
        if a1 == 'balamand':
            text1.insert('end', '[+]balamand:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', balamand_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="balamand acc", index=0, values=(
                'balamand', balamand_url, username, 'FOUND'))

    def ul():
        ul_url = 'https://www.ul.edu.lb/'
        r = requests.get(ul_url+username)
        soup = bc(r.content, 'html.parser')
        title25 = soup.find('title')
        a1 = title.__str__
        if a1 == 'lebanon uni':
            text1.insert('end', '[+]ul:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ul_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ul acc", index=0, values=(
                'ul', ul_url, username, 'FOUND'))

    def bau():
        bau_url = 'https://www.bau.edu.lb/'
        r = requests.get(bau_url+username)
        soup = bc(r.content, 'html.parser')
        title26 = soup.find('title')
        a1 = title.__str__
        if a1 == 'bau ':
            text1.insert('end', '[+]bau:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', bau_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="bau acc", index=0, values=(
                'bau', bau_url, username, 'FOUND'))

    def mtv():
        mtv_url = 'https://www.mtv.com.lb/'
        r = requests.get(mtv_url+username)
        soup = bc(r.content, 'html.parser')
        title27 = soup.find('title')
        a1 = title.__str__
        if a1 == 'mtv ':
            text1.insert('end', '[+]mtv:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mtv_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mtv acc", index=0, values=(
                'mtv', mtv_url, username, 'FOUND'))

    def aljadeed():
        aljadeed_url = 'https://www.aljadeed.tv/'
        r = requests.get(aljadeed_url+username)
        soup = bc(r.content, 'html.parser')
        title28 = soup.find('title')
        a1 = title.__str__
        if a1 == 'aljadeed':
            text1.insert('end', '[+]aljadeed:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', aljadeed_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="aljadeed acc", index=0, values=(
                'aljadeed', aljadeed_url, username, 'FOUND'))

    def amut():
        amut_url = 'https://www.amut.edu.lb/'
        r = requests.get(amut_url+username)
        soup = bc(r.content, 'html.parser')
        title29 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amut':
            text1.insert('end', '[+]amut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', amut_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="amut acc", index=0, values=(
                'amut', amut_url, username, 'FOUND'))

    def usj():
        usj_url = 'https://www.usj.edu.lb/'
        r = requests.get(usj_url+username)
        soup = bc(r.content, 'html.parser')
        title30 = soup.find('title')
        a1 = title.__str__
        if a1 == 'amut':
            text1.insert('end', '[+]amut:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', usj_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="usj acc", index=0, values=(
                'usj ', usj_url, username, 'FOUND'))

    def mubs():
        mubs_url = 'https://www.mubs.edu.lb/'
        r = requests.get(mubs_url+username)
        soup = bc(r.content, 'html.parser')
        title31 = soup.find('title')
        a1 = title.__str__
        if a1 == 'mubs':
            text1.insert('end', '[+]mubs:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mubs_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mubs acc", index=0, values=(
                'mubs ', mubs_url, username, 'FOUND'))

    def ua():
        ua_url = 'https://www.ua.edu.lb/'
        r = requests.get(ua_url+username)
        soup = bc(r.content, 'html.parser')
        title32 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ua':
            text1.insert('end', '[+]ua:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ua_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ua acc", index=0, values=(
                'ua', ua_url, username, 'FOUND'))

    def ndu():
        ndu_url = 'https://www.ndu.edu.lb/'
        r = requests.get(ndu_url+username)
        soup = bc(r.content, 'html.parser')
        title32 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ndu':
            text1.insert('end', '[+]ndu:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ndu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ndu acc", index=0, values=(
                'ndu', ndu_url, username, 'FOUND'))

    def tiktok():
        tiktok_url = 'https://www.tiktok.com/'
        r = requests.get(tiktok_url+username)
        soup = bc(r.content, 'html.parser')
        title33 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tiktok':
            text1.insert('end', '[+]tiktok:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tiktok_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tiktok acc", index=0, values=(
                'tiktok', tiktok_url, username, 'FOUND'))

    def ebay():
        ebay_url = 'https://www.ebay.com/'
        r = requests.get(ebay_url+username)
        soup = bc(r.content, 'html.parser')
        title34 = soup.find('title')
        a1 = title.__str__
        if a1 == 'ebay':
            text1.insert('end', '[+]ebay:', 'red')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', ebay_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="ebay acc", index=0, values=(
                'ebay', ebay_url, username, 'FOUND'))

    def spotify():
        spotify_url = 'https://www.spotify.com/'
        r = requests.get(spotify_url+username)
        soup = bc(r.content, 'html.parser')
        title35 = soup.find('title')
        a1 = title.__str__
        if a1 == 'spotify':
            text1.insert('end', '[+]spotify:', 'lime')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', spotify_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="spotify acc", index=0, values=(
                'spotify', spotify_url, username, 'FOUND'))

    def autodraw():
        autodraw_url = 'https://www.autodraw.com/'
        r = requests.get(autodraw_url+username)
        soup = bc(r.content, 'html.parser')
        title35 = soup.find('title')
        a1 = title.__str__
        if a1 == 'autodraw':
            text1.insert('end', '[+]autodraw:', 'lime')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', autodraw_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="autodraw acc", index=0, values=(
                'autodraw', autodraw_url, username, 'FOUND'))

    def figma():
        figma_url = 'https://www.figma.com/'
        r = requests.get(figma_url+username)
        soup = bc(r.content, 'html.parser')
        title36 = soup.find('title')
        a1 = title.__str__
        if a1 == 'figma':
            text1.insert('end', '[+]figma:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', figma_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="figma acc", index=0, values=(
                'figma', figma_url, username, 'FOUND'))

    def envision():
        envision_url = 'https://www.envisionapp.com/'
        r = requests.get(envision_url+username)
        soup = bc(r.content, 'html.parser')
        title37 = soup.find('title')
        a1 = title.__str__
        if a1 == 'envision':
            text1.insert('end', '[+]envision:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', envision_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="envision acc", index=0, values=(
                'envision', envision_url, username, 'FOUND'))

    def templatemonster():
        monster_url = 'https://www.templatemonster.com/'
        r = requests.get(monster_url+username)
        soup = bc(r.content, 'html.parser')
        title38 = soup.find('title')
        a1 = title.__str__
        if a1 == 'monster':
            text1.insert('end', '[+]monster:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', monster_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="monster acc", index=0, values=(
                'monster', monster_url, username, 'FOUND'))

    def designmodo():
        mddesign_url = 'https://www.designmodo.com/'
        r = requests.get(mddesign_url+username)
        soup = bc(r.content, 'html.parser')
        title39 = soup.find('title')
        a1 = title.__str__
        if a1 == 'design modo':
            text1.insert('end', '[+]mddesign:', 'pink')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', mddesign_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="mddesign acc", index=0, values=(
                'mddesign', mddesign_url, username, 'FOUND'))

    def houzz():
        houzz_url = 'https://www.houzz.com/'
        r = requests.get(houzz_url+username)
        soup = bc(r.content, 'html.parser')
        title40 = soup.find('title')
        a1 = title.__str__
        if a1 == 'houzz':
            text1.insert('end', '[+]houzz:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', houzz_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="houzz acc", index=0, values=(
                'houzz', houzz_url, username, 'FOUND'))

    def weebly():
        weebly_url = 'https://www.weebly.com/'
        r = requests.get(weebly_url+username)
        soup = bc(r.content, 'html.parser')
        title41 = soup.find('title')
        a1 = title.__str__
        if a1 == 'weebly':
            text1.insert('end', '[+]weebly:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', weebly_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="weebly acc", index=0, values=(
                'weebly', weebly_url, username, 'FOUND'))

    def bandcamp():
        bancamp_url = 'https://www.weebly.com/'
        r = requests.get(bancamp_url+username)
        soup = bc(r.content, 'html.parser')
        title42 = soup.find('title')
        a1 = title.__str__
        if a1 == 'bancamp':
            text1.insert('end', '[+]bancamp:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', bancamp_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="bancamp acc", index=0, values=(
                'bancamp', bancamp_url, username, 'FOUND'))

    def yandex():
        yandex_url = 'https://www.yandex.com/'
        r = requests.get(yandex_url+username)
        soup = bc(r.content, 'html.parser')
        title43 = soup.find('title')
        a1 = title.__str__
        if a1 == 'yandex':
            text1.insert('end', '[+]yandex:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', yandex_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="yandex acc", index=0, values=(
                'yandex', yandex_url, username, 'FOUND'))

    def g2g():
        g2g_url = 'https://www.g2g.com/'
        r = requests.get(g2g_url+username)
        soup = bc(r.content, 'html.parser')
        title43 = soup.find('title')
        a1 = title.__str__
        if a1 == 'g2g':
            text1.insert('end', '[+]g2g:', 'yellow')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', g2g_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="g2g acc", index=0, values=(
                'g2g', g2g_url, username, 'FOUND'))

    def udemu():
        udemu_url = 'https://www.udemu.com/'
        r = requests.get(udemu_url+username)
        soup = bc(r.content, 'html.parser')
        title44 = soup.find('title')
        a1 = title.__str__
        if a1 == 'g2g':
            text1.insert('end', '[+]udemu:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', udemu_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="udemu acc", index=0, values=(
                'udemu', udemu_url, username, 'FOUND'))

    def overflowstack():
        stack_url = 'https://www.stackoverflow.com/'
        r = requests.get(stack_url+username)
        soup = bc(r.content, 'html.parser')
        title45 = soup.find('title')
        a1 = title.__str__
        if a1 == 'stackoverflow':
            text1.insert('end', '[+]stackoverflow:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', stack_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="stack acc", index=0, values=(
                'stack', stack_url, username, 'FOUND'))

    def soundcloud():
        sound_url = 'https://www.soundcloud.com/'
        r = requests.get(sound_url+username)
        soup = bc(r.content, 'html.parser')
        title46 = soup.find('title')
        a1 = title.__str__
        if a1 == 'soundcloud':
            text1.insert('end', '[+]soundcloud:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', sound_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="sound acc", index=0, values=(
                'sound', sound_url, username, 'FOUND'))

    def skype():
        skype_url = 'https://www.skype.com/'
        r = requests.get(skype_url+username)
        soup = bc(r.content, 'html.parser')
        title47 = soup.find('title')
        a1 = title.__str__
        if a1 == 'skype':
            text1.insert('end', '[+]skype:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', skype_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="skype acc", index=0, values=(
                'skype', skype_url, username, 'FOUND'))

    def wechat():
        wechat_url = 'https://www.wechat.com/'
        r = requests.get(wechat_url+username)
        soup = bc(r.content, 'html.parser')
        title48 = soup.find('title')
        a1 = title.__str__
        if a1 == 'telegram':
            text1.insert('end', '[+]wechat:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', wechat_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="wechat acc", index=0, values=(
                'wechat', wechat_url, username, 'FOUND'))

    def telegram():
        telegram_url = 'https://www.telegram.org/'
        r = requests.get(telegram_url+username)
        soup = bc(r.content, 'html.parser')
        title49 = soup.find('title')
        a1 = title.__str__
        if a1 == 'telegram':
            text1.insert('end', '[+]telegram:', '#222')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', telegram_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="telegram acc", index=0, values=(
                'telegram', telegram_url, username, 'FOUND'))

    def whatsapp():
        whatsapp_url = 'https://www.whatsapp.com/'
        r = requests.get(whatsapp_url+username)
        soup = bc(r.content, 'html.parser')
        title50 = soup.find('title')
        a1 = title.__str__
        if a1 == 'whatsapp':
            text1.insert('end', '[+]whatsapp:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', whatsapp_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="whatsapp acc", index=0, values=(
                'whatsapp', whatsapp_url, username, 'FOUND'))

    def airnb():
        airnb_url = 'https://www.airbnb.com/'
        r = requests.get(airnb_url+username)
        soup = bc(r.content, 'html.parser')
        title51 = soup.find('title')
        a1 = title.__str__
        if a1 == 'airnb':
            text1.insert('end', '[+]airnb:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', airnb_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="airnb acc", index=0, values=(
                'airnb', airnb_url, username, 'FOUND'))

    def microsoft():
        microsoft_url = 'https://www.microsoft.com/'
        r = requests.get(microsoft_url+username)
        soup = bc(r.content, 'html.parser')
        title52 = soup.find('title')
        a1 = title.__str__
        if a1 == 'airnb':
            text1.insert('end', '[+]microsoft:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', microsoft_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="microsoft acc", index=0, values=(
                'microsoft', microsoft_url, username, 'FOUND'))

    def tumblr():
        tumblr_url = 'https://www.tumblr.com/'
        r = requests.get(tumblr_url+username)
        soup = bc(r.content, 'html.parser')
        title53 = soup.find('title')
        a1 = title.__str__
        if a1 == 'tumblr':
            text1.insert('end', '[+]tumblr:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', tumblr_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="tumblr acc", index=0, values=(
                'tumblr', tumblr_url, username, 'FOUND'))

    def vimeo():
        vimeo_url = 'https://www.vimeo.com/'
        r = requests.get(vimeo_url+username)
        soup = bc(r.content, 'html.parser')
        title54 = soup.find('title')
        a1 = title.__str__
        if a1 == 'vimeo':
            text1.insert('end', '[+]vimeo:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', vimeo_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="vimeo acc", index=0, values=(
                'vimeo', vimeo_url, username, 'FOUND'))

    def zara():
        zara_url = 'https://www.zara.com/'
        r = requests.get(zara_url+username)
        soup = bc(r.content, 'html.parser')
        title55 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zara':
            text1.insert('end', '[+]zara:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', zara_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="zara acc", index=0, values=(
                'zara', zara_url, username, 'FOUND'))

    def nike():
        nike_url = 'https://www.nike.com/'
        r = requests.get(nike_url+username)
        soup = bc(r.content, 'html.parser')
        title56 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zara':
            text1.insert('end', '[+]nike:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', nike_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="nike acc", index=0, values=(
                'nike ', nike_url, username, 'FOUND'))

    def asos():
        asos_url = 'https://www.asos.com/'
        r = requests.get(asos_url+username)
        soup = bc(r.content, 'html.parser')
        title56 = soup.find('title')
        a1 = title.__str__
        if a1 == 'asos':
            text1.insert('end', '[+]asos:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', asos_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="asos acc", index=0, values=(
                'asos', asos_url, username, 'FOUND'))

    def zomeus():
        zome_url = 'https://www.zome.us/'
        r = requests.get(zome_url+username)
        soup = bc(r.content, 'html.parser')
        title57 = soup.find('title')
        a1 = title.__str__
        if a1 == 'zome':
            text1.insert('end', '[+]zome:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', zome_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="zome acc", index=0, values=(
                'zome', zome_url, username, 'FOUND'))

    def icloud():
        icloud_url = 'https://www.icloud.com/'
        r = requests.get(icloud_url+username)
        soup = bc(r.content, 'html.parser')
        title58 = soup.find('title')
        a1 = title.__str__
        if a1 == 'icloud':
            text1.insert('end', '[+]icloud:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', icloud_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="icloud acc", index=0, values=(
                'icloud', icloud_url, username, 'FOUND'))

    def trello():
        trello_url = 'https://www.trello.com/'
        r = requests.get(trello_url+username)
        soup = bc(r.content, 'html.parser')
        title59 = soup.find('title')
        a1 = title.__str__
        if a1 == 'trello':
            text1.insert('end', '[+]trello:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', trello_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="trello acc", index=0, values=(
                'trello', trello_url, username, 'FOUND'))

    def asana():
        asana_url = 'https://www.asana.com/'
        r = requests.get(asana_url+username)
        soup = bc(r.content, 'html.parser')
        title60 = soup.find('title')
        a1 = title.__str__
        if a1 == 'asana':
            text1.insert('end', '[+]asana:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', asana_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="asana acc", index=0, values=(
                'asana', asana_url, username, 'FOUND'))

    def blogger():
        blogger_url = 'https://www.blogger.com'
        r = requests.get(blogger_url+username)
        soup = bc(r.content, 'html.parser')
        title62 = soup.find('title')
        a1 = title.__str__
        if a1 == 'blogger':
            text1.insert('end', '[+]blogger:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', blogger_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="blogger acc", index=0, values=(
                'blogger', blogger_url, username, 'FOUND'))

    def pepsi():
        pepsi_url = 'https://www.pepsi.com/'
        r = requests.get(pepsi_url+username)
        soup = bc(r.content, 'html.parser')
        title63 = soup.find('title')
        a1 = title.__str__
        if a1 == 'pepsi':
            text1.insert('end', '[+]pepsi:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', pepsi_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="pepsi acc", index=0, values=(
                'pepsi', pepsi_url, username, 'FOUND'))

    def prada():
        prada_url = 'https://www.prada.com/'
        r = requests.get(prada_url+username)
        soup = bc(r.content, 'html.parser')
        title63 = soup.find('title')
        a1 = title.__str__
        if a1 == 'prada':
            text1.insert('end', '[+]prada:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', prada_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="prada acc", index=0, values=(
                'prada', prada_url, username, 'FOUND'))

    def gucci():
        gucci_url = 'https://www.gucci.com/'
        r = requests.get(gucci_url+username)
        soup = bc(r.content, 'html.parser')
        title64 = soup.find('title')
        a1 = title.__str__
        if a1 == 'gucci':
            text1.insert('end', '[+]gucci:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', gucci_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="gucci acc", index=0, values=(
                'gucci', gucci_url, username, 'FOUND'))

    def chanel():
        channel_url = 'https://www.chanel.com/'
        r = requests.get(channel_url+username)
        soup = bc(r.content, 'html.parser')
        title65 = soup.find('title')
        a1 = title.__str__
        if a1 == 'channel':
            text1.insert('end', '[+]channel:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', channel_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="channel acc", index=0, values=(
                'channel', channel_url, username, 'FOUND'))

    def samsung():
        samsung_url = 'https://www.samsung.com/'
        r = requests.get(samsung_url+username)
        soup = bc(r.content, 'html.parser')
        title66 = soup.find('title')
        a1 = title.__str__
        if a1 == 'samsung':
            text1.insert('end', '[+]samsung:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', samsung_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="samsung acc", index=0, values=(
                'samsung', samsung_url, username, 'FOUND'))

    def techno():
        techno_url = 'https://www.techno-mobile.com/'
        r = requests.get(techno_url+username)
        soup = bc(r.content, 'html.parser')
        title67 = soup.find('title')
        a1 = title.__str__
        if a1 == 'samsung':
            text1.insert('end', '[+]techno:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', techno_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="techno acc", index=0, values=(
                'techno', techno_url, username, 'FOUND'))

    def school():
        school_url = 'https://www.w3schools.com/'
        r = requests.get(school_url+username)
        soup = bc(r.content, 'html.parser')
        title68 = soup.find('title')
        a1 = title.__str__
        if a1 == 'w3schools':
            text1.insert('end', '[+]w3schools:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', school_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="w3schools acc", index=0, values=(
                'w3schools', school_url, username, 'FOUND'))

    def code():
        code_url = 'https://www.code.org/'
        r = requests.get(code_url+username)
        soup = bc(r.content, 'html.parser')
        title69 = soup.find('title')
        a1 = title.__str__
        if a1 == 'code':
            text1.insert('end', '[+]code:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', code_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="code acc", index=0, values=(
                'code', code_url, username, 'FOUND'))

    def codecademy():
        codecademy_url = 'https://www.codecademy.com/'
        r = requests.get(codecademy_url+username)
        soup = bc(r.content, 'html.parser')
        title70 = soup.find('title')
        a1 = title.__str__
        if a1 == 'codecademy':
            text1.insert('end', '[+]codecademy:', 'green')
            text1.insert('end', username, 'red')
            text1.insert('end', '\n')
            text1.insert('end', codecademy_url+username)
            text1.insert('end', '[x] not found', 'red')
            text1.insert('end', '\n-----------\n')
        else:
            tv.insert(parent='', text="codecademy acc", index=0, values=(
                'codec', codecademy_url, username, 'FOUND'))
    # chanel()
    # codecademy()
    # school()
    # code()
    # samsung()
    # gucci()
    # aub()
    # pepsi()
    # techno()
    icloud()
    # prada()
    # asana()
    # blogger()
    nike()
    trello()
    # asos()
    # zomeus()
    # tumblr()
    # vimeo()
    # microsoft()
    # skype()
    # airnb()
    # zara()
    # telegram()
    # whatsapp()
    # wechat()
    # bandcamp()
    # udemu()
    # yandex()
    # overflowstack()
    # weebly()
    # g2g()
    # designmodo()
    # envision()
    # houzz()
    # autodraw()
    # ebay()
    # twicth()
    # templatemonster()
    # tiktok()
    # spotify()
    # figma()
    # amut()
    # mubs()
    # ndu()

    # usj()
    # balamand()
    # ua()
    # mtv()
    # aljadeed()
    # liu()

    # ul()
    # bau()
    # spacex()
    # soundcloud()
    # dropbox()
    # jinan()
    # aut()
    face()
    # tinkercad()
    # freelancer()
    github()
    # chatgpt()
    # tesla()
    # google()
    snapchat()
    youtube()
    amazon()
    instagram()
    linkedin()
    netflix()
    discord()
    twitter()
    fiverr()
    # reddit()
    # pinterest()
    canva()
    designevo()
    logojoy()


# =============button====================
button1 = Button(root, text='start testing', width=25,
                 height=2, cursor='hand2', bg='royalblue', fg='white', command=data)
button1.place(x=4, y=513)


def exit():
    root.destroy()


def startsearching():
    exit()
    import tkinter
    import re
    from tkinter import messagebox
    window = Tk()
    window.geometry("900x500+200+100")
    window.iconbitmap("download.ico")
    window.title("searching by her phone nb")
    window.resizable(False, False)
    frame = Frame(window)
    frame.place(x=0, y=0, width=230, height=500)
    addimage = PhotoImage(file="images1.png")
    labelimage = Label(frame, image=addimage)
    labelimage.place(x=0, y=0, width=230, height=350)

    # ====================buttons frame===========================
    buttonsframe = Frame(window)
    buttonsframe.place(x=0, y=350, width=230, height=250)
    labetitle = Label(buttonsframe, text="phnb:",
                      fg="#222", font=("Courier", 13))
    labetitle.place(x=3, y=23)
    labelsph = Entry(buttonsframe)
    labelsph.place(x=60, y=20, width=200, height=30)

    

    def opendata():
        def check():
            taha = labelsph.get()
            pattern = r'^\d{2}-\d{3}-\d{3}$'
            if taha == "" and re.match(pattern,taha):
                messagebox.showerror("error", "please enter phone number and you should enter a good pattern with this format 22-222-222")
            else:
               pass
        check()
        def globalinstagramsearch():
            url = f"http://instagram.com/phone_numbers/{taha}"
            response = requests.get(url)
            print(response)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    print(data,website_name,account,username,email,status)
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")
        
        def globalfacebooksearch():
            url = f"https://facebook.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def tiktoksearh():
            url = f"https://tiktok.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def snapchat():
            url = f"https://snapchat.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def google():
            url = f"https://google.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def google():
            url = f"https://google.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def zara():
            url = f"https://zara.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(response.json())
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def nike():
            url = f"https://nike.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def discord():
            url = f"https://discord.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def twitter():
            url = f"https://twitter.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def netflix():
            url = f"https://netflix.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def youtube():
            url = f"https://youtube.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def channel():
            url = f"https://channel.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def canva():
            url = f"https://canva.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def logojoy():
            url = f"https://logojoy.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def amazon():
            url = f"https://amazon.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def telegram():
            url = f"https://telegram.org/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def spotify():
            url = f"https://spotify.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def figma():
            url = f"https://figma.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def g2g():
            url = f"https://g2g.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def udemu():
            url = f"https://udemu.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def reddit():
            url = f"https://reddit.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def pinterest():
            url = f"https://pinterest.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")

        def designevo():
            url = f"https://designevo.com/phone_numbers/{taha}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    website_name = data.get("website_name")
                    account = data.get("account")
                    username = data.get("username")
                    email = data.get("email")
                    status = "Found"
                    tvs.insert("", "end", values=(
                        taha, website_name, account, username, email, status))

                except ValueError:
                    messagebox.showerror(
                        "error", "Inavlid Json Response")
        globalfacebooksearch()
        globalinstagramsearch()
        # nike()
        # logojoy()
        # udemu()
        # discord()
        # spotify()
        # netflix()
        # youtube()
        # reddit()
        # figma()
        # amazon()
        # globalinstagramsearch()
        # telegram()
        # designevo()
        # pinterest()
        # channel()
        # tiktoksearh()
        # g2g()
        # zara()
        # twitter()
        # snapchat()
        # canva()
        # google()
    bt2 = Button(buttonsframe, text="start searching", fg="white",
                 bg="royalblue", cursor="hand2", command=opendata)
    bt2.place(x=10, y=60, width=200, height=40)

    def exits():
        window.destroy()
    bt1 = Button(buttonsframe, text="exit",
                 fg="white", bg="red", cursor='hand2', command=exits)
    bt1.place(x=10, y=103, width=200, height=40)
    tvs = ttk.Treeview(window)
    styles = ttk.Style(window)
    styles.theme_use('clam')
    styles.configure('Treeview', rowheight=35, background='#d8d8d8',
                     fieldbackground='#d8d8d8', foreground='black')
    tvs['columns'] = ('namesocial', 'urlname', 'username', 'status')
    tvs.column('#0', anchor=CENTER, width=50)
    tvs.column('namesocial', anchor=CENTER, width=40)
    tvs.column('urlname', anchor=CENTER, width=130)
    tvs.column('username', anchor=CENTER, width=120)
    tvs.column('status', anchor=CENTER, width=30)
    tvs.heading('#0', text='phone number', anchor=CENTER)
    tvs.heading('namesocial', text='SOCIAL NAME', anchor=CENTER)
    tvs.heading('urlname', text='wbesite', anchor=CENTER)
    tvs.heading('username', text='user name', anchor=CENTER)
    tvs.heading('status', text='status', anchor=CENTER)
    tvs.place(x=230, y=0, width=670, height=500)
    tvse = sc.ScrolledText(tvs)

    window.mainloop()


button2 = Button(root, text="Exit", cursor="hand2",
                 bg="red", fg="white", command=exit)
button2.place(x=4, y=460, width=184, height=40)
# button3
button3 = Button(root, text="search by phnb", fg="white",
                 bg="#222", command=startsearching)
button3.place(x=4, y=410, width=184, height=40)
# ============treview==============
tv = ttk.Treeview(root)
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', rowheight=35, background='#d8d8d8',
                fieldbackground='#d8d8d8', foreground='black')
tv['columns'] = ('namesocial', 'urlname', 'username', 'status')
tv.column('#0', anchor=CENTER, width=50)
tv.column('namesocial', anchor=CENTER, width=40)
tv.column('urlname', anchor=CENTER, width=130)
tv.column('username', anchor=CENTER, width=120)
tv.column('status', anchor=CENTER, width=30)
tv.heading('#0', text='SOCIAL WEBSITE', anchor=CENTER)
tv.heading('namesocial', text='website name', anchor=CENTER)
tv.heading('urlname', text='wbesite', anchor=CENTER)
tv.heading('username', text='user name', anchor=CENTER)
tv.heading('status', text='status', anchor=CENTER)
tv.place(x=200, y=35, width=765, height=550)
taha = sc.ScrolledText(tv)
text1 = sc.ScrolledText(root)
text1['font'] = ('Courier', '10', 'bold')
text1.place(x=205, y=440, width=760, height=0)
# function


root.mainloop()
