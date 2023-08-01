# <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/ru







<div class="mw-translate-fuzzy">

## Установка драйверов 

### Linux

FreeCAD поддерживает драйвера из проекта [Spacenav](http://spacenav.sourceforge.net/). Это проект, нацеленный на создание драйвера с открытыми исходниками, совместимого с фирменными драйверами от 3Dconnexion.


</div>

### Linux 

FreeCAD supports drivers from project [Spacenav](http://spacenav.sourceforge.net/). This is a project aiming to create an open-sourced driver which is compatible with the proprietary drivers from 3Dconnexion.




<div class="mw-translate-fuzzy">

#### Установка из репозитория 

##### Ubuntu


</div>

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


:   spacenav needs these permissions:





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Restart spnavd and FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```




<div class="mw-translate-fuzzy">

#### Компиляция Spacenav из исходников 

Это рекомендуется если Ваш дистрибутив предлагает устаревшую версию.


</div>

This is recommended if your distribution might provide an outdated version.


<div class="mw-translate-fuzzy">

-   Загрузить следующие файлы:
    -   [spacenavd-0.5.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20daemon/spacenavd%200.5/spacenavd-0.5.tar.gz/download)
    -   [libspnav-0.2.2.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/libspnav%200.2.2/libspnav-0.2.2.tar.gz/download)
    -   [spnavcfg-0.2.1.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/spnavcfg%200.2.1/spnavcfg-0.2.1.tar.gz/download)
-   Распаковать архивы в папку в Вашем домашнем каталоге.
-   Перейти в каталог spacenavd-0.5 и запустить следующие команды:


</div>


:   
    
```python
    ./configure
    make
    
```
    


<div class="mw-translate-fuzzy">

-   При успехе запустить следующие команды **как root** (или с помощью sudo.)


</div>


:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Это установит демон spacenav, сконфигурирует его для автоматического запуска при старте системы и запустит демона без необходимости перезагрузки.
-   Теперь можно проверить, правильно ли определяется Ваше устройство. С отключённым устройством запустите следующую команду и затем подключите его.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Если вывод выглядит похожим образом, можно продолжать.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    


<div class="mw-translate-fuzzy">

-   Теперь войдите в каталог libspnav-0.2.2 и запустите следующие команды:


</div>


:   
    
```python
    ./configure
    make
    
```
    

-   Если make вывалится со следующей ошибкой: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... то Вам надо установить libgtkmm-2.4-dev. Под Ubuntu это делается так:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Когда make завершится успешно, запустите следующую команду **как root** (или через sudo.)

:   
    
```python
    make install
    
```
    


<div class="mw-translate-fuzzy">

-   Гляньте в каталог libspnav-0.2.2/examples/. Если Вы хотите протестировать Ваше устройство, скомпилируйте и запустите любой из двух примеров.


</div>

-   Следуйте той же схеме для компиляции и установки spnavcfg. Обязательно запустите spnavcfg как root, или установки не будут сохранены!

#### Starting spacenavd as a systemd service at boot 

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.




<div class="mw-translate-fuzzy">

#### Перезапуск

Если иногда навигатор перестаёт работать, полезно перезапустить драйвер. Для перезапуска откройте терминал и запустите:


</div>

If sometimes navigator stops working, it is good to restart driver. To restart it, go to Terminal and execute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

После этого перезапустите FreeCAD. В некоторых дистрибутивах это необходимо при каждой загрузке.

### Known Issues 

A user reported on the [forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) they saw the following:

 Spacenav daemon 0.6
 failed to open config file /etc/spnavrc: No such file or directory. using defaults.
 adding device.
 device name: 3Dconnexion SpacePilot
 using device: /dev/input/event5
 No protocol specified
 failed to open X11 display ":0.0" 

The workaround that worked for them:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```




<div class="mw-translate-fuzzy">

### OSX

Входные устройства 3Dconnexion поддерживаются OS X, если FreeCAD скомпилирован и используется на системе с установленным драйвером 3Dconnexion.


</div>

3Dconnexion input devices are supported on macOS, provided FreeCAD is built and used on a system with the 3Dconnexion drivers installed. You may need 3DxWare 10.7.2 or greater for macOS 12 Monterey.




<div class="mw-translate-fuzzy">

### Windows

Начиная с версии 0.13, трёхмерная мышь поддерживается под Windows. Вам следует установить фирменные драйвера, но поскольку поддержка спроектирована на низовом уровне, она перекрывает установки контрольной панели 3D Connexion. Тем не менее, большинство этих установок могут быть сделаны в диалоге Tools\>\>Customize, на вкладке Spaceball.


</div>

As of version 0.13, 3D mouse is supported under Windows. You need to have 3Dconnexion drivers installed.

#### Known Issue 

There is an issue where 3Dconnexion sends duplicate scroll events to FreeCAD, which causes the view to jump. To fix it:

1.  Open 3Dconnexion Properties. You can double-click its icon in the Taskbar, next to the Windows clock.
2.  Click on the Advanced Settings button.
3.  Open FreeCAD or switch to an already-open FreeCAD window.
4.  Switch back to 3Dconnexion Advanced Settings. Confirm that it says \"FreeCAD\" in the heading.
5.  Uncheck all boxes on the page.

ref: <https://freecadweb.org/tracker/view.php?id=1893>




<div class="mw-translate-fuzzy">

## Установка FreeCAD 

Поддержка трёхмерных мышей сделана с помощью проекта spnav на Linux, и на очень низком уровне на Windows. Это значит что нет поддержки к каким-либо установкам устройства, поскольку на Linux нет хорошей поддержки этого, и на Windows это переопределено. Вот поэтому для диалога \"Customize\" добавлено две дополнительные страницы.


</div>

3D mouse support was made with spnav project on Linux, and on a very low level on Windows. This means there was no support for any settings for a device, since on Linux there is no good support for this, and on Windows it is overridden. This is why two additional pages were added to \"Customize\" dialog.

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">




<div class="mw-translate-fuzzy">

### Spaceball Motion 

На этой вкладке Вы можете назначить некоторые общие установки пространственной мыши. Это включает:

-   Global Sensitivity - слайдер с возможностью установить общую чувствительность
-   Dominant - при разрешении доминантного режима учитывается лишь ось с максимальным движением
-   Flip YZ - эта опция разрешают менять на трёхмерной мыши оси Y и Z
-   Enable Translations - простой путь для разрешения/запрещения трансляций
-   Enable Rotations - простой путь разрешить/запретить вращения
-   Calibrate - позволяет калибровать пространственный навигатор. Нажимается когда пространственный навигатор стоит на месте.
-   Set To Default - сбрасывает все установки и устанавливает их в положение по умолчанию.


</div>

In this tab you have ability to set up some of general space mouse settings. They include:

-   Global Sensitivity - Slider with ability to set global sensitivity
-   Dominant - if you enable dominant mode, only axes with highest move will be considered
-   Flip YZ - This option enables you to flip Y and Z axes on 3D mouse
-   Enable Translations - easy way to enable/disable translations
-   Enable Rotations - easy way to enable/disable rotations
-   Calibrate - enables you to calibrate space navigator. It is pressed while space navigator is not moved.
-   Set To Default - removes all settings and sets them to default.

Кроме этого, для каждой оси есть возможность установить:

-   Enabled - разрешить/запретить оси
-   Reverse - реверсировать движение по осям
-   Sensitivity - слайдер с возможностью установить чувствительность




<div class="mw-translate-fuzzy">

### Spaceball Buttons 

Когда Вы откроете эту вкладку в первый раз, она будет пуста и не доступна. Чтобы её активировать, надо нажать одну из кнопок пространственной мыши. После этого слева появится список кнопок, а справа - список команд.


</div>

When you open this tab for the first time, it will be empty and unavailable. To activate it, you must press one of your space mouse buttons. After you do, list of buttons will appear on the left side, and list of commands will be available on the right side.

Для назначения некоторых команд кнопке выделите кнопку слева и её команду справа. Для стирания команды с кнопки нажмите \"Clear\".

### Troubleshooting

Check if your FreeCAD installation links to the spacenav library. The best way to check this is by running FreeCAD from the command line terminal `FreeCAD --log-file /tmp/freecad.log` and close it immediately again. Then open the file **/tmp/freecad.log** and search for the messages:


`Connected to spacenav daemon`

or


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

If none of them appears then your FreeCAD build doesn\'t link to the spacenav library. If the former message appears then it basically works. The latter message means there is probably a problem with the spacenav daemon.

## Related

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > 3Dconnexion input devices/ru
