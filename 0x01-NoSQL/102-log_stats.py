#!/usr/bin/env python3
"""a Python script that provides some stats
   about Nginx logs stored in MongoDB
"""
import pymongo
from pymongo import MongoClient


def log_stats(mongo_collection, option=None):
    """provides some stats about Nginx logs stored in MongoDB"""
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")

def print_top_ips(server_collection):
    """prints statistics about the top 10 HTTP IPs in a collection"""
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                "$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}
                },
            {
                "$sort": {"totalRequests": -1}
                },
            {
                "$limit": 10
                },
            ])
    for request_log in request_logs:
        ip = request_log["_id"]
        ip_requests_count = request_log["totalRequests"]
        print("\t{}: {}".format(ip, ip_requests_count))


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(mongo_collection)
