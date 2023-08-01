# Source documentation/es
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Vista general 

El código fuente de FreeCAD se comenta para permitir la generación automática de documentación de programación usando [Doxygen](Doxygen/es.md), un popular sistema de documentación de código fuente. Doxygen puede documentar tanto la parte C++ como la parte Python de FreeCAD, dando como resultado páginas HTML con hipervínculos a cada función y clase documentada.


<div class="mw-translate-fuzzy">

La documentación está alojada en línea en el [Sitio web de FreeCAD API](http://www.freecadweb.org/api/). Tenga en cuenta que esta documentación puede no estar siempre actualizada; si necesita más detalles, descargue el último código fuente de FreeCAD y compile la documentación usted mismo. Si tienes preguntas urgentes sobre el código, por favor, pregúntalas en la sección de desarrolladores del [Foro de FreeCAD](https://forum.freecadweb.org/index.php).


</div>

La compilación de la documentación de la API sigue los mismos pasos generales que la compilación del ejecutable de FreeCAD, como se indica en la página [Compilar en Linux](Compile_on_Linux/es.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Flujo de trabajo general para compilar la documentación de programación de FreeCAD. Los paquetes Doxygen y Graphviz deben estar en el sistema, así como el propio código fuente de FreeCAD. CMake configura el sistema de manera que con una sola instrucción de fabricación la documentación de todo el proyecto se compila en muchos archivos HTML con diagramas.*

## Construcción de la documentación del código fuente 

### Complete documentation 

Si tienes Doxygen instalado, es muy fácil construir la documentación. También instala [Graphviz](https://www.graphviz.org/) para poder producir diagramas que muestren las relaciones entre las diferentes clases y bibliotecas en el código de FreeCAD. Graphviz también es utilizado por [Gráfico de dependencia](Std_DependencyGraph/es.md) de FreeCAD para mostrar las relaciones entre diferentes objetos. 
```python
sudo apt install doxygen graphviz
```

Then follow the same steps you would do to compile FreeCAD, as described on the [compile on Linux](Compile_on_Linux.md) page, and summarized here for convenience.

-   Get the source code of FreeCAD and place it in its own directory `freecad-source`.
-   Create another directory `freecad-build` in which you will compile FreeCAD and its documentation.
-   Configure the sources with `cmake`, making sure you indicate the source directory, and specify the required options for your build.
-   Trigger the creation of the documentation using `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

Mientras estás dentro del directorio de construcción, da la siguiente instrucción para crear sólo la documentación. 
```python
make -j$(nproc --ignore=2) DevDoc
``` Como se mencionó en [Compilación (aceleración)](Compiling_(Speeding_up)/es.md), la `-j` opción establece el número de núcleos de CPU utilizados para la compilación. Los archivos de documentación resultantes aparecerán en el directorio. 
```python
freecad-build/doc/SourceDocu/html/
```

El punto de entrada a la documentación es el archivo `index.html`, que se puede abrir con un navegador web: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```

El objetivo `DevDoc` generará una cantidad significativa de datos, alrededor de 5 GB de nuevos archivos, particularmente debido a los diagramas creados por Graphviz.

### Reduced documentation 


<div class="mw-translate-fuzzy">

Se puede generar una versión alternativa y más pequeña de la documentación, que sólo requiere unos 600 MB, con un objetivo diferente. Esta es la versión que se muestra en el [sitio web de FreeCAD API](http://www.freecadweb.org/api/).


</div>


```python
make -j$(nproc --ignore=2) WebDoc
```

The documentation on the [FreeCAD API website](https://freecad.github.io/SourceDoc/) is produced automatically from <https://github.com/FreeCAD/SourceDoc> . Anyone can rebuild it and submit a pull request:

-   Fork the repo at <https://github.com/FreeCAD/SourceDoc>
-   on your machine: clone the FreeCAD code (if you haven\'t yet), create a build dir for the doc, and clone the above SourceDoc repo inside. That SourceDoc will be updated when you rebuild the doc, and you\'ll be able to commit & push the results afterwards:


```python
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Go to your fork online, and create a pull request.


<div class="mw-translate-fuzzy">

## Otras versiones 

[FreeCAD 0.12](http://free-cad.sf.net/SrcDocu/index.html) documentación alojada en Sourceforge.


</div>

## Integrar la documentación de Coin3D 

En los sistemas Unix es posible vincular la documentación de origen de Coin3D con la de FreeCAD. Esto permite una navegación más fácil y diagramas de herencia completos para las clases derivadas de Coin.

-   Instale el paquete `libcoin-doc`, `libcoin80-doc`, o un paquete de nombre similar.
-   Descomprima el archivo `coin.tar.gz` ubicado en `/usr/share/doc/libcoin-doc/html`; los archivos pueden estar ya descomprimidos en su sistema.
-   Genera de nuevo la documentación de fuente.

Si no instalas el paquete de documentación de Coin, se generarán los enlaces para acceder a la documentación en línea en [BitBucket](https://coin3d.bitbucket.io/Coin/). Esto sucederá si un archivo de etiquetas de Doxygen puede ser descargado en tiempo de configuración con `wget`.

## Usando Doxygen 

Vea la página [Doxygen](Doxygen/es.md) para una extensa explicación sobre cómo comentar el código fuente de C++ y Python para que pueda ser procesado por Doxygen para crear automáticamente la documentación.

Esencialmente, un bloque de comentarios, comenzando con `/**` o `///` para C++, o `##` para Python, debe aparecer antes de cada definición de clase o función, para que sea recogido por Doxygen. Muchos [comandos especiales](Doxygen/es#Doxygen_markup.md), que comienzan con `|` o `@`, pueden ser usados para definir partes del código y dar formato a la salida. [Markdown sintaxis](Doxygen#Markdown_support/es.md) también se entiende dentro del bloque de comentarios, lo que hace conveniente enfatizar ciertas partes de la documentación. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/es
