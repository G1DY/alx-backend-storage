#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if not mongo_collection:
        return []
    documents = mongo_collections.find()
    return [post for post in documents]
