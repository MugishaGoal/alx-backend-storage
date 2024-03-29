#!/usr/bin/env python3
"""
Log stats
"""


from pymongo import MongoClient


def count_logs(mongo_collection):
    """
    Count logs in collection
    """
    total_logs = mongo_collection.count_documents({})
    print("{} logs".format(total_logs))


def count_methods(mongo_collection):
    """
    Count methods
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    for method, count in method_counts.items():
        print("method {}: {}".format(method, count))


def top_ips(mongo_collection):
    """
    Top 10 IPs
    """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    for ip_data in top_ips:
        print("{}: {}".format(ip_data["_id"], ip_data["count"]))


def main():
    """
    Main function
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    count_logs(logs_collection)
    print("Methods:")
    count_methods(logs_collection)
    print("IPs:")
    top_ips(logs_collection)


if __name__ == "__main__":
    main()
