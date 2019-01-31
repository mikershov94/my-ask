from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import random

def do_login(login, password):
	try:
		user = User.objects.get(username=login)
	except User.DoesNotExist:
		return None

	if user.password != password:
		return None

	session = Session()
	session.key = random.randint()
	session.expires = datetime.now()+timedelta(days=5)
	session.save()

	return session.key
