import hashlib

def md5_encryption(content):
    a = hashlib.md5()
    a.update(content.encode(encoding='utf-8'))
    return a.hexdigest()




# print(md5_encryption('123456'))
