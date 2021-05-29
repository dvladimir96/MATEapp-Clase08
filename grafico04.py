import matplotlib.pyplot as plt
 
ej_Y = ['Programacion', 'Ciencia de datos', 'Matematicas', 'Ingenieria'] 

ej_X = [76,31,45,57]
 
plt.barh(ej_Y, ej_X, color="green")

plt.ylabel('Numero de Empleados')

plt.xlabel('Habilidades')

plt.title('Empleados con habilidades')

plt.show()