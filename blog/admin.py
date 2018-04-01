from django.contrib import admin

# Register your models here.
from blog.models import project, skill, article, education,work,product

admin.site.register(project)
admin.site.register(skill)
admin.site.register(education)
admin.site.register(article)
admin.site.register(work)
admin.site.register(product)