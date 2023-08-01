# Manual:Installing/es
{{Manual:TOC/es}}

FreeCAD utiliza la licencia [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License); puedes descargar, instalar, redistribuir y utilizar FreeCAD como quieras, independientemente del tipo de trabajo que vayas a realizar con él (comercial o no comercial). No estás obligado a ninguna cláusula o restricción, y los archivos que produzcas con él son totalmente tuyos. Lo único que la licencia prohíbe, en realidad, es afirmar que has programado FreeCAD tú mismo.

FreeCAD se comporta igual en Windows, Mac OS y Linux. Sin embargo, la forma de instalarlo difiere ligeramente dependiendo de tu plataforma. En Windows y Mac, la comunidad de FreeCAD proporciona paquetes precompilados (instaladores) listos para descargar; mientras que en Linux, el código fuente se pone a disposición de los mantenedores de las distribuciones de Linux, que son los responsables de empaquetar FreeCAD para su distribución específica. Como resultado, en Linux, normalmente puedes instalar FreeCAD directamente desde la aplicación de gestión de software.

La página oficial de descarga de FreeCAD para Windows y Mac OS es <https://github.com/FreeCAD/FreeCAD/releases>

**Versiones de FreeCAD**

Las versiones oficiales de FreeCAD, que puedes encontrar en la página referenciada arriba y en el gestor de software de tu distribución, son versiones estables. Sin embargo, ¡el desarrollo de FreeCAD es rápido! Nuevas características y correcciones de errores se añaden casi todos los días. Dado que a menudo pasa mucho tiempo entre las versiones estables, podrías estar interesado en probar una versión más avanzada de FreeCAD. Estas versiones de desarrollo, o pre-lanzamientos, se suben de vez en cuando a la [página de descargas](https://github.com/FreeCAD/FreeCAD/releases) mencionada anteriormente, o, si estás usando Ubuntu o Fedora, la comunidad de FreeCAD también mantiene [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) y [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) \'daily builds\' que se actualizan regularmente con los cambios más recientes.

Si estás instalando FreeCAD en una máquina virtual, ten en cuenta que el rendimiento puede ser pobre (en algunos casos inutilizable) debido a los límites de soporte de [OpenGL](https://en.wikipedia.org/wiki/OpenGL) en la mayoría de las máquinas virtuales.

### Instalación en Windows 

1.  Descargue un paquete instalador (.exe) correspondiente a su versión de Windows (32bit o 64bit) desde la \[página de descargas <https://github.com/FreeCAD/FreeCAD/releases>\]. Los instaladores de FreeCAD deberían funcionar en cualquier versión de Windows a partir de Windows 7.
2.  Haz doble clic en el instalador descargado.
3.  Acepta los términos de la licencia LGPL, este será uno de los pocos casos en los que puedes realmente, con seguridad, hacer clic en el botón \"aceptar\" sin leer el texto. No hay cláusulas ocultas: ![](images/Freecad-windows-install-01.jpg )
4.  Puede dejar la ruta por defecto aquí, o cambiarla si lo desea: ![](images/Freecad-windows-install-02.jpg )
5.  No es necesario establecer la variable PYTHONPATH, a menos que planee hacer algo de programación avanzada en python, en cuyo caso probablemente ya sepa para qué sirve: ![](images/Freecad-windows-install-03.jpg )
6.  Durante la instalación, se instalarán también un par de componentes adicionales, que están incluidos en el instalador: ![](images/Freecad-windows-install-04.jpg )
7.  Eso es todo, FreeCAD está instalado. Lo encontrarás en tu menú de inicio. ![no](images/Freecad-windows-install-05.jpg )

**Instalación una versión desarrollo**

Empaquetar FreeCAD y crear un instalador lleva algo de tiempo y dedicación, así que normalmente las versiones de desarrollo (también llamadas pre-lanzamiento) se proporcionan como archivos .zip (o .7z). Estos no necesitan ser instalados; sólo tienes que descomprimirlos y lanzar FreeCAD haciendo doble clic en el archivo FreeCAD.exe que encontrarás dentro. Esto también te permite mantener tanto la versión estable como la \"inestable\" juntas en el mismo ordenador.

### Instalación en Linux 

En la mayoría de las distribuciones modernas de Linux (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary, etc), FreeCAD puede instalarse con el clic de un botón, directamente desde la aplicación de gestión de software proporcionada por su distribución (el aspecto de la misma puede diferir de las imágenes de abajo, cada distribución utiliza su propia herramienta).

1.  Abre el gestor de software y busca \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Haz clic en el botón \"instalar\" y ya está, FreeCAD se instala. ¡No te olvides de calificarlo después!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Vías alternativas**

Una de las grandes alegrías de usar Linux es la multitud de posibilidades de adaptar el software, así que no te limites. En Ubuntu y derivados, FreeCAD también puede instalarse desde un [PPA](https://launchpad.net/~freecad-maintainers) mantenido por la comunidad de FreeCAD (contiene versiones estables y de desarrollo). En Fedora, las versiones de desarrollo recientes de FreeCAD pueden instalarse desde [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), y como se trata de software de código abierto, también puedes fácilmente [compilar FreeCAD tú mismo](Compiling/es.md).

### Instalación en Mac OS 

Instalar FreeCAD en Mac OSX es hoy en día tan fácil como en otras plataformas. Sin embargo, dado que hay menos gente en la comunidad que posee un Mac, los paquetes disponibles a veces van un poco por detrás de las otras plataformas.

1.  Descargue el paquete comprimido correspondiente a su versión desde la página [página de descarga](https://github.com/FreeCAD/FreeCAD/releases).
2.  Abra la carpeta de descargas, y expanda el archivo zip descargado: ![](images/Freecad-mac-01.jpg )
3.  Arrastra la aplicación FreeCAD desde el interior del zip a la carpeta de Aplicaciones: ![](images/Freecad-mac-02.jpg )
4.  ¡Ya está, FreeCAD está instalado! ![](images/Freecad-mac-03.jpg )

5\. Si el sistema impide que FreeCAD se inicie debido a los permisos restringidos para aplicaciones que no provienen de la tienda de aplicaciones, tendrás que habilitarlo en la configuración del sistema: ![](images/Freecad-mac-04.jpg )

### Desinstalación

Es de esperar que no quieras desinstalar FreeCAD, pero es bueno saber cómo hacerlo. En Windows y Linux, desinstalar FreeCAD es muy sencillo. En Windows, usa la opción estándar de \"eliminar software\" que se encuentra en el panel de control; en Linux, elimínalo con el mismo gestor de software que usaste para instalarlo. En Mac OS, simplemente elimínalo de la carpeta de aplicaciones.

### Configuración de las preferencias básicas 

Una vez instalado FreeCAD, puede que quieras abrirlo y cambiar algunas preferencias. Los ajustes de preferencias en FreeCAD se encuentran en el menú **Edición → Preferencias**. A continuación se enumeran algunos ajustes básicos que puedes querer cambiar; puedes navegar por las páginas de preferencias para ver si hay algo más que quieras cambiar.

1.  **Idioma**: (categoría *General*, pestaña *General*) FreeCAD elegirá automáticamente el idioma de tu sistema operativo, pero puede que quieras cambiarlo. FreeCAD está casi completamente traducido a cinco o seis idiomas; otros están actualmente sólo parcialmente traducidos. Puedes fácilmente [ayuda para traducir FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Módulo de carga automática**: (categoría *General*, pestaña *General*) Normalmente, FreeCAD comenzará mostrando la página de inicio. Puedes omitir esto y comenzar una sesión de FreeCAD directamente en el banco de trabajo que elijas, listado en *Inicio*, *Cargar automáticamente el módulo después del inicio*. Los [Bancos de trabajo](Workbenches.md) se explicarán en detalle en el [próximo capítulo](Manual:The_FreeCAD_Interface/es.md).
3.  **Crear un nuevo documento al inicio**: (*Categoría general*, pestaña *Documento*) Combinado con la opción *Cargar automáticamente el módulo* de arriba, si se marca esto se inicia FreeCAD listo para trabajar. ![](images/Freecad-basic-options02.jpg )
4.  **Opciones de almacenamiento**: (categoría *General*, pestaña *Documento*) Como con cualquier aplicación compleja, FreeCAD probablemente contiene errores que hacen que se bloquee ocasionalmente. Aquí puedes configurar las opciones que te ayudarán a recuperar tu trabajo en caso de un fallo.
5.  **Autorización y licencia**: (*Categoría general*, pestaña *Documento*) Aquí estableces los valores que se utilizarán para los nuevos archivos que crees. Considera hacer tus archivos compartibles desde el principio, usando una licencia más amigable, [copyleft](https://en.wikipedia.org/wiki/Copyleft) como [Creative Commons](https://creativecommons.org/).
6.  **Redirigir los mensajes internos de python**: (categoría *General*, pestaña *Ventana de salida*) Estas dos opciones son siempre buenas para comprobar, ya que harán que los mensajes del intérprete interno de python se muestren en el [Vista de informe](Manual:The_FreeCAD_Interface#Report_view.md) cuando hay un problema al ejecutar un script de python. ![](images/Freecad-basic-options03.jpg )
7.  **Unidades**: (categoría *General*, pestaña *Unidades*) Aquí puede establecer el sistema de unidades por defecto que desea utilizar. ![](images/Freecad-basic-options04.jpg )
8.  **Zoom en el cursor**: (*Categoría de visualización*, pestaña *3D*) Si se establece, las operaciones de zoom se centrarán en el puntero del ratón. Si no se establece, el centro de la vista actual es el foco del zoom.
9.  **Invertir zoom**: (*Categoría de visualización*, pestaña *3D*) Invierte la dirección del zoom en relación con el movimiento del ratón. ![](images/FreeCAD-v0-18-Preferences-Display.png )

### Instalación de contenidos adicionales 


<div class="mw-translate-fuzzy">

Como el proyecto FreeCAD y su comunidad crecen rápidamente, y también porque es fácil de extender, las contribuciones externas y los proyectos secundarios realizados por los miembros de la comunidad y otros entusiastas comienzan a aparecer por todas partes en Internet. La mayoría de estos proyectos externos son ambientes de trabajo o macros, y pueden ser fácilmente instalados desde FreeCAD a través del [Gestor de Complementos](Std_AddonMgr/es.md) situado en el menú **Herramientas**. El gestor de complementos te permitirá instalar muchos componentes interesantes, por ejemplo:


</div>

1.  Una [Biblioteca Piezas](https://github.com/FreeCAD/FreeCAD-library), que contiene todo tipo de modelos útiles, o piezas de modelos, creados por los usuarios de FreeCAD que pueden ser utilizados libremente en sus proyectos. La biblioteca puede ser utilizada y accedida directamente desde tu instalación de FreeCAD.
2.  [Ambientes de trabajo adicionales](https://github.com/FreeCAD/FreeCAD-addons), que amplían la funcionalidad de FreeCAD para ciertas tareas, por ejemplo animar partes de tus modelos, o áreas, como el plegado de chapa o BIM. Más explicaciones de cada ambiente de trabajo y qué herramientas contiene se dan en cada página de complementos, que puedes visitar haciendo clic en el enlace correspondiente en el gestor de complemento.
3.  Una [colección de macros](https://github.com/FreeCAD/FreeCAD-macros), que también están disponibles [en el wiki de FreeCAD](Macros_recipes/es.md) junto con la documentación sobre cómo usarlas.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

Si estás usando el sistema operativo Ubuntu, algunos de los complementos anteriores también están disponibles como paquetes en el [FreeCAD complementos PPA](https://launchpad.net/freecad-extras)

**Leer más**

-   [Más opciones de descarga](Download/es.md)
-   [FreeCAD PPA para Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD complementos PPA para Ubuntu](https://launchpad.net/freecad-extras)
-   [Compilar FreeCAD tú mismo](Compiling/es.md)
-   [Traducciones de FreeCAD](https://crowdin.com/project/freecad)
-   [Página de FreeCAD en github](https://github.com/FreeCAD)
-   [El gestor de complementos de FreeCAD](Std_AddonMgr/es.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/es
