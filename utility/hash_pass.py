import hashlib


def hash_pwd(str):
    salt = b'jiFNCqikRSnqstPS7wso'
    md5 = hashlib.md5(salt)
    md5.update(str.encode('utf-8'))
    password = md5.hexdigest()
    return password