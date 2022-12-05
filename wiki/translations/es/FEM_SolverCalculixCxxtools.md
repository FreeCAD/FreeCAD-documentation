---
- GuiCommand:
   Name:FEM SolverCalculixCxxtools
   MenuLocation:Solve → Solver CalculiX Standard
   Workbenches:[FEM](FEM_Workbench.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM SolverCalculixCxxtools/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

CalculiXccxTools permite usar el solucionador [CalculiX](http://dhondt.de/). Puedes usarlo para

1.  configurar los parámetros de análisis
2.  seleccionar directorio de trabajo
3.  Ejecutar el solucionador de CalculiX.


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  
    **<img src="images/FEM_Solver.png" width=24px> CalculiXccxTools
**objeto se crea automáticamente con la creación de **<img src="images/FEM_Analysis.png" width=24px> [Analysis container](FEM_Analysis.md)**. De lo contrario utilizar **Solve** → **Solver CalculiX Standard** , **X** keyso presione **S** luego las teclas **X**

2.  Opcionalmente, configure las propiedades de datos del objeto **<img src="images/_FEM_Solver.png" width=24px> CalculiXccxTools
**

3.  Haga doble clic en el objeto **<img src="images/_FEM_Solver.png" width=24px> CalculiXccxTools
**

4.  Seleccione el tipo de análisis

5.  Haga clic en **Write .inp file**

6.  Haga clic en **Run CalculiX**


</div>

## Opciones


<div class="mw-translate-fuzzy">

Al usar **Edit.inp file** puede mostrar y editar el archivo de entrada de CalculiX manualmente antes de ejecutar el análisis. En este caso, puede ser útil usar el parámetro \"Split Input Writer = true\".


</div>

## Propiedades


<div class="mw-translate-fuzzy">

Los valores por defecto se pueden configurar en el menú. **Edit** → **Preferences** → **FEM** → **CalculiX**


</div>


<div class="mw-translate-fuzzy">

-    **Analysis Type**:

    -   estática
    -   frecuencia
    -   Thermomech - para cargas mecánicas y térmicas.


</div>

-    **Beam Shell Result Output 3D**:

tenga en cuenta que CalculiX expande internamente los elementos 1D y 2D en elementos 3D para realizar el análisis FE

-   -   falso: los resultados de los elementos 1D y 2D se promediarán a los nodos de la malla 1D o 2D original (es decir, el haz puramente curvado mostrará 0 esfuerzos nodales debido al promediado)
    -   verdadero - la malla resultante contendrá elementos 1D y 2D expandidos a elementos 3D


<div class="mw-translate-fuzzy">

-    **Eigenmode High Limit**: Los valores propios por encima de este límite no serán calculados


</div>

-    **Eigenmode Low Limit**: Los valores propios por debajo de este límite no serán calculados

-    **Eigenmodes Count**: Número de modos propios más bajos para calcular

-    **Geometric Nonlinearity**:

    -   el análisis lineal - lineal se realizará si el modelo no contiene material no lineal
    -   no lineal - se realizará análisis no lineal


<div class="mw-translate-fuzzy">

-    **Iterations Control parameter Cutb**: define la segunda línea de parámetros de iteración avanzada en la tarjeta \* CONTROLS, utilizada cuando \"Iterations Control Parameter Time Use\" es verdadero


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Control Parameter Iter**: define la primera línea de parámetros de iteración avanzada en la tarjeta \* CONTROLS, utilizada cuando \"Iterations Control Parameter Time Use\" es verdadero


</div>


<div class="mw-translate-fuzzy">

-    **Iterations Control Parameter Time Use**-   true: activa \"Iterations Control Parameter Cutb\" y \"Iterations Control Parameter Iter\"


</div>

-    **Iterations Thermo Mech Maximum**:Número máximo de incrementos en el análisis termomecánico después del cual se detendrá el trabajo.

-    **Iterations User Defined Incrementations**:

    -   verdadero - el control de incremento automático se desactivará con el parámetro DIRECTO
    -   falso - el control de incremento será automático


<div class="mw-translate-fuzzy">

-    **Iterations User Defined Time Step Length**:

    -   true: activa los parámetros \"Time End\" y \"Time Initial Step\"


</div>


<div class="mw-translate-fuzzy">

-    **Material Nonlinearity**:

    -   lineal: solo se incluirán propiedades de material lineales en el análisis
    -   no lineal - se usarán propiedades de materiales no lineales de**<img src="images/FEM_MaterialMechanicalNonlinear.png" width=24px> '''[Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md)'''** object


</div>


<div class="mw-translate-fuzzy">

-    {{PropertyData | Matrix Solver Type}}: tipo de solucionador para resolver el sistema de ecuaciones dentro del análisis FE. Puede afectar significativamente la velocidad de cálculo y las demandas de memoria. La idoneidad depende de su modelo FE y hardware disponible

    -   predeterminado: selecciona automáticamente el solucionador de matrices dependiendo de los solucionadores disponibles (probablemente será Spooles)
    -   spooles - solucionador directo con soporte de múltiples CPUs. El número de CPU debe configurarse en {{KEY | Edit}} → {{KEY | Preferences}} → {{KEY | FEM}} → {{KEY | CalculiX}} → Valores predeterminados del solucionador → Número de CPU para usar)
    -   iterativescaling: solucionador iterativo con menos demandas de memoria, adecuado si el modelo contiene principalmente elementos 3D
    -   iterativecholesky - solucionador iterativo con preacondicionamiento con y con poca demanda de memoria, adecuado si el modelo contiene principalmente elementos 3D


</div>

-    **Split Input Writer**:

    -   falso: escriba toda la entrada en un archivo \* .inp para ser utilizado por el solucionador de CalculiX
    -   true - divide las entradas del solucionador en más archivos \* .inp, que pueden aclarar la edición manual

-    **Thermo Mechanical Steady State**:

    -   verdadero - análisis termo-mecánico de estado estable
    -   Falsa - Análisis termo-mecánico transitorio.


<div class="mw-translate-fuzzy">

-    **Time End**: período de tiempo del paso, utilizado cuando el parámetro \"Iteraciones incrementadas definidas por el usuario\" o \"Iteraciones definidas por el usuario Tiempo de paso\" es verdadero


</div>


<div class="mw-translate-fuzzy">

-    **Time Initial Step**: incremento de tiempo inicial del paso, que se usa cuando el parámetro \"Iteraciones de incrementos definidos por el usuario\" o \"Iteraciones de tiempo de paso definidas por el usuario\" es verdadero


</div>

-    **Working Dir**: Ruta al directorio de trabajo que se utilizará para los archivos de análisis de CalculiX.

## Limitaciones

When running a CalculiX, you might end up with **error 4294977295**. This means you don\'t have enough RAM space. You have then 2 options:

1.  reduce the number of mesh nodes, preferably by omitting geometry that is not absolutely necessary for your analysis
2.  buy more RAM for your PC

## Notas

La documentación original de CalculiX se puede encontrar en <http://dhondt.de/> in the \"ccx\" paragraph.

## Programación





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/es
