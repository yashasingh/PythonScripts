import os

closelist = ["sudo service apache2 stop"]
for i in closelist:
	os.system(i)
	