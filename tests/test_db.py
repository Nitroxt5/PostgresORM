from datetime import date
from pytest import raises

import tests.models as models
from postgresorm.db.operations import add_like_to_the_latest_post, insert_post, clear_posts_table, get_latest_post_id, count_rows, get_posts
from postgresorm.post.post import Post
from postgresorm.utils import BadFetch


def test_insert_post():
    insert_post(models.Post, Post("adv", "vadv", "ffbsd", date(2000, 5, 30), 100))
    insert_post(models.Post, Post("dfb", "adsda", "bfdg", date(2012, 4, 12), 50))

    rows = count_rows(models.Post)
    clear_posts_table(models.Post)

    assert rows == 2


def test_add_like_to_the_latest_post():
    insert_post(models.Post, Post("adv", "vadv", "ffbsd", date(2000, 5, 30), 100))
    insert_post(models.Post, Post("dfb", "adsda", "bfdg", date(2012, 4, 12), 50))

    add_like_to_the_latest_post(models.Post, 0, 0)
    post_id = get_latest_post_id(models.Post)
    print(post_id)
    print(*get_posts(models.Post))
    likes = models.Post.select(models.Post.likes).where(models.Post.id == post_id).scalar()
    clear_posts_table(models.Post)

    assert likes == 51


def test_add_like_to_the_latest_post_empty_db():
    with raises(BadFetch):
        add_like_to_the_latest_post(models.Post, 0, 0)
