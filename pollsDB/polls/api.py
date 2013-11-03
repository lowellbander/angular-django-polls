from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from polls.models import Poll, Option
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization = Authorization()

class PollResource(ModelResource):
	class Meta:
		queryset = Poll.objects.all()
		authorization = Authorization()

class OptionResource(ModelResource):
	poll = fields.ForeignKey(PollResource, 'poll')
	class Meta:
		queryset = Option.objects.all()
		authorization = Authorization()

# vote resource (and of course first a choice model)