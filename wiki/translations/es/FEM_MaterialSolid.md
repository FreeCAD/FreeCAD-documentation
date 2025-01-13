# FEM MaterialSolid/es
---
 GuiCommand:   Name: FEM MaterialSolid    MenuLocation: Model , FEM material for solid   ---


</div>



## Descripción


<div class="mw-translate-fuzzy">

Agrega propiedades de material a una parte.


</div>

![](images/FEMMaterialSolidProperties.png ) 
*The FEM material task panel*




<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

-   Haga clic en ![ 32px](images/_FEM_MaterialSolid.png ) o seleccione {{KEY | Model}} → {{KEY | <img src="images/_FEM_MaterialSolid.png_" width= 32px> Material de FEM para sólidos}} desde el menú superior.
-   Haga doble clic en el objeto {{KEY | <img src="images/_FEM_MaterialSolid.png_" width= 32px> SolidMaterial}} creado

![](images/FEMMaterialProperties.PNG )

-   -   Seleccione un material. Para el análisis mecánico de ingeniería, {{KEY | CalculiX-Steel}} es una opción típica.
    -   Siempre que esté aplicando material a todo el objeto, no seleccione ninguna entidad geométrica (deje la lista de referencias vacía). El material se aplicará a todo el modelo. De lo contrario, asigne material a partes del modelo en particular manualmente seleccionando algunas de ellas para cada material insertado, pero no deje ninguna parte del modelo sin el material asignado.
    -   Puedes ajustar las propiedades del material, como la densidad, el módulo de Young, el Coeficiente de Poisson, etc., sin embargo, la mayoría de los materiales comunes ya están disponibles en los ajustes preestablecidos y no necesitan ningún ajuste.
    -   Si realiza modificaciones, puede guardar su material personalizado.
-   Haga clic en **Close** para cerrar el cuadro de diálogo y crear **<img src="images/FEM_MaterialSolid.png" width=32px> SolidMaterial** objeto


</div>



## Notas


<div class="mw-translate-fuzzy">

1.  El material mecánico utiliza la tarjeta \* MATERIAL en CalculiX. Los detalles sobre el material mecánico se explican enhttp://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html


</div>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/es
