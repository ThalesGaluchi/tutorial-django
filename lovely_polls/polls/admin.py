from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_data', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ("Date information", {
            'fields':['pub_data'],
            'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = [
        'question_text', 'pub_data', 'was_published_recently'
    ]
    list_filter = ['pub_data']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
