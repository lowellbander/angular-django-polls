from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from polls.models import Poll, Option
from tastypie import fields

class PollResource(ModelResource):
	# one to many!!!!!
	# choices = Poll. 
	class Meta:
		queryset = Poll.objects.all()
		authorization = Authorization()

class OptionResource(ModelResource):
	poll = fields.ForeignKey(PollResource, 'poll')
	class Meta:
		queryset = Option.objects.all()
		authorization = Authorization()