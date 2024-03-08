#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
#app.route is a decorator
def index():
    if request.method =='POST':
        return (render_template("index.html"))
    else:
        return (render_template("index.html"))

if __name__ == "__main__":
    app.run()


# In[ ]:




