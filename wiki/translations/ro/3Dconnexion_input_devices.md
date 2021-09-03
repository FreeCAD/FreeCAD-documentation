 <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> {{TOCright}}


<div class="mw-translate-fuzzy">

## Instalrea Driver-ului {#instalrea_driver_ului}

### Linux

FreeCAD supportă drivere din proiect [Spacenav](http://spacenav.sourceforge.net/).Acesta este un proiect care are ca scop crearea unui driver cu sursă deschisă, compatibil cu driverele proprietare de la 3Dconnexion.


</div>

### Linux {#linux_1}

FreeCAD supports drivers from project [Spacenav](http://spacenav.sourceforge.net/). This is a project aiming to create an open-sourced driver which is compatible with the proprietary drivers from 3Dconnexion.


<div class="mw-translate-fuzzy">

#### Instalare din repo {#instalare_din_repo}

##### Ubuntu


</div>

##### Ubuntu {#ubuntu_1}


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

#### Compilați Spacenav de la sursă {#compilați_spacenav_de_la_sursă}

Acest lucru este recomandat în cazul în care distribuția dvs. ar putea oferi o versiune depășită.


</div>

This is recommended if your distribution might provide an outdated version.


<div class="mw-translate-fuzzy">

-   Descărcați următoarele fișiere:
    -   [spacenavd-0.5.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20daemon/spacenavd%200.5/spacenavd-0.5.tar.gz/download)
    -   [libspnav-0.2.2. tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/libspnav%200.2.2/libspnav-0.2.2.tar.gz/download)
    -   [spnavcfg-0.2.1.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/spnavcfg%200.2.1/spnavcfg-0.2.1.tar.gz/download)
-   Despachetați arhivele într-un director din directorul de acasă.
-   Introduceți directorul spacenavd-0.5


</div>


:   
    
```python
    ./configure
    make
    
```
    


<div class="mw-translate-fuzzy">

-   Dacă acest lucru a avut succes, executați următoarele comenzi \'\' \'ca root\' \'\' (sau prefix cu sudo.)


</div>


:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Aceasta instalează daemonul spacenav, configurează-l să se încarce automat în boot-ul sistemului și pornește daemonul fără a trebui să repornească.
-   Acum este timpul să verificați dacă dispozitivul dvs. este detectat corespunzător. Cu dispozitivul deconectat, executați următoarea comandă și apoi conectați-l.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

Dacă ieșirea arată cam așa, puteți continua.

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

-   Acum introduceți directorul numit libspnav-0.2.2 și executați următoarele comenzi:


</div>


:   
    
```python
    ./configure
    make
    
```
    

-   Dacă eșuează cu următoarea eroare: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... atunci trebuie să instalați libgtkmm-2.4-dev. Sub Ubuntu, aceasta se face astfel:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Când s-a terminat cu succes, executați următoarea comandă \'\' \'ca root\' \'\' (sau prefix cu sudo.)

:   
    
```python
    make install
    
```
    


<div class="mw-translate-fuzzy">

-   Uitați-vă în directorul libspnav-0.2.2 / examples /. Dacă doriți să vă testați dispozitivul, compilați și executați unul dintre cele două exemple.


</div>

-   Urmați același model pentru a compila și instala spnavcfg. Asigurați-vă că rulați spnavcfg ca root, sau altfel nu vor fi salvate setări!

#### Starting spacenavd as a systemd service at boot {#starting_spacenavd_as_a_systemd_service_at_boot}

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.


<div class="mw-translate-fuzzy">

#### Restart

Dacă uneori navigatorul nu mai funcționează, este bine să reporniți driverul. Pentru a reporni, accesați Terminal și executați:


</div>

If sometimes navigator stops working, it is good to restart driver. To restart it, go to Terminal and execute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

După aceea, reporniți FreeCAD. La unele distro-uri este necesar ca la fiecare boot.

### Known Issues {#known_issues}

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

Dispozitivele de intrare 3Dconnexion sunt acceptate pe OS X, cu condiția ca FreeCAD să fie construit și utilizat într-un sistem cu driverele 3Dconnexion instalate.


</div>

3Dconnexion input devices are supported on OS X, provided that FreeCAD is built and used on a system with the 3Dconnexion drivers installed.


<div class="mw-translate-fuzzy">

### Windows

De la versiunea 0.13, mouse-ul 3D este suportat sub Windows. Trebuie să aveți instalate drivere proprii, dar din moment ce suportul a fost dezvoltat la nivel inferior, acesta va suprascrie setările pe care le-ați setat în panoul de control 3D Connexion. Cu toate acestea, majoritatea acestor setări pot fi setate în caseta de dialog Instrumente \>\> Particularizare, sub filele \"Spaceball\".


</div>

As of version 0.13, 3D mouse is supported under Windows. You need to have 3Dconnexion drivers installed.

#### Known Issue {#known_issue}

There is an issue where 3Dconnexion sends duplicate scroll events to FreeCAD, which causes the view to jump. To fix it:

1.  Open 3Dconnexion Properties. You can double-click its icon in the Taskbar, next to the Windows clock.
2.  Click on the Advanced Settings button.
3.  Open FreeCAD or switch to an already-open FreeCAD window.
4.  Switch back to 3Dconnexion Advanced Settings. Confirm that it says \"FreeCAD\" in the heading.
5.  Uncheck all boxes on the page.

ref: <https://freecadweb.org/tracker/view.php?id=1893>


<div class="mw-translate-fuzzy">

## Configurarea FreeCAD {#configurarea_freecad}

Suportul mouse-ului 3D a fost realizat cu un proiect spnav pe Linux, și la un nivel foarte scăzut pe Windows. Aceasta înseamnă că nu a existat niciun suport pentru setările pentru un dispozitiv, deoarece pe Linux nu există un suport bun pentru acest lucru, iar pe Windows este suprasolicitat. Acesta este motivul pentru care au fost adăugate două pagini suplimentare în dialogul \"Personalizare\".


</div>

3D mouse support was made with spnav project on Linux, and on a very low level on Windows. This means there was no support for any settings for a device, since on Linux there is no good support for this, and on Windows it is overridden. This is why two additional pages were added to \"Customize\" dialog.

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">


<div class="mw-translate-fuzzy">

### Spaceball Motion {#spaceball_motion}

În această filă aveți posibilitatea de a configura unele dintre setările generale ale mouse-ului spațial. Ei includ:

-   Sensibilitate globală - Slider cu capacitatea de a seta sensibilitate globală
-   Dominant - dacă activați modul dominant, vor fi luate în considerare numai axele cu cea mai mare mișcare
-   Flip YZ - Această opțiune vă permite să răsturnați axele Y și Z pe mouse-ul 3D
-   Enable Translations - o modalitate ușoară de a activa / dezactiva traducerile
-   Enable Rotations - modalitate ușoară de a activa / dezactiva rotațiile
-   Calibrare - vă permite să calibrați navigatorul spațial. Este apăsat în timp ce navigatorul spațial nu este mutat.
-   Setare implicită - elimină toate setările și le restabilește la setările implicite.


</div>

In this tab you have ability to set up some of general space mouse settings. They include:

-   Global Sensitivity - Slider with ability to set global sensitivity
-   Dominant - if you enable dominant mode, only axes with highest move will be considered
-   Flip YZ - This option enables you to flip Y and Z axes on 3D mouse
-   Enable Translations - easy way to enable/disable translations
-   Enable Rotations - easy way to enable/disable rotations
-   Calibrate - enables you to calibrate space navigator. It is pressed while space navigator is not moved.
-   Set To Default - removes all settings and sets them to default.

În afară de aceasta, pentru fiecare axă aveți posibilitatea de a seta:

-   Activat - Activați / Dezactivați axele
-   Reverse - Mișcarea inversă pe axe
-   Sensibilitate - cursor cu capacitatea de a seta sensibilitatea


<div class="mw-translate-fuzzy">

### Butoane pentru Spaceball {#butoane_pentru_spaceball}

Când deschideți această filă pentru prima dată, va fi goală și indisponibilă. Pentru a o activa, trebuie să apăsați unul din butoanele mouse-ului spațial. După ce faceți acest lucru, lista de butoane va apărea în partea stângă, iar lista de comenzi va fi disponibilă în partea dreaptă.


</div>

When you open this tab for the first time, it will be empty and unavailable. To activate it, you must press one of your space mouse buttons. After you do, list of buttons will appear on the left side, and list of commands will be available on the right side.

Pentru a conecta anumite comenzi cu un buton, selectați butonul din partea stângă și este comanda pe partea dreaptă. Pentru a șterge comenzile de la buton, apăsați \"Șterge\".

## Related

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)

[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:3rd Party{{\#translation:}}](Category:3rd_Party.md)
