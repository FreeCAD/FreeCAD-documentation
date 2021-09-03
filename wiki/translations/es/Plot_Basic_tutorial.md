


<div class="mw-translate-fuzzy">


{{TutorialInfo/es
|Topic=Plot Workbench
|Level=Beginner
|Time=
|Author=
|FCVersion=
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

En este tutorial vamos a aprender a crear gráficos usando el módulo de graficado y la consola Python. Puedes aprender más sobre el [módulo de graficado aquí](Plot_Module/es.md).


</div>

<img alt="Ejemplo de gráfico" src=images/Plot_Trigonometric_Example.png  style="width:600px;">


<center>

Ejemplo de gráfico.


</center>


<div class="mw-translate-fuzzy">

En la imagen anterior puedes ver una muestra del gráfico que pretendemos generar. Mediante este tutorial aprenderás:

-   A crear un documento de gráfico mediante la consola de Python.
-   A graficar series de datos mediante la consola de Python.
-   A mostrar la malla.
-   A mostrar la legenda.
-   A configurar los títulos de las series usando [LaTeX](http://www.latex-project.org).
-   A configurar los títulos de los ejes usando [LaTeX](http://www.latex-project.org).
-   A configurar la apariencia de las series.
-   A guardar el gráfico como archivo de imagen.


</div>

## Graficar

El módulo de graficado no necesita de ningún documento de FreeCAD para poder comenzar a trabajar, simplemente despliega la consola de Python, o genera los [macros](Macros/es.md) oportunos y comienza a trabajar.


<div class="mw-translate-fuzzy">

### Crear un documento de gráfico {#crear_un_documento_de_gráfico}

Los gráficos son documentos especiales dentro de FreeCAD, y pueden ser creados bien manualmente, bien automáticamente cuando se pretende trazar graficos y todavía no existe un documento activo. Crear manualmente los gráficos tiene dos ventajas:

-   Puedes elegir la etiqueta de la ventana.
-   Puedes controlar facilmente en que documento se trazan los gráficos.


</div>

Para crear un documento de gráfico nuevo simplemente lanza los siguientes comandos desde la terminal:


```python
import Plot
Plot.figure("TrigonometricTest")
```

Esto creará un nuevo documento llamado **TrigonometricTest**. Éste nuevo documento ya contiene unos ejes. Cada documento de gráfico debe tener al menos un set de ejes que no se podrá borrar a menos que se entre en profundidad en la interfaz matplotlib.


<div class="mw-translate-fuzzy">

### Trazar curvas {#trazar_curvas}

Usted podría haber comenzado su trabajo en este punto, pues cuando se solicita al módulo de graficado que traze una curva sin existir un documento apropiado, el módulo genera uno nuevo, no obstante todos los consiguientes trazados se incluirán en el mismo documento hasta que se cree uno nuevo. Por esta razón es buena idea siempre tener controlado el número de documentos.

Lo primero que necesitamos para trazar las curvas es generar los datos:


</div>


```python
import math
t = range(0,101)
t = [tt/100.0 for tt in t]
s = [math.sin(2.0*math.pi*tt) for tt in t]
c = [math.cos(2.0*math.pi*tt) for tt in t]
```

Lo que creará tres vectores (con 101 puntos):

-   *t* = Tiempo en segundos.
-   *s* = Función seno.
-   *c* = Función coseno.

Para trazar las curvas correspondientes tan sólo será necesario lanzar los siguientes comandos:


```python
Plot.plot(t,s)
Plot.plot(t,c)
```

Lo que graficará los datos. El comando **plot** admite que se le pase el título de la serie como tercer argumento, no obstante como vamos a editar manualmente esos datos optaremos por no emplear esta propiedad.

## Configuración del gráfico {#configuración_del_gráfico}

### Mostrar la malla y la legenda {#mostrar_la_malla_y_la_legenda}

Cambie al [módulo de graficado](Plot_Module.md) mediante el menú Ver/Escenario. Cuando haya cargado el módulo podrá emplear la herramienta de mostrado/ocultado de la malla para mostrar la malla.


<div class="mw-translate-fuzzy">

![Icono de la herramienta para mostrar/ocultar la malla](images/Plot_Grid.png‎ )


<center>

Icono de la herramienta para mostrar/ocultar la malla.


</center>


</div>

Volviendo a presionar sobre el botón se vuelve a ocultar la malla. De la misma forma usted puede mostrar la legenda mediante la herramienta correspondiente.


<div class="mw-translate-fuzzy">

![Icono de la herramienta para mostrar/ocultar la legenda](images/Plot_Legend.png‎ )


<center>

Icono de la herramienta para mostrar/ocultar la legenda.


</center>


</div>


<div class="mw-translate-fuzzy">

Como observará la legenda está vacía debido a que las series no tienen asignado un título todavía. En el [módulo de graficado](Plot_Module.md) las series sin título asignado no son consideradas por la legenda, permitiendo crear líneas auxiliares dentro del gráfico.


</div>

### Establecer los títulos de las series {#establecer_los_títulos_de_las_series}

Con la herrameitna de edición de series usted puede editar algunos parámetros de las curvas trazadas.


<div class="mw-translate-fuzzy">

![Icono de la herramienta de edición de series](images/Plot_Series.png‎ )


<center>

Icono de la herramienta de edición de series.


</center>


</div>

Comenzaremos seleccionando la primera serie, para la cuál desmarcaremos la casilla **No label**, lo que hará que aparezca la serie en la legenda, y nos permitirá establecer el siguiente título:


```python
$y = \sin \left( 2 \pi t \right)$
```

Al estar [LaTeX](http://www.latex-project.org) soportado por [matplotlib](http://matplotlib.org) usted siempre podrá establecer los titulos y etiqutas haciendo uso de él. Establezca el siguiente título para la función coseno:


```python
$y = \cos \left( 2 \pi t \right)$
```

### Configurar la apariencia de las series {#configurar_la_apariencia_de_las_series}

Usted puede, con la misma herramienta, cambiar algunas propiedades del aspecto visual de sus curvas. Intente configurarlas como las de la imagen de ejemplo cambiando el color y el estilo de la línea.

### Configurar los títulos de los ejes {#configurar_los_títulos_de_los_ejes}

Con la herramienta de configuración de títulos usted puede establecer las etiquetas asociadas con cada set de ejes.


<div class="mw-translate-fuzzy">

![Icono de la herramienta de configuración de títulos](images/Plot_Labels.png‎ )


<center>

Icono de la herramienta de configuración de títulos.


</center>


</div>

Establezca los siguientes títulos:

-   Title = Trigonometric functions example
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$

Cambie también sus tamaños a 20.

## Guardando la imagen {#guardando_la_imagen}

Con la herramienta de salvado usted podrá guardar su trabajo en diferentes formatos.


<div class="mw-translate-fuzzy">

![Icono de la herramienta de guardado](images/Plot_Save.png‎ )


<center>

Icono de la herramienta de guardado.


</center>


</div>

Lo primero de todo seleccione el archivo donde desea guardar la imagen. Puede usted ayudarse del selector de archivo que se despliega cuando se presiona el botón a la derecha del editor de ruta.

También puede seleccionar el tamaño de la imagen de salida en pulgadas, por ejemplo puede elegir 11.7x8.3 correspondiente a un **DIN A4**. El parámetro DPI (puntos por pulgada) permite controlar la resolución de la imagen, por ejemplo 100 dpi creará una imagen de 1170x830 pixels. {{Tutorials navi}} {{Plot Tools navi}} 
