from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from polls.models import Poll, Choice

class PollResource(ModelResource):
	class Meta:
		queryset = Poll.objects.all()
		authorization= Authorization()

class ChoiceResource(ModelResource):
	class Meta:
		queryset = Choice.objects.all()
		authorization= Authorization()