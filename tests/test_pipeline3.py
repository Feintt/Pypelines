from pypelines import Pipeable

blog_post = {
    "title": "the future of web development",
    "summary": "This post explores emerging trends in web development, including new frameworks, APIs, and tools that are shaping the future.",
    "body": "Web development is evolving rapidly.\nNew frameworks like React, Vue, and Angular offer powerful tools for building interactive applications.\nAPIs are becoming more important than ever, allowing for more dynamic content and functionality."
}


# Define additional custom transformations needed
def ensure_keyword(value, keyword):
    if keyword.lower() not in value.lower():
        return f"{value}. {keyword}."
    return value


def body_to_html(value):
    paragraphs = value.split('\n')
    return ''.join(f"<p>{para}</p>" for para in paragraphs if para.strip())


def to_upper(data, key):
    data[key] = data[key].upper()
    return data


# Transformation pipeline
result = Pipeable(blog_post) | (to_upper, "title")

# Since the pipeline is designed to work with single values, you may need to adjust the implementation
# to handle dictionary transformations or adapt the example to fit your pipeline design.

# Output the transformed blog post
print(blog_post)
