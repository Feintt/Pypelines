from pypelines import Pipeable
from datetime import datetime

blog_post = {
    "title": "the future of web development",
    "summary": "This post explores emerging trends in web development, including new frameworks, APIs, and tools that are shaping the future.",
    "body": "Web development is evolving rapidly.\nNew frameworks like React, Vue, and Angular offer powerful tools for building interactive applications.\nAPIs are becoming more important than ever, allowing for more dynamic content and functionality."
}


def to_upper(data, key):
    data[key] = data[key].upper()
    return data


def add_start_date(data):
    return "change", {"start_date": datetime.now()}


# Transformation pipeline
result = Pipeable(blog_post) | (to_upper, "title") | add_start_date | print

# Output the transformed blog post
# print(result.get_changeset())
