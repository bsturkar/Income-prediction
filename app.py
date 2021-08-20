from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import pandas as pd

#from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl', 'rb'))
edu_dic=pickle.load(open('dict.pkl','rb'))
columns=pd.read_csv('col.csv')
a=pd.DataFrame(columns)
#b=a.iloc[:,1].to_list()
b=[i.replace(' ','') for i in a.iloc[:,1].to_list()]

#v=list(np.zeros(len(b)))
v=[0 for i in range (len(b))]
app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('boot.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
     if request.method == 'POST':
           age= int(request.form['age'])
           v[b.index('age')]=age
           
           education=request.form['education']
           education_num=edu_dic[education]
           
           v[b.index('education-num')]=education_num
           
           capgain= int(request.form['capital-gain'])
           v[b.index('capital-gain')]=capgain
           
           caploss= int(request.form['capital-loss'])
           v[b.index('capital-loss')]=caploss
           
           hoursperweek= int(request.form['hours-per-week'])
           v[b.index('hours-per-week')]=hoursperweek
           
           
           work=request.form['workclass']
           if work=='Never-worked':
               pass
           else:
              v[b.index(work)]=1
           
            
           married=request.form['marital-status']
           if married=='Divorced':
               pass
           else:
               v[b.index(married)]=1
           
           occupation=request.form['occupation']
           if occupation=='Adm-clerical':
               pass
           else:
               v[b.index(occupation)]=1
           
           relation=request.form['relation']
           if relation=='Husband':
               pass
           else:
               v[b.index(relation)]=1
               
           
           race=request.form['race']
           if race=='Amer-Indian-Eskimo':
               pass
           else:
               v[b.index(race)]=1
           
           sex=request.form['sex']
           if sex=='Female':
               pass
           else:
               v[b.index(sex)]=1
           
           country=request.form['country']
           if country=='Cambodia':
               pass
           else:
               v[b.index(country)]=1
           
         
         
           prediction=model.predict([v])[0]
       
           if prediction==0:
                  return render_template('boot.html',prediction_text="INCOME IS LESS THAN 50000")
           else:
            return render_template('boot.html',prediction_text="INCOME IS MORE THAN 50000")
     else:
        return render_template('boot.html')

if __name__=="__main__":
    app.run(debug=True)

