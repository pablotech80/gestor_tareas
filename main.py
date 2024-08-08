import os
from flask import Flask, render_template, request, redirect, url_for, flash
import db
from models import Tarea
from datetime import datetime

# Inicializo la aplicación Flask
app = Flask(__name__)
# Configuro una clave secreta para manejar sesiones y mensajes flash donde informa que se realizo la tarea.
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')
# Creo la ruta principal para mostrar la página de inicio y las tareas
@app.route('/')
def home():
    # Creo una sesión a la base de datos
    session = db.SessionLocal()
    # Consulto todas las tareas de base de datos
    todas_las_tareas = session.query(Tarea).all()
    # Cierro la sesión de la base de datos
    session.close()
    # Renderizo la plantilla index.html y le paso la lista de tareas
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

# Creo la ruta para manejar la creación de nuevas tareas
@app.route('/crear-tarea', methods=['POST'])
def crear():
    session = db.SessionLocal()
    # Creo una nueva instancia de Tarea con el contenido del formulario para marcarla como no hecha
    tarea = Tarea(
        contenido=request.form['contenido_tarea'],
        categoria=request.form['categoria_tarea'],
        fecha_limite=datetime.strptime(request.form['fecha_limite'], '%Y-%m-%d'),
        hecha=False
    )
    # Añadimos la nueva tarea a la sesión de la base de datos
    session.add(tarea)
    # Confirmo la transacción para guardar la tarea en la base de datos
    session.commit()
    # Cierro la sesión de la base de datos
    session.close()
    # Muestro un mensaje flash indicando que la tarea fue guardada
    flash('Tarea guardada')
    # Redirigo a la página principal
    return redirect(url_for('home'))

# Creo la ruta para eliminar las tareas
@app.route('/eliminar-tarea/<int:id>')
def eliminar(id):
    session = db.SessionLocal()
    tarea = session.query(Tarea).filter_by(id=id).delete()
    session.commit()
    session.close()
    flash('Tarea eliminada')
    return redirect(url_for('home'))

# Creo la ruta para manejar el cambio de estado de la tarea (hecha o no hecha)
@app.route('/tarea-hecha/<int:id>')
def hecha(id):

    session = db.SessionLocal()
    tarea = session.query(Tarea).filter_by(id=id).first()
    tarea.hecha = not tarea.hecha
    session.commit()
    session.close()
    flash('Tarea completada')
    return redirect(url_for('home'))

# Creo la nueva ruta para editar tareas
@app.route('/editar-tarea/<int:id>', methods=['GET', 'POST'])
def editar(id):
    session = db.SessionLocal()
    tarea = session.query(Tarea).filter_by(id=id).first()
    if request.method == 'POST':
        tarea.contenido = request.form['contenido_tarea']
        tarea.categoria = request.form['categoria_tarea']
        tarea.fecha_limite = datetime.strptime(request.form['fecha_limite'], '%Y-%m-%d')
        session.commit()
        session.close()
        flash('Tarea actualizada')
        return redirect(url_for('home'))
    session.close()
    return render_template('editar.html', tarea=tarea)


# Punto de entrada y control de la aplicación
if __name__ == '__main__':
    # Creao todas las tablas en la base de datos (si no existen)
    db.Base.metadata.create_all(db.engine)
    # Ejecuto la aplicación Flask en modo debug y en el puerto 5001 el 5000 me dio algún problema(no se por que?)
    app.run(debug=True, port=5001)
