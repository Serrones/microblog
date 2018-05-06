from app import app, mongo


class MongoLord:
    def __init__(self):
        self.el_mongo = mongo.db.microblog_mdb_log

    def mongo_logging(self, request_method, request_endpoint,
                      request_url, time):
        log_info = {"method": request_method, "endpoint": request_endpoint,
                    "url": request_url, "data": time}
        self.el_mongo.insert(log_info)
