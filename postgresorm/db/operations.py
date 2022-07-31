from peewee import fn

from postgresorm.utils import time_counter, BadFetch


@time_counter
def get_posts(model):
    return model.select().order_by(model.id).tuples()


def get_latest_post_id(model):
    return model.select(fn.MAX(model.id)).scalar()


def count_rows(model):
    return model.select().count()


def insert_post(model, post):
    model.insert(name=post.name, author=post.author, description=post.description, created_at=post.created_at, likes=post.likes).execute()


def add_like_to_the_latest_post(model, thread_num: int, call_num: int):
    post_id = model.select().order_by(model.id.desc()).limit(1).for_update().get_or_none()
    if post_id is None:
        raise BadFetch(thread_num, call_num)
    model.update({model.likes: model.likes + 1}).where(model.id == post_id).execute()


def clear_posts_table(model):
    model.delete().execute()
