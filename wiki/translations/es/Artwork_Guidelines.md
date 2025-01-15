# Artwork Guidelines/es
## Introducción


**Nota:**

para todos los iconos del árbol de fuentes, ver [Obras de Arte](Artwork/es.md).


<div class="mw-translate-fuzzy">

Un icono de FreeCAD se compone de 6 elementos que pueden ser recordados por el acrónimo SALCHO: **S** troke, **A** lignment, **L** ighting, **C** olor, **H** ighlighting, **O** utline. (español: *Trazo*, *Alineación*, *Iluminación*, *Color*, *Resaltar*, *Contorno*)


</div>

He aquí un ejemplo concreto, aunque arbitrario:

![](images/FreeCAD_icon_example_details.svg )

  --- 
  A   El color de realce se utiliza para toda esta superficie para indicar que la luz cae desde arriba.
  B   El contorno oscuro obligatorio rodea la forma del icono para proporcionar un contraste de forma.
  C   Justo dentro del contorno, el trazo de iluminación (Color de realce) proporciona contraste en los fondos oscuros.
  D   Esta cara es principalmente el color base, pero un ligero gradiente desde la luz (arriba a la izquierda) hasta la base (abajo a la derecha) da la impresión de que la luz cae desde arriba a la izquierda.
  E   La resaltación aquí es el color base (un tono menos) para dar la impresión de que esta es la cara más alejada de la luz.
  F   Esta cara es como la D pero va desde la Base (arriba a la izquierda) hasta la Oscuridad (abajo a la derecha), para indicar que es la cara más alejada de la luz.
  --- 

Las siguientes secciones explican estos elementos con más detalle.

Este icono se muestra de la siguiente manera:

+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:64px;"> | 64 px, tamaño original, botones grandes.                                          |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:32px;"> | 32 px, tamaño medio, botones regulares.                                           |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:16px;"> | 16 px, pequeño tamaño, como aparece en el [vista árbol](Tree_view/es.md). |
+++



## Colores


**Obligatorio**

FreeCAD utiliza una paleta adaptada de la [Tango paleta](https://web.archive.org/web/20190921043652/http://tango.freedesktop.org/tango_icon_theme_guidelines). Cada color principal viene en 4 tonos: Resaltar, Base, Oscuro y Contorno. Observa que el Contorno no es completamente negro, sino una variación muy oscura de la Base.

+++++
| #fce94f         | #edd400         | #c4a000         | #302b00         |
| (252, 233, 79)  | (237, 212, 0)   | (196, 160, 0)   | (48, 43, 0)     |
| Butter 1        | Butter 2        | Butter 3        | Butter 4        |
+=================+=================+=================+=================+
| #8ae234         | #73d216         | #4e9a06         | #172a04         |
| (138, 226, 52)  | (115, 210, 22)  | (78, 154, 6)    | (23, 42, 4)     |
| Chameleon 1     | Chameleon 2     | Chameleon 3     | Chameleon 4     |
+++++
| #fcaf3e         | #f57900         | #ce5c00         | #321900         |
| (252, 175, 62)  | (245, 121, 0)   | (206, 92, 0)    | (50, 25, 0)     |
| Orange 1        | Orange 2        | Orange 3        | Orange 4        |
+++++
| #729fcf         | #3465a4         | #204a87         | #0b1521         |
| (114, 159, 207) | (52, 101, 164)  | (32, 74, 135)   | (11, 21, 33)    |
| Sky Blue 1      | Sky Blue 2      | Sky Blue 3      | Sky Blue 4      |
+++++
| #ad7fa8         | #75507b         | #5c3566         | #171018         |
| (173, 127, 168) | (117, 80, 123)  | (92, 53, 102)   | (23, 16, 24)    |
| Plum 1          | Plum 2          | Plum 3          | Plum 4          |
+++++
| #e9b96e         | #c17d11         | #8f5902         | #271903         |
| (233, 185, 110) | (193, 125, 17)  | (143, 89, 2)    | (39, 25, 3)     |
| Chocolate 1     | Chocolate 2     | Chocolate 3     | Chocolate 4     |
+++++
| #ef2929         | #cc0000         | #a40000         | #280000         |
| (239, 41, 41)   | (204, 0, 0)     | (164, 0, 0)     | (40, 0, 0)      |
| Scarlet Red 1   | Scarlet Red 2   | Scarlet Red 3   | Scarlet Red 4   |
+++++
| #34e0e2         | #16d0d2         | #06989a         | #042a2a         |
| (52, 224, 226)  | (22, 208, 210)  | (6, 152, 154)   | (4, 42, 42)     |
| FreeTeal 1      | FreeTeal 2      | FreeTeal 3      | FreeTeal 4      |
+++++
| #ffffff         | #eeeeec         | #d3d7cf         | #babdb6         |
| (255, 255, 255) | (238, 238, 236) | (211, 215, 207) | (186, 189, 182) |
| Snowy White     | Aluminium 1     | Aluminium 2     | Aluminium 3     |
+++++
| #888a85         | #555753         | #2e3436         | #000000         |
| (136, 138, 133) | (85, 87, 83)    | (46, 52, 54)    | (0, 0, 0)       |
| Aluminium 4     | Aluminium 5     | Aluminium 6     | Jet Black       |
+++++


<div class="mw-translate-fuzzy">



*Ejemplo de una familia de colores de 4 tonos (Camaleón)*


</div>

A selection of some key colors.

      
                                                                                                                                                          Use the Yellow tones for tools that create objects; for an example, see [Part](Part_Workbench.md) and [Draft Workbenches](Draft_Workbench.md).
  style=\"background-color:#729fcf;\|   style=\"background-color:#3465a4;\|   style=\"background-color:#204a87;\|   style=\"background-color:#0b1521;\|   Use the Blue tones for tools that modify objects; for an example, see [Part](Part_Workbench.md) and [Draft Workbenches](Draft_Workbench.md).
  style=\"background-color:#34e0e2\|    style=\"background-color:#16d0d2\|    style=\"background-color:#06989a\|    style=\"background-color:#042a2a\|    Use the Teal tones for view-related tools; for an example, see the [View Menu](Std_View_Menu.md).
  style=\"background-color:#ef2929\|    style=\"background-color:#cc0000\|    style=\"background-color:#a40000\|    style=\"background-color:#280000\|    Use the Red tones for Constraint related tools; for an example, see [Sketcher Workbench](Sketcher_Workbench.md).
      


<div class="mw-translate-fuzzy">

   
  style=\"width: 25%;\|¿Por qué limitarse a estos colores?   Restringir los colores a una paleta definida ayuda a evitar una iconografía heterogénea y mejora la legibilidad cuando hay muchos iconos.
  ¿Cómo utilizo la paleta de FreeCAD?                        Instalar [la paleta](https://drive.google.com/open?id=0B_xxY57wUEV-RWNaMHV2OGpoY00) es tan fácil como [copiarla en su carpeta de paletas de Inkscape](https://inkscape.org/en/learn/faq/#how-install-new-extensions-palettes-document-templates-symbol-sets-icon-sets-etc).
   


</div>



## Rejilla y ancho del trazo 


**Obligatorio**

Los iconos de FreeCAD tienen un tamaño nominal de 64 píxeles tanto en anchura como en altura. Cuando crees o edites un icono, asegúrate de que el tamaño del documento es de 64 x 64 con las unidades siendo píxeles (px). Dejar un margen interior de 2px de espacio vacío alrededor del área del documento es útil ya que evita efectos como el antialiasing (difuminado de los bordes). Es decir, el espacio utilizable para el icono debe considerarse de 60 x 60, y los bordes deben dejarse vacíos.

<img alt="" src=images/FreeCAD_icon_size.svg  style="width:128px;"> 
*Dibuja el icono dentro del área azul y todo funcionará bien.*

También se recomienda encarecidamente utilizar una rejilla visual que tenga una línea de rejilla menor cada píxel y una línea de rejilla mayor cada 2 píxeles. Los trazos del icono deben alinearse a lo largo de las intersecciones de la rejilla menor.

Los trazos no deben ser *más finos* que 2px, con tapas y esquinas redondeadas en la mayoría de los casos. Los trazos pueden ser *más gruesos*, pero es preferible que sean un múltiplo de 2px para minimizar la borrosidad de la escala.

<img alt="" src=images/FreeCAD_icon_stroke_2px.svg  style="width:320px;"> 
*Rejilla con trazos que son múltiplos de 2px.*

   
  ¿Por qué usar esta rejilla y tamaño de trazo?   Por razones históricas, FreeCAD utiliza un icono de 64x64 que luego se reduce. No es lo ideal, pero añade carácter. Como resultado, mantener las cosas alineadas a una rejilla de potencia de dos con espesores que son potencias de dos ayuda a evitar o al menos mitigar los problemas de anti-aliasing al re-escalar.
  ¿Cómo puedo cumplir con esto?                   Si está usando Inkscape, vaya a **Archivo → Propiedades del documento** y confirme que la anchura, la altura y las unidades de su página son correctas. Luego vaya a la pestaña **Rejillas**, haga clic en **Nuevo**, establezca las unidades a `px`, `Distancia X` y `Distancia Y` a 1 y `Major grid line every` a 2.
   



## Contorno


**Obligatorio**

Basándose en el color principal del icono, asegúrese de que hay un contorno oscuro de 2px, como se ha mencionado anteriormente. Esto funciona al unísono con el resaltado para asegurar un buen contraste de forma sobre múltiples tonos de fondo.

<img alt="" src=images/Draft_Point.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Point_backgrounds.svg  style="width:" height="128px;"> 
*El borde oscuro del icono es el contorno.*

   
  ¿Por qué es necesario el contorno?   El contorno es el esqueleto del que cuelga todo lo demás añadiendo contraste de forma. El uso del color del contorno o del color oscuro depende de la situación, pero sin esta línea, la gama de fondos en los que el icono es visible se limita drásticamente
  ¿Cómo puedo cumplir con esto?        Simplemente añada un trazo de 2px alrededor de cada parte del icono que será adyacente al color de fondo, es decir, el contorno es para trazos externos. En el caso de las formas que tienen un agujero en el centro, por ejemplo, un donut, el contorno debe añadirse también al agujero interior. Ajuste los nodos de su trazado a la rejilla siempre que sea posible, apuntando a las intersecciones menores de la rejilla.
   



## Resaltar


**Muy recomendable**

Usando el color de Resaltar, añada un trazo interno de 2px para ayudar a que ese contorno resalte. En los fondos oscuros, es este resaltado el que dará la forma al icono.

<img alt="" src=images/Draft_Move.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Move_backgrounds.svg  style="width:" height="128px;"> 
*El resaltado de la luz ayuda en los fondos oscuros.*

   
  ¿Por qué utilizar el resaltado?   El resaltado funciona al unísono con el contorno para mejorar el contraste de la forma, especialmente en fondos oscuros. Nunca es una mala idea, pero si no tienes espacio, por ejemplo, tienes una línea muy fina, puedes prescindir de ella siempre que hayas asegurado un contraste suficiente entre el color principal y el contorno.
  ¿Cómo se cumple esto?             Al igual que con el contorno, simplemente trace un trazo de 2px alrededor del lado interno del contorno, ajustando los nodos a la rejilla cuando sea posible, apuntando a las intersecciones menores de la rejilla.
   



## Iluminación


**Opcional**

Según las directrices de Tango, si está añadiendo un efecto de iluminación de gradiente, trate de hacer que parezca que la luz viene de la parte superior izquierda. Esto se hace añadiendo el color de realce arriba a la izquierda y el color base u oscuro abajo a la derecha. Observe que sólo se utilizan colores de la paleta.

<img alt="" src=images/Draft_Clone.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Clone_backgrounds.svg  style="width:" height="128px;"> 
*Sutil efecto de iluminación procedente de la parte superior izquierda.*

   
  style=\"width:25%;\|¿Por qué utilizar la iluminación?   La iluminación es una forma más de unir los iconos y garantizar que haya distintos niveles de [\"valor\"](https://en.wikipedia.org/wiki/Lightness) para mejorar su legibilidad. Sin embargo, siempre que el contorno y el resaltado estén presentes, puede considerarse opcional
  ¿Cómo cumplir con esto?                                 Configure el relleno para que sea un gradiente lineal o radial. En Inkscape esto está disponible en los ajustes de trazo y relleno; con \"F2\" es posible mover los nodos del gradiente para asegurarse de que están en el ángulo correcto.
   



## Formato de grabación recomendado 

Todos los iconos deben crearse en formato [SVG](SVG/es.md) con una aplicación de imágenes vectoriales, como [Inkscape](http://inkscape.org). Esto facilita la aplicación de cambios y la derivación de iconos adicionales en el mismo espacio de la aplicación.

Cuando se comprometan iconos para ser utilizados directamente por FreeCAD (en un archivo \*.qrc), guárdalos como \"Puro SVG\". Esto reducirá el tamaño del icono y ahorrará espacio en el disco y en la memoria.



## Comentarios finales 

Recuerda: **SALCHO**, Stroke, Alignment, Lighting, Color, Highlight, Outline

Aquí tienes algunos consejos para comprobar tu trabajo.



### Controlar el tamaño 

Inkscape tiene una práctica herramienta para comprobar su icono en varios tamaños. Vaya a **Ver → Vista de icono...** y le mostrará vistas previas de su icono redimensionado a 16, 24, 32 y 64 píxeles.



### Comprobar su contorno 

1.  Pon tu icono en un rectángulo grande que sea del mismo color que el más oscuro de tu icono.
2.  ¿Todavía se ve bien? Genial. Ve al siguiente paso. Si no, ajusta el resaltado.
3.  Haz lo mismo pero esta vez usando el color más claro.
4.  ¿Todavía se ve bien? Genial. Los contornos y las iluminaciones se han utilizado adecuadamente. Si no es así, ajusta el contorno.

<img alt="" src=images/Draft_Move_backgrounds_outline.svg  style="width:" height="128px;"> 
*Probar el icono con los colores más oscuros y más claros como fondo*

   
  Mi icono es apenas visible.   Tiene un contraste de forma pobre. Compruebe de nuevo el contorno y el resaltado, probablemente falte uno de ellos o esté mal aplicado.
   



### Comprobar el contraste 

1.  Exportar su icono de SVG a un formato de mapa de bits, como `.png` o `.jpg`.
2.  Cargue su mapa de bits en un programa de imagen, y cámbielo a escala de grises. Por ejemplo, en GIMP iría a **Imagen → Modo → Escala de grises**.
3.  Inkscape le permite convertir el SVG directamente a escala de grises usando **Extensiones → Color → Escala de grises**.
4.  ¿Todavía puede distinguir claramente algún detalle interno? Genial. El contraste es bueno.

Una imagen en escala de grises permite identificar más fácilmente los problemas de contraste, ya que sólo hay una mezcla de blanco y negro. Probar imágenes en escala de grises también es bueno para los usuarios daltónicos. Si pueden ver los detalles de una imagen en escala de grises, es probable que el contraste de la imagen totalmente coloreada también sea bueno.

<img alt="" src=images/Draft_Move_contrast_grayscale.svg  style="width:" height="128px;"> 
*Probar el contraste del icono en escala de grises*

   
  No puedo distinguir todos los detalles.   Los colores que has elegido tienen poco contraste de valores. Intenta usar colores que estén más separados en tu paleta de 4 tonos, es decir, un verde destacado al lado de un amarillo destacado será difícil de ver, baja uno de esos colores a Base u Oscuro.



---
⏵ [documentation index](../README.md) > [Artwork](Category_Artwork.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Artwork Guidelines/es
