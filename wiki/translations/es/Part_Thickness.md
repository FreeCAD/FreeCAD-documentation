---
- GuiCommand:/es
   Name:Part Thickness
   Name/es:Part Espesor
   MenuLocation:Pieza → Espesor
   Workbenches:[Part](Part_Workbench/es.md)
   SeeAlso:[Part Offset](Part_Offset.md)
---

# Part Thickness/es


</div>

## Descripción

La herramienta <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Espesor](Part_Thickness/es.md) trabaja sobre una forma sólida y la transforma en un objeto hueco, dando a cada una de sus caras un espesor definido. Con algunos sólidos permite un ahorro de trabajo significativo, pues evita hacer extrusiones y vaciados.

## Uso

1.  Crear un sólido.
2.  Seleccionar una o más caras.
3.  Pinchar sobre el botón de la herramienta **<img src="images/Part_Thickness.svg" width=16px> '''Part Espesor'''** o Utilidad para aplicar un espesor.
4.  Seleccionar los parámetros (ver [Opciones](#Options/es.md)).
5.  Pinchar **OK** para confirmar, creando la operación y saliendo de la función.
6.  En la tabla de Propiedades, ajustar los parámetros que sean necesarios.

## Opciones

-   Espesor: Espesor de la pared del objeto resultante. Seleccionar el valor deseado.
    -   Un valor positivo creará el espesor de las caras hacia afuera.
    -   Un valor negativo creará el espesor de las caras hacia adentro.
-   Modo:
    -   Piel: Seleccionando esta opción se obtiene un objeto como un jarrón, con un vaciado desde la cara superior, pero conservando la cara inferior.
    -   Tubo: Seleccionando esta opción se obtiene un objeto como un tubo, sin las caras superior ni inferior. En este caso es conveniente seleccionar las caras a ser eliminadas antes de iniciar la herramienta. Se pueden utilizar los botones de vistas predeterminadas o usar las teclas numéricas como ayuda a la selección de caras
    -   RectoVerso:
-   Tipo de unión:
    -   Arco: Cuando el valor de espesor es positivo, quita los bordes exteriores y crea un redondeo de las aristas de un radio igual al espesor definido. Si el valor de espesor es negativo y lo aplica hacia el interior, hace los bordes rectos.
    -   Tangente:
    -   Intersección: Hace los bordes siempre rectos, sin redondeos, independientemente de si el valor de espesor es positivo o negativo.
-   Intersección:
-   Auto-intersección: Habilita la auto-intersección.
-   Caras / Hecho: Permite seleccionar las caras que se tienen que quitar, pulsando sobre ellas con el ratón. Pinchar después sobre Hecho.
-   Actualizar vista: Actualiza automáticamente la vista en tiempo real.

## Notes


<div class="mw-translate-fuzzy">

Las formas complejas pueden producir extraños e impredecibles resultados. Inspeccione cuidadosamente la forma resultante y grabe su trabajo antes de aplicar la operación.


</div>

## Enlaces

Puede ver un buen ejemplo de como usar esta herramienta en el foro: [Re: Help designing a simple enclosure](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)

## Ejemplos

**Tubo**

1.  Crear **<img src="images/Part_Cylinder.svg" width=16px> [Cilindro](Part_Cylinder.md)** de radio 10mm y altura 20mm.
2.  Seleccionar las caras superior e inferior del cilindro.
3.  Pulsar sobre el botón **<img src="images/Part_Thickness.svg" width=16px> Espesor** (no es necesario cambiar los ajustes por defecto) y confirmar **OK**.

Notas:

-   Para conseguir este mismo objeto, considere usar la herramienta**<img src="images/Part_Tube.svg" width=16px> [Tubo](Part_Tube.md)** en vez de la de espesor. {{Version/es|0.19}}
-   Seleccionar solamente la superficie superior del cilindro para crear un contenedor.

-   Creación de un contenedor:

![](images/ThicknessEsempio1.png )

Seleccionar la cara superior del cilindro.

![](images/ThicknessEsempio2.png )

Ajustar los valores de espesor y modo piel.

**Anexos**

![](images/ThicknessEsempio3.png )

Vista del perfil del contenedor, donde se puede apreciar el espesor aplicado uniformemente a las caras restantes.

![](images/ThicknessEsempio4.png )

En este objeto se han seleccionado y eliminado dos caras adyacentes.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/es
