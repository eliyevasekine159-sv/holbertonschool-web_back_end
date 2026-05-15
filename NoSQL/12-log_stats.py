#!/usr/bin/env python3
""" Modul sənədləşməsi: Nginx loglarının statistikasını təqdim edir """
from pymongo import MongoClient


def log_stats():
    """ Funksiya sənədləşməsi: MongoDB-dəki nginx loglarını analiz edir """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Ümumi log sayını tapırıq
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Metodların statistikasını çıxarırıq
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET metodu və /status path-i olan logların sayı
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
