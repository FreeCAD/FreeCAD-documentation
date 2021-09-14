# 3Dconnexion input devices/it

 <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> {{TOCright}}

### Installare i driver 

#### Linux

FreeCAD supporta i driver dal progetto [Spacenav](http://spacenav.sourceforge.net/). Si tratta di un progetto che mira a creare un driver open-source che sia compatibile con i driver proprietari di 3Dconnexion.

#### Installare da repo 

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


<div class="mw-translate-fuzzy">

spacenav ha bisogno di queste autorizzazioni


</div>


:   
    
```python
    cp ~/.Xauthority /root/
    
```
    


<div class="mw-translate-fuzzy">

-   Riavvia spnavd e FreeCAD


</div>


:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```

#### Compilare Spacenav dal codice sorgente 

Questo sistema è consigliato in quanto la propria distribuzione potrebbe fornire una versione non aggiornata.


<div class="mw-translate-fuzzy">

-   Scaricare i seguenti file:
    -   [spacenavd-0.5.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20daemon/spacenavd%200.5/spacenavd-0.5.tar.gz/download)
    -   [libspnav-0.2.2.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/libspnav%200.2.2/libspnav-0.2.2.tar.gz/download)
    -   [spnavcfg-0.2.1.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/spnavcfg%200.2.1/spnavcfg-0.2.1.tar.gz/download)
-   Scompattare gli archivi in una cartella nella propria directory /home.
-   Entrare nella directory spacenavd-0.5 ed eseguire i seguenti comandi:


</div>


:   
    
```python
    ./configure
    make
    
```
    


<div class="mw-translate-fuzzy">

-   Se questo ha successo, eseguire i seguenti comandi come root (o con prefisso sudo).


</div>


:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Questo installa il demone di spacenav, lo configura per caricarlo automaticamente all\'avvio del sistema, e avvia il demone senza dover riavviare.
-   Ora si deve verificare che il dispositivo sia rilevato correttamente. Con il dispositivo scollegato, eseguire il seguente comando e quindi collegarlo.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Se il risultato è qualcosa di simile a questo, è possibile continuare.

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

-   Ora entrare nella directory denominata libspnav-0.2.2 ed eseguire i seguenti comandi:


</div>


:   
    
```python
    ./configure
    make
    
```
    

-   Se make fallisce con il seguente errore: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... allora si deve installare libgtkmm-2.4-dev. In Ubuntu, si fà in questo modo:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Quando make si completata correttamente, eseguire il seguente comando come root (o con prefisso sudo.)

:   
    
```python
    make install
    
```
    


<div class="mw-translate-fuzzy">

-   Consultare la directory libspnav-0.2.2/examples/. Se si desidera provare il proprio dispositivo, compilare ed eseguire uno dei due esempi.


</div>

-   Seguire lo stesso procedimento per compilare e installare spnavcfg. Ricordarsi di eseguire spnavcfg come root, altrimenti non verrà salvata nessuna impostazione!

#### Starting spacenavd as a systemd service at boot 

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.

#### Riavviare spacenavd 

Se talvolta navigatore smette di funzionare, è bene riavviare il conducente. Per riavviarlo, andare al terminale ed eseguire:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Dopo avere riavviare FreeCAD. Su alcune distro è necessario a ogni avvio.

### Problemi conosciuto 

Un utente segnalato nel [forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) ha visualizzato quanto segue:

  Demone di Spacenav 0.6
  impossibile aprire il file di configurazione /etc/spnavrc: nessun file o directory. usando i valori predefiniti.
  aggiunta di dispositivo.
  nome del dispositivo: 3Dconnexion SpacePilot
  utilizzando il dispositivo: /dev/input/event5
  Nessun protocollo specificato
  impossibile aprire il display X11 ":0.0"

La soluzione alternativa che ha funzionato per loro:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```

### OSX

Su OS X i dispositivi di input 3Dconnexion sono supportati, purché FreeCAD sia costruito e utilizzato su un sistema con i driver 3Dconnexion installati.

### Windows

A partire dalla versione 0.13, mouse 3D è supportato sotto windows. È necessario avere installato i driver appropriati, ma dato che il supporto è stato sviluppato su un livello inferiore, eseguirà l\'override le impostazioni che impostato nel pannello di controllo 3D Connexion. Tuttavia, la maggior parte di tali impostazioni è possibile impostare in strumenti \>\> finestra di dialogo Personalizza, sotto schede Spaceball.

#### Problemi conosciuto 

C\'è un problema in cui 3Dconnexion invia eventi di scorrimento duplicati a FreeCAD, causando il salto della vista. Per risolverlo:

1.  Apri proprietà 3Dconnexion. Puoi fare doppio clic sulla sua icona nella barra delle applicazioni, accanto all\'orologio di Windows.
2.  Fare clic sul pulsante Impostazioni avanzate.
3.  Apri FreeCAD o passa a una finestra di FreeCAD già aperta.
4.  Torna alle impostazioni avanzate di 3Dconnexion. Conferma che dice \"FreeCAD\" nell\'intestazione.
5.  Deseleziona tutte le caselle nella pagina.

ref: <https://freecadweb.org/tracker/view.php?id=1893>

## Setting up FreeCAD 

Il supporto per il mouse 3D è stata fatta con il progetto spnav su Linux e su un livello molto basso su Windows. Questo significa che non c\'era alcun supporto per tutte le impostazioni per un dispositivo, dato che su Linux non c\'è nessun buon supporto per questo, e su Windows è sottoposto a override. Ecco perché due pagine supplementari sono stati aggiunti alla finestra di dialogo \"Personalizza\".

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">

### Spaceball Motion 

In questa scheda si avrà la possibilità di impostare alcune delle impostazioni del mouse spazio generale. Essi comprendono:

-   Global Sensitivity - Slider con possibilità di impostare la sensibilità globale
-   Dominant - Abilita la modalità dominante, solo gli assi con movimento più alto saranno considerati
-   Flip YZ - questa opzione consente di capovolgere gli assi Y e Z mouse 3D
-   Enable Translations - modo semplice per abilitare/disabilitare traduzioni
-   Enable Rotations - modo semplice per abilitare/disabilitare rotazioni
-   Calibrare - consente di calibrare il navigatore spaziale. Esso viene premuto mentre il navigatore dello spazio non viene spostato.
-   Set To Default - Rimuove tutte le impostazioni e li imposta come predefinito.

Oltre a ciò, per ogni assi avete possibilità di impostare:

-   Enabled - attiva/disattiva assi
-   Reverse - Reverse movimento sugli assi
-   Sensitivity - slider con possibilità di impostare la sensibilità

### Spaceball Buttons 

Quando si apre questa scheda per la prima volta, sarà vuota e non disponibile. Per attivarlo, è necessario premere i pulsanti del mouse lo spazio. Dopo aver fatto, elenco di tasti apparirà sul lato sinistro, e l\'elenco dei comandi saranno disponibile sul lato destro.

Per collegare alcuni comando con un pulsante, selezionare il pulsante sul lato sinistro e esso comando sul lato destro. Premere per cancellare comandi dal pulsante \"Clear\".

## Related

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)

[Category:User Documentation](Category:User_Documentation.md) [Category:3rd Party](Category:3rd_Party.md)
