@ decorators with parameters
 from flask import flask
    app=flask(_name_)
@app.rout('hello/<name>')
    def hello_name(name_):
    return'hello%s!'%name
    if_name_=="_main_"
    app.run(debug=true) 