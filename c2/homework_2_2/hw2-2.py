#! /usr/bin/python

# remove the grade of type "homework" with the lowest score 
# for each student from the dataset in the handout.

import pymongo
import sys

# establish connection
connection = pymongo.MongoClient("mongodb://localhost")

def remove_lowest_homework():
    db = connection.students
    grades = db.grades
    print "test"
    docs = grades.find({"type":"homework"})\
        .sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
    curr_id = -1;
    for doc in docs:
        if doc['student_id'] != curr_id:
            curr_id = doc['student_id']
            # print doc
            grades.delete_one(doc)


remove_lowest_homework()
