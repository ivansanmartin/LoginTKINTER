from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from SQLConnect import create_connection

connection = create_connection()
cursor = connection.cursor()


class Login:
    def __init__(self, window):
        self.wind = window

        frame = LabelFrame(self.wind, text="Login")
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=55)

        # Titulo nombre

        Label(frame, text="Ingrese usuario:").grid(row=1, column=0)

        # Input nombre
        self.user = Entry(frame)
        self.user.focus()
        self.user.grid(row=1, column=1)

        # Titulo password
        Label(frame, text="Ingrese contrasena:").grid(row=2, column=0)

        # Input password
        self.password = Entry(frame)
        self.password.grid(row=2, column=1)

        Button(frame, text="Login", command=self.verify_login).grid(row=3, column=0, sticky=W + E, columnspan=2,
                                                                    pady=10, padx=15)

    def verify_login(self):
        nombre = self.user.get()
        password = self.password.get()
        print(nombre)
        print(password)

        sql = """SELECT nombre, password FROM USER"""
        obtener_usuario = cursor.execute(sql).fetchall()

        for usuarios in obtener_usuario:
            print(usuarios)
            if nombre == usuarios[0] and password == usuarios[1]:
                messagebox.showinfo("Exito", "Has iniciado sesion correctamente")
            elif nombre != usuarios[0] or password != usuarios[1]:
                messagebox.showwarning("Error", "Contrasena o usuario incorrecto")


def main():
    connection = create_connection()
    cursor = connection.cursor()

    window = Tk()
    aplicacion = Login(window)
    window.title("Login System")
    window.resizable(False, False)
    window.geometry("350x150")
    window.mainloop()

    # sql = """INSERT INTO USER (nombre, password) VALUES ('Ivan', 'asd123')"""
    # cursor.execute(sql)

    # connection.commit()

print("asd")


if __name__ == "__main__":
    main()
