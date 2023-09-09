from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio, WorkExperience


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Work Experience - 
@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'job_title', 'start_date', 'end_date')
    readonly_fields = ('formatted_description',)  # Add this line

    def formatted_description(self, obj):
        # Convert the description text to a bullet list
        description_list = obj.description.split('\n')
        formatted_description = '<ul>'
        for item in description_list:
            if item.strip():  # Check if the item is not empty
                formatted_description += f'<li>{item}</li>'
        formatted_description += '</ul>'
        return formatted_description

    formatted_description.allow_tags = True
    formatted_description.short_description = 'Description (Formatted)'

    
# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)