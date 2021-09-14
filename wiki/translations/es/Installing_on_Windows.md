# Installing on Windows/es






Puede instalar FreeCAD en Windows descargando uno de los siguientes instaladores:


{{DownloadWindowsStable}}

Después de descargar el archivo .exe (NSIS Installer), haga doble clic en él para iniciar el proceso de instalación.

Abajo hay más información sobre algunas opciones técnicas. Sin embargo, la mayoría de los usuarios no necesitan más que los anteriores archivos .exe. Continuar a [Empieza](Getting_started/de.md) después de que la instalación se haya completado.

## Instalación simple del instalador del NSIS 

La forma más fácil de *instalar FreeCAD en Windows* es usando el paquete de instalación descargable de arriba. Esta página describe el uso y las características del *NSIS Instalador* para más opciones de instalación.

Si desea descargar una versión en desarrollo (que puede ser inestable), mira la página [Descargas](Download/es.md).

## Chocolatey

Sin embargo, se recomienda encarecidamente utilizar un gestor de paquetes como Chocolatey para mantener el software actualizado. Puede instalar Chocolatey siguiendo [estas instrucciones](https://chocolatey.org/install) y luego abrir un terminal PowerShell como administrador y ejecutarlo:


```python
choco install freecad
```

de vez en cuando puedes actualizar tu software con


```python
choco upgrade freecad
```

para obtener la última versión disponible en el repositorio de Chocolatey. Si hay algún problema con el paquete de chocolatey, puede contactar con los mantenedores en [esta página](https://chocolatey.org/packages/freecad).

### Instalación desde la línea de comandos 

Con las utilidades del comando *msiexec.exe*, están disponibles características adicionales, como la instalación no interactiva y la instalación administrativa.

### Instalación no interactiva 

Con la línea de comandos


```python
msiexec /i FreeCAD<version>.msi
```

la instalación se puede iniciar mediante programación. Se pueden pasar parámetros adicionales al final de la línea de comando, por ejemplo


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Interfaz de usuario limitada 

La cantidad de interfaces de usuario que le instalador muestra puede controlarse con opciones /q, en particular:


<div class="mw-translate-fuzzy">

-   /qn - Sin interfaz
-   /qb - Interfaz básica - simplemente un pequeño letrero de diálogo mostrando el progreso de la instalación
-   /qb! - Como /qb, pero ocultando el botón de cancelar
-   /qr - Interfaz reducida - Muestra todos los letreros de diálogo que no requieren interacción del usuario (evita todos los letreros de diálogo modales)
-   /qn+ - Como /qn, pero muestra el letrero de diálogo \"Completed\" al final
-   /qb+ - Como /qb, pero muestra el letrero de diálogo \"Completed\" al final


</div>

### Directorio de destino 

El directorio de destino correspondiente TARGETDIR determina el directorio raíz de la instalación de FreeCAD. Por ejemplo, se puede indicar una unidad de instalación diferente con


```python
TARGETDIR=R:\FreeCAD25
```

El directorio de destino por defecto (TARGETDIR) es \[WindowsVolume\\Programm Files\\\]FreeCAD.

### Instalación para todos los usuarios 

Añadiendo


```python
ALLUSERS=1
```

causa una instalación utilizable por todos los usuarios. Por defecto, una instalación no interactiva (/i) hace que el paquete sea utilizable sólo por el usuario actual (el que realiza la instalación); una instalación interactiva presenta un diálogo que por defecto es \"todos los usuarios\" si el usuario que realiza la instalación tiene suficientes privilegios.

### Selección de características 

Un número de propiedades permite la selección de características a ser instaladas, reinstaladas, o eliminadas. El conjunto de características para el instalador de FreeCAD son

-   Característica predeterminada - Instala el software adecuado, más las librerías principales
-   Documentación - Instala la documentación
-   Código fuente - Instala el código fuente
-   \... ToDo

Además, ALL especifica todas las características. Todas las características dependen de DefaultFeature, así que instalando cualquier característica automáticamente también se instala la característica por defecto. Las siguientes propiedades controlan las operaciones a ser instaladas o eliminadas

-   ADDLOCAL - Lista de características a ser instaladas en la máquina local
-   REMOVE - Lista de características que deben ser eliminadas de la máquina local
-   ADDDEFAULT - Lista de características añadidas en su configuración por defecto (la cual es local para todas las características de FreeCAD)
-   REINSTALL - Lista de características a ser reinstaladas/reparadas
-   ADVERTISE - Lista de características para realizar un anuncio de instalación

Hay algunas propiedades adicionales disponibles; mira la documentación del MSDN para más detalles.

Con estas opciones, añadiendo


```python
ADDLOCAL=Extensions
```

instala el interprete y registra las extensiones, pero no instala nada más.

## Desinstalación

Con


```python
msiexec /x FreeCAD<version>.msi
```

se puede desinstalar FreeCAD. No es necesario disponer del archivo MSI para la desinstalación; alternativamente, el paquete o código del producto también puede ser especificado. Puedes encontrar el código del producto buscando en las propiedades del acceso directo de desinstalación que es instalado por FreeCAD en el menú de Inicio.

## Instalación Administrativa 

Con


```python
msiexec /a FreeCAD<version>.msi
```

se puede iniciar una instalación \"administrativa\" (de red). Los archivos se descomprimen en el directorio de destino (que debería estar en un directorio en red), pero no se realiza ninguna otra modificación al sistema local. Además, se genera otro archivo mis (más pequeño) en el directorio de destino, cuyos clientes pueden utilizar para realizar una instalación local (Las futuras versiones podrán también ofrecer mantener algunas características completamente en la unidad de red).

Actualmente, no hay una interfaz de usuario para la instalación administrativa, de modo que el directorio de destino debe pasarse en la línea de comandos.

No existe un procedimiento específico de desinstalación para una instalación administrativa - simplemente eliminar el directorio de destino si ningún cliente ya no lo utiliza más.

## Anuncios

Con


```python
msiexec /jm FreeCAD<version>.msi
```

sería posible, en principio, \"anunciar\" FreeCAD a una máquina (con /ju para un usuario). Esto hará que los iconos aparezcan en el menú de inicio, y que las extensiones sean registradas, sin el software realmente instalado. El primer uso de una característica hará que dicha característica sea instalada.

El instalador de FreeCAD actualmente sólo soporta simplemente los anuncios de las entradas en el menú de inicio, pero no los de los accesos directos.

## Instalación automática en un grupo de máquinas 

Con las políticas de grupo de Windows, es posible automáticamente instalar FreeCAD en un grupo de máquinas. Para hacerlo, hay que realizar los siguientes pasos:

1.  Acceder al controlador de dominio
2.  Copiar el archivo MSI en un directorio que esté compartido con acceso a todas las máquinas.
3.  Abrir el complemento MMC \"Directorio activo de usuarios y ordenadores\"
4.  Navegar hasta el grupo de ordenadores que necesitan FreeCAD
5.  Abrir las Propiedades
6.  Abrir las políticas de grupo
7.  Añadir una nueva política, y editarla
8.  En Configuración del ordenador/Instalación de software, seleccionar Nuevo/Paquete
9.  Seleccionar el archivo MSI a través de la ruta de red
10. Opcionalmente, seleccionar que quieres que FreeCAD sea desinstalado si los ordenadores abandonan el alcance de la política.

La propagación de las políticas de grupo tipicamente lleva algo de tiempo - para deplegar el paquete de duentes fiables, todas las máquinas deberían reiniciarse.

## Instalación en Linux utilizando Crossover Office 

Puedes instalar la versión de Windows de FreeCAD en un sistema Linux utilizando *CXOffice 5.0.1*. Ejecuta *msiexec* desde la línea de comandos de CXOffice, asumiendo que el paquete de instalación está ubicado en el directorio \"software\" el cual tiene asignado a la unidad \"Y:\":


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD se está ejecutando, pero se ha informado de que la pantalla de OpenGL no funciona, como con otros programas que se ejecutan bajo [Wine](wikipedia:Wine_(software).md) es decir, Google [SketchUp](wikipedia:SketchUp.md).






