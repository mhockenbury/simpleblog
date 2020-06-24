from django.http import HttpResponse
import datetime
import random
import json
import os
from django.template import loader
from simpleblog.models import Comment, CommentForm

module_dir = os.path.dirname(__file__)

with open((module_dir + '/static/data/content_api.json')) as json_data:
    content_data = json.load(json_data)

with open((module_dir + '/static/data/quotes_api.json')) as json_data:
    quote_data = json.load(json_data)

def get_by_uuid(article_list, uuid):
    return next(article for article in article_list if article['uuid'] == uuid)

def get_by_slug(article_list, slug_value):
    return next(article for article in article_list if has_tag_value(article['tags'], "slug", slug_value))

def has_tag_value(tag_list, target_key, target_value):
    for tag in tag_list:
        if tag[target_key] == target_value:
            return True
    return False

def article(request, uuid):
    template = loader.get_template('simpleblog/article.html')
    article_content = get_by_uuid(content_data["results"], uuid)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # TODO: make author optional; assign as Anonymous
            comment = form.save(commit=False)
            comment.article_uuid = uuid
            comment.created_at = datetime.datetime.now() # UTC time?
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
