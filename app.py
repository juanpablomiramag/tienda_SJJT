from flask import Flask, render_template, request
app= Flask(__name__)


titulos=("Nombre","Telefono","saldo")
informacion=[]

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/registrar")
def registrar_cliente():
  return render_template('registrar_cliente.html')

@app.route("/actualizar")
def actualizar():
  return render_template('actualizar.html')

@app.route("/datos")
def datos():
  return render_template("datos.html",titulos_tabla=titulos,data=informacion)


@app.route("/agregar_persona", methods=["POST"])
def agregar_persona():
  if (request.method=="POST"):
    
    Nombre=request.form["Nombre"]
    Telefono=request.form["Telefono"]
    Saldo=request.form["Saldo"]

    listainfo=[Nombre,Telefono,Saldo]
    informacion.append(listainfo)

    print("***************************************")

  return render_template("registrar_cliente.html",data=informacion)

if (__name__ == "__main__"):
  app.run(debug=True,port=5000)




