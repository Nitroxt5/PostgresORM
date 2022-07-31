from datetime import date

from postgresorm.post.post import Post


def test_str():
    post = Post("Candy", "Max", "Abcde", date(2017, 8, 21), 15)

    expect = "name: Candy\nauthor: Max\ndescription: Abcde\ncreated at: 2017-08-21\nlikes count: 15"

    assert str(post) == expect
