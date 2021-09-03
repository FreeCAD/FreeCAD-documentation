





{{TOCright}}

## Vista general {#vista_general}

Esta página muestra las diferentes formas de iniciar FreeCAD y las características de configuración más importantes.

## Iniciando FreeCAD desde la línea de comandos {#iniciando_freecad_desde_la_línea_de_comandos}

FreeCAD puede iniciarse normalmente, haciendo doble clic en el icono del escritorio o seleccionándolo en el menú de inicio, pero también sr puede iniciar directamente desde la línea de comandos. Esto te permite cambiar algunos de las opciones por defecto de inicio.

### Usar las opciones de la línea de comandos sin un shell de línea de comandos {#usar_las_opciones_de_la_línea_de_comandos_sin_un_shell_de_línea_de_comandos}

-   En Ubuntu puedes crear un icono de escritorio y editar sus propiedades. Añade las opciones de la línea de comandos separadas por espacios detrás del nombre del programa en el campo \"Comando\".
-   En Windows crea un acceso directo y edita las propiedades. Añade las opciones de la línea de comandos separadas por espacios en el campo \"Objetivo\".

### Opciones de la línea de comandos {#opciones_de_la_línea_de_comandos}

Las opciones de la línea de comandos están sujetas a cambios frecuentes, por lo que es conveniente comprobar las opciones actuales escribiendo:

FreeCAD --help

En la respuesta puedes leer los posibles parámetros:

 Usage: FreeCAD [options] File1 File2 ...
 
 Allowed options:
 
 Generic options:
   -v [ --version ]          Prints version string
   -h [ --help ]             Prints help message
   -c [ --console ]          Starts in console mode
   --response-file arg       Can be specified with '@name', too
   --dump-config             Dumps configuration
   --get-config arg          Prints the value of the requested configuration key
 
 Configuration:
   -l [ --write-log ]        Writes a log file to:
                             /home/username/.FreeCAD/FreeCAD.log
   --log-file arg            Unlike --write-log this allows logging to an 
                             arbitrary file
   -u [ --user-cfg ] arg     User config file to load/save user settings
   -s [ --system-cfg ] arg   System config file to load/save system settings
   -t [ --run-test ] arg     Test case - or 0 for all
   -M [ --module-path ] arg  Additional module paths
   -P [ --python-path ] arg  Additional python paths
   --single-instance         Allow to run a single instance of the application

In the following table, selected options are described in more detail:

+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Long option                               | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                                                                                                                                         |
+===========================================+================================================================+==================================================================================================================================================================================================================================================================+
|                            | UserParameter                                                  | Filename or relative path that ends with a filename. Defaults to `user.cfg`.                                                                                                                                                              |
| `--user-cfg <filename>`          |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | Prepends to AdditionalModulePaths                              | Directory that contains modules. This option can be given repeatedly to specify multiple directories.                                                                                                                                                            |
| `--module-path <dir>`            |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | most                                                           | Outputs the requested value in a popup dialog. Exits upon confirmation with **OK**. Cannot be used repeatedly. If an unknown/illegal variable name is used, the response is empty. The `--console` flag is not honored. |
| `--get-config <config-var-name>` |                                                                |                                                                                                                                                                                                                                                                  |
|                                        |                                                                |                                                                                                                                                                                                                                                                  |
+-------------------------------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Options can written in two forms: `--long-option arg` and `--long-option<nowiki>=</nowiki>arg`.

### Respuesta y archivos de configuración {#respuesta_y_archivos_de_configuración}

FreeCAD puede leer algunas de estas opciones desde un archivo de configuración. Este archivo debe estar en la ruta de la papelera y debe llamarse {{FileName|FreeCAD.cfg}}. Tenga en cuenta que las opciones especificadas en la línea de comandos anulan el archivo de configuración.

Algunos sistemas operativos tienen límites de longitud muy bajos para la línea de comandos. El modo más habitual de evitar esas limitaciones es utilizar un archivo de respuesta. Un archivo de respuesta es simplemente un archivo de configuración que utiliza la misma sintaxis que la línea de comandos. Si la línea de comandos especifica un nombre de archivo de respuesta a utilizar, es cargado y analizado sintáticamente en adición a la línea de comandos:

    FreeCAD @ResponseFile.txt 

o:

    FreeCAD --response-file=ResponseFile.txt

or:

    FreeCAD --response-file ResponseFile.txt

### Opciones ocultas {#opciones_ocultas}

Existen varias opciones no visibles por el usuario. Estas opciones son por ejemplo los parámetros de X-Window analizados por el sistema Windows:

-   -display display, establece la visualización de X (por defecto es \$DISPLAY).
-   -geometry geometry, establece la geometría cliente de la primera ventana que es mostrada.
-   -fn or -font font, Define la fuente de letra de la aplicación. La fuente de letra debería estar especificada utilizando una descripción de fuente lógica de X.
-   -bg or -background color, establece el color de fondo por defectoy una paleta para la aplicación (se calculan las sombras iluminadas y oscuras).
-   -fg or -foreground color, establece el color de primer planor.
-   -btn or -button color, establece el color por defecto de los botones.
-   -name name, establece el nombre de la aplicación.
-   -title title, establece el título de la aplicación.
-   -visual TrueColor, fuerza a la aplicación a utilizar la visualización TrueColor en una visualización de 8-bit.
-   -ncols count, limita el número de colores asignados en el cubo de color de visualización de 8-bit, si la aplicación está utilizando la especificación del color QApplication::ManyColor. Si el computo es 216 entonces se utiliza un cubo de color de 6x6x6 (por ejemplo 6 niveles de rojo, 6 de verde y 6 de azul); para otros valores, se utiliza un cubo aproximadamente proporcional a un cubo de 2x3x1.
-   -cmap, cause que la aplicación instale un mapa de color privado en una visualización de 8-bit.


<div class="mw-translate-fuzzy">

## Ejecución de FreeCAD sin interfaz de usuario {#ejecución_de_freecad_sin_interfaz_de_usuario}


</div>


<div class="mw-translate-fuzzy">

FreeCAD normalmente se inicia en el modo de interfaz de usuario gráfico GUI, pero puedes forzar que inicie en modo consola escribiendo:


</div>

FreeCAD --console


<div class="mw-translate-fuzzy">

desde la línea de comandos. En el modo consola, no se mostrará el interfaz de usuario, y tendrás presente la consola del interprete de Python. Desde ella tienes la misma funcionalidad que desde el interprete de Python que se ejecuta dentro del interfaz de usuario gráfico GUI de FreeCAD, y acceso normal a todos los módulos y plugins de FreeCAD, exceptuando el módulo FreeCADGui. Ten en cuenta que los módulos que dependan del FreeCADGui podrían tampoco estar disponibles.


</div>

To read more about console or headless mode, checkout [Headless FreeCAD](Headless_FreeCAD.md).

### Running modules, macros and scripts {#running_modules_macros_and_scripts}

+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| File type       | System           | Command line example                                                                                                               |
+=================+==================+====================================================================================================================================+
| Module          | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`                                                                                    |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`                                                                     |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 |                  |                                                                                                                                    |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
| .FCMacro or .py | Windows          |                                                                                                                     |
|                 |                  | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"` |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux            |                                                                                                                     |
|                 |                  | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                                |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+
|                 | Linux (AppImage) |                                                                                                                     |
|                 |                  | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`                                                 |
|                 |                  |                                                                                                                                 |
+-----------------+------------------+------------------------------------------------------------------------------------------------------------------------------------+

See [Macro at Startup](Macro_at_Startup.md) on how to set up a macro to automatically run at FreeCAD startup.

## Environment variables {#environment_variables}

FreeCAD supports the following environment variables, which can be used to configure directories: <small>(v0.19)</small> 

+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Environment variable         | Corresponding [config var name](#Configuration_set.md) | Synopsis                                                                                                                                    |
+==============================+================================================================+=============================================================================================================================================+
|               | UserHomePath                                                   | FreeCAD\'s \"base\" directory for keeping local user data.                                                                                  |
| `FREECAD_USER_HOME` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|               | UserAppData                                                    | If not set, defaults to `FREECAD_USER_HOME/.FreeCAD`, but only if `FREECAD_USER_HOME` is set. |
| `FREECAD_USER_DATA` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
|               | AppTempPath                                                    | If not set, defaults to `FREECAD_USER_HOME/temp`, but only if `FREECAD_USER_HOME` is set.     |
| `FREECAD_USER_TEMP` |                                                                |                                                                                                                                             |
|                           |                                                                |                                                                                                                                             |
+------------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

If the specified path does not exist, the setting is ignored!

The above environment variables are meant to be used to realize a *portable* FreeCAD environment. For an example how environment variables can be used from the command line on Linux refer to the [notes for Linux users on the downloads page](Download#Notes_for_GNU.2FLinux_users.md).

### `HOME`

FreeCAD uses [Qt](Third_Party_Libraries#Qt.md), which does honor the `HOME` environmental variable. Thus, setting `HOME` can be used to specify the base directory of Qt-related configuration files (`.config/FreeCAD/FreeCAD.conf`).

FreeCad itself does not honor the `HOME` environmental variable (because it determines the user\'s home directory from a lower-level system API). Use `FREECAD_USER_HOME` for this pupose.

### `TMPDIR` {#section_1}

The default temporary directory is {{FileName|/tmp/}}. The `TMPDIR` environmental variable can be used to override the default. (*Editor: precedence?*).


<div class="mw-translate-fuzzy">

Algunas bibliotecas necesitan llamar a variables de entorno del sistema. A veces cuando existe un problema con una instalación de FreeCAD, es porque algunas variables de entorno no están o se han definido mal. Por tanto, algunas variables importantes son duplicadas en la Configuración y guardadas en el archivo de registro.


</div>


<div class="mw-translate-fuzzy">

**Variables de entorno relativas a Python:**


</div>

-   PYTHONPATH
-   PYTHONHOME
-   TCL\_LIBRARY
-   TCLLIBPATH


<div class="mw-translate-fuzzy">

**Variables de entorno relativas a OpenCascade:**


</div>

-   CSF\_MDTVFontDirectory
-   CSF\_MDTVTexturesDirectory
-   CSF\_UnitsDefinition
-   CSF\_UnitsLexicon
-   CSF\_StandardDefaults
-   CSF\_PluginDefaults
-   CSF\_LANGUAGE
-   CSF\_SHMessage
-   CSF\_XCAFDefaults
-   CSF\_GraphicShr
-   CSF\_IGESDefaults
-   CSF\_STEPDefaults


<div class="mw-translate-fuzzy">

## El conjunto de configuración {#el_conjunto_de_configuración}


</div>


<div class="mw-translate-fuzzy">

En cada inicio FreeCAD examina sus alrededores y los parámetros de la línea de comandos. Esto construye un **conjunto de configuración** que guarda la esencia de toda la información de la ejecución. Esta información es después utilizada para determinar la ubicación donde guardar los datos del usuario o archivos de registro. También es muy importante para los análisis postmortem. Por lo tanto es guardado en el archivo de registro.


</div>

### Información relativa al usuario {#información_relativa_al_usuario}


<div class="mw-translate-fuzzy">

  Nombre variable configuración   Sinopsis                                                                          Ejemplo M\$                                                                   Ejemplo Posix (Linux)
  ------------------------------- --------------------------------------------------------------------------------- ----------------------------------------------------------------------------- ------------------------------------
  UserAppData                     Ruta donde FreeCAD almacena los datos de la aplicación relativos al usuario.      C:\\Documents and Settings\\username\\Application Data\\FreeCAD               /home/username/.FreeCAD
  UserParameter                   Archivo donde FreeCAD almacena los datos de la aplicación relativos al usuario.   C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\user.cfg     /home/username/.FreeCAD/user.cfg
  SystemParameter                 Archivo donde FreeCAD almacena datos relativos a la aplicación.                   C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\system.cfg   /home/username/.FreeCAD/system.cfg
  UserHomePath                    Ruta de la carpeta de inicio del usuario actual                                   C:\\Documents and Settings\\username\\My Documents                            /home/username

  : Entradas de configuración de usuario


</div>

Note: For Linux distributions, an additional configuration file that relates to [Qt](Third_Party_Tools#Qt-Toolkit.md) may exist at path {{FileName|/home/username/.config/FreeCAD/FreeCAD.conf}}.

### Argumentos de la línea de comando {#argumentos_de_la_línea_de_comando}


<div class="mw-translate-fuzzy">

  Nombre variable configuración   Sinopsis                                                                                                                                                                                                                                                                                                                                                                               Ejemplo
  ------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------
  LoggingFile                     1 si el logging está activado                                                                                                                                                                                                                                                                                                                                                          1
  LoggingFileName                 Nombre de archivo en el que está ubicado el registro                                                                                                                                                                                                                                                                                                                                   C:\\Documents and Settings\\username\\Application Data\\FreeCAD\\FreeCAD.log
  RunMode                         Esto indica como funcionará el bucle principal. **\"Script\"** significa que el archivo de guión dado se llamará y luego se saldrá. **\"Cmd\"** ejecuta el interprete de la línea de comandos. **\"Internal\"** ejecuta un archivo de guión interno. **\"Gui\"** introduce el bucle de eventos de la interfaz de usuario gráfica GUI. **\"Module\"** carga un módulo de Python dado.   \"Cmd\"
  FileName                        Su significado depende del modo de ejecución                                                                                                                                                                                                                                                                                                                                           
  ScriptFileName                  Su significado depende del modo de ejecución                                                                                                                                                                                                                                                                                                                                           
  Verbose                         Nivel de verborrea de FreeCAD                                                                                                                                                                                                                                                                                                                                                          \"\" o \"strict\"
  OpenFileCount                   Mantiene el número de archivos abiertos a través de argumentos de la línea de comandos                                                                                                                                                                                                                                                                                                 \"12\"
  AdditionalModulePaths           Mantiene las rutas de módulos adicionales dados en la línea de comandos                                                                                                                                                                                                                                                                                                                \"extraModules/\"

  : Entradas de configuración de usuario


</div>

### Relativos al sistema {#relativos_al_sistema}


<div class="mw-translate-fuzzy">

  Nombre variable configuración   Sinopsis                                                                                                                      Ejemplo M\$                Ejemplo Posix (Linux)
  ------------------------------- ----------------------------------------------------------------------------------------------------------------------------- -------------------------- -----------------------
  AppHomePath                     Ruta en la que es instalado FreeCAD \| c:/Progam Files/FreeCAD\_0.7                                                           /user/local/FreeCAD\_0.7   
  PythonSearchPath                Mantiene una lista de las rutas en las cuales Python busca módulos. Esto es al inicio se puede cambiar durante la ejecución                              

  : Entradas de configuración de usuario


</div>

### Información relativa a la construcción {#información_relativa_a_la_construcción}


<div class="mw-translate-fuzzy">

La tabla de abajo muestra la información disponible sobre la versión de construcción. La mayoría proviene del repositorio de Subversion. Esto es necesario para reconstruir exactamente una versión!


</div>


<div class="mw-translate-fuzzy">

  Nombre variable configuración   Sinopsis                                                                              Ejemplo
  ------------------------------- ------------------------------------------------------------------------------------- -------------------------------------------------------------------
  BuildVersionMajor               Número de versión principal de la construcción. Definida en src/Build/Version.h.in    0
  BuildVersionMinor               Número de versión secundario de la construcción. Definida en src/Build/Version.h.in   7
  BuildRevision                   Número de revisión del repositorio SVN del src en la construcción. Generado por SVN   356
  BuildRevisionRange              Rango de diferentes cambios                                                           123-356
  BuildRepositoryURL              URL del repositorio                                                                   <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>
  BuildRevisionDate               Fecha de la revisión de arriba                                                        2007/02/03 22:21:18
  BuildScrClean                   Indica si el código fuente fue modificado después de su descarga                      Src modified
  BuildScrMixed                                                                                                         Src not mixed

  : Entradas de configuración de usuario


</div>

### Relativos al marcado {#relativos_al_marcado}


<div class="mw-translate-fuzzy">

Estas entradas de configuración son relativas al mecanismo de marcado de FreeCAD. Mira [Marcado](Branding/es.md) para más detalles.


</div>


<div class="mw-translate-fuzzy">

  Nombre variable configuración   Sinopsis                                                                                                                  Ejemplo
  ------------------------------- ------------------------------------------------------------------------------------------------------------------------- ---------------------
  ExeName                         Nombre del archivo ejecutable de la construcción. Puede diferir de la de FreeCAD si es utilizado un main.cpp diferente.   FreeCAD.exe
  ExeVersion                      Versión global mostrada al inicio                                                                                         V0.7
  AppIcon                         Icono que es utilizado por el ejecutable, mostrado en Application MainWindow.                                             \"FCIcon\"
  ConsoleBanner                   Banner que es mostrado en modo consola                                                                                    
  SplashPicture                   Nombre del icono utilizado por la pantalla de bienvenida                                                                  \"FreeCADSplasher\"
  SplashAlignment                 Alineación del texto en el letrero de diálogo de bienvenida                                                               \"Bottom\|Left\"
  SplashTextColor                 Color del texto de bienvenida                                                                                             \"\#000000\"
  StartWorkbench                  Nombre del entorno que comenzará automáticamente después del inicio                                                       \"Part design\"
  HiddenDockWindow                Lista de dockwindows (separadas por un punto y coma) que serán mostradas                                                  \"Property editor\"

  : Entradas de configuración de usuario


</div>

### Querying the configuration {#querying_the_configuration}

**From FreeCAD\'s Python console**

Entries of the configuration set can be queried with the **config var name** (see tables above) from the [Python console](Python_console.md). For example:

 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'

If the name is not found, an empty string is returned.

**From command line**

Use the `--get-config <config-var-name>` option to query a single name. Not all names are supported. For example:

 FreeCAD_0.19 --get-config ExeVersion

Use the `--dump-config` option to get a list of names and their values. Not all names are supported.

**From FreeCAD console**

Start FreeCAD in console mode with `--console` and query with Python code. For example:

 $ FreeCAD_0.19 --console
 [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
 >>> FreeCAD.ConfigGet("ExeVersion")
 '0.19'
 >>> exit()

For Linux (bash shell) you can modify the following command line to suit your needs:

 $ FreeCAD_0.19 --console <<EOF
 print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
 print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
 exit()
 EOF

## Starting FreeCAD from the desktop {#starting_freecad_from_the_desktop}

### Linux: Creating an additional start option {#linux_creating_an_additional_start_option}

The following assumes that your desktop is configured such that you can launch FreeCAD from it. Depending on your Linux distribution and desktop environment, you may have to adapt the following steps:

1.  Copy the freedesktop entry file for FreeCAD from {{FileName|/usr/share/applications/freecad.desktop}} to {{FileName|~/.local/share/applications}}.
2.  Change the name from {{FileName|freecad.desktop}} to something else (e.g. {{FileName|MyFreeCADConfig.desktop}}).
3.  Open the file with a text editor and change how FreeCAD is invoked by modifying the line starting with `Exec`.
4.  As a result, an additional entry in your start menu/application launcher is available. This way, you can have multiple FreeCAD entries with various launch options.

## Starting FreeCAD from a portable USB medium {#starting_freecad_from_a_portable_usb_medium}


<small>(v0.19)</small> 

**Windows**

Put the FreeCAD executable, {{FileName|FreeCAD.exe}}, on the USB medium. Create a batch file, {{FileName|FreeCAD.bat}}, and put it into the same directory as {{FileName|FreeCAD.exe}}. Inside the batch file write:


```python
set CURRENTDIR=%cd%
set FREECAD_USER_HOME=%CURRENTDIR%
start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log 
```

[or](https://forum.freecadweb.org/viewtopic.php?f=12&t=54784&start=60#p474759) with `FREECAD_USER_DATA`


```python
set CURRENTDIR="%cd%"
set FREECAD_USER_DATA=%CURRENTDIR%/..
start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg```

Now double-click the batch file to start FreeCAD. ([see](https://forum.freecadweb.org/viewtopic.php?f=4&t=49028))


<div class="mw-translate-fuzzy">


{{docnav/es|Third Party Tools/es|FreeCAD Build Tool/es}}


</div>


 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
