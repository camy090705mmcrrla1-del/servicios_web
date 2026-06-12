from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "proyecto123"


def conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="proyecto1"
    )



@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nombre = request.form["nombre"]
        password = request.form["password"]

        con = conexion()
        cursor = con.cursor()

        sql = """
        SELECT * FROM administradores
        WHERE nombre=%s AND password=%s
        """

        cursor.execute(sql, (nombre, password))

        admin = cursor.fetchone()

        con.close()

        if admin:
            session["admin"] = admin[1]
            return redirect("/menu")

        return render_template(
            "login.html",
            mensaje="Usuario o contraseña incorrectos"
        )

    return render_template("login.html")



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



@app.route("/menu")
def menu():

    if "admin" not in session:
        return redirect("/")

    return render_template("menu.html")



@app.route("/administradores", methods=["GET", "POST"])
def administradores():

    if "admin" not in session:
        return redirect("/")

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        password = request.form["password"]
        edad = request.form["edad"]
        puesto = request.form["puesto"]

        sql = """
        INSERT INTO administradores
        (nombre,password,edad,puesto)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (nombre, password, edad, puesto)
        )

        con.commit()

    cursor.execute(
        "SELECT * FROM administradores"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "administradores.html",
        administradores=datos,
        editar=None
    )


@app.route("/administradores/eliminar/<int:id>")
def eliminar_admin(id):

    con = conexion()
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM administradores WHERE id=%s",
        (id,)
    )

    con.commit()
    con.close()

    return redirect("/administradores")


@app.route("/administradores/editar/<int:id>",
           methods=["GET", "POST"])
def editar_admin(id):

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        password = request.form["password"]
        edad = request.form["edad"]
        puesto = request.form["puesto"]

        sql = """
        UPDATE administradores
        SET nombre=%s,
            password=%s,
            edad=%s,
            puesto=%s
        WHERE id=%s
        """

        cursor.execute(
            sql,
            (nombre, password, edad, puesto, id)
        )

        con.commit()

        con.close()

        return redirect("/administradores")

    cursor.execute(
        "SELECT * FROM administradores WHERE id=%s",
        (id,)
    )

    editar = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM administradores"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "administradores.html",
        administradores=datos,
        editar=editar
    )



@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():

    if "admin" not in session:
        return redirect("/")

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        password = request.form["password"]
        edad = request.form["edad"]
        telefono = request.form["telefono"]

        sql = """
        INSERT INTO usuarios
        (nombre,password,edad,telefono)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (nombre, password, edad, telefono)
        )

        con.commit()

    cursor.execute(
        "SELECT * FROM usuarios"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "usuarios.html",
        usuarios=datos,
        editar=None
    )


@app.route("/usuarios/eliminar/<int:id>")
def eliminar_usuario(id):

    con = conexion()
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id=%s",
        (id,)
    )

    con.commit()
    con.close()

    return redirect("/usuarios")


@app.route("/usuarios/editar/<int:id>",
           methods=["GET", "POST"])
def editar_usuario(id):

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        password = request.form["password"]
        edad = request.form["edad"]
        telefono = request.form["telefono"]

        sql = """
        UPDATE usuarios
        SET nombre=%s,
            password=%s,
            edad=%s,
            telefono=%s
        WHERE id=%s
        """

        cursor.execute(
            sql,
            (nombre, password, edad,
             telefono, id)
        )

        con.commit()

        con.close()

        return redirect("/usuarios")

    cursor.execute(
        "SELECT * FROM usuarios WHERE id=%s",
        (id,)
    )

    editar = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM usuarios"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "usuarios.html",
        usuarios=datos,
        editar=editar
    )



@app.route("/servicios", methods=["GET", "POST"])
def servicios():

    if "admin" not in session:
        return redirect("/")

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        precio = request.form["precio"]
        periodo = request.form["periodo"]
        tipo = request.form["type"]

        sql = """
        INSERT INTO servicios
        (nombre,precio,periodo,type)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (nombre, precio, periodo, tipo)
        )

        con.commit()

    cursor.execute(
        "SELECT * FROM servicios"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "servicios.html",
        servicios=datos,
        editar=None
    )


@app.route("/servicios/eliminar/<int:id>")
def eliminar_servicio(id):

    con = conexion()
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM servicios WHERE id=%s",
        (id,)
    )

    con.commit()
    con.close()

    return redirect("/servicios")


@app.route("/servicios/editar/<int:id>",
           methods=["GET", "POST"])
def editar_servicio(id):

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        precio = request.form["precio"]
        periodo = request.form["periodo"]
        tipo = request.form["type"]

        sql = """
        UPDATE servicios
        SET nombre=%s,
            precio=%s,
            periodo=%s,
            type=%s
        WHERE id=%s
        """

        cursor.execute(
            sql,
            (
                nombre,
                precio,
                periodo,
                tipo,
                id
            )
        )

        con.commit()

        con.close()

        return redirect("/servicios")

    cursor.execute(
        "SELECT * FROM servicios WHERE id=%s",
        (id,)
    )

    editar = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM servicios"
    )

    datos = cursor.fetchall()

    con.close()

    return render_template(
        "servicios.html",
        servicios=datos,
        editar=editar
    )



@app.route("/reportes", methods=["GET", "POST"])
def reportes():

    if "admin" not in session:
        return redirect("/")

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        usuario = request.form["usuario"]
        servicio = request.form["servicio"]
        direccion = request.form["direccion"]
        urgencia = request.form["urgencia"]
        descripcion = request.form["descripcion"]

        sql = """
        INSERT INTO reportes
        (usuario,servicio,direccion,
        urgencia,descripcion)
        VALUES(%s,%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                usuario,
                servicio,
                direccion,
                urgencia,
                descripcion
            )
        )

        con.commit()

    cursor.execute("""
        SELECT r.id,
               u.nombre,
               s.nombre,
               r.direccion,
               r.urgencia,
               r.descripcion
        FROM reportes r
        INNER JOIN usuarios u
        ON r.usuario=u.id
        INNER JOIN servicios s
        ON r.servicio=s.id
    """)

    datos = cursor.fetchall()

    cursor.execute(
        "SELECT id,nombre FROM usuarios"
    )
    usuarios = cursor.fetchall()

    cursor.execute(
        "SELECT id,nombre FROM servicios"
    )
    servicios = cursor.fetchall()

    con.close()

    return render_template(
        "reportes.html",
        reportes=datos,
        usuarios=usuarios,
        servicios=servicios,
        editar=None
    )


@app.route("/reportes/eliminar/<int:id>")
def eliminar_reporte(id):

    con = conexion()
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM reportes WHERE id=%s",
        (id,)
    )

    con.commit()
    con.close()

    return redirect("/reportes")


@app.route("/reportes/editar/<int:id>",
           methods=["GET", "POST"])
def editar_reporte(id):

    con = conexion()
    cursor = con.cursor()

    if request.method == "POST":

        usuario = request.form["usuario"]
        servicio = request.form["servicio"]
        direccion = request.form["direccion"]
        urgencia = request.form["urgencia"]
        descripcion = request.form["descripcion"]

        sql = """
        UPDATE reportes
        SET usuario=%s,
            servicio=%s,
            direccion=%s,
            urgencia=%s,
            descripcion=%s
        WHERE id=%s
        """

        cursor.execute(
            sql,
            (
                usuario,
                servicio,
                direccion,
                urgencia,
                descripcion,
                id
            )
        )

        con.commit()

        con.close()

        return redirect("/reportes")

    cursor.execute(
        "SELECT * FROM reportes WHERE id=%s",
        (id,)
    )

    editar = cursor.fetchone()

    cursor.execute("""
        SELECT r.id,
               u.nombre,
               s.nombre,
               r.direccion,
               r.urgencia,
               r.descripcion
        FROM reportes r
        INNER JOIN usuarios u
        ON r.usuario=u.id
        INNER JOIN servicios s
        ON r.servicio=s.id
    """)

    datos = cursor.fetchall()

    cursor.execute(
        "SELECT id,nombre FROM usuarios"
    )
    usuarios = cursor.fetchall()

    cursor.execute(
        "SELECT id,nombre FROM servicios"
    )
    servicios = cursor.fetchall()

    con.close()

    return render_template(
        "reportes.html",
        reportes=datos,
        usuarios=usuarios,
        servicios=servicios,
        editar=editar
    )

if __name__ == "__main__":
    app.run(debug=True)