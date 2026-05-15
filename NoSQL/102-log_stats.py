#!/usr/bin/env python3
""" Modul sənədləşməsi: Nginx loglarının statistikası və Top 10 IP """
from pymongo import MongoClient


def log_stats():
    """ Funksiya sənədləşməsi: Metodları, statusları və top 10 IP-ni analiz edir """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Ümumi log sayı
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Metodların statistikası
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status yoxlamalarının sayısı
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # Top 10 ən çox daxil olan IP-lər (Aggregation Pipeline)
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    log_stats()
