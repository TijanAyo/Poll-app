from django.contrib import admin

from .models import Question, Choice

# Changes to the Site_Header, Site_Title, and Index title
admin.site.site_header = 'PollMaker'
admin.site.site_title = 'PollMaker Admin'
admin.site.index_title = 'Welcome to PollMaker'

"""admin.site.register(Question)
admin.site.register(Choice)"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3   # incase you want to add more choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes':
                ['Collapse']})]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin) # Registering the site on the admin page