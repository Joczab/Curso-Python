user = {
    'username':'username 1',
    'status': False
}

print(user.items())

#new_user = {key : value for (key, value) in user.items()}
new_user = {key : 'CAmbio de nombre' if value == 'username 1' else value for (key, value) in user.items()}

print(new_user)

