#!/usr/bin/env python3
""" Modul sənədləşməsi: Kolleksiyadakı bütün sənədləri siyahılamaq """


def list_all(mongo_collection):
    """ Funksiya sənədləşməsi: Verilmiş kolleksiyadakı bütün sənədləri qaytarır """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
