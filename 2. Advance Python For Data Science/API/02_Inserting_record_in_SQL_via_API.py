from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host='localhost', user = 'root', passwd = 'mechengg.@nagpur8766')
print(mydb)
cursor = mydb.cursor()

app = Flask(__name__)

# Write a program to insert a record in SQL Table via API
@app.route('/insert', methods = ['GET','POST'] )
def insert_func() :
    try:                                                    # With Exception handling we can do more efficient coding
        if (request.method=='POST') :
            for i in range(1,5) :                           # This is just for Repetition of data
                emp_id = request.json['Number']
                emp_name = request.json['Name']
                email_ID = request.json['Email']
                contact_number = request.json['Mob.Number']
                salary = request.json['Salary']
                designation = request.json['Designation']
                department = request.json['Department']
                joining_date = request.json['Joining_Date']
                cursor.execute('INSERT INTO kunal.employee_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s )'
                               ,(emp_id,emp_name,email_ID,contact_number, salary,designation,department,joining_date))
                mydb.commit()
            return jsonify(str('Data Entering Successful'))
    except Exception :
        print('Please check the data you have entered')


# Write a program to update a record via API
@app.route('/update', methods = ['GET','POST'])
def update_func() :
    if (request.method=='POST') :
        emp_name = request.json['get_name']
        cursor.execute("UPDATE kunal.employee_details SET salary = (salary + 5000) WHERE emp_name = %s ",(emp_name,))
        mydb.commit()
        return jsonify(str('Salary updated'))


@app.route('/delete', methods = ['GET','POST'])
def delete_func() :
    if(request.method == 'POST') :
        del_name = request.json['Employee_name_to_delete']
        cursor.execute('DELETE FROM kunal.employee_details WHERE emp_name = %s ',(del_name,))
        mydb.commit()
        return jsonify(str('Record Deletion Successfully'))

if __name__ == '__main__' :
    app.run()