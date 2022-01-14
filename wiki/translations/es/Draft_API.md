# Draft API/es
<div class="mw-translate-fuzzy">

Estas funciones son parte del módulo de Draft (Borrador) y pueden utilizarse en archivos de guión y macros o desde el interprete de Python, una vez se halla importado el módulo Draft.


</div>

These functions are part of the [Draft Workbench](Draft_Workbench.md) and can be used in [macros](macros.md) and from the [Python](Python.md) console once the `Draft` module has been imported.

Ejemplo: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction/es|cut|FreeCAD.Object, FreeCAD.Object|Devuelve un objeto cut creado a partir de la diferencia de 2 objetos dados. Los objetos originales se ocultan.|El nuevo objeto creado}}


{{APIFunction/es|extrude|FreeCAD.Object, Vector|Extruye el objeto dado en la dirección indicada por el vector. El objeto original se oculta.|El nuevo objeto creado}}


{{APIFunction/es|formatObject|FreeCAD.Object, [FreeCAD.Object]|Esta función aplica  al objeto de objetivo indicado las propiedades actuales establecidas en la barra del entorno Borrador (línea, color y ancho de línea), o copia las propiedades a un segundo objeto si se indica. También pone el objeto en el grupo "En construcción" si el botón "Construcción" está presionado.|Nada}}


{{APIFunction/es|fuse|FreeCAD.Object, FreeCAD.Object|Devuelve un objeto creado a partir de la unión de dos objetos dados. Si los objetos son coplanares, se utiliza una polilínea de borrador especial, en otro caso el objeto final es una fusión de piezas estándar.|El nuevo objeto creado}}


{{APIFunction/es|getDraftPath|[string]|Devuelve la ruta del usuario o sistema desde donde se está ejecutando el módulo Borrador. Si se suministra una sub-ruta o un nombre de archivo, devuelve la ruta completa a la sub-ruta dentro del módulo Borrador.|Una ruta de archivo}}


{{APIFunction/es|getGroupContents|list|Escanea recursivamente por la lista de grupos indicada. Si se encuentran los grupos, su contenido es añadido a la lista.|Una lista de objetos de FreeCAD}}


{{APIFunction/es|getRealName|string|Quita los números de rastreo a partir de un nombre de objeto.|El nombre del objeto desnudado}}


{{APIFunction/es|getSelection| |Devuelve la selección actual de FreeCAD.|La selección actual de FreeCAD.}}


{{APIFunction/es|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|Crea un objeto circunferencia con un radio dado. Si se indica una ubicación, se utiliza. Si facemode es False, la circunferencia se muestra como una polilínea, en otro caso como una cara. Si startangle y endangle se indicad (in grados), se utilizan y el objeto aparece como un arco.|El nuevo objeto creado.}}


{{APIFunction/es|makeDimension|Vector, Vector, [Vector] o FreeCAD.Object, int, int, [Vector]|Creates un objeto Dimension o Cota midiendo la distancia entre el primer y segundo vector, con la línea de cota pasando por el tercer vector si se indica. Se utilizará el ancho de línea y el color actuales. En lugar de 2 vectores, puedes pasarle un objeto de FreeCAD, y dos enteros (y opcionalmente un vector por donde la línea de cota debe pasar). En este caso, la dimensión se asociará con el objeto, y medirá dos de sus vértices, indicados por los dos números de índice.|El nuevo objeto creado.}}


{{APIFunction/es|makeLine|Vector, Vector|Crea una línea entre los dos objetos dados. Se utilizará el ancho de línea y color de la barra de herramientas de Borrador.|El nuevo objeto creado.}}


{{APIFunction/es|makeRectangle|length, width, [placement], [facemode]|Crea un objeto rectángulo con longitud en dirección X y altura en dirección Y. Si se indica una ubicación, se utiliza. Si facemode es False, el rectángulo se muestra como una polilínea, en caso contrario como una cara. Se utilizan el ancho de línea y color de la barra de herramientas de Borrador.|El nuevo objeto creado.}}


{{APIFunction/es|makeText|string o list, [Vector], [screenmode]|Crea un objeto de texto, en la posición indicada si se proporciona un vector, conteniendo la cadena de texto o cadenas dadas en la lista, una cadena de texto por línea. Se utilizan el color actual de la barra de herramientas Borrador y la altura de texto y fuente especificadas en las preferencias. Si screenmode es True, el texto siempre mira en la dirección de la vista, en otro caso se sitúa sobre el plano XY.|El nuevo objeto creado.}}


{{APIFunction/es|makeWire|list o Part.Wire, [closed], [placement], [facemode]|Crea un objeto polilínea a partir de la lista de vectores indicada o a partir de la polilínea indicada. Si closed es True o si el primer y último punto son idénticos, la polilínea es cerrada. Si facemode es True (y la polilínea es cerrada), la polilínea se mostrará rellena. Se utilizará el ancho de línea y color de la barra de herramientas Borrador.|El nuevo objeto creado.}}


{{APIFunction/es|move|FreeCAD.Object o list, Vector, [copymode]|Mueve el objeto dado o los objetos contenidos en la lista dada en la direccióny distancia indicada por el vector dado. Si copymode es True, el objeto actual no se mueve, sino que se crea una copia en su lugar.|Los objetos (o sus copias si copymode era True).}}


{{APIFunction/es|precision| |Devuelve el valor de precisión de la configuración del usuario para el borrador.|Un entero.}}


{{APIFunction/es|rotate|FreeCAD.Object o list, angle, [center], [axis] ,[copymode]|Gira el objeto dado o los objetos contenidos en la lista indicada con el ángulo dado alrededor del centro si es indicado, utilizando eje como eje de rotación. Si se omite el eje, la rotación será alrededor del eje Z. Si copymode es True, los objetos actuales no se mueven, sino que se crea una copia en su lugar.|El objeto (o sus copias).}}


{{APIFunction/es|scale|FreeCAD.Object o list, vector, [center], [copymode]|Escala el objeto dado o los objetos contenidos en la lista dada con un factor de escala definido por el vector dado (en las direcciones X, Y y Z) alrededor del centro dado si es proporcionado. Si copymode es True, el objeto actual no se mueve, sino que se crea una copia en su lugar.|Los objetos (o sus copias).}}


{{APIFunction/es|select|FreeCAD.Object|Deselecciona todo y selecciona solo el objeto pasado|Nada.}}


{{APIFunction/es|shapify|FreeCAD.Object|Transforma una objeto forma paramétricas en no paramétrico.|El nuevo objeto.}}


{{APIFunction/es|draftify|FreeCAD.Object o list|Cambia el objeto dado o cada objeto de la lista dada en polilíneas paramétricas del borrador.|Nada.}}


{{APIFunction/es|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|Crea una representación SVG de los objetos dados. El atributo linemodifier es un factor de escala (en porcentajes) para el ancho de línea, y textmodifier para la altura del texto. También puedes opcionalmente proporcionar una tupla de vectores para definir una proyección plana, en otro caso la geometrís se proyectará sobre el plano XY.|Una cadena de texto conteniendo una representación SVG del objeto dado.}}


 




[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > [Draft](Draft_Workbench.md) > Draft API/es
