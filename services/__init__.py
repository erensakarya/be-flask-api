from services.mongodb_service import MongodbService


def init_services(app, mode):
    app.config.mongodb_service = MongodbService(mode=mode)
    return app
