from knowledgeBase.models import Memo, Tag, Jurisdiction, Article, Faq, Library
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Faq)
admin.site.register(Jurisdiction)
admin.site.register(Library)
admin.site.register(Memo)
admin.site.register(Tag)
