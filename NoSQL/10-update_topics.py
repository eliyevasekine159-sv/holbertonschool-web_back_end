#!/usr/bin/env python3
""" Modul sənədləşməsi: Məktəb mövzularını yeniləmək """


def update_topics(mongo_collection, name, topics):
    """ Funksiya sənədləşməsi: Adı bərabər olan sənədin mövzularını yeniləyir """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
