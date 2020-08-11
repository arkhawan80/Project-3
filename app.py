from flask import Flask, render_template, redirect, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Render the page
@app.route("/")
def home():
   
    # Return template and data
    return render_template("LoanForm.html")


#receives info from the form entry
@app.route("/api/loanroute/<HHIncome>/<Credit>/<Location>/<Gender>/<Married>/<Graduate>/<LoanTerm>/<LoanAmount>")
def LoanApp(HHIncome,Credit,Location,Gender,Married,Graduate,LoanTerm,LoanAmount):
    values=[]
    values.append(HHIncome)
    values.append(Credit)
    values.append(Location)
    values.append(Gender)
    values.append(Married)
    values.append(Graduate)
    values.append(LoanTerm)
    values.append(LoanAmount)
    
    df=pd.DataFrame([values])
    print(df)


    loaded_model= pickle.load(open("model.sav","rb"))

    predictions = loaded_model.predict(df)
    print(f"Predictions: {predictions}")

    if predictions==0: 
        Loanoutcome="Not Approved"
    else: 
        Loanoutcome="Approved"

    return_value= {
        "outcome": Loanoutcome

    }

    return jsonify(return_value)

if __name__ == "__main__":
    app.run(debug=True)
