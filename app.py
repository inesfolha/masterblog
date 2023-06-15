from flask import Flask, render_template, request, redirect, url_for
import uuid
from masterblog.static import file_handler

app = Flask(__name__)


def id_generator():
    """Generates a unique ID using UUID."""
    return str(uuid.uuid4())


@app.route('/')
def index():
    """Renders the index.html template with blog posts."""
    blog_posts = file_handler.load_file('blog_posts.json')
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handles the addition of a new blog post.

    If the request method is POST, processes the form data and adds a new post to the 'blog_posts.json' file.
    After adding the post, redirects to the index page
    If the request method is GET, renders the add.html template.
    """
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        blog_posts = file_handler.load_file('blog_posts.json')
        post_id = id_generator()
        new_post = {
            'id': post_id,
            'author': author,
            'title': title,
            'content': content,
            'likes': 0
        }
        blog_posts.append(new_post)

        file_handler.save_file('blog_posts.json', blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<string:post_id>', methods=['GET', 'POST'])
def delete(post_id):
    """
    Handles the deletion of a blog post.

    If the request method is POST, deletes the post with the given post_id from the 'blog_posts.json' file.
    After deleting the post, redirects to the index page.
    """
    blog_posts = file_handler.load_file('blog_posts.json')
    post_to_delete = None
    for post in blog_posts:
        if post['id'] == post_id:
            post_to_delete = post
            break

    if post_to_delete:
        blog_posts.remove(post_to_delete)
        file_handler.save_file('blog_posts.json', blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handles the updating of a blog post.

    If the request method is POST, update the post with the given post_id in the 'blog_posts.json' file.
    After updating the post, redirects to the index page
    If the request method is GET, renders the update.html template with the post details.
    """
    blog_posts = file_handler.load_file('blog_posts.json')
    post_to_update = None
    for post in blog_posts:
        if post['id'] == post_id:
            post_to_update = post
            break
    if post_to_update is None:
        return "Post not found", 404

    if request.method == 'POST':
        updated_author = request.form['author']
        updated_title = request.form['title']
        updated_content = request.form['content']

        post_to_update['author'] = updated_author
        post_to_update['title'] = updated_title
        post_to_update['content'] = updated_content

        file_handler.save_file('blog_posts.json', blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post_to_update)


@app.route('/like/<string:post_id>', methods=['POST'])
def like(post_id):
    """
    Handles the increment of likes for a blog post.

    Increments the 'likes' count for the post with the given post_id in the 'blog_posts.json' file.
    Redirects to the index page after incrementing the likes count.
    """
    blog_posts = file_handler.load_file('blog_posts.json')
    for post in blog_posts:
        if post['id'] == post_id:
            if 'likes' in post:
                post['likes'] += 1
            else:
                post['likes'] = 1
            break
    file_handler.save_file('blog_posts.json', blog_posts)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    """Renders the 404.html template """
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
