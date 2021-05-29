from matplotlib import pyplot

paises = ["Estados Unidos", "Mexico", "Brasil", "Peru", "chile", "Bolivia"]

valores = [230000, 150000, 150000, 180000, 170000, 100000]

colores = ["purple", "green", "yellow", "red", "blue", "gray"]

pyplot.title("Producto Exportacion por Paises en el 2021")

pyplot.bar(paises, height= valores, color= colores, width= 0.5)

pyplot.show()