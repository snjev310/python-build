class Dog:
	name = 'Pluto'

	def __init__(self):
		self.nickname = 'Venus'

	def __len__(self):
		return(len(self.nickname))

B = Dog()
print(B.name, B.nickname)
C = Dog()
Dog.name = 'Changed'
C.nickname = 'Also changed'
print(B, B.name, B.nickname)
print(C, C.name, C.nickname)

print(len(B))