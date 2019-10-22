from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from pathlib import Path
import os
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conn=sqlite3.connect('App/data.db',check_same_thread=False)


@app.route('/event_number/<string:id>/',methods=['GET'])
def get_tickets(id):
    cur = conn.cursor()
    all_tickets = cur.execute("select sum(Quantity) from vivid_data where Event_Id='"+id+"'") 
    result=dict(Event_number=id,Total_tickets_available=all_tickets.fetchall())
    return result

@app.route('/add_new',methods=['POST'])
def add_new_ticket():
    eid=request.json['Event_Id']
    sec=request.json['Section']
    qua=request.json['Quantity']
    pri=request.json['Price']
    row=request.json['Row']
    avail=request.json['Availability']
    cur = conn.cursor()
    add_new_ticket = cur.execute("""INSERT INTO vivid_data (Event_Id,Section,Quantity,Price,Row,Availability) VALUES (?,?,?,?,?,?)""",(eid,sec,qua,pri,row,avail)) 
    cur.execute('commit')
    return "Added new tickets for Event_ID'"+eid+"'. You can see new tickets with the event_id or get_best GET requests"

@app.route('/get_best/<string:eid>/',methods=['GET'])
def get_best_tickets(eid):
    cur = conn.cursor()
    best_tickets = cur.execute("select Price,Quantity from vivid_data where Event_Id='"+eid+"'LIMIT 10") 
    best_result=dict(Price_sorted_and_tickets_available=best_tickets.fetchall())
    return best_result

@app.route('/update',methods=['PUT'])
def update_ticket():
    eid=request.json['Event_Id']
    qua=request.json['Quantity']
    sec=request.json['Section']
    avail=request.json['Availability']
    print(eid,qua,sec,avail)
    cur = conn.cursor()
    if avail=="Yes":
        updat_ticket = cur.execute("""UPDATE vivid_data SET Quantity=Quantity+(?),Availability='Yes' WHERE Event_ID=(?) AND Section=(?) """,(qua,eid,sec))
        return "Ticket status is changed to Yes and the Quantity is updated"
    elif avail=="No":
        updat_ticket = cur.execute("""UPDATE vivid_data SET Quantity=Quantity-(?),Availability='No' WHERE Event_ID=(?)AND Section=(?) """,(qua,eid,sec))
        return "Ticket status is changed to No and the Quantity is updated"
    else:
        return "Please update the Availability as either Yes or No. Check the alphabet case in Availability" 

   
if __name__ == '__main__':
  app.run('0.0.0.0',5000, debug=True)