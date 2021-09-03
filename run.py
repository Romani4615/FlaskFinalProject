from app import app, db
from app.models import User, Post


# // good to have to not have to repeat in shell
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }