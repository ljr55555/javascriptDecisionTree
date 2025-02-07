from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def decision_tree():
    return render_template('decision_tree.html')

if __name__ == '__main__':
    app.run(debug=True)