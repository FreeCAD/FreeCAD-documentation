# Embedding FreeCAD/es
## Introduction


<div class="mw-translate-fuzzy">

FreeCAD tiene la asombrosa capacidad de poder importarse como un módulo de Python en otros programas o en una consola independiente de Python, junto con todos sus módulos y componentes. Incluso es posible importar el GUI de FreeCAD como módulo Python (aunque con algunas restricciones).


</div>




<div class="mw-translate-fuzzy">

### Usando FreeCAD sin interfaz gráfica de usuario GUI 


</div>


<div class="mw-translate-fuzzy">

Una primera, directa, fácil y útil aplicación que puedes hacer de esto es para importar documentos de FreeCAD en tu programa. En el siguiente ejemplo, vamos a importar la geometría de la pieza de un documento de FreeCAD en [Blender](http://www.blender.org). Aquí está el archivo de guión completo. Espero que te impresione por su sencillez:


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.pyd file,
# for Windows you must either use \\ or / in the path, using a single \ is problematic
# FREECADPATH = 'C:\\FreeCAD\\bin'
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

La primera parte, importante, es estar seguro de que Python encontrará nuestra biblioteca de FreeCAD. Una vez que la encuentra, todos los módulos de FreeCAD como el de Pieza (que también utilizaremos) estarán disponibles de forma automática. Así que, simplemente, tomamos la variable sys.path, que es donde Python busca sus módulos, y añadimos la ruta de acceso de FreeCAD lib. Esta modificación es sólo temporal, y se perderá cuando cerremos nuestro intérprete de Python. Otra forma podría ser hacer un enlace a tu librería de FreeCAD en una de las rutas de búsqueda de Python. Yo he puesto la ruta en una constante (FREECADPATH), por lo que será más fácil para otro usuario del archivo de guión adaptarlo a su propio sistema.


</div>


{{Code|lang=python|code=
FREECADPATH = 'C:\\FreeCAD\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
import sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

Una vez que estamos seguros de que la biblioteca se carga (la secuencia try/except), podemos trabajar con FreeCAD del mismo modo que lo haríamos en el propio intérprete de Python que tiene FreeCAD. Abrimos el documento de FreeCAD que nos pasa la función main(), y hacemos una lista de sus objetos. Luego, como hemos escogido ocuparnos sólo de la geometría de la Pieza, verificamos que la propiesdad Type de cada objeto contiene \"Parte\", y despues lo *teselamos*.


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

El proceso de *teselado* elabora una lista de vértices y una lista de caras definidas por vértices índexados. Esto es perfecto, ya que es exactamente del mismo modo se definen las mallas en *Blender*. Por lo tanto, nuestra tarea es ridículamente simple, sólo tienes que añadir los contenidos de ambas listas a los vértices y caras de una malla de *Blender*. Cuando todo esté hecho, volvemos a dibujar la pantalla, y eso es todo!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

Por supuesto, como este archivo de guión es muy simple (de hecho hice uno más avanzados [aquí](http://yorik.orgfree.com/scripts/import_freecad.py)), es posible que desees ampliarlo, por ejemplo añadiendo la importación de objetos malla, o importando geometría de piezas que no tenga caras, o importar otros formatos de archivo de los que puede leer FreeCAD. Es posible que también desees exportar la geometría a un documento de FreeCAD, lo cual se puede hacer de la misma manera. Es posible que también quieras construir un cuadro de diálogo, con el que el usuario pueda elegir qué importar, etc .. La belleza de todo esto reside realmente en el hecho de que tu dejas a FreeCAD hacer el trabajo en la sombra, mientras que la presentación de los resultados se hace en el programa de tu elección.


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.




<div class="mw-translate-fuzzy">

### Uso de FreeCAD con interfaz gráfica de usuario GUI 


</div>

Desde la versión 4.2, Qt tiene capacidad para incrustar plugins Qt dependientes del interfaz gráfica de usuario GUI en aplicaciones host (anfitrión) no-Qt y compartir el bucle de eventos del host (anfitrión).

En concreto, para FreeCAD esto significa que puede ser importado (incrustado) con toda su GUI (interfaz de usuario) dentro de otra aplicación (host), con lo que desde la aplicación host se tiene el control total sobre FreeCAD.

El código en Python para lograr todo eso tiene sólo dos líneas


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Si la aplicación host se basa en Qt, entonces esta solución debería funcionar en todas las plataformas que soporte Qt. Sin embargo, el anfitrión debe vincularse a la misma versión de Qt que FreeCAD porque de lo contrario podrías obtener errores de ejecución inesperados.

Para aplicaciones que no son Qt, sin embargo, hay algunas limitaciones que debes tener en cuenta. Esta solución probablemente no funcionará con todos los demás toolkits. Para Windows funcionará siempre y cuando la aplicación host se base directamente en Win32 o en cualquier otro kit que use internamente el API Win32 como wxWidgets, MFC o WinForms. Para hacerlo funcionar bajo X11, la aplicación host debe vincularse a la biblioteca \"glib\".

Ten en cuenta, por supuesto, que para cualquier aplicación de consola, esta solución no funciona porque no hay ningún bucle de eventos en ejecución.

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter, this is not a common usage scenario and requires some care. Generally, it is better to use the Python included with FreeCAD, run FreeCAD via command line, or as a subprocess. See [Start up and Configuration](Start_up_and_Configuration.md) for more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure Python module), it can only be imported from a compatible Python interpreter. Generally this means that the Python interpreter must be compiled with the same C compiler as was used to build FreeCAD. Information about the compiler used to build a Python interpreter (including the one built with FreeCAD) can be found as follows:


```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Embedding FreeCAD/es
