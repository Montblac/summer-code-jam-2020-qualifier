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
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""
    def __set_name__(self, owner, name):
        self.name = name

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not issubclass(type(value), self.field_type):
            def type_to_str(type_obj):
                type_obj = str(type_obj)
                start = type_obj.find("'")
                end = type_obj.rfind("'")
                return type_obj[start+1:end]

            raise TypeError("expected an instance of type '{}' for attribute '{}', got '{}' instead".format(
                type_to_str(self.field_type), self.name, type_to_str(type(value))))

        instance.__dict__[self.name] = value

class Article:
    """The `Article` class you need to write for the qualifier."""
    id = -1

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self.last_edited = None

        Article.id += 1
        self.id = Article.id

    def __setattr__(self, name, value):
        if name == 'content':
            self.last_edited = datetime.datetime.now()
        super().__setattr__(name, value)

    def __repr__(self):
        return '<Article title={title} author={author} publication_date={publication_date}>'.format(
            title=repr(self.title),
            author=repr(self.author),
            publication_date=repr(self.publication_date.isoformat()))

    def __len__(self):
        return len(self.content)

    def __eq__(self, other):
        return self.publication_date == other.publication_date

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def short_introduction(self, n_characters: int):
        if len(self.content) <= n_characters or self.content[n_characters].isspace():
            return self.content[:n_characters].strip()
        return self.short_introduction(n_characters-1)

    def most_common_words(self, n_words: int):
        result = dict()
        for word in re.split('[^a-z]+', self.content, flags=re.IGNORECASE):
            if not word:
                continue
            word = word.lower()
            result[word] = result[word] + 1 if word in result else 1
        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:n_words])
