from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # detail page
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # listing / grid
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # filter on listing page
    list_filter = ['pub_date']
    # search bar
    search_fields = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)