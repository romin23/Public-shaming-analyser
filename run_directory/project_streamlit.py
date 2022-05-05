import streamlit as st
import os 
import glob
import joblib
from instabot import Bot
from PIL import Image
import requests
# username="hatespeechdetector_",password='Romin@123456789'

def get_inference(data_dict, block):
    model = joblib.load(os.path.join(os.getcwd(), 'new_model'))
    blocked_users = {}    

    for user, data in data_dict.items():
        print(data)
        for text in data[1:]:
            profile_URL= data[0]
            inf = model.predict([text])
            if inf[0] == 1:
                print(text)
                try:
                    block.unfollow(user)
                    print(text)
                except:
                    pass
                if user in blocked_users:
                    blocked_users[user].append(text)
                    print('============BLOCKED==================')
                else:
                    blocked_users[user] = [profile_URL,text]
                    print('============BLOCKED==================')
    return blocked_users

def get_comm_data(user, passcode, ig_url, block):
    
    cookie_del = glob.glob("config/*cookie.json")
    try:
        # os.remove(cookie_del[0])
        st = block.login(username= user,password=passcode)
    except:
        pass

    # st = block.login(username= user,password=passcode)
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

def main():

    st.title("Public Shamming Analyzer")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Submit"):
        instagram_URL = 'https://www.instagram.com/' + username

        block = Bot()

        data_dict = get_comm_data(username, password, instagram_URL, block)
        print (data_dict)
        blocked_users = get_inference(data_dict, block)
        print(blocked_users)

        if len(blocked_users) != 0:
            print('yes'*10)
            for key, value in blocked_users.items():
                
                profile_URL = value[0]
                img_data=requests.get(profile_URL).content
                with open(f'C:/Users/romin/Downloads/shamming_analyzer/pic/{key}.jpg','wb') as handler :
                    handler.write(img_data)
                
                image = Image.open(f'C:/Users/romin/Downloads/shamming_analyzer/pic/{key}.jpg')
                st.image(image,caption=key)
                st.success(f"User {key} has been unfollowed/Blocked due to following comments flagged as offensive, {value[1:]}")
                
                # image = Image.open(profile_URL)
                
                # st.success(profile_URL)
                print(key, value)
                # print(f'User {key} has been unfollowed/Blocked due to following comments flagged as offensive')
                # print(value)

main()