import os
from log_sign_in import logger, open_json_file, save_to_json_file

def main():
    # Opens
    db = open_json_file('db.json', 'r')
    user, password = logger(db)
    save_to_json_file(db, 'db.json')
    player_db = db[user]



if __name__ ==  "__main__":
    main()