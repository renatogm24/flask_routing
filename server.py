from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
  return 'Hola Mundo!'

@app.route('/dojo')
def dojo():
  return '¡Dojo!'

@app.route('/say/<string:name>')
def say(name):
  return f"¡Hola, {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
  text = ""
  for x in range(num):
    text += f"{word} \n"
  return text

@app.route('/<word>/')
def anything(word):
  if word not in ["dojo","say","repeat"]:
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":
  app.run(debug=True)