import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

indice = {}
combinaciones = []

class AplicacionModificarCSV:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación para Modificar CSV")

        # Variables para almacenar la ruta del archivo CSV y su contenido
        self.ruta_archivo = None
        self.df = None

        # Centrar la ventana en la pantalla
        self.centra_ventana()
        # Crear los widgets de la interfaz gráfica
        self.crear_widgets()

    def centra_ventana(self):
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.master.winfo_screenwidth()
        alto_pantalla = self.master.winfo_screenheight()
        # Calcular las coordenadas para centrar la ventana
        x_coordinate = (ancho_pantalla - 300) // 2
        y_coordinate = (alto_pantalla - 200) // 2
        # Establecer la geometría de la ventana
        self.master.geometry(f"300x200+{x_coordinate}+{y_coordinate}")

    def cargar_csv(self):
        # Abrir el cuadro de diálogo para seleccionar un archivo CSV
        self.ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if self.ruta_archivo:
            try:
                # Leer el archivo CSV y almacenarlo en un DataFrame
                self.df = pd.read_csv(self.ruta_archivo)
                self.df.fillna('', inplace=True)
                messagebox.showinfo("Información", "Archivo CSV cargado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo CSV: {e}")

    def modificar_csv(self):
        if self.df is not None:
            try:
                self.recorrer()
                combinaciones, cadena_modificada = self.generar_combinaciones()

                # Guardar combinaciones en un nuevo archivo CSV
                df_combinaciones = pd.DataFrame({'combinaciones': combinaciones, 'cadena_modificada': cadena_modificada})
                ruta_nuevo_archivo = "combinaciones.csv"
                df_combinaciones.to_csv(ruta_nuevo_archivo, index=False)

                messagebox.showinfo("Información", "CSV modificado y guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al modificar el archivo CSV: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor carga un archivo CSV primero.")

    def recorrer(self):
        if self.df is not None:
            secuencia = self.df["string_a_modificar"].iloc[0]
            ventana = 10
            desplazamiento = 5
            for i in range(0, len(secuencia), desplazamiento):
                ventana_actual = secuencia[i:i+ventana]
                alteraciones = self.df["alteracion"][self.df["posicion"].isin(range(i, i+ventana))]
                combinaciones_ventana = []

                for alteracion in alteraciones:
                    combinacion = ventana_actual.replace("referencia", alteracion)
                    combinaciones_ventana.append(combinacion)
                
                indice[i] = combinaciones_ventana

    def generar_combinaciones(self):
        combinaciones = []
        cadena_modificada = ""

        for i, combinaciones_ventana in indice.items():
            for combinacion in combinaciones_ventana:
                combinaciones.append(combinacion)
        
        cadena_modificada = "".join(combinaciones)
        cadena_modificada = cadena_modificada[:len(self.df["string_a_modificar"].iloc[0])]

        return combinaciones, cadena_modificada

    def crear_widgets(self):
        # Etiqueta para indicar la selección del archivo CSV
        self.etiqueta_archivo = tk.Label(self.master, text="Seleccionar archivo CSV:")
        self.etiqueta_archivo.pack()

        # Botón para buscar el archivo CSV
        self.boton_buscar_archivo = tk.Button(self.master, text="Buscar archivo", command=self.cargar_csv)
        self.boton_buscar_archivo.pack()

        # Botón para modificar el CSV
        self.boton_modificar_csv = tk.Button(self.master, text="Modificar CSV", command=self.modificar_csv)
        self.boton_modificar_csv.pack()

        # Botón para abrir más opciones
        self.boton_mas_opciones = tk.Button(self.master, text="Más opciones", command=self.abrir_ventana_mas_opciones)
        self.boton_mas_opciones.pack()

    def abrir_ventana_mas_opciones(self):
        # Crear una nueva ventana para mostrar más opciones
        ventana_mas_opciones = tk.Toplevel(self.master)
        ventana_mas_opciones.title("Más opciones")

        # Centrar la ventana en la pantalla
        ventana_mas_opciones.geometry(self.master.geometry())

        # Botón para cerrar la ventana de más opciones
        boton_cerrar = tk.Button(ventana_mas_opciones, text="Cerrar", command=ventana_mas_opciones.destroy)
        boton_cerrar.pack()

        # Botón para combinar todo
        boton_combinar_todo = tk.Button(ventana_mas_opciones, text="Combinar todo", command=self.combinar_todo)
        boton_combinar_todo.pack()

        # Botón para combinar dos variables
        boton_combinar_variables = tk.Button(ventana_mas_opciones, text="Combinar dos variables", command=self.abrir_ventana_combinar_variables)
        boton_combinar_variables.pack()

        # Botón para combinación por rangos
        boton_combinar_rangos = tk.Button(ventana_mas_opciones, text="Combinación por rangos", command=self.abrir_ventana_combinacion_rangos)
        boton_combinar_rangos.pack()

    def abrir_ventana_combinar_variables(self):
        # Crear una nueva ventana para combinar dos variables
        ventana_combinar_variables = tk.Toplevel(self.master)
        ventana_combinar_variables.title("Combinar dos variables")

        # Centrar la ventana en la pantalla
        ventana_combinar_variables.geometry(self.master.geometry())

        # Etiqueta y campo de entrada para la primera variable
        label_variable1 = tk.Label(ventana_combinar_variables, text="Variable 1:")
        label_variable1.pack()
        entry_variable1 = tk.Entry(ventana_combinar_variables)
        entry_variable1.pack()

        # Etiqueta y campo de entrada para la segunda variable
        label_variable2 = tk.Label(ventana_combinar_variables, text="Variable 2:")
        label_variable2.pack()
        entry_variable2 = tk.Entry(ventana_combinar_variables)
        entry_variable2.pack()

        # Botón para combinar las dos variables
        boton_combinar = tk.Button(ventana_combinar_variables, text="Combinar", command=lambda: self.combinar_dos_variables(entry_variable1.get(), entry_variable2.get()))
        boton_combinar.pack()

    def abrir_ventana_combinacion_rangos(self):
        # Crear una nueva ventana para la combinación por rangos
        ventana_combinacion_rangos = tk.Toplevel(self.master)
        ventana_combinacion_rangos.title("Combinación por rangos")

        # Centrar la ventana en la pantalla
        ventana_combinacion_rangos.geometry(self.master.geometry())

        # Etiqueta y campo de entrada para el inicio del rango
        label_inicio_rango = tk.Label(ventana_combinacion_rangos, text="Inicio del rango:")
        label_inicio_rango.pack()
        entry_inicio_rango = tk.Entry(ventana_combinacion_rangos)
        entry_inicio_rango.pack()

        # Etiqueta y campo de entrada para el fin del rango
        label_fin_rango = tk.Label(ventana_combinacion_rangos, text="Fin del rango:")
        label_fin_rango.pack()
        entry_fin_rango = tk.Entry(ventana_combinacion_rangos)
        entry_fin_rango.pack()

        # Botón para generar la combinación por rangos
        boton_generar = tk.Button(ventana_combinacion_rangos, text="Generar", command=lambda: self.combinacion_por_rangos(entry_inicio_rango.get(), entry_fin_rango.get()))
        boton_generar.pack()

    def combinar_todo(self):
        if self.df is not None:
            try:
                combinaciones_rango = []
                ventana = 10
                desplazamiento = 5
                valor1 = 0
                valor2 = len(self.df["string_a_modificar"].iloc[0])  # Longitud de la secuencia
                for i in range(valor1, valor2):
                    for j in range(0, len(self.combinaciones), desplazamiento):
                        ventana_actual = self.combinaciones[j:j+ventana]
                        cadena = ''.join(ventana_actual)
                        alteraciones = self.df["alteracion"][self.df["posicion"].isin(range(i, i+ventana))]

                        for alteracion in alteraciones:
                            combinacion_rango = cadena.replace("referencia", alteracion)
                            combinaciones_rango.append(combinacion_rango)

                df_combinaciones = pd.DataFrame({'combinaciones': combinaciones_rango})
                ruta_nuevo_archivo = "combinaciones_todo.csv"
                df_combinaciones.to_csv(ruta_nuevo_archivo, index=False)

                messagebox.showinfo("Combinar todo", f"Combinaciones guardadas en {ruta_nuevo_archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al combinar todo: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor carga un archivo CSV primero.")

    def combinar_por_rangos(self, valor1, valor2):
        if self.df is not None:
            try:
                combinaciones_rango = []
                ventana = 10
                desplazamiento = 5
                for i in range(int(valor1), int(valor2)):
                    for j in range(0, len(self.combinaciones), desplazamiento):
                        ventana_actual = self.combinaciones[j:j+ventana]
                        cadena = ''.join(ventana_actual)
                        alteraciones = self.df["alteracion"][self.df["posicion"].isin(range(i, i+ventana))]

                        for alteracion in alteraciones:
                            combinacion_rango = cadena.replace("referencia", alteracion)
                            combinaciones_rango.append(combinacion_rango)

                df_combinaciones = pd.DataFrame({'combinaciones': combinaciones_rango})
                ruta_nuevo_archivo = "combinaciones_rangos.csv"
                df_combinaciones.to_csv(ruta_nuevo_archivo, index=False)

                messagebox.showinfo("Combinar por rangos", f"Combinaciones guardadas en {ruta_nuevo_archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al combinar por rangos: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor carga un archivo CSV primero.")

    def combinar_dos_variables(self, com1, com2):
        if self.df is not None:
            try:
                combinaciones_uno_a_uno = []
                combinaciones_finales = []
                com1 = int(com1)
                com2 = int(com2)
                combinacion1 = self.combinaciones[com1]
                combinacion2 = self.combinaciones[com2]
                combinaciones_finales.append(combinacion1)
                combinaciones_finales.append(combinacion2)
                ventana = 10
                desplazamiento = 5
                for i in range(com1, com2):
                    for j in range(0, len(combinaciones_finales), desplazamiento):
                        ventana_actual = combinaciones_finales[j:j+ventana]
                        cadena = ''.join(ventana_actual)
                        alteraciones = self.df["alteracion"][self.df["posicion"].isin(range(i, i+ventana))]

                        for alteracion in alteraciones:
                            combinacion_uno_a_uno = cadena.replace("referencia", alteracion)
                            combinaciones_uno_a_uno.append(combinacion_uno_a_uno)

                df_combinaciones = pd.DataFrame({'combinaciones': combinaciones_uno_a_uno})
                ruta_nuevo_archivo = "combinaciones_dos_variables.csv"
                df_combinaciones.to_csv(ruta_nuevo_archivo, index=False)

                messagebox.showinfo("Combinar dos variables", f"Combinaciones guardadas en {ruta_nuevo_archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al combinar las dos variables: {e}")
        else:
            messagebox.showwarning("Advertencia", "Por favor carga un archivo CSV primero.")

def main():
    root = tk.Tk()
    app = AplicacionModificarCSV(root)
    root.mainloop()

main()

















