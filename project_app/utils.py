import pandas as pd
import numpy as np
import pickle
import json
import os

class Insurance:
    def __init__(self, age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region='region_'+ region
        
    def load_model(self):
        model_file_path = os.path.join(os.path.dirname(__file__),"medical_insurance_DecisionTreeRegression.pkl")
        json_file_path = os.path.join(os.path.dirname(__file__),"Project_data.json")

        with open(model_file_path,"rb") as f:
            self.model = pickle.load(f)

        with open(json_file_path,"r") as f:
            self.json_data = json.load(f)
            #self.feature_names = self.json_data["Columns"]

            # Assign feature names to the model
            #self.model.feature_names = self.feature_names
    
    def get_predicted_value(self):

        self.load_model()    # to create instance of model and json_data

        region_index=self.json_data['column_names'].index(self.region)
        test_array=np.zeros(len(self.json_data['column_names']))

        test_array[0]=self.age
        test_array[1]=self.json_data['sex'][self.sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data['smoker'][self.smoker]
        test_array[region_index]= 1

        test_array

        prediction = round(self.model.predict([test_array])[0],2)

        return prediction
    

if __name__ == "__main__":

    age=29
    sex='male'
    bmi=26.9
    children=0
    smoker='no'
    region='northwest'

    med_ins = Insurance(age,sex,bmi,children,smoker,region)
    prediction = med_ins.get_predicted_value()
    print(f"Predicted Insurance Premium charge is Rs. {prediction} /- only")