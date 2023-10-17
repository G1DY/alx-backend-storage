#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if mongo_collection is None:
        return []

    documents = mongo_collection.find()
    return [document for document in documents]
