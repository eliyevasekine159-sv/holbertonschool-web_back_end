#!/usr/bin/env python3
""" Modul sənədləşməsi: Mövzuya görə məktəbləri tapmaq """


def schools_by_topic(mongo_collection, topic):
    """ Funksiya sənədləşməsi: Müəyyən bir mövzuya sahib olan məktəblərin siyahısını qaytarır """
    return list(mongo_collection.find({"topics": topic}))
