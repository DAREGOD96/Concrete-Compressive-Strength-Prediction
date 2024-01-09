from flask import Flask,request,render_template
from src.Concrete_strength_prediction.pipeline.prediction import PredictionPipeline
from src.Concrete_strength_prediction.pipeline.userdata_conversion import UserData
from src.Concrete_strength_prediction.logger import logging
import time
applicaiton=Flask(__name__)
app=applicaiton



@app.route("/",methods=['GET','POST'])
def prediction():
    if request.method =='GET':
        return render_template('index.html')
    else:
        user_data=UserData(
            cement=float(request.form.get('cement')),
            blast_furnace_slag=float(request.form.get('blast_furnace_slag')),
            fly_ash=float(request.form.get('fly_ash')),
            water=float(request.form.get('water')),
            superplasticizer=float(request.form.get('superplasticizer')),
            coarse_aggregate=float(request.form.get('coarse_aggregate')),
            fine_aggregate=float(request.form.get('fine_aggregate')),
            age=int(request.form.get('age'))
        )
        start_time = time.time()
        features=user_data.convert_data_into_dataframe()
        prediction_pipeline_object=PredictionPipeline()  
        prediction = prediction_pipeline_object.predict(features)
        end_time = time.time()

        elapsed_time = end_time - start_time
        logging.info(f"Time taken for prediction: {elapsed_time} seconds")
        

        return render_template("index.html",prediction=prediction[0])

if __name__=="__main__":
    app.run(host="0.0.0.0")   

        
