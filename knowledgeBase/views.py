from django.shortcuts import render_to_response
from knowledgeBase.models import Memo, Article, Faq, Library



def index(request):
    latest_faq_list = Faq.objects.all().order_by('-created')[:5]
    latest_memo_list = Memo.objects.all().order_by('-created')[:5]
    latest_article_list = Article.objects.all().order_by('-created')[:5]
    latest_library_list = Library.objects.all().order_by('-created')[:5]
    return render_to_response('knowledgeBase/index.html', {'latest_faq_list': latest_faq_list, 'latest_memo_list': latest_memo_list, 'latest_article_list': latest_article_list, 'latest_library_list': latest_library_list})
