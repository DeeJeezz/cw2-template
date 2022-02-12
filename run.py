from app import app
import routes # noqa
import settings
from repository import get_data_repository


if __name__ == '__main__':

    app.config['JSON_AS_ASCII'] = False
    app.config['repository'] = get_data_repository(settings.DATA_STORAGE_NAME, settings.REPO_SETTINGS)

    app.run(debug=True)
