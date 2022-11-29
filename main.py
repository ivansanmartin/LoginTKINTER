from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from SQLConnect import create_connection

connection = create_connection()
cursor = connection.cursor()


class Login:
    def __init__(self, window):
        self.window = window
        self.new_user = None
        self.new_password = None
        self.new_password_confirm = None

        frame = LabelFrame(self.window, text="Login")
        frame.grid(row=0, column=0, padx=50, pady=50, ipadx=10, ipady=10)

        # User etiqueta

        Label(frame, text="Nombre de usuario:").grid(row=1, column=0)

        # User entrada
        self.user = Entry(frame)
        self.user.grid(row=1, column=1)
        self.user.focus()

        # Password etiqueta

        Label(frame, text="Contrasena:").grid(row=2, column=0, pady=10)

        # Password entrada
        self.password = Entry(frame)
        self.password.grid(row=2, column=1)

        # Boton login

        Button(frame, text="Iniciar sesion", command=self.verify_login).grid(row=3, column=0, ipadx=10, columnspan=2)

    def verify_login(self):
        user_entry = self.user.get()
        password_entry = self.password.get()

        sql = """SELECT nombre, password FROM USER;"""
        obtener_usuarios = cursor.execute(sql).fetchall()

        for usuarios in obtener_usuarios:
            print(usuarios)
            if user_entry == usuarios[0] and password_entry == usuarios[1]:
                messagebox.showinfo("Correcto", "Has iniciado sesion correctamente.")
                # Frame agregar usuarios y contrasena

                frame_usuarios = LabelFrame(self.window, text="Agregar usuario")
                frame_usuarios.grid(row=2, column=0)

                # Etiqueta agregar usuario
                Label(frame_usuarios, text="Usuario: ").grid(row=3, column=0)

                # Entrada usuario
                self.new_user = Entry(frame_usuarios)
                self.new_user.focus()
                self.new_user.grid(row=3, column=1)

                # Etiqueta agregar contrasena

                Label(frame_usuarios, text="Contrasena:").grid(row=4, column=0)

                # Entrada contrasena
                self.new_password = Entry(frame_usuarios)
                self.new_password.grid(row=4, column=1)

                # Etiqueta agregar contrasena confirmar

                Label(frame_usuarios, text="Confirmar contrasena:").grid(row=5, column=0)

                # Entrada contrasena confirmacion
                self.new_password_confirm = Entry(frame_usuarios)
                self.new_password_confirm.grid(row=5, column=1)

                # Boton agregar
                Button(frame_usuarios, text="Agregar",
                                        command=lambda: self.add_new_user(self.new_user.get(), self.new_password.get())).grid(row=6, column=0, columnspan=2, pady=10)

                return

        for usuarios in obtener_usuarios:
            if user_entry != usuarios[0] or password_entry != usuarios[1]:
                messagebox.showerror("Error", "Tu contrasena o usuario es incorrecto.")
                break

    def add_new_user(self, user, passowrd):
        sql = f"""INSERT INTO USER (nombre, password) VALUES ('{user}', '{passowrd}');"""
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo(f"Proceso satisfactorio", f"Se agrego a {user} correctamente en la base de datos.")


def main():
    # SQLITE

    # sql = """CREATE TABLE USER (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #                            nombre VARCHAR(45) NOT NULL,
    #                           password VARCHAR(45) NOT NULL);"""
    # sql = """INSERT INTO USER (nombre, password) VALUES ('Ivan', 'asd123');"""
    # cursor.execute(sql)
    # connection.commit()

    window = Tk()
    aplicacion = Login(window)
    window.geometry("350x400")
    window.title("Iniciar sesion")
    window.mainloop()


if __name__ == "__main__":
    main()
