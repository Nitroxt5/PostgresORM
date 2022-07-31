from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from time import sleep

import db.models as models
from db.operations import get_posts, insert_post, clear_posts_table, add_like_to_the_latest_post
from post.post_generator import generate_post
from post.post import Post
from utils import time_counter, BadFetch


def main():
    post_per_thread_count = 20
    likes_per_thread_count = 30
    thread_count = 8

    # with ThreadPoolExecutor(max_workers=thread_count) as executor:
    #     futures = [executor.submit(fill_posts_table, models.Post, post_per_thread_count) for _ in range(thread_count)]
    #     for _ in as_completed(futures):
    #         print("job done!")
    insert_post(models.Post, Post("Test", "Max", "abcde", date(2000, 1, 1), 0))

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = []
        for i in range(thread_count):
            futures.append(executor.submit(like_latest_post, models.Post, likes_per_thread_count, i))
            # sleep(0.01)
        for _ in as_completed(futures):
            print("job done!")
    # like_latest_post(models.Post, conn.cursor(), likes_per_thread_count)

    posts = get_posts(models.Post)
    print(*posts, sep="\n")

    clear_posts_table(models.Post)


@time_counter
def fill_posts_table(model, post_count: int):
    for i in range(post_count):
        insert_post(model, generate_post())


@time_counter
def like_latest_post(model, likes_count: int, thread_num: int):
    for i in range(likes_count):
        try:
            add_like_to_the_latest_post(model, thread_num, i)
        except BadFetch as error:
            print(error)


if __name__ == "__main__":
    main()
