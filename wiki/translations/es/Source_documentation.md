# Source documentation/es
## Vista general 

El código fuente de FreeCAD se comenta para permitir la generación automática de documentación de programación usando [Doxygen](Doxygen/es.md), un popular sistema de documentación de código fuente. Doxygen puede documentar tanto la parte C++ como la parte Python de FreeCAD, dando como resultado páginas HTML con hipervínculos a cada función y clase documentada.

La documentación está alojada en línea en el [Sitio web de FreeCAD API](https://freecad.github.io/SourceDoc/). Tenga en cuenta que esta documentación puede no estar siempre actualizada; si necesita más detalles, descargue el último código fuente de FreeCAD y compile la documentación usted mismo. Si tienes preguntas urgentes sobre el código, por favor, pregúntalas en la sección de desarrolladores del [Foro de FreeCAD](https://forum.freecadweb.org/index.php).

La compilación de la documentación de la API sigue los mismos pasos generales que la compilación del ejecutable de FreeCAD, como se indica en la página [Compilar en Linux](Compile_on_Linux/es.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Flujo de trabajo general para compilar la documentación de programación de FreeCAD. Los paquetes Doxygen y Graphviz deben estar en el sistema, así como el propio código fuente de FreeCAD. CMake configura el sistema de manera que con una sola instrucción de fabricación la documentación de todo el proyecto se compila en muchos archivos HTML con diagramas.*



## Construcción de la documentación del código fuente 



### Documentación completa 

Si tienes Doxygen instalado, es muy fácil construir la documentación. También instala [Graphviz](https://www.graphviz.org/) para poder producir diagramas que muestren las relaciones entre las diferentes clases y bibliotecas en el código de FreeCAD. Graphviz también es utilizado por [Gráfico de dependencia](Std_DependencyGraph/es.md) de FreeCAD para mostrar las relaciones entre diferentes objetos. 
```python
sudo apt install doxygen graphviz
```

Luego siga los mismos pasos que seguiría para compilar FreeCAD, como se describe en la página [Compilar en Linux](Compile_on_Linux/es.md) y se resume aquí para mayor comodidad.

* Obtenga el código fuente de FreeCAD y colóquelo en su propio directorio `freecad-source`.
* Crea otro directorio `freecad-build` en el que compilarás FreeCAD y su documentación.
* Configure las fuentes con `cmake`, asegurándose de indicar el directorio de fuentes y especificar las opciones requeridas para su compilación.
* Activa la creación de la documentación usando `make`.


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



### Documentación reducida 

La documentación completa usa alrededore de 3Gb de espacio en disco. Se puede generar una versión alternativa y más pequeña de la documentación, que sólo requiere unos 600 MB, con un objetivo diferente. Esta es la versión que se muestra en el [sitio web de FreeCAD API](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

La documentación en el [sitio web de FreeCAD API](https://freecad.github.io/SourceDoc/) se genera automáticamente desde <https://github.com/FreeCAD/SourceDoc>. Cualquiera puede reconstruirlo y enviar un pull request:

-   Bifurca el repositorio en <https://github.com/FreeCAD/SourceDoc>

* en su máquina: clone el código FreeCAD (si aún no lo ha hecho), cree un directorio de compilación para el documento y clone el repositorio de SourceDoc anterior en él.  Ese SourceDoc se actualizará cuando reconstruyas el documento y podrás confirmar y enviar los resultados después:


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

-   Vaya a su bifurcación en línea y cree un pull request.

## Otras versiones 

[Desarrollo de FreeCAD 0.19](https://iesensor.com/FreeCADDoc/0.19/) documentación creada por [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).



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



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source documentation/es
