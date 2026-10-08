from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola_mundo():
    return '<a href="https://www.draftea.mx/">Haz clic aquí</a>'

if __name__ == '__main__':
    app.run(debug=True)