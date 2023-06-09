def calcular_promedio_ponderado(lab1, lab2):
    promedio_ponderado = (lab1 * 0.3) + (lab2 * 0.7)
    return round(promedio_ponderado, 1)

diccionario_estudiantes = {}

for i in range(3):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
    nota_lab1 = float(input("Ingrese la nota del Laboratorio N°1: "))
    nota_lab2 = float(input("Ingrese la nota del Laboratorio N°2: "))
    promedio_ponderado = calcular_promedio_ponderado(nota_lab1, nota_lab2)
    
    diccionario_estudiantes[nombre_estudiante] = {
        'Asignatura': nombre_asignatura,
        'Laboratorio N°1': nota_lab1,
        'Laboratorio N°2': nota_lab2,
        'Promedio Ponderado': promedio_ponderado
    }

for estudiante, info in diccionario_estudiantes.items():
    print("Estudiante:", estudiante)
    print("Asignatura:", info['Asignatura'])
    print("Laboratorio N°1:", info['Laboratorio N°1'])
    print("Laboratorio N°2:", info['Laboratorio N°2'])
    print("Promedio Ponderado:", info['Promedio Ponderado'])
    print()