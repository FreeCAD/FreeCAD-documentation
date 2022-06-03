# Document structure/es
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

![](images/Screenshot_treeview.jpg )

Un *documento* FreeCAD contiene todos los objetos de la escena. Puede contener grupos y objetos hechos con cualquier *entorno de trabajo*. Por lo tanto, puedes cambiar entre los *entornos de trabajo*, y seguir trabajando en el mismo documento. El documento es lo que se guarda en el disco al guardar tu trabajo. También puedes abrir varios documentos al mismo tiempo en FreeCAD, y abrir varias vistas del mismo documento.


<div class="mw-translate-fuzzy">

En el documento, los objetos se pueden mover e incorporar a grupos, y cada objeto tiene un nombre único, exclusivo. La gestión de grupos, objetos y nombres de objeto se hace principalmente en la vista de árbol. También se puede hacer, por supuesto, como todo en FreeCAD, desde el intérprete de Python. En la vista de árbol, se pueden crear grupos, mover objetos a grupos, eliminar objetos o grupos,\... haciendo clic con el botón derecho del ratón en la vista en árbol o en un objeto, cambiar el nombre de los objetos haciendo doble clic sobre sus nombres,\... o posiblemente otras operaciones, en función del *entorno de trabajo* en curso.


</div>


<div class="mw-translate-fuzzy">

Los objetos dentro de un documento FreeCAD pueden ser de diferentes tipos. Cada *entorno de trabajo* puede crear sus propios tipos de objetos, por ejemplo, el [Entorno de trabajo de mallas](Mesh_Workbench/es.md) crea objetos de malla, el [Entorno de trabajo de piezas](Part_Workbench/es.md) crear objetos de piezas, el [Entorno de croquizado 2D](Draft_Workbench/es.md) también crea objetos Pieza, etc


</div>

Si hay uno o más documentos abiertos en FreeCAD, siempre alguno de ellos, y sólo uno, será el *documento activo*. Ese es el documento que aparece en la vista 3D actual, el documento con el que se está trabajando actualmente.

## Aplicación e interfaz de usuario 


<div class="mw-translate-fuzzy">

Como casi todo lo demás en FreeCAD, la interfaz de usuario (*GUI*) del entorno de trabajo de piezas está separada de la aplicación base de piezas. Esto también es válido para los documentos. Los documentos también están hechos de dos partes   * el documento de la aplicación, que contiene nuestros objetos, y el documento *Vista*, que contiene la representación en pantalla de nuestros objetos.


</div>


<div class="mw-translate-fuzzy">

Piensa en ello como dos espacios, donde los objetos están definidos. Sus parámetros constructivos (¿es un cubo? ¿Un cono? ¿Qué tamaño? \...) se almacenan en el documento de aplicación, mientras que su representación gráfica (¿es dibujado con línea negra? ¿Con las caras azules? \...) se almacena en el documento Vista. ¿Por qué? Porque FreeCAD también puede ser utilizado sin interfaz gráfica, por ejemplo dentro de otros programas y, aún así, tenemos que ser capaces de manipular nuestros objetos, incluso si no se dibujan en la pantalla.


</div>

Otra cosa que está contenida en el *documento Vista* son las *vistas* 3D. Un documento puede tener varias vistas abiertas, así que puedes inspeccionar tu documento desde varios puntos de vista al mismo tiempo. Tal vez te gustaría ver una vista superior y una vista frontal de tu trabajo, al mismo tiempo. De ese modo, tendrías dos puntos de vista del mismo documento, ambos almacenados en el documento Vista. Crear puntos de vista nuevos o cerrar vistas se puede hacer desde el *menú* Vista o haciendo clic derecho en la *pestaña* de una vista.

## Archivos de guión 


<div class="mw-translate-fuzzy">

Los documentos se pueden crear fácilmente, acceder y modificar desde el intérprete de Python. Por ejemplo   *


</div>


```python
FreeCAD.ActiveDocument
```

devolverá el documento activo actual 
```python
FreeCAD.ActiveDocument.Blob
``` accedería a un objeto llamado \"Blob\" dentro de tu documento 
```python
FreeCADGui.ActiveDocument
``` devolvería el *documento vista* asociado al documento actual 
```python
FreeCADGui.ActiveDocument.Blob
``` accedería a la parte representación gráfica (*vista*) de nuestro objeto Blob 
```python
FreeCADGui.ActiveDocument.ActiveView
``` devolverá la vista actual


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Document structure/es
