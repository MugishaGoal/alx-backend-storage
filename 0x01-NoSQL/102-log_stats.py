#!/usr/bin/env python3
"""
Log stats
"""


from pymongo import MongoClient



def nginx_log_request(nginx_collection):
    """A script that print nginx request logs"""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        request_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, request_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def print_top_ips(server_collection):
    """Print ip"""
    print('IPs:')
    request_logs = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        count_ip_requests = request_log['totalRequests']
        print('\t{}: {}'.format(ip, count_ip_requests))


def start():
    """Main function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log_request(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == '__main__':
    start()
