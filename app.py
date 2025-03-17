from flask import Flask, render_template,request, redirect, url_for
import requests


app=Flask(__name__)

tasks=[]

@app.route('/')
def return_task_web():
    return render_template('tasks.html')

@app.route('/delete_task/<task_name>',methods=['POST'])
def delete_task(task_name):
    global tasks
    tasks=[task for task in tasks if task["name"]!=task_name]
    return redirect(url_for('show_tasktrack'))





@app.route('/tasks')
def show_tasktrack():
    url="https://zenquotes.io/api/random"
    response=requests.get(url)
    data=response.json()
    if data:
        quote=data[0]['q']
    else:
        return "Never lose hope" 
    
    return render_template('tasks.html',tasks=tasks,quote=quote)

@app.route('/form' , methods=['GET','POST'])
def return_form_page():
    if request.method=='POST':
        task_name=request.form['task_name']
        task_date=request.form['task_date']
        task_time=request.form['task_time']
        task_desc=request.form['task_description']
        task_type=request.form['task_type']
        task={
            "name":task_name,
            "date":task_date,
            "time":task_time,
            "desc":task_desc
        }

        if task_type=='Priority':
            tasks.insert(0,task)
        else:
            tasks.append(task)

        return redirect(url_for('show_tasktrack'))
    return render_template('form.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
