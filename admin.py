from django.contrib import admin
# Make sure to import the 7 required classes here
from .models import Course, Lesson, Question, Choice, Submission

# 1. Choice Inline within the Question admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

# 2. Question Inline within the Lesson admin page
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

# 3. Question Admin layout
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson', 'grade']

# 4. Lesson Admin layout
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# Registering models to the admin site
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)
# (Ensure Course is registered as well if required)
