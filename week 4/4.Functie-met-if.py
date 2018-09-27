oldpassword = '12345677'
newpassword = '12345677asdf'

def passwordcheck(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        return True
    else:
        return False

print(passwordcheck(oldpassword,newpassword))