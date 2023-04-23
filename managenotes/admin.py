from django.contrib import admin



class ClassAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view for the Class model
    list_display = ('_class_name', 'name_word', 'is_hidden')

    # Define the available actions for the Class model
    actions = ['hide_classes', 'unhide_subjects']

    # Define the filters to display in the sidebar for the Class model
    list_filter = ('is_hidden',)

    # Define the action to hide selected classes
    def hide_classes(self, request, queryset):
        queryset.update(is_hidden=True)
        self.message_user(request, f"{queryset.count()} classes were successfully hidden.")
    hide_classes.short_description = "Hide selected classes"

    # Define a custom action to unhide selected subjects
    def unhide_subjects(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_subjects.short_description = "Unhide selected subjects"

    # Add the unhide_subjects action to the list of actions
    actions = [hide_classes,unhide_subjects]


class SubjectAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view for the Subject model
    list_display = ('_subject_name', 'class_field', 'is_hidden')

    # Define the available actions for the Subject model
    actions = ['hide_subjects', 'unhide_subjects']

    # Define the filters to display in the sidebar for the Subject model
    list_filter = ('class_field', 'is_hidden')

    # Define the default ordering for the Notes model
    ordering = ('class_field','is_hidden')

    # Define the action to hide selected subjects
    def hide_subjects(self, request, queryset):
        queryset.update(is_hidden=True)
        self.message_user(request, f"{queryset.count()} subjects were successfully hidden.")
    hide_subjects.short_description = "Hide selected subjects"

    # Define a custom action to unhide selected subjects
    def unhide_subjects(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide_subjects.short_description = "Unhide selected subjects"



class NotesAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view for the Notes model
    list_display = ('_chapter_name', 'subject', 'class_name', 'is_hidden')

    # Define the available actions for the Notes model
    actions = ['hide_notes', 'unhide_notes']

    # Define the filters to display in the sidebar for the Notes model
    list_filter = ('subject__class_field', 'subject', 'is_hidden')

    # Define the default ordering for the Notes model
    ordering = ('subject__class_field__name_computing', 'subject', 'chapter_number')

    # Define the method to get the class name for each note
    def class_name(self, obj):
        return obj.subject.class_field.name
    class_name.admin_order_field = 'subject__class_field__name_computing'  # Set the admin order field

    # Define the method to hide selected notes
    def hide_notes(self, request, queryset):
        queryset.update(is_hidden=True)
        self.message_user(request, f"{queryset.count()} notes were successfully hidden.")
    hide_notes.short_description = "Hide selected notes"

    # Define a custom action to unhide selected notes
    def unhide_notes(self, request, queryset):
        queryset.update(is_hidden=False)
        self.message_user(request, f"{queryset.count()} notes were successfully unhidden.")
    unhide_notes.short_description = "Unhide selected notes"


# Register models
from .models import *

admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Notes, NotesAdmin)