from django.contrib import admin
from .models import Company,MenuButton,CompanyInfo,Branch, Vacancy, Question

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(MenuButton)
admin.site.register(CompanyInfo)
admin.site.register(Branch)
admin.site.register(Vacancy)
admin.site.register(Question)

