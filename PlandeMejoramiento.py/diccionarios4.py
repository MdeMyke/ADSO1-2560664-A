'''Tenemos almacenadas las notas de un examen en un diccionario. Es necesario separar al
alumnado que aprobó y al que suspendió en dos diccionarios. Igualmente habrá que pasar a
mayúsculas el nombre del alumnado que aprobó y a minúsculas el nombre del alumnado que
suspendió. Escriba un programa en Python que realice esta operación usando diccionarios
por comprensión.'''

michael = {
    'John': 4,
    'Marc': 7,
    'Meryl': 2,
    'Anthony': 8,
    'Carol': 3,
    'Sarah': 6,
}

aprobados = {student.upper(): mark for student, mark in michael.items() if mark >= 5}
denegados  = {student.lower(): mark for student, mark in michael.items() if mark < 5}

print(f'Aprobaron: {aprobados}')
print(f'Suspendieron: {denegados}')

