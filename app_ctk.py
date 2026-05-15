import customtkinter as ctk
from logica import buscar_estudiante, ASIGNATURAS, validar_nota, validar_asistencia, calcular_estado
def buscar():
    doc = entry_doc.get().strip()
    nombre = buscar_estudiante(doc)
    if not nombre:
        # lbl_resultado.configure(text = "Estudiante no encontrado", text_color = "red")
        # _habilitar_formulario(False)
        return
    entry_nombre.configure(state = "normal")
    entry_nombre.delete(0, "end")
    entry_nombre.insert(0, nombre)
    entry_nombre.configure(state = "disable")
    #lbl_resultado.configure(text = "Estudiante encontrado", text_color = "green")
    #_habilitar_formulario(True)


app = ctk.CTk()
app.title("Sistema Académico - CustomTKinter")
app.geometry("400x620")

ctk.CTkLabel(app, text = "Documento:").pack(pady=5)
entry_doc = ctk.CTkEntry(app)
entry_doc.pack()

ctk.CTkButton(app, text = "Buscar Estudiante", command = buscar).pack(pady = 8)

ctk.CTkLabel(app, text = "Nombre Estudiante:").pack(pady = 5)
entry_nombre = ctk.CTkEntry(app, state = "disabled")
entry_nombre.pack()

#ctk.CTkLabel(app, text = "Buscar Estudiante:").pack(pady = 5)


# def habilitar_formulario():
#     pass

app.mainloop()

