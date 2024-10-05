from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = open('loanapp.pkl','rb')
print("pickle file is opened")
loan = pickle.load(model)



#loan.predict([[]])

@app.route("/")
def ho():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])

def predict():
    if request.method == "POST":
        instance=[]
        # Date_of_Journey
        name_of_app = request.form.get('name_of_app')
        gender = request.form.get('gender')
        property_area = request.form.get('Property_area')
        dependents = request.form.get('Dependents')
        education = request.form.get('education')
        employment = request.form.get('employment')
        loan_amount_term = request.form.get('Loan_Amount_Term')
        loan_amount = request.form.get('Loan_Amount')
        credit_history = request.form.get('credit_history')
        marital_status = request.form.get('marital_status')
        application_income = request.form.get('Application_Income')
        coapplicant_income = request.form.get('Coapplicant_Income')
        print(name_of_app)
        
        
        print(gender)
        if gender=="Male":
            gender_n=1
        else:
            gender_n=0
        instance.append(gender_n)
        
        print(marital_status)
        if marital_status=="Married":
            marital_status_n=1
        else:
            marital_status_n=0
        instance.append(marital_status_n)
        
        print(education)
        if education=="Educated":
            education_n=1
        else:
            education_n=0
        instance.append(education_n)
        
        
        print(employment)
        if employment=="Yes":
            employment_n=1
        else:
            employment_n=0
        instance.append(employment_n)
        
        print(application_income)
        application_income_n=int(application_income)
        instance.append(application_income_n)
        
         
        print(coapplicant_income)
        coapplicant_income_n=int(coapplicant_income)
        instance.append(coapplicant_income_n)
         
        print(loan_amount)
        loan_amount_n=int(loan_amount)
        instance.append(loan_amount_n)
        
        print(loan_amount_term)
        loan_amount_term_n=int(loan_amount_term)
        instance.append(loan_amount_term_n)
        
          
        print(credit_history)
        if credit_history=="Below_threshold":
            credit_history_n=0
        else:
            credit_history_n=1
        instance.append(credit_history_n)
        
        print(property_area)
        if property_area=="Rural":
            property_area_n=1
        elif property_area=="semiurban":
            property_area_n=2
        else:
            property_area_n=3
        instance.append(property_area_n)
        
        
        
        print(dependents)
        dependents_n=int(dependents)
        instance.append(dependents_n)
        
        
     
       
        print(instance)
        prediction=loan.predict([instance])
        print(prediction)
        if prediction[0]==1:
            result="the loan is approved.."
        else:
             result="loan is rejected"
        return render_template('result.html',name=name_of_app,g=gender,pa=property_area,dp=dependents ,ed=education ,emp=employment ,lat=loan_amount_term,la=loan_amount ,cs=credit_history,ms=marital_status,ap_i=application_income,co_i=coapplicant_income,res= result )
if __name__ == "__main__":
    
    app.run()