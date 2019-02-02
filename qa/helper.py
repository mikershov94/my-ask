from django.contrib.auth.models import User
from qa.models import Session
from datetime import datetime, timedelta
from django.utils import timezone
import random

import pudb

def do_login(login, password):
	pudb.set_trace()
	try:
		user = User.objects.get(username=login)
	except User.DoesNotExist:
		return None

	if user.password != password:
		return None

	session = Session()
	session.session_key = random.randint(1 , 1687953)
	session.user = user
	session.expire_date = timezone.now()+timedelta(days=5)
	session.save()

	return session.session_key
