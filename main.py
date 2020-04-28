class InvalidPassword(Exception):
    pass

def check(password):
    characters = list(password)
    nnum = 0
    try:
        if len(characters) >= 7:
            pass
        else:
            raise InvalidPassword('Invalid Password')
            
        for item in characters:
            try:
                int(item)
                nnum += 1
            except:
                continue
                
        if nnum >= 2:
            pass
        else:
            raise InvalidPassword('Invalid Password')

        special = 0
        for item in characters:
            if item in ['!', '@', '#', '$', '%', '&', '*']:
                special += 1
                    
        if special >= 2:
            return 'Strong'
        else:
            raise InvalidPassword('Invalid Password')
    except:
        return 'Weak'

print(check(input()))
