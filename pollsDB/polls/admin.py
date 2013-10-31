from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question'] # reorders default field ordering
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date Information', {'fields': ['pub_date'], 'classes' : ['collapse']}),
	] # groups fields into fieldsets
	inlines = [ChoiceInLine]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)