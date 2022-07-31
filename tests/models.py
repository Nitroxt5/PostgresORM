import peewee as pw

from tests.credentials import user, password, host, port, test_db


class Post(pw.Model):
    id = pw.AutoField()
    name = pw.TextField()
    author = pw.TextField()
    description = pw.TextField()
    created_at = pw.DateField()
    likes = pw.IntegerField()

    class Meta:
        database = pw.PostgresqlDatabase(test_db, user=user, password=password, host=host, port=port)
        table_name = "posts"
