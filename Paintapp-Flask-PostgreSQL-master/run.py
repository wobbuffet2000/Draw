import os
import sys
import json
from flask import Flask, render_template, request, redirect, url_for
import psycopg2


app = Flask(__name__)
everything = """
            database='postgres://cpjuhmlcfrteqt:1a7d2c1a74e75f2b96cf0a2eae2a2e09228d27c8ff4bbdeddccdbe372458\
            3fd6@ec2-54-243-107-66.compute-1.amazonaws.com:5432/d5jvikb9npnt5r'
            user='wobb'
            password='hopefully'
"""


@app.route('/', methods=['GET', 'POST'])
def paintapp():
    if request.method == 'GET':
        return render_template("paint.html")
    '''if request.method == 'POST':
        filename = request.form['save_fname']
        data = request.form['save_cdata']
        canvas_image = request.form['save_image']
        conn = psycopg2.connect(everything)
        cur = conn.cursor()
        cur.execute("INSERT INTO files (name, data, canvas_image) VALUES (%s, %s, %s)", [filename, data, canvas_image])
        conn.commit()
        conn.close()
        return redirect(url_for('save'))        
        '''
        
@app.route('/save', methods=['GET', 'POST'])
def save():
    conn = psycopg2.connect(everything)
    return 'Can\'t connect'
    cur = conn.cursor()
    cur.execute("SELECT id, name, data, canvas_image from files")
    files = cur.fetchall()
    conn.close()
    return render_template("save.html", files=files)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template("search.html")
    '''if request.method == 'POST':
        filename = request.form['fname']
        conn = psycopg2.connect(database="paintmyown", user="wobb")
        cur = conn.cursor()
        cur.execute("select id, name, data, canvas_image from files")
        files = cur.fetchall()
        conn.close()
        return render_template("search.html", files=files, filename=filename)'''
    
if __name__ == '__main__':
    app.run(debug=True)
