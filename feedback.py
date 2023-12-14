from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_feedback', methods=['POST'])
def enviar_feedback():
    feedback_texto = request.form['feedback']
    # Aqui você pode processar o feedback, armazená-lo em um banco de dados, etc.
    # Por enquanto, apenas retornaremos uma mensagem simples.
    return 'Feedback recebido: {}'.format(feedback_texto)

if __name__ == '__main__':
    app.run(debug=True)


