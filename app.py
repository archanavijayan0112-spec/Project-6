
from flask import Flask, render_template
app=Flask(__name__)

alerts=[
 {"type":"Brute Force","severity":"High","score":92},
 {"type":"Suspicious Login","severity":"Medium","score":71}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', alerts=alerts)

if __name__=='__main__':
    app.run(debug=True)
