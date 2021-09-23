---
- GuiCommand:/es
   Name:PartDesign WizardShaft
   Name/es:DiseñoPiezas AsistenteEje
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
---

# PartDesign WizardShaft/es

## Descripción

Esta herramienta permite crear un árbol a partir de una tabla de valores y analizar las fuerzas y los momentos. Puede iniciar el asistente desde el menú Diseño de la pieza **DiseñoPieza → <img src=images/PartDesign_WizardShaft.svg style="width:20px"> Asistente Diseño Ejes...**.

El asistente se iniciará y mostrará una tabla por defecto, la parte eje correspondiente y los gráficos de fuerza/momento.

<img alt="" src=images/WizardShaft_Part.jpg  style="width:780px;"> 

La parte superior de la ventana está ocupada por la tabloa. Está organizada en en columnas numeradas que se corresponden a segmentos del eje. Un segmento del eje se caracteriza por tener una longitud y diámetro determinados. La ventana principal muestra dos pestañas. Una es la ventana del archivo de pieza del eje (una operación de revolución), mostrada en la imagen superior. La segunda pestaña muestra un gráfico de las fuerzas de corte y los momentos creados por las cargas definidas en la tabla.

<img alt="" src=images/shaftwizard1.jpg  style="width:1024px;"> 

## Prerrequisitos

El asistente diseño ejes depende de la biblioteca [matplotlib](http://matplotlib.org/) para crear y mostrar los gráficos de fuerza cortante y momento flector. En los sistemas basados en Debian/Ubuntu, está disponible a través del paquete python-matplotlib.

## Parámetros

Para cada segmento de eje, se pueden definir los siguientes parámetros

-   Longitud del segmento
-   Diámetro del segmento
-   Tipo de carga. Observa que tienes que designar sobre la entrada deseada en el menú después de acceder a él, en otro caso no se seleccionará!
    -   Ninguna: Sin cargas
    -   Fija: El extremo del eje está fijo (por ejemplo soldado a otra pieza). Este tipo de carga sólo puede definirse para el primer o el último segmento.
    -   Estática: Una carga estática en este segmento del eje
-   Carga en el segmento del eje
-   Ubicación en la que se aplica la carga al segmento. La ubicación se cuenta desde la arista izquierda del segmento

(Existen otras filas y tipos de cargas pero aún no se ha implantado dicha funcionalidad)

## Menús

Para añadir un nuevo segmento de eje, pulsa con el botón derecho en un espacio en blanco a la derecha de la tabla, y selecciona \"Añadir columna\".

## Limitaciones

-   No es posible tener segmentos adyacentes del eje con el mismo diámetro.

## Funcionalidad planeada 

-   Chaflanes y redondeos conducidos por la tabla sobre las aristas del eje
-   Reconocer un asistente de eje creado previamente e iniciar los valores de la tabla a partir de él
-   Cálculo de tensiones del eje
-   Visualización de cargas sobre el eje (puede utilizar la misma funcionalidad que en el módulo de CAE)
-   Definición de cargas como un Objeto de Documento (puede utilizar la misma funcionalidad que en el módulo de CAE)
-   Base de datos de materiales
-   Permitir cargas en la dirección Z así como en la dirección Y (requiere la definición de cargas como Objeto de Documento, en otro caso la tabla sería demasiado larga)


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/es
