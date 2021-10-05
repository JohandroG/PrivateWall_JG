import re
from flask import render_template, session, redirect, request
from login_app import app
from flask_bcrypt import Bcrypt
from flask import flash
from login_app.models.message import Message

@app.route('/dashboard/send', methods = ['POST'])
def sendMSJ():

    message = request.form['message']
    user_id = request.form['user_id']
    sender_id = session['user_id']

    messageInfo = (message,user_id,sender_id)
    
    Message.sendMSJ(messageInfo)

    return redirect ('/dashboard')

@app.route('/dashboard/delete', methods = ['POST'])
def deleteMSJ():
    
    msjID = request.form['message_id']
    print(msjID)
    Message.deletemsj(msjID)
    
    return redirect ('/dashboard')

