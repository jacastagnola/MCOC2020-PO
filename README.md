# MCOC2020-PO
Marca

  •	Asus

Modelo

  •	TUF GAMING FX504GD_FX80GD

Tipo

  •	Notebook

Año adquisición

  •	 Enero 2019

Procesador

  •	Marca: Intel Core I5-8300H 8th Gen

  •	Velocidad 2.3 GHz

  •	4.00 GHz frecuencia turbo máxima

  •	4 núcleos

  •	8 subprocesos

Tamaños caches del procesador

  •	L1: 256 kB

  •	L2: 1.0 MB

  •	L3: 8.0 MB

Memoria RAM

  •	8 GB

  •	Velocidad 2667 MHz

  •	Tipo de memoria ddr3

Disco duro

  •	1 Tb

  •	HDD

Tarjeta de video

  •	NVIDIA GeForce GTX1050

  •	Memoria dedicada 8044

  •	Resolución 1920 x 1080

Internet 

  •	VTR Banda Ancha

# "Desempeño MATMUL"

![graficos rendimiento](https://user-images.githubusercontent.com/69158084/89698502-a7aae680-d8ef-11ea-96f2-eac3dbbe0870.png)

¿Como difiere del gráfico del profesor/ayudante?

• Comparando los graficos con el del profesor encuanto a los tiempos podemos observar que para las primeras matrices mas pequeñas el tiempo del profesor es mucho menor al mio siendo el del profesor cerca de los 0.1 ms y el mio siendo entre 0.1 s y 1 s . ademas se observa que el posee unos peaks del grafico de tiempo entre tamaño de matriz 50 y 100 y yo entre 20 y 50

¿A qué se pueden deber las diferencias?

• Estas diferencias se deben a las capacidades de cada computador ya que el profesor posee 32 Gb de ram y yo solo posee 8 Gb lo que puede explicar la diferencias. Ademas el profesor al tener memorias ssd tiene una velocidad de escritura mas rapida lo que tambien explica las diferencias de rendimiento

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

• El grafico de memoria es lineal porque cada unidad de una matriz ocupa 8 bytes y al aumentar el numero de unidades de una matriz este aumenta linealmente. En el caso del grafico del tiempo transcurrido este depende de mas factores como que procesos estan corriendo en paralelo al correr el programa y ademas cada vez que parte un proceso el computador lo hace de manera distinta. 

¿Qué versión de python está usando?

  • Python 3.7.6
  
¿Qué versión de numpy está usando?

  • Numpy 1.18.1
  
Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.

  • se usaron 8 procesadores logicos.
  
  
  ![procesadores3](https://user-images.githubusercontent.com/69158084/89698842-60bdf080-d8f1-11ea-8dcc-f9f0e1e89145.png)
  
  
  # "Desempeño MIMATMUL"
  
  
  

