from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL
from django.contrib.auth.models import User
from polls.models import Poll, Option
from tastypie import fields


# see if we can pass in args (for example, so that we can get the choice set for poll 1)

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
		filtering = {
			'poll' : ALL,
		}

# vote resource (and of course first a choice model)