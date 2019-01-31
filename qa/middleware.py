from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session

class CheckSessionMiddleware(MiddlewareMixin):
	def process_request(request):
		try:
			sessid = request.COOKIE.get('sessid')
			session = Session.objects.get(
				sessid=sessid,
				expires__gt = datetime.now(),
				)
			request.session = session
		except Session.DoesNotExist:
			request.session = None
