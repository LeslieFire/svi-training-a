import requests
from pprint import pprint

#URL = 'https://api.github.com/search/users?q=language:java+go+location:&per_page=100&access_token=55d6e563dc7008aee8cc4f6d585754e5a145442'
URL = 'https://api.github.com/search/users'
payload = {'q':'language:go location:francisco',
           'sort':'followers',
           'type':'user',
           'order':'desc',
           'per_page':'100',
           'access_token':'secret'
           }

r = requests.get(URL,params=payload)
#print r.url
users_dict = r.json()

#print users_dict
#raw_input('...')
users_list = users_dict['items']

login_names = []

for user in users_list:
    login_names.append(user['login'])

generic_user_url = 'https://api.github.com/users/'
dev_urls = []

for i in login_names:
    user_url = str(generic_user_url) + str(i) + '?' + 'access_token=' + access_token
    dev_urls.append(user_url)


final_list = []

for i in dev_urls:
    user_dict = {}
    r = requests.get(i)
    user_dict_raw = r.json()

    user_dict['login'] = user_dict_raw.get('login')
    user_dict['name'] = user_dict_raw.get('name')
    user_dict['company'] = user_dict_raw.get('company')
    user_dict['blog'] = user_dict_raw.get('blog')
    user_dict['location'] = user_dict_raw.get('location')
    user_dict['email'] = user_dict_raw.get('email')
    user_dict['public_repos'] = user_dict_raw.get('public_repos')
    user_dict['followers'] = user_dict_raw.get('followers')

    final_list.append(user_dict)

final_dict = {}
final_dict['top go users'] = final_list

pprint(final_dict)
