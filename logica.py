ESTUDIANTES = {
    "123": "Gabriel Rodriguez",
    "456": "Elena Luna",
    "789": "Carlos Perez",
    "101": "Ana Garcia",
    "202": "Luis Morales"
}

ASIGNATURAS = [
    "Logica Computacional",
    "Introduccion a la Ingenieria de Datos"
    "Calculo Diferencial"
    "Algebra Lineal"
]

def buscar_estudiante(documento):
    return ESTUDIANTES.get(documento, None)

def validar_nota(valor):
    try:
        nota = float(valor)
        return 0 <= nota <= 5
    except ValueError:
        return False

def validar_asistencia(valor):
    try: 
        asistencia = float(valor)
        return 0 <= asistencia <= 100
    except ValueError:
        return False

def calcular_estado(notas, asistencia):
    promedio = sum(notas) / len(notas)
    if asistencia < 80:
        return promedio, "Reprobó por inasistencia", "red"
    elif promedio >= 3.0:
        return promedio, "Aprobado", "green"
    else:
        return promedio, "Reprobó por nota", "red"