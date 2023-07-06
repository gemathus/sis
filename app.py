from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/estudiantes')
def estudiantes():
    estudiantes = [
        'Alberto Preciado',
        'Gerardo Mathus',
        'Elsa Serrano',
        'Euris',
        'Isa López',
        'Alejandro',
        'María',
        'Jacobo'
    ]
    return render_template('estudiantes.html', students=estudiantes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
