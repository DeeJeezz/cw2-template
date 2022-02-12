import json
from abc import abstractmethod, ABCMeta
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Type


@dataclass
class Post:
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int


class RepositoryNotFoundError(Exception):
    pass


class Repository(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def get_posts_all(self, *args, **kwargs) -> List[Post]:
        ...


class JSONRepository(Repository):

    def __init__(self, posts_file_path: str, comments_file_path: str, bookmarks_file_path: str):
        self._posts_file_path: str = posts_file_path
        self._comments_file_path: str = comments_file_path
        self._bookmarks_file_path: str = bookmarks_file_path

    def get_posts_all(self) -> List[Post]:
        with open(self._posts_file_path, encoding='utf-8') as f:
            raw_posts: List[dict] = json.load(f)
        return [Post(**post) for post in raw_posts]


class DataRepositories(Enum):
    JSON = JSONRepository

    @classmethod
    def get(cls, name: str) -> Type[Repository]:
        try:
            return cls[name].value
        except KeyError:
            raise RepositoryNotFoundError('Repository with name "%s" not found', name)


def get_data_repository(repository_name: str, repo_settings: dict) -> Repository:
    repository_class: Type[Repository] = DataRepositories.get(repository_name)

    repository: Repository = repository_class(**repo_settings)

    return repository
