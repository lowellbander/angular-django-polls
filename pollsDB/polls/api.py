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
			'id' : ALL,
			'option_text' : ALL,
			'poll' : ALL,
			'resource_uri' : ALL,
			'votes' : ALL,
		}
	# def get_object_list(self, request):
	# 	return super(OptionResource, self).get_object_list(request).filter(id__in=1,2,3)
		# return super(OptionResource, self).get_object_list(request).filter(myid=request.id)
		# return super(OptionResource, self).get_object_list(request)


# That should work like this: in get_object_list, go to the request and get the parameter you want from there: user_id = int(request.GET.get('user')). Then just load that user from the database as user = User.objects.get(pk=user_id) and then do everything as shown above.


# vote resource (and of course first a choice model)

# def get_object_list(self, request):
        # return super(MyResource, self).get_object_list(request).filter(start_date__gte=now)



# class PostResource(ModelResource):
#     class Meta:
#         queryset = Post.objects.all()

#     def get_object_list(self, request):
#         this_users_posts = super(PostResource, self).get_object_list(request).filter(user=User.objects.get(user=request.user))
#         all_the_posts_this_user_follows = super(PostResource, self).get_object_list(request).filter(follower=User.objects.get(user=request.user))

#         return this_users_posts | all_the_posts_this_user_follows


