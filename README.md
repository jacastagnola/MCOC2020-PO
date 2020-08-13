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
  
  
  ![grafico rendimineto mimatmul](https://user-images.githubusercontent.com/69158084/89846329-e8546b00-db4e-11ea-9571-3805f8909ac8.PNG)
  

•Comparando los graficos la gran diferencia que se puede observar es el tiempo en el cual se demora en procesar la informacion que es mucha mas usando mimatmul que la funcion que ya viene en python. Debido a esto hice 10 corridas con matrices de tamaña maximo de 500x500 debido altiempo en que se demoraba en correr el programa. Para cada corrida se demoro un aproximado entre 3 a 5 minutos y esto por 10 lo hace bastante tiempo corriendo el programa. En cuanto al uso de memoria este fue muy similar al anterior.

• Comparando con los graficos del ayudante y profesor se puede observar es principalmente problema de hardware ya que el profesor posee una mayor memoria RAM y ademas discos SSD los cuales tienen una velocidad de lectura mucho mas rapida que un HDD el que uno posee.

• Podemos decir que el grafico de memoria no es lineal  ya que entran diferentes procesos a la vez los cuales despues de ciertas operaciones se ven saturados por la capacidad de procesamiento. Esto genera un aumento ni lineal en el grafico Log - Log entre el tiempo de procesamiento y el tamaño de las matrices. En cambio en el grafico memoria tamaño de matrices el Log-Log es lineal.

• Otro factor que afecta es como trabaja python ya que este no define las variables como int y tiene que ir chequeandpo cada vez que lee una linea debe cheaquear que tipo de variable es. Esto se debe a que python no compila antes de correr el programa como JAVA o C.

• Python 3.7.6

• Numpy 1.18.1

• se usaron 8 procesadores logicos.


![procesadores mimatmul](https://user-images.githubusercontent.com/69158084/89849066-b2ff4b80-db55-11ea-985d-1017e17bb248.PNG)


# Desempeño de INV

• Segun los programas realizados cada tipo de dato ocupa la siguiente cantidad de memoria en el computador

 * np.half: float 16 = 4 bytes
 * np.single: float 32 = 4 bytes
 * np.double: float 64 = 8 bytes
 * np.longdouble: float 64 = 8 bytes

• Caso 1 usando numpy.linalg.inv solo se realizaron los graficos np.single y np.double ya que numpy linalg no soportaba np.half(float16) y np.longdouble(float64). ademas se puede observa que el uso de datos de tipo np.double ocupan mas memoria que los de tipo np.single. Si observamos el tiempo el que posee una mayor variacion en este es el np.double.

![datos_timing_inv_caso_1_double](https://user-images.githubusercontent.com/69158084/90082002-b2dd8800-dcdc-11ea-988d-52cb6de1ea9a.png)

![datos_timing_inv_caso_1_single](https://user-images.githubusercontent.com/69158084/90082012-b8d36900-dcdc-11ea-847e-4586770b0707.png)


• Caso 2 usando scipy.linalg.inv con overwrite_a=False no hubo problemas con ningun dato y se lograron graficar los rendimientos de los 4 casos. al observar los graficos de tiempos de cada tipo de dato podemos observar que el que es mas estable es el double el cual no presenta peaks notorios despues los otros presentan peaks notorios pero el mas inesteble es el half. El dato tipo longdouble es el que mas ocupa meeria seguido por el double single y half.

![datos_timing_inv_caso_2_double](https://user-images.githubusercontent.com/69158084/90082284-55960680-dcdd-11ea-927f-335a445c5050.png)

![datos_timing_inv_caso_2_half](https://user-images.githubusercontent.com/69158084/90082302-66df1300-dcdd-11ea-90c0-7f98c25504f5.png)

![datos_timing_inv_caso_2_longdouble](https://user-images.githubusercontent.com/69158084/90082317-778f8900-dcdd-11ea-9cc9-d58b9d0741cf.png)

![datos_timing_inv_caso_2_single](https://user-images.githubusercontent.com/69158084/90082323-7c543d00-dcdd-11ea-987c-d54945619638.png)

• Caso 3

![datos_timing_inv_caso_3_double](https://user-images.githubusercontent.com/69158084/90087034-ce02c480-dce9-11ea-859b-340ea449ba8e.png)

![datos_timing_inv_caso_3_half](https://user-images.githubusercontent.com/69158084/90087062-dce97700-dce9-11ea-9142-fb45fb3c8601.png)
  
![datos_timing_inv_caso_3_longdouble](https://user-images.githubusercontent.com/69158084/90087089-ed015680-dce9-11ea-8887-52a273211ddb.png)
)

![datos_timing_inv_caso_3_single](https://user-images.githubusercontent.com/69158084/90087107-fa1e4580-dce9-11ea-9868-badd0ada8754.png)
