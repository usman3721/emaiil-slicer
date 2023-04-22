
# # importing Flask and other modules
from flask import Flask, request, render_template

# import random  # for generating random integers

# # Flask constructor
from app import app



@app.route('/'  , methods=["POST","GET"])
def email_slicer():
    email1=""
    domain=""
    error=""
    
    
    if request.method=="POST":
        email=request.form.get("email")
        email=email.strip()
        
        if email.count("@")==1 :
            email1=email.split("@")[0]
            domain=email.split("@")[1]
        else:
            error="Error! No/Wrong Input!"
        
    return render_template("index_templates.html", email=email1, domain=domain,error=error)
            


   
#    email=email1,domain=user_domain






# #   keep_asking=True
#     # while keep_asking:

#     #
#     #     format=(f"Your user name is{user_name} and your domain is {domain_name}")
#     #     print(format)
#     #     stop=input("Would you like to continue? ")

#     #     if stop =="no":
#     #         keep_asking=False
