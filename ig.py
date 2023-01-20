from instabot import Bot
bot = Bot()
#enter your username and password in the given spaces below
bot.login(username = "__________", password = "__________")
#enter the user name of account you want your account to follow
bot.follow("__________")
#uploading any picture by giving path of the picture you want to upload
#change \ to / in path and puth .jpg in the end of the path
bot.upload_photo("_____________" caption = "hey whats up ?")
#unfollowing a person. enter the username of the account you want to unfollow
bot.unfollow("___________")
#sending a message to multipke users. enter as many usernames as you want and the message will be delivered to all
bot.send_message("hey how are you ?", ["________","_______","_______"])
#checking your followers and following or other informations. Enter the username in the blank space below
followers = bot.get_user_followers("______")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("______")
for Following in following:
    print(bot.get_user_info(Following))