from flask import render_template, request, redirect, Flask
import os
import csv

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    data = []
    
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename'] # This line uses the same variable and worked fine
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)
            
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            
            return render_template('index.html', data=data)
    
    return render_template('index.html')



app.config['FILE_UPLOADS'] = "uploadds"
if __name__ == "__main__":
    app.run()
