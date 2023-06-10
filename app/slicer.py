
# # importing Flask and other modules
from flask import Flask, request, render_template,redirect


# # Flask constructor
from app import app


@app.route('/', methods=["POST", "GET"])
def email_slicer():
    email1 = ""
    domain = ""
    error = ""

    if request.method == "POST":
        email = request.form.get("email")
        email = email.strip()

        if email.count("@") == 1:
            email1 = email.split("@")[0]
            domain = email.split("@")[1]
            error = ""

        else:
            
            error = "Wrong Input ! ! !"
        

    return render_template("index_templates.html", email=email1, domain=domain, Error=error)
