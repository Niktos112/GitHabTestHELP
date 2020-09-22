def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit() or (password.isalpha() and
                                (password.islower() or password.isupper())):
        return 'Ненадежный пароль'
    elif (password.isalpha() and not password.islower()
          and not password.isupper()) or\
         (password.isalnum() and (password.isupper() or password.islower())):
        return 'Слабый пароль'
    elif password.isalnum() and not \
            password.islower() and not password.isupper():
        return 'Надежный пароль'
print(password_level(input()))
