import requests
# basic url of instagram to a connect the user
base_url = 'https://api.instagram.com/v1/'


def owner_info():
    owner_url = base_url + 'users/self/?access_token=' + app_access_token
print "Owner Details Get Request Url: - " + owner_url
owner_data = requests.get(owner_url).json()
if owner_data['meta']['code'] == 200:
    if len(owner_data['data']):
        print "Owner Information Are Following : -"
print "\t UserName : %s " % (owner_data['data']['username'])
print "\t Full Name: %s " % (owner_data['data']['full_name'])
print "\t Number of Post: %s " % (owner_data['data']['counts']['media'])
print "\t you are Following: %s People. and %s People Following You on Instagram." % (
(owner_data['data']['counts']['follows']), (owner_data['data']['counts']['followed_by']))
else:
    print "User Does not Exist"
else:
    print "Status Code Other than 200 Received. Something goes Wrong"


def get_user_id(insta_username):
search_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username, app_access_token)
    print '\nSearch Query GET url of User Name: ' + insta_username + " is Following : \n" + search_url

query_result = requests.get(search_url).json()
if query_result['meta']['code'] == 200:
    if len(query_result['data']):

print "\t User Name: %s \n\t User ID: %s" % (query_result['data'][0]['username'], query_result['data'][0]['id'])
user_id = query_result['data'][0]['id']
return user_id
else:
    return None
else:
    print 'Status code other than 200 received!'
exit()


def user_details(username):


specific_user_id = get_user_id(username)

user_id_url = (base_url + 'users/%s?access_token=%s') % (specific_user_id, app_access_token)
print '\nSelected user Profile Get Url is : %s' % user_id_url

user_info = requests.get(user_id_url).json()

if user_info['meta']['code'] == 200:
    if len(user_info['data']):
        print "Searched User Information Are Following : -"
print "\t UserName : %s " % (user_info['data']['username'])
print "\t Full Name: %s " % (user_info['data']['full_name'])
print "\t Profile Pic : %s " % (user_info['data']['profile_picture'])
print "\t Number of Post: %s " % (user_info['data']['counts']['media'])
print "\t Following: %s \n\t Followers %s" % (
(user_info['data']['counts']['follows']), (user_info['data']['counts']['followed_by']))
else:
print "User Does not Exist"
else:
print "Status Code Other than 200 Received. Something goes Wrong"

def get_own_post():
    get_self_media = base_url + 'users/self/media/recent/?access_token=' + app_access_token


print "Get Recent Media Url: " + get_self_media
recent_media = requests.get(get_self_media).json()
if recent_media['meta']['code'] == 200:
    if len(recent_media['data']):
        image_name = recent_media['data'][0]['id'] + '.jpeg'
image_url = recent_media['data'][0]['images']['standard_resolution']['url']
urllib.urlretrieve(image_url, image_name)
print 'Your image has been downloaded!'
return recent_media['data'][0]['id']
else:
    print "There is no recent post!"
return None
else:
    print 'Status code other than 200 received!'
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)


get_self_media = base_url + 'users/' + user_id + '/media/recent/?access_token=' + app_access_token
print "Get Recent Media Url: " + get_self_media
recent_media = requests.get(get_self_media).json()
if recent_media['meta']['code'] == 200:
    if len(recent_media['data']):
        image_name = recent_media['data'][0]['id'] + '.jpeg'
image_url = recent_media['data'][0]['images']['standard_resolution']['url']
urllib.urlretrieve(image_url, image_name)
print 'Your image has been downloaded!'
return recent_media['data'][0]['id']
else:
    print "There is no recent post!"
return None
else:
    print 'Status code other than 200 received!'



def like_a_post(insta_username):



media_id = get_user_post(insta_username)

like_url = base_url + 'media/' + media_id + '/likes'
payload = {"access_token": app_access_token}
print 'Like Post URL: ' + like_url

post_a_like = requests.post(like_url, payload).json()
if post_a_like['meta']['code'] == 200:
    print 'Like on post Successfully  .'
else:
    print 'Your like was unsuccessful. Try again!!!'
def post_a_comment(insta_username):
media_id = get_user_post(insta_username)
comment_text = raw_input("\nEnter Your Comment Here: \t")

comment_text = comment_text.capitalize()

if len(comment_text) < 300:
payload = {"access_token": app_access_token, "text": comment_text}
comment_url = (base_url + 'media/%s/comments') % media_id
print 'Posting Comment to URL : %s' % comment_url

make_comment = requests.post(comment_url, payload).json()

if make_comment['meta']['code'] == 200:
    print "\n\tSuccessfully Post a new comment! -_-.\n\n\n"
else:
    print "\n\tUnable to add comment. Try again!\n\n\n"
else:
print "\n\tPlease Enter only Text 300 Alphabet's\n\n\n"


def delete_negative_comment(insta_username):


media_id = get_user_post(insta_username)
delete_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
print 'Delete Comment url : %s' % delete_url
delete_comment_info = requests.get(delete_url).json()
print delete_comment_info

if delete_comment_info['meta']['code'] == 200:
    if len(delete_comment_info['data']):

pass
else:
print 'There are no existing comments on the post!'
else:
print 'Status code other than 200 received!'


def start_bot():
    while True:
        print '\nYou Can Perform Following Task By Using This App on Your Instagram Data.'


print "\t1.Get your own details."
print "\t2.Get details of a user by username."
print "\t3.Get your own recent post."
print "\t4.Get the recent post of a user by username."
print "\t5.Get a list of people who have liked the recent post of a user."
print "\t6.Like the recent post of a user."
print "\t7.Get a list of comments on the recent post of a user."
print "\t8.Make a comment on the recent post of a user."
print "\t9.Delete negative comments from the recent post of a user."
print "\t10.Exit"

choice = raw_input("Enter you choice of Task To Do: ")


if choice == "1":
    owner_info()


elif choice == "2":
user = "\nif You Want to Search Specific user Details Please Enter User name: \t"
username = raw_input(user)

user_details(username)


elif choice == "3":
get_own_post()


elif choice == "4":

user = "\nif You Want to Get any Specific User Recent Post Please Enter User name :\t"
username = raw_input(user)

get_user_post(username)


elif choice == "6":

user = "\nif You Want to Like any Specific User Recent Post Please Enter User name :\t"
username = raw_input(user)

like_a_post(username)


elif choice == "8":

user = "\nif You Want to Comment any Specific User Recent Post Please Enter User name :\t"
username = raw_input(user)
post_a_comment(username)


elif choice == "9":
user = "\nif You Want to Comment any Specific User Recent Post Please Enter User name :\t"
username = raw_input(user)
delete_negative_comment(username)


elif choice == "10":
exit()


else:
print "\n\t\t!!! Please Select a Valid Option from above \n\n\n"


print '\nWelcome to Smart-Insta-Bot\n'
question = 'want to continue with the default user : "________________________________________________________" (Y/N): \t'

token_option = raw_input(question)
if token_option.upper() == "Y":

app_access_token = '___________________________________________________'

start_bot()
elif token_option.upper() == "N":
app_access_token = raw_input("Please Enter Instagram Access Token :\t")

if len(app_access_token) > 10:

start_bot()
else:
print "\n!!! Access Token Not Valid. !!! \nPlease Enter a Valid Access Token and Try Again."

else:
print "please select only (y/n) and try again."