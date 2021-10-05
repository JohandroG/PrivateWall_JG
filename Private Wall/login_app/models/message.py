from login_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class Message:
    def __init__(self,data):

        self.id = data['message_id']
        self.message = data['message_info']
        self.user_id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def sendMSJ(cls,data):
        query = "INSERT INTO messages (message_info,id,sender_id,created_at,updated_at) VALUES (%(message)s,%(user_id)s,%(sender_id)s,SYSDATE(),SYSDATE())"

        msjinfo = {
            'message' : data[0],
            'user_id' : data[1],
            'sender_id': data[2]
        }

        results = connectToMySQL('loginform').query_db(query,msjinfo)
        return results


    @classmethod
    def deletemsj(cls,data):
        query = "DELETE FROM messages WHERE message_id = %(message_id)s"

        msjID = {
            'message_id' : data
        }

        results = connectToMySQL('loginform').query_db(query,msjID)
        return results