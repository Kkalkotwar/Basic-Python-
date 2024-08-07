"""def test(a,b) :
    return a+b

print(test(4,5))"""

"""
If we run the above function, and we want to see the results,
We need to print it in the run console, but what if we need to access the same function
from some other external source... then API comes into picture.
"""

# WHAT IS AN API?
"""
API is been used to communicate or establish a communication between two hetrogeneous or
two homogeneous systems so that these two system can talk with eachother and
then it will be able to execute something, some of the functions, some of the classes or anything.

Or API is the set of Protocalls / Rules by which we will be able to reach out to a respective system.
and then we will be able to execute the respective function.
"""


# Flask framework is the framework which will help us out to expose our function/task to the outer world
from flask import Flask , request , jsonify

app = Flask(__name__) # 'app' is an object which will access all the functions and variables available in
                      # Flask library
"""
Here route is the function in which we define the path of the execution
In this, we are using 'GET' and 'POST' which are two methods.
So with the help of 'GET' or 'POST' we will be able to send a data to a defined particular root
in our case right now it is '/abc' and next we are passing it into the function(root) which is
available inside the class Flask.

@ is nothing but the annotation, that just after this line, whichever function is there, execute that.
"""
@app.route('/abc',methods = ['GET','POST'])
def test() :
    if(request.method=='POST') :
        a = request.json['Num_1']
        b = request.json['Num_2']
        c = a+b
        return jsonify((str(c)))

@app.route('/abc2',methods = ['GET','POST'])
def test2() :
    if(request.method=='POST') :
        a = request.json['Num_1']
        b = request.json['Num_2']
        c = a*b
        return jsonify((str(c)))


if __name__ == '__main__' :
    app.run()
"""
So basically when we are sending the data we are sending it in two way, 
i.e., 1. In the form of URL (It will be a  visible data)
      2. In the form of Body (It will be not visible)
Sending a data in the form of body will be the best way of sending it.

Here in case of an API, 
'GET' means posting a data in URL.
'POST' means posting a data in the form of body.
When data security is the primary consern, we send it with POST
"""

# TASKS:
"""
1. Write a program to insert a record in SQL Table via API
2. Write a program to update a record via API
3. Write a program to delete a record via API
4. Write a program to fetch a record via API
5. All the above question you have to answer for mongoDB as well
"""

