# caesar-cipher
# 凯撒密码示例
#

MAX_KEY_SIZE = 26

def getMode():
	while True:
		print()
		print('Do you wish to encrypt or decrypt a message?')
		mode = input().lower()

		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
			print('!!!!!')
			print('Enter either "encrypt e" or "decrypt d".')

def getMessage():
	print()
	print('Enter you message:')
	return input()

def getKey():
	key = 0
	while True:
		print('Enter the key number (1 - %s)' % MAX_KEY_SIZE)
		key = int(input())	
		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key

def getTanslateMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	
	for symbol in message:
		# 检查字符串是否为字符组成
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)						 	
		else:
			translated += symbol

	return translated
	
def init():
	mode = getMode()
	message = getMessage()
	key = getKey()

	print('Your tanslated text is:')
	print(getTanslateMessage(mode, message, key))

init()				
