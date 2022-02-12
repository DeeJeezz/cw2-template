import os.path
from typing import Dict

DATA_STORAGE_NAME: str = 'JSON'

BASE_DATA_PATH: str = 'data'
REPO_SETTINGS: Dict[str, str] = {
    'posts_file_path': os.path.join(BASE_DATA_PATH, 'data.json'),
    'comments_file_path': os.path.join(BASE_DATA_PATH, 'comments.json'),
    'bookmarks_file_path': os.path.join(BASE_DATA_PATH, 'bookmarks.json'),
}
