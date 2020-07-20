def get_string_list_of_formatted_tags(list_of_blog_posts):
    """
    Given a list of blog posts, get the string values of all tags and
    returns them as a list.

    By default you will get a list of lists.
    """
    tag_list_raw = []
    tag_list = []

    try:
        for post in list_of_blog_posts:
            tag_list_raw.append(post.tags.split(','))
    except:
        tag_list_raw.append(list_of_blog_posts.tags.split(','))
    
    for tag in tag_list_raw:
        for i in tag:
            if i.strip() not in tag_list:
                tag_list.append(i.strip())
    
    
    return sorted(tag_list)
