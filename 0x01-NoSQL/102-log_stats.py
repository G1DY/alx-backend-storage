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

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips = mongo_collection.aggregate(pipeline)
    print("Top 10 IPs:")
    for index, ip_info in enumerate(top_ips, start=1):
        print(f"\t#{index}: IP {ip_info['_id']} - Count: {ip_info['count']}")


if __name__ == "__main__":
    mongo_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(mongo_collection)
