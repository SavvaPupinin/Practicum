from flask import Flask, request
import pickle
from hashlib import sha256
from datetime import datetime
import re
import random
import string



def hasher(password, salt = None):
	if salt == None:
		letters_and_digits = string.ascii_letters + string.digits
		salt = ''.join(random.sample(letters_and_digits, 16))
		salt = salt.encode('utf-8')

	password = sha256((password).encode('utf-8')+salt).hexdigest()
	return salt,password




def response(result, more = ''):
	return {"result":result, "more":more}

def email_validator(email):
	dmp = loader()
	return not bool(dmp.get(email))


def check_user(req_from):
	dmp = loader()
	email = req_from["email"]
	password = req_from["password"]
	curr_pass = dmp.get(email)
	if not curr_pass:
		return response(False,"Нет такого пользователя")
	curr_pass = curr_pass["password"]
	checked = hasher(password, curr_pass[0])
	if curr_pass == checked:
		return response(True, "Успешно авторизовались")
	else:
		return response(False, "another password", "Invalid password")


def saver(dmp):
	with open(DUMP, "wb") as picklefile:
		pickle.dump(dmp, picklefile)


def saveInfo(req_from):
	dmp = loader()
	password = req_from["password"]
	if not re.search("^(\w|\d|\_){8,}$", password):
		return False
	email = req_from["email"]
	date = datetime.now().strftime("%H:%M:%S, %d.%m.%Y")
	password = hasher(password)
	dmp[email] = {"password": password, "date": date, }
	saver(dmp)
	return True

def loader():
	try:
		with open(DUMP, "rb") as picklefile:
			loaded = pickle.load(picklefile)
		return loaded
	except:
		return {}	


app = Flask(__name__)
DUMP = "dump.pickle"


@app.route('/user/login', methods=['POST'])
def auth():
	req_from = request.get_json()
	return check_user(req_from)


@app.route('/user/register', methods=['POST'])
def reg():
	req_from = request.get_json()
	dmp = loader()
	if not bool(dmp.get(req_from["email"])):
		if saveInfo(req_from):
			return response(True, "зарегистрирован")
		else:
			return response(False,"Буквы цифры и _ разрешены в пароле" )
	else:
		return response(False,"Такой пользователь уже существует")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)







