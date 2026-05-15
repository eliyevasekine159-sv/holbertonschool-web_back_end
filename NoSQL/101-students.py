#!/usr/bin/env python3
""" Modul sənədləşməsi: Tələbələrin ortalama ballarını hesablamaq və sıralamaq """


def top_students(mongo_collection):
    """ Funksiya sənədləşməsi: Tələbələri averageScore key-i ilə azalan sıra ilə qaytarır """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
