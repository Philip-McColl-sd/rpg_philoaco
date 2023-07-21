import json

# manages log in for user
def logger(db):
    # keeps or stop the main 'log_in cicle'
    flag = True
    #  main 'log_in cicle'
    while flag:
        user = str(input('Enter your username: '))
        password = str(input('Enter your password: '))
        # checks if the username exists in the players db
        if user not in db.keys():
            print()
            sing = input('User not found. Would you like to create a new account (Y/N): ')
            if sing in ['y', 'Y', 'yes', 'Yes']:
                sign_in(db)
                flag = False
            else:
                pass
        # check if the password is correct for the given username
        else:
            if db[user]['password']==password:
                # stops the main log_in cicle if the password is correct
                flag = False
    print('welcome to the game')
    return user, password

# manages sign in for user
def sign_in(db):
    flag = True
    while flag  == True:
        user = str(input('Enter your username: '))
        if user not in db:
            password = str(input('Enter password: '))
            db[user] = {}
            db[user]['password'] = password
            db[user]['HP']=100
            db[user]['xy']=[0,0]
            db[user]['inventory']={}
            db[user]['wardrobe']={'Head': '', 'Shoulder': '', 'Core': '', 'Greaves': '', 'Boots': '', 'Weapon': ''}
            flag = False
        else:
            print('Username already exists')
    

# opens the json database
def open_json_file(file_path, mode) -> dict:
    with open(file_path, mode) as file:
        data = json.load(file)
    return data

def save_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
