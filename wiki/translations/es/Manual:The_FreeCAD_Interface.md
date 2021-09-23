# Manual:The FreeCAD Interface/es
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">


{{Manual:TOC/es}}

FreeCAD utiliza el [Qt framework](https://en.wikipedia.org/wiki/Qt_(software)) para dibujar y gestionar su interfaz. Este framework se utiliza en una amplia gama de aplicaciones, por lo que la interfaz de FreeCAD es muy clásica y no presenta ninguna dificultad especial para su comprensión. La mayoría de los botones son estándar y se encontrarán donde los esperas **Archivo → Abrir, Editar → Pegar, etc**. Este es el aspecto de FreeCAD cuando lo abres por primera vez, justo después de la instalación, mostrando el centro de inicio:


</div>

![](images/FreeCAD-v0-18-FirstStart.png )

El centro de inicio es una conveniente \"pantalla de bienvenida\", que muestra información útil para los recién llegados, como los últimos archivos en los que has estado trabajando, las novedades en el mundo de FreeCAD, o información rápida sobre los Ambientes de trabajo más comunes. También te notificará si una nueva versión estable de FreeCAD está disponible.

Después de un tiempo, cuando estés más familiarizado con FreeCAD, puede que hayas hecho cambios en las preferencias para que cuando FreeCAD se inicie te encuentres directamente en uno de los bancos de trabajo con un nuevo documento abierto. O, simplemente cierra la pestaña de la página de inicio y crea un nuevo documento:

![](images/FreeCAD-v0-18-NewProject.png )

### Ambientes de trabajo 

Observa que algunos de los iconos han cambiado entre las dos capturas de pantalla anteriores. Aquí es donde entra en juego el concepto más importante utilizado en la interfaz de FreeCAD: Las ambientes de trabajo.

Ambientes de trabajo son grupos de herramientas (botones de la barra de herramientas, menús y otros controles de la interfaz) que se agrupan por especialidad. Piensa en un taller en el que hay diferentes personas trabajando juntas: Una persona que trabaja con el metal, otra con la madera. Cada uno de ellos tiene, en su taller, una mesa separada con herramientas específicas para su trabajo. Sin embargo, todos pueden trabajar en los mismos objetos. Lo mismo ocurre en FreeCAD.

El control más importante de la interfaz de FreeCAD es el selector de Ambiente de trabajo, que se utiliza para cambiar de un Ambiente de trabajo a otro:

![](images/FreeCAD-v0-18-WorkbenchMenu.png )

Las ambientes de trabajo a menudo confunden a los nuevos usuarios, ya que no siempre es fácil saber en qué ambiente de trabajo buscar una herramienta específica. Pero son rápidos de aprender, y después de un corto tiempo se sentirá natural \-- dándose cuenta de que es una manera conveniente de organizar la multitud de herramientas que FreeCAD tiene para ofrecer. Las ambientes de trabajo también son totalmente personalizables (ver más abajo). La misma herramienta puede aparecer en más de un ambiente de trabajo. El icono del botón para una herramienta en particular siempre será el mismo sin importar en qué ambiente de trabajo aparezca.

Más adelante en este manual, también encontrará una tabla que muestra el contenido de todos las ambientes de trabajo.

### La interfaz 

Veamos mejor las diferentes partes de la interfaz:

![](images/FreeCAD-v0-18-Cube.png )

-   **La vista 3D** es el componente principal de la interfaz; es donde se dibujan y manipulan los objetos con los que se trabaja. Puede tener varias vistas del mismo documento (o de los mismos objetos), o varios documentos abiertos al mismo tiempo. Cada una de estas vistas puede desacoplarse individualmente de la ventana principal. Puede seleccionar objetos o partes de objetos haciendo clic en ellos, y puede desplazar, ampliar y girar la vista con los botones del ratón. Esto se explicará con más detalle en el próximo capítulo.

Además del panel de vista 3D, están disponibles los siguientes paneles de información. Pueden hacerse visibles u ocultarse seleccionándolos desde **Ver → Paneles**. . El nombre del panel aparece en la esquina superior izquierda del panel cuando se muestra:

-   **La vista combinada** tiene dos pestañas:
    -   La pestaña Modelo le muestra el contenido y la estructura de su documento arriba y las propiedades (o parámetros) del objeto u objetos seleccionados abajo. Estas propiedades se dividen en dos categorías:
        -   Datos (propiedades que afectan a la propia geometría)
        -   Vista (propiedades que afectan al aspecto de la geometría en la pantalla).
    -   La pestaña de Tareas es donde FreeCAD te pedirá valores específicos para el banco de trabajo y la herramienta que estés utilizando en ese momento. Por ejemplo, introduciendo un valor de \'longitud\' cuando se está utilizando la herramienta [Ambiente de trabajo Borrador Hierramenta Línea](Draft_Line/es.md). Se borrará y volverá a la pestaña Modelo después de que se pulse el botón **OK** (o Cancelar). Al hacer doble clic en el objeto relacionado en la pestaña Modelo, normalmente se volverá a abrir la pestaña Tareas correspondiente para modificar los ajustes.
        La pestaña Tareas a veces tiene efectos secundarios desconcertantes y frustrantes. Si la pestaña Tareas no está vacía, algunas operaciones de FreeCAD no funcionarán como se espera. Por ejemplo, si tienes un solo objeto en tu modelo como un cubo, al hacer doble clic en él se abrirá la pestaña Tareas para permitirte modificar los parámetros que caracterizan al cubo. Si tienes la [Vista de selección](#Vista_de_selección.md) abierta, verás el nombre interno del cubo listado allí. Todo el cubo se volverá verde en el panel 3D, indicando que todo el cubo está seleccionado. Al hacer clic en el fondo se deseleccionará todo el cubo y se borrará la vista de selección. Hasta ahora, este es un comportamiento normal. Sin embargo, si ahora hace clic en una cara del cubo, en lugar de estar seleccionada esa cara, no se seleccionará nada --- porque la pestaña Tareas no se ha completado. Incluso si no has hecho ninguna modificación a los parámetros allí, FreeCAD está esperando el botón **OK** (u otro) en la pestaña Tareas.

-   **La vista de informe** está normalmente oculta, pero es una buena idea abrirla ya que listará cualquier información, advertencias o errores para ayudarte a descifrar (o depurar) lo que puedes haber hecho mal.
-   **La consola de Python** también está oculta por defecto. Aquí es donde puedes interactuar con el contenido del documento usando el [lenguaje Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29). Dado que cada acción que haces en la interfaz de FreeCAD ejecuta en realidad un trozo de código Python, tener esto abierto te permite ver cómo se desarrolla el código en tiempo real --- permitiéndote una maravillosa y fácil manera de aprender un poco de Python en el camino, casi sin darte cuenta.
-   **La vista de árbol** sólo muestra el árbol de objetos que aparece bajo la pestaña Modelo en la vista combinada. Normalmente está oculto.
-   **La vista de propiedades** sólo muestra la información de las propiedades de los objetos que aparecen en la parte inferior de la vista combinada. Normalmente está oculta.
-   La vista de selección muestra los nombres de los objetos que están seleccionados en ese momento. Estos son los objetos a los que se aplicará una operación del banco de trabajo. Puede utilizarse para refinar la selección deseleccionando algunos de esos objetos antes de aplicar una operación del banco de trabajo. La vista de selección también puede utilizarse para buscar objetos por su nombre y luego seleccionarlos. Por defecto, la vista de selección está oculta. Aunque a menudo se puede determinar el objeto(s) actualmente seleccionado(s) mirando el árbol de objetos en la pestaña Modelo de la vista combinada, para las operaciones complejas que requieren múltiples selecciones y en las que la selección es difícil, es útil hacer visible esta vista para poder ver las etiquetas y contar los objetos seleccionados.

![](images/FreeCAD-v0-18-ExtrudeTask.png )

### Personalización de la interfaz 

La interfaz de FreeCAD es altamente personalizable. Todos los paneles y barras de herramientas pueden moverse a diferentes lugares o apilarse unos sobre otros. También pueden cerrarse y reabrirse cuando sea necesario desde el menú Ver o haciendo clic con el botón derecho en un área vacía de la interfaz. Sin embargo, hay muchas más opciones disponibles, como la creación de barras de herramientas personalizadas con herramientas de cualquiera de las ambientes de trabajo, o la asignación y modificación de atajos de teclado.

Estas opciones de personalización avanzada están disponibles en el **Herramientas → Personalizar**:

![](images/FreeCAD-v0-18-CustomizeInterface.png )

**Leer más**

-   [Cómo empezar con FreeCAD](Getting_started/es.md)
-   [Personalizar la interfaz](Interface_Customization/es.md)
-   [Ambientes de trabajo](Workbenches/es.md)
-   [Más sobre Python](https://www.python.org)


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > Manual:The FreeCAD Interface/es
