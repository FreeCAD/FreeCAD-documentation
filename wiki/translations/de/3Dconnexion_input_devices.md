# <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/de






## Treiberinstallation



### Linux

FreeCAD unterstützt die Treiber des Projekts [Spacenav](http://spacenav.sourceforge.net/). Dies ist ein Projekt mit dem Ziel, einen quelloffenen Treiber zu entwickeln, der mit den proprietären Treibern von 3Dconnexion kompatibel ist.



#### Installation aus dem Paketarchiv 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Beachte aber, dass die Version 0.6, die unter Ubuntu 20.04 (und möglicherweise älteren) verfügbar ist, nicht zu funktionieren scheint. Du musst dann spacenavd wie unten beschrieben aus dem Quell-Code kompilieren.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```


:   spacenav benötigt folgende Berechtigungen:





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Neustart von spnavd und FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```



#### Kompiliere Spacenav aus der Quelle 

Dies wird empfohlen, wenn deine Distribution eine veraltete Version bereitstellen könnte.

-   Lade die folgenden Dateien herunter:
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) (neueste Version)
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) (aktuellste libspnav Version abrufen)
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) (neueste libspnav Version abrufen)
-   Entpacke die Archive in einen Ordner in deinem Home Verzeichnis.
-   Rufe das Verzeichnis spacenavd-x.x auf und führe die folgenden Befehle aus:

:   
    
```python
    ./configure
    make
    
```
    

-   Wenn dies erfolgreich war, führe die folgenden Befehle aus **als root** (oder Präfix mit sudo.)

:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Dies installiert den spacenav-Dämon, konfiguriert ihn so, dass er automatisch beim Systemstart geladen wird und startet den Dämon, ohne neu starten zu müssen.
-   Jetzt ist es an der Zeit, zu überprüfen, ob dein Gerät ordnungsgemäß erkannt wird. Wenn dein Gerät nicht angeschlossen ist, führe den folgenden Befehl aus und stecke es dann ein.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Wenn die Ausgabe etwa so aussieht, kannst du fortfahren.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    

-   Gib nun das Verzeichnis libspnav-x.x.x ein und führe die folgenden Befehle aus:

:   
    
```python
    ./configure
    make
    
```
    

-   Wenn make mit dem folgenden Fehler fehlschlägt: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... dann musst Du libgtkmm-2.4-dev installieren. Unter Ubuntu wird dies so gemacht:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Wenn make erfolgreich abgeschlossen wurde, führe den folgenden Befehl aus **als root** (oder Präfix mit sudo.)

:   
    
```python
    make install
    
```
    

-   Schau in das Verzeichnis libspnav-x.x.x/examples/. Wenn du dein Gerät testen möchtest, kompiliere und führe eines der beiden Beispiele aus.

-   Folge dem gleichen Muster, um spnavcfg zu kompilieren und zu installieren. Achte jedoch darauf, spnavcfg als root auszuführen, sonst werden keine Einstellungen gespeichert!



#### Starten von spacenavd als systemd-Service während des Systemstarts 

Wenn Du spacenavd während des Systemstarts mit systemd starten möchtest, dann führe folgendes aus:

-   Gehe zum Verzeichnis, in das du das spacenavd-Repository geklont hast (zum Wurzelverzeichnis des Repositorys)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", falls du es sofort starten möchtest.

Dies ist nur bei der Installation aus dem Quell-Code notwendig.



#### Neustarten von spacenavd 

Wenn der Navigator manchmal aufhört zu arbeiten, ist es gut, den Treiber neu zu starten. Um ihn neu zu starten, gehe zum Terminal und führe aus:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Danach starten Sie FreeCAD neu. Bei einigen Distributionen ist dies nach jedem Boot nötig.



#### Bekannte Probleme 

Ein Benutzer berichtete im [Forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) und sah folgendes:

Spacenav daemon 0.6
 failed to open config file /etc/spnavrc: No such file or directory. using defaults.
 adding device.
 device name: 3Dconnexion SpacePilot
 using device: /dev/input/event5
 No protocol specified
 failed to open X11 display ":0.0"  

Die Abhilfe, die für sie funktionierte:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```



### MacOS

3Dconnexion Eingabegeräte werden unter macOS unterstützt, vorausgesetzt, dass FreeCAD auf einem System mit installierten 3Dconnexion-Treibern erstellt und verwendet wird. Für macOS 12 sollte man 3DxWare 10.7.2 oder neuer verwenden.

### Windows

Ab der Version 0.13 wird die 3D-Maus unter Windows unterstützt. Sie müssen die 3Dconnexion Treiber installiert haben. In FreeCAD Version 1.0 wurde eine [new integration with 3Dconnexion devices](https://github.com/FreeCAD/FreeCAD/pull/12929) eingeführt. Wenn Sie mit dieser Integration kompilieren, wird nur neuere Hardware unterstützt: Um ältere Geräte zu unterstützen, müssen Sie selbst kompilieren und die cMake-Variable FREECAD_3DCONNEXION_SUPPORT auf \"Raw Input\" setzen. Windows-Benutzer sollten sich darüber im Klaren sein, dass der Treiber von 3Dconnexion (*nicht* der Code in FreeCAD) ein Telemetriepaket enthält, das Informationen über die installierte Software an 3Dconnexion übermittelt.



#### Bekannte Probleme 

-   In FreeCAD Version 1.0 und neuer führt das Ändern der Einstellungen im 3DX-Konfigurationsfenster eventuell nicht zu den erwarteten Ergebnissen ([issue](https://github.com/FreeCAD/FreeCAD/issues/14044)). Um dies zu beheben:
    1.  Den Treiber anhalten (durch Ausführen von Stop 3DxWare).
    2.  Zu **..<user>\AppData\Roaming\3Dconnexion\3DxWare\Cfg** wechseln und die Datei **FreeCAD.xml** löschen.
    3.  Den Treiber starten (durch Ausführen von Start 3DxWare).
    4.  FreeCAD starten und prüfen, ob die Einstellungen der [Spaceball Bewegung](#Spaceball_Motion/.md) eingestellt werden können.



## FreeCAD einrichten 


{{VersionPlus/de|1.0}}

: Das 3Dconnexion-Eigabegerät kann in seiner Treiber-App eingestellt werden (3DxWare-Software).


{{VersionMinus/de|0.21}}

: Wird eine 3D-Maus erkannt, können folgende Reiter im [Dialog zum Anpassen der Oberfläche](Interface_Customization/de.md) zum Ändern der Einstellungen eingesetzt werden:

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">



### Spaceball Bewegung 

In diesem Reiter hast du die Möglichkeit, einige allgemeine Einstellungen der Space Maus einzurichten. Dazu gehören:

-   Globale Empfindlichkeit - Schieberegler mit der Möglichkeit, die globale Empfindlichkeit einzustellen.
-   Dominant - wenn du den Dominanzmodus aktivierst, werden nur Achsen mit der höchsten Bewegung berücksichtigt.
-   Drehe YZ - Diese Option ermöglicht es dir, die Y- und Z-Achse der 3D Maus zu drehen.
-   Übersetzungen aktivieren - einfacher Weg zum Aktivieren/Deaktivieren von Übersetzungen
-   Rotationen aktivieren - einfacher Weg, um Rotationen zu aktivieren/deaktivieren.
-   Kalibrieren - ermöglicht es Dir, den Space Navigator zu kalibrieren. Sie wird gedrückt, während der Space Navigator nicht bewegt wird.
-   Auf Standard setzen - entfernt alle Einstellungen und setzt sie auf Standard.

Ansonsten hast Du für jede Achse die Möglichkeit, diese einzustellen:

-   Aktiviert - Achsen aktivieren/deaktivieren
-   Rückwärts - Rückwärtsbewegung an den Achsen
-   Empfindlichkeit - Schieberegler mit der Möglichkeit, die Empfindlichkeit einzustellen.



### Spaceball Tasten 

Wenn Du diese Registerkarte zum ersten Mal öffnest, ist sie leer und nicht verfügbar. Um sie zu aktivieren, musst du eine deiner Space Maustasten drücken. Danach erscheint auf der linken Seite eine Liste der Schaltflächen und auf der rechten Seite eine Liste der Befehle.

Um einen bestimmten Befehl mit einer Schaltfläche zu verbinden, wähle die Schaltfläche auf der linken Seite und den Befehl auf der rechten Seite. Um die Befehle der Taste zu löschen, drücke \"Löschen\".



### Fehlersuche

Prüfen Sie ob Ihre FreeCAD-Installation auf die spacenav-Bibliothek verweist. Der beste Weg dies herauszufinden ist FreeCAD von der Kommandozeile aus zu starten `FreeCAD --log-file /tmp/freecad.log` und gleich wieder zu schliessen. Danach die Datei **/tmp/freecad.log** öffnen und nach der Nachricht zu suchen:


`Connected to spacenav daemon`

oder


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

Sollte keines von Beiden erscheinen dann verweist Ihr FreeCAD nicht auf die spacenav-Bibliothek. Erscheint die erste Meldung funktioniert es grundsätzlich. Die zweite Meldung bedeutet dass wahrscheinlich ein Problem mit dem spacenav-Daemon vorliegt.



## Verwandtes

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > 3Dconnexion input devices/de
