---
- GuiCommand:/es
   Name:Arch Nest   Name/es:Arch Nest
   MenuLocation:Arch → Panel tools → Nest
   Workbenches:[Arch](Arch_Workbench/es.md)
   SeeAlso:[[Arch Panel/es]], [[Arch Panel Sheet/es]]
---

# Arch Nest/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Nido permite seleccionar una forma plana para ser un contenedor y una serie de otras formas planas para organizarlas dentro del espacio definido por la forma del contenedor. Esto es típicamente necesario para las operaciones CNC, donde se desea cortar una serie de piezas de un panel base, y necesita organizar esas piezas de la mejor forma compacta posible para que ocupen menos espacio en el panel.


</div>

El algoritmo detrás de la herramienta Nido está en constante evolución y actualmente no está totalmente optimizado. En el futuro, el rendimiento de esta herramienta debería ser mucho mejor.

<img alt="" src=images/Arch_Nest_example.jpg  style="width:600px;">

*La imagen de arriba muestra una serie de formas antes y después de la operación de anidación*

## Utilización


<div class="mw-translate-fuzzy">

1.  Presiona el botón **<img src="images/_Arch_Nest.png" width=16px> [Arch Nest](Arch_Nest/es.md)
**
2.  Seleccione un objeto para ser el contenedor. Este objeto debe ser plano, y, de momento, rectangular
3.  Haz clic en el botón \"Elegir contenedor\" para usar ese objeto como contenedor
4.  Seleccione una serie de otros objetos planos que desee colocar dentro del contenedor. Todos estos objetos deben ser planos y en el mismo plano que el contenedor.
5.  Ajuste las opciones deseadas a continuación
6.  Inicie el proceso de cálculo
7.  Al final del cálculo, haga clic en el botón **Vista previa** para crear una vista previa temporal del resultado.
8.  Si desea aplicar el resultado (mueva y gire las formas reales en su lugar), haga clic en Aceptar.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_Nest_panel.jpg  style="width:600px;">


</div>

## Notas

-   Todos los objetos deben tener una cara
-   Por el momento, la herramienta solo funcionará con objetos planos que tengan la misma orientación.
-   Por el momento, el contenedor debe ser rectangular.
-   En este momento, el margen/espacio entre las piezas aún no está implementado
-   El cálculo puede tomar mucho tiempo con muchos objetos. Eso se optimizará en el futuro


<div class="mw-translate-fuzzy">


{{docnav/es|[Panel Sheet](Arch_Panel_Sheet.md)|[Frame](Arch_Frame.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Panel_Sheet.svg |IconC=Workbench_Arch.svg |IconR=Arch_Frame.svg}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Nest/es
