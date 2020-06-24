def get_by_uuid(article_list, uuid):
    return next(article for article in article_list if article['uuid'] == uuid)

def get_by_slug(article_list, slug_value):
    return next(article for article in article_list if has_tag_value(article['tags'], "slug", slug_value))

def has_tag_value(tag_list, target_key, target_value):
    for tag in tag_list:
        if tag[target_key] == target_value:
            return True
    return False
