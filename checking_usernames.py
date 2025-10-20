current_users = ['billy', 'admin', 'sarah', 'bob', 'jonathan']
current_users_title = ['Billy', 'Admin', 'Sarah', 'Bob', 'Jonathan']
new_users = ['Sarah', 'mike', 'jonathan', 'alice', 'david']

for new_user in new_users:
    if new_user in current_users or new_user in current_users_title:
        print(f"Sorry {new_user}, that username is already taken. Please choose a different username.")
    else:
        print(f"Congratulations {new_user}, that username is available!")