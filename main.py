from flask import Flask,render_template,request
import pickle
import sklearn

app = Flask(__name__)
model = pickle.load(open('credit_card_fraud_model.pickle','rb'))
model


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    Income_type_Working = 0
    Income_type_Pensioner = 0
    Income_type_Student = 0
    Income_type_State_Servent = 0
    
    
    Family_type_Single = 0
    Family_type_Seperated = 0
    Family_type_Widow = 0
    
    House_type_House = 0
    House_type_with_parents = 0
    House_type_Municipal_Apartment = 0
    House_type_Rented_Apartment = 0
    House_type_Office_Apartment = 0
    
    Education_type_lower_secondary = 0
    Education_type_secondary = 0
    Education_type_incomplete_higher = 0
    Education_type_higher = 0
    

    if request.method == 'POST':
        Income = float(request.form['income'])
        Family_size = int(request.form['family_size'])
        Begin_month = int(request.form['begin_month'])
        Age = int(request.form['Age'])
        Years_employed = float(request.form['years_employed'])
        Work_phone = request.form['work_phone']
        if (Work_phone =='yes'):
            Work_phone=1
        else:
            Work_phone = 0
            
        Phone = request.form['phone']
        if (Phone == 'yes'):
            Phone = 1
        else:
            Phone =0
            
        Email = request.form['Email']
        if (Email == 'yes'):
            Email = 1
        else:
            Email = 0
            
        Gender = request.form['Gender']
        if (Gender == 'Male'):
            Gender = 1
        else:
            Gender = 0
            
        Car = request.form['Car']
        if (Car == 'yes'):
            Car = 1
        else:
            Car = 0
            
        Reality = request.form['Reality']
        if (Reality == 'yes'):
            Reality = 1
        else:
            Reality = 0
            
        Income_type = request.form['Income Type']
        if Income_type == 'Working':
            Income_type_Working = 1
            Income_type_Pensioner = 0
            Income_type_Student = 0
            Income_type_State_Servent = 0
        elif (Income_type == 'Student'):
             Income_type_Working = 0
             Income_type_Pensioner = 0
             Income_type_Student = 1
             Income_type_State_Servent = 0
        elif (Income_type == 'State Servent'):
             Income_type_Working = 0
             Income_type_Pensioner = 0
             Income_type_Student = 0
             Income_type_State_Servent = 1
        elif (Income_type_Pensioner == 'Pensioner'):
             Income_type_Working = 0
             Income_type_Pensioner = 1
             Income_type_Student = 0
             Income_type_State_Servent = 0
        else:
            Income_type_Working = 0
            Income_type_Pensioner = 0
            Income_type_Student = 0
            Income_type_State_Servent = 0
        
        Family_type = request.form['Family Type']
        if Family_type == 'Single':
                Family_type_Single = 1
                Family_type_Seperated = 0
                Family_type_Widow = 0
        elif Family_type == 'Seperated':
                Family_type_Single = 0
                Family_type_Seperated = 1
                Family_type_Widow = 0
        elif Family_type == 'Widow':
                Family_type_Single = 0
                Family_type_Seperated = 0
                Family_type_Widow = 1
        else:
                Family_type_Single = 0
                Family_type_Seperated = 0
                Family_type_Widow = 0
        
        House_type = request.form['House Type']
        if House_type == 'House':
            House_type_House = 1
            House_type_with_parents = 0
            House_type_Municipal_Apartment = 0
            House_type_Rented_Apartment = 0
            House_type_Office_Apartment = 0
        elif House_type == 'With Parents':
            House_type_House = 0
            House_type_with_parents = 1
            House_type_Municipal_Apartment = 0
            House_type_Rented_Apartment = 0
            House_type_Office_Apartment = 0
        elif House_type == 'Municipal Apartment':
            House_type_House = 0
            House_type_with_parents = 0
            House_type_Municipal_Apartment = 1
            House_type_Rented_Apartment = 0
            House_type_Office_Apartment = 0
        elif House_type == 'Rented Apartment':
            House_type_House = 0
            House_type_with_parents = 0
            House_type_Municipal_Apartment = 0
            House_type_Rented_Apartment = 1
            House_type_Office_Apartment = 0
        elif House_type == 'Office Apartment':
            House_type_House = 0
            House_type_with_parents = 0
            House_type_Municipal_Apartment = 0
            House_type_Rented_Apartment = 0
            House_type_Office_Apartment = 1
        else:
            House_type_House = 0
            House_type_with_parents = 0
            House_type_Municipal_Apartment = 0
            House_type_Rented_Apartment = 0
            House_type_Office_Apartment = 0
            
        Education_type = request.form['Education Type']
        if Education_type == 'Lower Secondary':
            Education_type_lower_secondary = 1
            Education_type_secondary = 0
            Education_type_incomplete_higher = 0
            Education_type_higher = 0
        elif Education_type == 'Secondary':
            Education_type_lower_secondary = 0
            Education_type_secondary = 1
            Education_type_incomplete_higher = 0
            Education_type_higher = 0
        elif Education_type == 'Incomplete Higher':
            Education_type_lower_secondary = 0
            Education_type_secondary = 0
            Education_type_incomplete_higher = 1
            Education_type_higher = 0
        elif Education_type == 'Higher':
            Education_type_lower_secondary = 0
            Education_type_secondary = 0
            Education_type_incomplete_higher = 0
            Education_type_higher = 1
        else:
            Education_type_lower_secondary = 0
            Education_type_secondary = 0
            Education_type_incomplete_higher = 0
            Education_type_higher = 0
            
        prediction = model.predict([[Income,Work_phone,Phone,Email,Family_size,Begin_month,Age,Years_employed,Gender,Car,Reality,Income_type_Pensioner,Income_type_State_Servent,Income_type_Student,Income_type_Working,
                                     Family_type_Seperated,Family_type_Single,Family_type_Widow,House_type_House,House_type_Municipal_Apartment,House_type_Office_Apartment,House_type_Rented_Apartment,House_type_with_parents,
                                     Education_type_higher,Education_type_incomplete_higher,Education_type_lower_secondary,Education_type_secondary]])
        output = prediction
        if output> 0:
            return render_template('index.html',prediction_text="Fraud may not happen")
        else:
            return render_template('index.html',prediction_text="Fraud may happen")
    else:
        return render_template('index.html')
        
if __name__ == '__main__':
    app.run()
