import hashlib
import os

def md5(text):
	return hashlib.md5(text.encode()).hexdigest()

hugo = md5('hugo')

def enc(pwd):
	return md5(md5(pwd) +hugo)[8:24]

def trypwd(tar):
	for i in range(0,1000000):
		pwd = f'{i:06}'
		if enc(pwd) == tar:
			return pwd
	return None

def main():
	print('计算还原密码请用记事本打开 C:\\ProgramData\\Seewo\\SeewoCore\\SeewoCore.ini 并记录 PASSWORDV2 的值\n计算锁屏密码请用记事本打开 C:\\Users\\当前用户名\\AppData\\Seewo\\SeewoAbility\\SeewoLockConfig.ini 并记录 LockPasswardV2 的值')
	tar = input('请输入值：')
	print('正在计算...')
	ans = trypwd(tar)
	if ans is None:
		print('失败：密码不是六位数字')
	else:
		print('密码是：' + ans)
	os.system( 'pause ')

if __name__ == '__main__':
	main()
