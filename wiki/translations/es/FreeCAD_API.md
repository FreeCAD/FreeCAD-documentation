# FreeCAD API/es
**(Octubre 2019) No editar esta página. La información está incompleta y desactualizada.  Para obtener la API más reciente, consulte la [https://www.freecadweb.org/api documentación de API generada automáticamente] o genere la documentación usted mismo, consulte [Documentación de fuente](Source_documentation.md).**

Este es el módulo principal (raíz) de FreeCAD. También puede ser llamado por \"App\" desde el interprete de FreeCAD. Contiene todo lo que es necesario para manipular documentos y sus contenidos (objectos).

Ejemplo: 
```python
import FreeCAD
print FreeCAD.listDocuments()
mydoc = FreeCAD.activeDocument()
```


{{APIFunction/es|ConfigDump| |Muestra un diccionario conteniendo todo el entorno de configuración de FreeCAD.| }}


{{APIFunction/es|ConfigGet|[string]|Devuelve el valor de una clave dada. Si no se indica la clave, devuelve la configuración completa.|Una cadena de texto.}}


{{APIFunction/es|ConfigSet|string, string|Establece la clave dada (primera cadena de texto) al valor indicado (segunda cadena de texto).| }}


{{APIFunction/es|Version| |Muestra la versión de FreeCAD.| }}


{{APIFunction/es|activeDocument| ||Devuelve el documento activo o Nada si no hay ningún documento activo.|Un documento de FreeCAD.}}


{{APIFunction/es|addExportType|string, string|Añade un nuevo tipo de formato de archivo de exportación a FreeCAD. La primera cadena de texto debe estar formada como en este ejemplo: "Documento de Word (*.doc)". La segunda cadena es el nombre de un archivo de guión / módulo de Python conteniendo una función export().| }}


{{APIFunction/es|addImportType|string, string|Añade un nuevo tipo de formato de archivo de importación a FreeCAD, funciona del mismo modo que addExportType, el módulo de Python debe contener una función open() y/o import().| }}


{{APIFunction/es|closeDocument|Document name|Cierra el documento indicado| }}


{{APIFunction/es|getDocument|Document name|Devuelve un documento o eleva una excepción si no existe un documento con el nombre indicado.| }}


{{APIFunction/es|getExportType|string|Devuelve el nombre del módulo que puede exportar el tipo de archivo especificado.|Una cadena de texto.}}


{{APIFunction/es|getImportType|string|Devuelve el nombre del módulo que puede exportar el tipo de archivo especificado.|Una cadena de texto.}}


{{APIFunction/es|listDocuments| |Devuelve una lista de nombres de todos los documentos.|Una lista de nombres.}}


{{APIFunction/es|newDocument|[string]|Crea y devuelve un nuevo documento con el nombre indicado. El nombre del documento debe ser único, lo que se comprueba de forma automática. Si no se indica ningún nombre, el documento se llamará "Untitled". Si se pasa <tt>hidden<nowiki>=</nowiki>True</tt>, entonces FreeCAD en modo GUI no mostrará el documento y no mostrará una pestaña para el documento;  esto permite realizar operaciones automáticas en un documento y cerrarlo sin interrumpir la interfaz de usuario.|El nuevo documento creado.}}


{{APIFunction/es|open|string|Ver openDocument| }}


{{APIFunction/es|openDocument|filepath, [hidden]|Crea y devuelve un documento y carga un archivo de proyecto dentro del documento. La cadena de texto del argumento debe apuntar a un archivo existente. Si no existe el archivo o si no puede cargarse se lanza una excepción I/O. En este caso el documento creado se guarda, pero estará vacío. Si se pasa <tt>hidden<nowiki>=</nowiki>True</tt>, entonces FreeCAD en modo GUI no mostrará el documento y no mostrará una pestaña para el documento;  esto permite realizar operaciones automáticas en un documento y cerrarlo sin interrumpir la interfaz de usuario.|El documento de FreeCAD abierto.}}


{{APIFunction/es|setActiveDocument|Document name|Establece el documento activo por su nombre.| }}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCAD API/es
