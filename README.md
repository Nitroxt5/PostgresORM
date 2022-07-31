# PostgreSQL & Pytest

---

This repository contains an example of working with PostgreSQL DB, using pool of threads and peewee ORM, with some unit tests. 

## Formulation of the problem

---

Resolve situation when many threads try to update a single record in DB using an ORM.