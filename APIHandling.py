import requests
#  Get Rendom User
def fetch_API():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =  requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
       user_data = data['data']
       street_number = user_data['location']['street']['number']
       phone_number = user_data['phone']
       cell = user_data['cell']
       username = user_data['login']['username']
       email =  user_data['email']
       country = user_data['location']['country']
       return username , email , country , cell , street_number, phone_number
    else:
        raise Exception('Fail to fetch User data ') 
    
def main():
        try:
            username , email , country , cell , street_number , phone_number = fetch_API()
            print(f"Username : {username}\n Email : {email} \n Phone Number : {phone_number} \n Street Number : {street_number} ")
        except Exception as e:
            print(e)

if __name__ == '__main__':
     main()

# fetch_API()
# Random Jocks ++++++++++++++++++++++++++++++
import random
def Jock_api():
    url = "https://api.freeapi.app/api/v1/public/randomjokes" 
    response = requests.get(url)
    data = response.json()
    if data['success'] and 'data' in data:
        jock = data['data']['data']
        random_index = random.choice(jock)['content']
        return random_index
    else:
        raise Exception('Fail to fetch API')
   
def main_one():
    try:
        random_index = Jock_api()
        print(f"Random Jock :: {random_index}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main_one()
