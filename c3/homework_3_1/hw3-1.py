#! /usr/bin/python

# remove the grade of type "homework" with the lowest score in scores array
# for each student from the dataset in the handout.
# 
# {
#    "_id" : 0,
#    "name" : "aimee Zank",
#    "scores" : [
#        {
#            "type" : "exam",
#            "score" : 1.463179736705023
#        },
#        {
#            "type" : "quiz",
#            "score" : 11.78273309957772
#        },
#        {
#            "type" : "homework",
#            "score" : 6.676176060654615
#        },
#        {
#            "type" : "homework",
#            "score" : 35.8740349954354
#        }
#    ]
#}

import pymongo
import sys

# establish connection
connection = pymongo.MongoClient("mongodb://localhost")

def remove_lowest_homework():
    db = connection.school
    students = db.students
    docs = students.find()

    # it will be easier with aggregation
    for doc in docs:
        print "test"
        min = 999
        scores = doc["scores"]
        for score in scores:
            # ignore other type of scores
            if score["type"] != "homework":
                continue
            if score["score"] < min:
                min = score["score"]
        # pull: remove homework with smallest score
        students.update({"_id":doc["_id"]}, {"$pull": {"scores":{"type":"homework", "score":min}} })


remove_lowest_homework()
