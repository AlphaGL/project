from django.contrib import admin
from .models import Student, Position, Contestant, Vote

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('reg_number', 'full_name')  # Display these fields in the list view
    search_fields = ('reg_number', 'full_name')  # Enable search by these fields
    ordering = ('reg_number',)  # Default ordering by registration number

    # Remove filter_horizontal, list_filter, and fieldsets if they're not applicable
    filter_horizontal = ()  # No fields for horizontal filters
    list_filter = ()  # No fields for list filtering
    fieldsets = ()  # No custom fieldsets

admin.site.register(Student, StudentAdmin)
admin.site.register(Position)
admin.site.register(Contestant)
admin.site.register(Vote)