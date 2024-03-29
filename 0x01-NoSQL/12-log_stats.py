#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


def nginx_log_request(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        request_count = len(list(nginx_collection.find({'method': method})))
        print('\method {}: {}'.format(method, request_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log_request(client.logs.nginx)


if __name__ == '__main__':
    run()
