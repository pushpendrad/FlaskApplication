from flask import Flask , render_template
app = Flask(__name__)

employees=[
    {
        "emp_id":"13518",
        "emp_name":"pushpendra"
    },
    {
        "emp_id":"13542",
        "emp_name":"vaibhav jain"
    },
    {
        "emp_id":"13535",
        "emp_name":"sumit kumar"
    }
]
students=[
    {
        "student_rollnum":"1",
        "student_name":"Pushpendra Dewangan"
    },
    {
        "student_rollnum":"2",
        "student_name":"Vaibhav Jain"
    },
    {
        "student_rollnum":"3",
        "student_name":"Sudhanshu Shrivastva"
    }
]


@app.route('/')
def langing():
    return render_template('home.html')

@app.route('/employees')
def getEmployees():
    return render_template('displayEmployee.html',employees=employees)
    

@app.route('/students')
def getStudents():
    return render_template('displayStudent.html',students=students)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
