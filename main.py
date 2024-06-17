from flask import Flask, request, render_template, redirect, session
from conexionSQL import conexionBD


app= Flask(__name__)
app.secret_key = 'your_secret_key'

#Obtener el cursos de la BD
cursor = conexionBD()

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            cursor.execute("EXEC CrearUsuario @NickName=?, @Contrasena=?", (username, password))
            cursor.commit()
            return redirect('/')
        except Exception as ex:
            print(ex)
            return 'Error occurred during registration'
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            cursor.execute("EXEC VerificarUsuario @nickName=?, @contrasena=?", (username, password))
            result = cursor.fetchone()[0]
            if result == 1:  # Usuario encontrado
                if username == 'jdcrespo' and password == '123456':
                    return redirect('/admin')
                else:
                    session['username'] = username
                    return redirect('/')
            else:
                return 'Login failed'
        except Exception as ex:
            print("Error en la autenticación:", ex)
            return 'Error en la autenticación'
        #finally:
        #    cursor.close()
    
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/admin')
def admin():
    try:
        cursor.execute("EXEC ListarUsuario")
        users = cursor.fetchall()
        return render_template('admin.html', users=users)
    except Exception as ex:
        print("Error al listar usuarios:", ex)
        return 'Error al listar usuarios'
    
@app.route('/edit_user', methods=['POST'])
def edit_user():
   if request.method == 'POST':
        user_id = request.form['user_id']
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        try:
            cursor.execute("EXEC EditarUsuario @idUsuario=?, @NickName=?, @Contrasena=?", (user_id, new_username, new_password))
            cursor.commit()
            return redirect('/admin')
        except Exception as ex:
            print("Error al editar usuario:", ex)
            return 'Error al editar usuario'
        finally:
            cursor.close()

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
    # Aquí debes implementar la lógica para eliminar el usuario con el ID dado
    try:
        cursor.execute("EXEC EliminarUsuario @idUsuario = ?", (user_id))
        cursor.commit()
        return redirect('/admin')
    except Exception as ex:
        print("Error al eliminar usuario:", ex)
        return 'Error al eliminar usuario'



    
if __name__== "__main__":
    app.run(debug=True, port=6660)
