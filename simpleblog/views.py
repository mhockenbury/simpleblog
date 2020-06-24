from django.http import HttpResponse
import datetime
import random
import json
import os
from django.template import loader
from simpleblog.models import Comment, CommentForm
from simpleblog.utils import get_by_uuid, get_by_slug, has_tag_value

module_dir = os.path.dirname(__file__)

with open((module_dir + '/static/data/content_api.json')) as json_data:
    content_data = json.load(json_data)

with open((module_dir + '/static/data/quotes_api.json')) as json_data:
    quote_data = json.load(json_data)

def article(request, uuid):
    template = loader.get_template('simpleblog/article.html')
    article_content = get_by_uuid(content_data["results"], uuid)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)

            if not comment.author:
                comment.author = "Internet Stranger"
            comment.article_uuid = uuid
            comment.created_at = datetime.datetime.utcnow()
            comment.save()

    # TODO: return 404 if no matching article id
    # TODO: style comments html
    context = {
        "article_content": article_content,
        "quote_content": random.sample(quote_data, 3),
        "form": form,
        "comments": Comment.objects.filter(article_uuid=uuid),
        "title": article_content["headline"],
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('simpleblog/home.html')
    context = {
        "top_article": get_by_slug(content_data["results"], "10-promise"),
        "title": "This is home",
        "content": random.sample(content_data["results"], 3),
    }
    return HttpResponse(template.render(context, request))
