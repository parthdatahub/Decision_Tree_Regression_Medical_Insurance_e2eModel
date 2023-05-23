from flask import Flask, render_template, request
from project_app.utils import Insurance

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_premium", methods=["POST", "GET"])
def get_inputs():
    if request.method == "GET":
                        
            age = eval(request.args.get("age"))
            sex = request.args.get("sex")
            bmi = eval(request.args.get("bmi"))
            children = eval(request.args.get("children"))
            smoker = request.args.get("smoker")
            region = request.args.get("region")

            

            premium_prediction = Insurance(age,sex,bmi,children,smoker,region)
            prediction = premium_prediction.get_predicted_value()
  
            print(f"Your LIC Insurance premium is Rs. {prediction} /- only")

            return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
