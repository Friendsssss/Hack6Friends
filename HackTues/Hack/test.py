#coding: utf-8
tt = open("test2.txt", "r")
txt = tt.read()

z = txt.find(". .")
print("last", z)
word = "19"
a = txt.find(word)
print("word", a)
b = txt.find(".", 0, txt.find(word))
for b1 in range(0, z):
	b1 = txt.find(".", b1, txt.find(word))
	if b1>-1:
		b = b1
print("start", b)
c = txt.find(". ", a+1, z+2)
print("end", c)

f = open("./Hack/static/texts/test.txt", "w")

for i in range(b+2, c+1):
	f.write(txt[i])
f.close()
f = open("./Hack/static/texts/test.txt", "r")
print(f.read())
f.close()

