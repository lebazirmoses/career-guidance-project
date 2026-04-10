from django.contrib import admin
from .models import Test, Question, UserTestAttempt, UserAnswer

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'test_type', 'is_mandatory')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'test', 'difficulty', 'order')
    list_filter = ('test', 'difficulty')

@admin.register(UserTestAttempt)
class UserTestAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'status', 'completed_at')
    readonly_fields = ('started_at', 'completed_at')

admin.site.register(UserAnswer)