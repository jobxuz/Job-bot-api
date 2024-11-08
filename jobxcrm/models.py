from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Company(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")

    def __str__(self):
        return self.name

class MenuButton(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="menu_buttons")
    description = models.TextField()

    def __str__(self):
        return self.name

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/companyimg', null=True, blank=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_infos", null=True, blank=True)
    button = models.ForeignKey(MenuButton, on_delete=models.CASCADE, related_name="company_infos", null=True, blank=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="branches", null=True, blank=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/companyimg', null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies", null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="vacancies")

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField()
    queue = models.IntegerField(null=True, blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="questions")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="questions", null=True, blank=True)

    def __str__(self):
        return self.question
