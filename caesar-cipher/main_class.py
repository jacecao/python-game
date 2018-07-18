# 凯撒密码
# 通过类来实现

class CaesarCipher (object):
	def __init__(self):
		self.__MAX_KEY_SIZE = 26
		self.init()

	def getMode(self):
		while True:
			print()
			print('Do you wish to encrypt or decrypt a message?')
			mode = input().lower()

			if mode in 'encrypt e decrypt d'.split():
				return mode
			else:
				print('!!!!!!')
				print('Enter either "encrypt e" or "decrypt d".')

	def getMessage(self):
		print()
		print('Enter your message:')
		return input()

	def getKey(self):
		key = 0
		while True:
			print('Enter the key number (1 - %s)' % self.__MAX_KEY_SIZE)
			key = int(input())
			if (key >= 1 and key <= self.__MAX_KEY_SIZE):
				return key

	def getTanslateMessage(self, mode, message, key):
		if mode[0] == 'd':
			key = -key

		translated = ''

		for symbol in message:
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

	def init(self):
		mode = self.getMode()
		message = self.getMessage()
		key = self.getKey()

		print('Your translated text is :')
		print(self.getTanslateMessage(mode, message, key))											

CaesarCipher()		