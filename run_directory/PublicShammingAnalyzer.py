# import streamlit as st
# import import_ipynb
# import Instagram_screaper as ig_scrape
import os 
import glob
import joblib
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pprint
from selenium.webdriver.support.wait import WebDriverWait
from instabot import Bot

def get_inference(data_dict, block):
    model = joblib.load(os.path.join(os.getcwd(), 'new_model'))
    blocked_users = {}    

    for user, data in data_dict.items():
        for text in data[1:]:
            inf = model.predict([text])
            if inf[0] == 1:
                try:
                    block.unfollow(user)
                except:
                    pass
                if user in blocked_users:
                    blocked_users[user].append(text)
                else:
                    blocked_users[user] = [text]
    return blocked_users




def get_post_links(user, passcode, ig_url):
    ig_url = ig_url
    driver = webdriver.Chrome()
    driver.delete_cookie('romin_23k')
    driver.delete_cookie('9595113046')
    # driver.get("https://www.instagram.com/")
    driver.get(ig_url)

    try:    
        #target username
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        #enter username and password
        username.clear()
        # username.send_keys("romin_23k")
        username.send_keys(user)
        password.clear()
        # password.send_keys("9595113046")
        password.send_keys(passcode)

        #target the login button and click it
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    except :
        pass

    # scroll to the bottom of the page
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True

    # find all links on the page and if they match '/p' append to list named posts
    post_links = []
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post:
          post_links.append( post )
    return post_links




# def get_comm_data(user, passcode, ig_url, block):
    
#     cookie_del = glob.glob("config/*cookie.json")
#     try:
#         os.remove(cookie_del[0])
#     except:
#         pass
#     st = block.login(username= user,password=passcode)
#     post_links = get_post_links(user, passcode, ig_url)
#     data_dict = {}
#     for i in post_links:
#         media_id = block.get_media_id_from_link(i)
#         comm_list = block.get_media_comments(media_id)

#         for comm in comm_list:
#             text = comm['text']
#             comm_owner = comm['user']['username']
#             comm_owner_pp = comm['user']['profile_pic_url']

#             if comm_owner in data_dict:
#                 data_dict[comm_owner].append(text)
#             else:
#                 data_dict[comm_owner] = [comm_owner_pp, text]
#     return data_dict

def get_comm_data(user, passcode, ig_url, block):
    
    cookie_del = glob.glob("config/*cookie.json")
    try:
        os.remove(cookie_del[0])
    except:
        pass
    st = block.login(username= user,password=passcode)
    media = block.get_your_medias(user)
    media = media[0]
    id = str(media['caption']['media_id'])
    # post_links = ig_scrape.get_post_links(user, passcode, ig_url)
    data_dict = {}
    # for i in post_links:
    #     media_id = block.get_media_id_from_link(i)
    comm_list = block.get_media_comments(id)
    for comm in comm_list:
        text = comm['text']
        comm_owner = comm['user']['username']
        comm_owner_pp = comm['user']['profile_pic_url']
        if comm_owner in data_dict:
            data_dict[comm_owner].append(text)
        else:
            data_dict[comm_owner] = [comm_owner_pp, text]
    return data_dict



def execute(username, password):
    instagram_URL = 'https://www.instagram.com/' + username
    block = Bot()
    data_dict = get_comm_data(username, password, instagram_URL, block)
    blocked_users = get_inference(data_dict, block)
    # if len(blocked_users) != 0:
            # for key, value in blocked_users.items():
            #     st.success(f"User {key} has been unfollowed/Blocked due to following comments flagged as offensive")
            #     # print(f'User {key} has been unfollowed/Blocked due to following comments flagged as offensive')
            #     print(value)
    return blocked_users

# execute(username, password)
