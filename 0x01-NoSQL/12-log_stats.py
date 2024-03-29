#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def count_documents(mongo_collection, query=None):
    """Count the number of documents in the collection matching the query"""
    if query is None:
        return mongo_collection.count_documents({})
    return mongo_collection.count_documents(query)


def main():
    """Main function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = count_documents(collection)
    print("{} logs".format(total_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = count_documents(collection, {"method": method})
        print("    method {}: {}".format(method, count))

    status_check_count = count_documents(
            collection, {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    main()
