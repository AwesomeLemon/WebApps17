# coding=UTF-8
'''
Created on 24.09.2017

@author: sysoev
'''
from google.appengine.ext import db
from google.appengine.api import users

import datetime
import time
import logging

from myusers import MyUser


def force_unicode(string):
    if type(string) == unicode:
        return string
    return string.decode('utf-8')

class Project(db.Model):
    name = db.StringProperty(multiline=False)

def getProjectsList(user):
    return None

def updateProject(key, name):
    p = Project.get(key)
    if not p:
        return
    p.name = name
    p.put()

def addProject(name):
    p = Project()
    p.name = name
    p.put()
    return p.key()


class UserProject(db.Model):
    user_key = db.ReferenceProperty(MyUser)
    project_key = db.ReferenceProperty(Project)

def addUserProject(user_name, project_key):
    up = UserProject()
    query = MyUser.all()
    up.user_key = query.filter('name = ' + user_name).get().key
    up.project_key = project_key
    up.put()
    return up.key()

def deleteUserProject(user_key, project_key):
    query = UserProject.all()
    query.filter('user_key = ', user_key).filter('project_key = ', project_key)
    query.get().key.delete()

def getUserProjects(user_key):
    query = UserProject.all()
    query.filter('user_key = ', user_key)
    return query.fetch()