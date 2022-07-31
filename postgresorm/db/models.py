import peewee as pw

from postgresorm.db.credentials import user, password, host, port, prod_db


class Post(pw.Model):
    id = pw.AutoField()
    name = pw.TextField()
    author = pw.TextField()
    description = pw.TextField()
    created_at = pw.DateField()
    likes = pw.IntegerField()

    class Meta:
        database = pw.PostgresqlDatabase(prod_db, user=user, password=password, host=host, port=port)
        table_name = "posts"
