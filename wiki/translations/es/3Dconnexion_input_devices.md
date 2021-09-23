# 3Dconnexion input devices/es
 <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> {{TOCright}}

## Instalación de controladores 

### Linux

FreeCAD soporta los drivers del proyecto [Spacenav](http://spacenav.sourceforge.net/). Este es un proyecto que pretende crear un controlador de código abierto que sea compatible con los controladores propietarios de 3Dconnexion.

#### Instalar desde un repositorio 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Note, however, that version 0.6 available on Ubuntu 20.04 (and probably older ones) does not seem to work. You then have to compile spacenavd from source as explained below.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```


:   spacenav necesita estos permisos:





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Reiniciar spnavd y FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```

#### Compilar Spacenav desde el código fuente 

Esto se recomienda si su distribución puede proporcionar una versión obsoleta.

-   Descargue los siguientes archivos:
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) (última versión)
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) (obtener la última versión de libspnav)
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) (obtener la última versión de libspnav)
-   Descomprima los archivos en una carpeta de su directorio personal.
-   Entra en el directorio spacenavd-x.x y ejecuta los siguientes comandos:

:   
    
```python
    ./configure
    make
    
```
    

-   Si esto tuvo éxito, ejecute los siguientes comandos **como root**\' (o con el prefijo sudo.)

:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Esto instala el demonio de spacenav, lo configura para cargar automáticamente al iniciarse el sistema, e inicia el demonio sin tener que reiniciar.
-   Ahora es tiempo de verificar que tu dispositivo se detecta correctamente. Con tu dispositivo desconectado, ejecuta los siguientes comandos y luego conéctalo.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Si la salida se parece a algo como esto, puedes continuar.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    

-   Ahora entra en el directorio libspnav-x.x.x y ejecuta los siguientes comandos:

:   
    
```python
    ./configure
    make
    
```
    

-   Si make falla con el siguiente error: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... entonces necesitas instalar libgtkmm-2.4-dev. En Ubuntu, se hace así:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Cuando make se realice completamente bien, ejecuta el siguiente comando **como root** (o añade el prefijo sudo)

:   
    
```python
    make install
    
```
    

-   Mira en el directorio libspnav-x.x.x/examples/. Si quieres probar tu dispositivo, compila y ejecuta uno de los siguientes dos ejemplos.

-   Sigue el mismo patrón para compilar e instalar spnavcfg. Asegúrate de ejecutar spnavcfg como root, o no se guardará la configuración!

#### Starting spacenavd as a systemd service at boot 

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.

#### Reinicio spacenavd 

Si a veces el navegador deja de funcionar, es bueno reiniciar el controlador. Para reiniciarlo, vaya al Terminal y ejecute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Después reinicia FreeCAD. En algunas distribuciones esto es necesario en cada reinicio.

### Problemas conocidos 

Un usuario informó en el [foro](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) que vio lo siguiente:

 Spacenav daemon 0.6
 failed to open config file /etc/spnavrc: No such file or directory. using defaults.
 adding device.
 device name: 3Dconnexion SpacePilot
 using device: /dev/input/event5
 No protocol specified
 failed to open X11 display ":0.0" 

La solución que les ha funcionado:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```

### OSX

Los dispositivos de entrada de 3Dconnexion son compatibles con OS X, siempre que FreeCAD se construya y utilice en un sistema con los controladores de 3Dconnexion instalados.

### Windows

A partir de la versión 0.13, el ratón 3D es compatible con Windows. Es necesario tener instalados los controladores de 3Dconnexion.

#### Problemas conocidos 

Hay un problema en el que 3Dconnexion envía eventos de desplazamiento duplicados a FreeCAD, lo que hace que la vista salte. Para solucionarlo:

1.  Abra las propiedades de 3Dconnexion. Puede hacer doble clic en su icono en la barra de tareas, junto al reloj de Windows.
2.  Haga clic en el botón Configuración avanzada.
3.  Abra FreeCAD o cambie a una ventana de FreeCAD ya abierta.
4.  Vuelva a la configuración avanzada de 3Dconnexion. Confirme que dice \"FreeCAD\" en el encabezado.
5.  Desmarque todas las casillas de la página.

ref: <https://freecadweb.org/tracker/view.php?id=1893>

## Configuración en FreeCAD 

El soporte del ratón 3D se hizo con el proyecto spnav en Linux, y a bajo nivel en Windows. Esto significa que no existe soporte para cualquier configuración para un dispositivo, ya que en Linux no existe un buen soporte, y en Windows se sobreescribe. Este es el motivo de añadir dos páginas adicionales al letrero de diálogo \"Personalización\".

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">

### Movimiento Bola Espacial 

En esta pestaña podrás configurar alguno de los aspectos generales del space mouse. Incluido:

-   Sensibilidad global - Selector para definir la sensibilidad global
-   Dominante - Si activas el modo dominante, sólo los ejes con mayor movimiento se considerarán
-   Invertir YZ - Esta opción permite invertir los ejes Y y Z en un 3D mouse
-   Permitir traslaciones - Modo simple para activar / desactivar las traslaciones
-   Permitir rotaciones - Modo simple para activar / desactivar las rotaciones
-   Calibrado - Permite calibrar el space navigator. Se presiona mientras no se mueva el space navigator.
-   Establecer por defecto - Elimina las configuraciones y las pones por defecto.

Otras, para cada eje tienes la posibilidad de:

-   Activar - Activar / Desactivar ejes
-   Invertir - Invertir el movimiento en un eje
-   Sensibilidad - Establecer la sensibilidad

### Botones Bola Espacial 

Cuando abres esta pestaña por primera vez, estará vacía y no disponible. Para activarla, presiona uno de los botones del space mouse. De este modo, una lista de botones aparecerá en la izquierdaq, y una lista de comandos estará disponible a la derecha.

Para conectar un determinado comando con un botón, selecciona el botón en la izquierda, y el comando a la derecha. Para limpiar comandos de botones, presiona \"Limpiar\".

## Relacionados


<div class="mw-translate-fuzzy">

-   <https://forum.freecadweb.org/viewtopic.php?f=3&t=51023>


</div>

[Category:User Documentation](Category:User_Documentation.md) [Category:3rd Party](Category:3rd_Party.md)
