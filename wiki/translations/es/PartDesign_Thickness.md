---
- GuiCommand   */es
   Name   *PartDesign Thickness
   Name/es   *PartDesign Espesor
   MenuLocation   *Part Design → Apply a dress up feature → Espesor
   Workbenches   *[PartDesign](PartDesign_Workbench/es.md)
   Version   *0.17
   SeeAlso   *[Part Thickness](Part_Thickness/es.md)
---

# PartDesign Thickness/es


</div>

## Descripción

La herramienta **Espesor** trabaja sobre un cuerpo sólido y lo transforma en un objeto hueco con una pared de un grosor determinado, con al menos una cara abierta, dando a cada una de sus caras restantes un espesor uniforme. Con algunos sólidos permite un ahorro significativo de trabajo, evitando hacer extrusiones y vaciados innecesarios.

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width   *600px;"> 
*The thickness tool applied to a face (B) of a solid (A), resulting in the hollow object (C).*

## Uso


<div class="mw-translate-fuzzy">

1.  Seleccionar una o más caras del Body (cuerpo) activo.
2.  Presionar el botón **<img src="images/PartDesign_Thickness.svg" width=24px> '''Espesor'''**.
3.  Definir los **Parámetros de espesor** (Ver [Opciones](#Options/es.md)).
4.  Para añadir más caras a abrir, presionar el botón **Añadir cara** y seleccionarla(s) en [3D view](3D_view/es.md).
5.  Para eliminar una cara seleccionada previamente, presionar el botón **Eliminar cara** y seleccionar una nueva cara en la vista 3D, o pulsar con el botón derecho en la etiqueta del nombre de la cara de la lista y seleccionar *Remove*.
6.  Confirmar con **OK**.


</div>

## Opciones

-   **Espesor**   * Grosor de la pared del objeto resultante. Introducir el valor deseado en números positivos.
-   **Modo**
    -   *Piel*   * Seleccionando esta opción se obtiene un objeto como un jarrón, con un vaciado desde la cara superior, pero conservando la cara inferior.
    -   *Tubo*   * Seleccionando esta opción se obtiene un objeto como un tubo, sin las caras superior ni inferior. En este caso es conveniente seleccionar las caras a ser eliminadas antes de iniciar la herramienta. Se pueden utilizar los botones de vistas predeterminadas o usar las teclas numéricas como ayuda a la selección de caras.
    -   *Recto Verso*   *
-   **Tipo de unión**
    -   *Arco*   * Añade el espesor hacia el exterior de las paredes, quitando los bordes exteriores y creando un redondeo de las aristas de un radio igual al espesor definido.
    -   *Intersección*   * Cuando el espesor se aplica hacia afuera, crea los bordes rectos, sin redondear.
-   **Hacer el grosor hacia el interior**   * Al seleccionar esta casilla, el espesor es aplicado hacia el interior de las caras, con los bordes rectos, sin redondear.

## Limitaciones

-   Debe seleccionarse al menos una cara para ser abierta.
-   Si el espesor va hacia adentro, el valor debe de ser menor que la altura más pequeña del Body (cuerpo).
-   La operación podría fallar con formas complejas. En este contexto, la superficie, por ejemplo, de un cono, tiene que ser considerada como compleja.
    -   Las herramientas [Tubo aditivo](PartDesign_AdditivePipe/es.md) (barrido) o [Additive Loft](PartDesign_AdditiveLoft/es.md) (interpolación de secciones) podrían trabajar mejor para crear formas complejas.

## Ejemplo

1.  Crear una extrusión desde un boceto.
2.  Crear un segundo boceto sobre el plano XY.
3.  Crear una segunda extrusión desde el segundo boceto.

Como en las siguientes imágenes   *

![](images/Braga-primoPad.png )

![](images/Braga-secondoschizzo.png )

![](images/Braga-secondo_Pad.png )


<div class="mw-translate-fuzzy">

Seguidamente   *

1.  Seleccionar una cara circular.
2.  Pulsar el botón **<img src="images/PartDesign_Thickness.svg" width=24px> Espesor
**
3.  Añadir las otras caras circulares a la selección.


</div>

Resultado   * ![](images/Brga-spessore.png )

## Errores conocidos 


<div class="mw-translate-fuzzy">

-   BRep\_API   * Operación no realizada.
-   BRep\_Tool   *   * Ningún parámetro sobre el borde.
-   Fallos silenciosos.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/es
