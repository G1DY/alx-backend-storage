#!/usr/bin/env python3
"""a Python script that provides some stats
   about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """provides some stats about Nginx logs stored in MongoDB"""
    if option:
        value = mongo_collection.count_documents({"method": option})
        print(f"Method {option}: {value}")
    else:
        result = mongo_collection.count_documents({})
        print(f"Total logs: {result}")
        print("Methods:")
        for method in METHODS:
            log_stats(mongo_collection, method)
        status_check = mongo_collection.count_documents({"path": "/status"})
        print(f"Status check logs: {status_check}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx
    log_stats(mongo_collection)
