import hashlib
passwd=input('enter passwd:')
p=hashlib.new('md4').hexdigest()
print(p)
