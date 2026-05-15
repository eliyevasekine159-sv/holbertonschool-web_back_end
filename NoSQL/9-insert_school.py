#!/usr/bin/env python3
""" Modul sənədləşməsi: Kolleksiyaya yeni sənəd əlavə etmək """


def insert_school(mongo_collection, **kwargs):
    """ Funksiya sənədləşməsi: kwargs əsasında sənəd daxil edir və _id qaytarır """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
