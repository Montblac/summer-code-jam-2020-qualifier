"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return '<Article title={title} author={author} publication_date={publication_date}>'.format(
            title=repr(self.title),
            author=repr(self.author),
            publication_date=repr(self.publication_date.isoformat()))

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        if len(self.content) <= n_characters or self.content[n_characters].isspace():
            return self.content[:n_characters].strip()
        return self.short_introduction(n_characters-1)
