

class Urls:

	def func(self):
		return 1 + 1

f = Urls()

dic = {
	"1": f.func(),
	"2": "Seconde"
}

for x in dic:
	a = dic[x]
	print(a)

