from django.utils.deprecation import MiddlewareMixin
from qa.models import Session
from datetime import datetime
from django.utils import timezone
import pytz
import pudb

class CheckSessionMiddleware(MiddlewareMixin):
	def process_request(self, request):
		#pudb.set_trace()
		try:
			sessid = request.COOKIES.get('sessid')
			session = Session.objects.get(
				session_key=sessid,
				expire_date__gt = timezone.now(),
				)
			request.session = session
			request.user = session.user
		except Session.DoesNotExist:
			request.session = None
			request.user = None
