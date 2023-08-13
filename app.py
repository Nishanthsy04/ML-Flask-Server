from flask import render_template, Flask, request
import pickle

app = Flask(__name__)
models = {}

# Load models for each city
subdivisions = ['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'BIHAR', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'COASTAL KARNATAKA', 'EAST MADHYA PRADESH', 'EAST RAJASTHAN', 'EAST UTTAR PRADESH', 'GANGETIC WEST BENGAL', 'GUJARAT REGION', 'HARYANA DELHI & CHANDIGARH', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'JHARKHAND', 'KERALA', 'KONKAN & GOA', 'LAKSHADWEEP', 'MADHYA MAHARASHTRA', 'MATATHWADA', 'NAGA MANI MIZO TRIPURA', 'NORTH INTERIOR KARNATAKA', 'ORISSA', 'PUNJAB', 'RAYALSEEMA', 'SAURASHTRA & KUTCH', 'SOUTH INTERIOR KARNATAKA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'TAMIL NADU', 'TELANGANA', 'UTTARAKHAND', 'VIDARBHA', 'WEST MADHYA PRADESH', 'WEST RAJASTHAN', 'WEST UTTAR PRADESH']
for subdivision in subdivisions:
    model_file_name = f"models/{subdivision}.pkl"
    file = open(model_file_name, "rb")
    model = pickle.load(file)
    file.close()
    models[subdivision] = model

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        subdivision = myDict["Subdivision"]
        
        model = models[subdivision]
        pred = [Year, Month]
        res = model.predict([pred])[0]
        res = round(res, 2)
        return render_template('result.html', Month=Month, Year=Year, subdivision=subdivision, res=res)
    
    return render_template('index.html', subdivisions=subdivisions)

if __name__ == "__main__":
    app.run(debug=True)
