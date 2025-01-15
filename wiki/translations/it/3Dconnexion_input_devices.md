# <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/it






### Installare i driver 



#### Linux

FreeCAD supporta i driver dal progetto [Spacenav](http://spacenav.sourceforge.net/). Si tratta di un progetto che mira a creare un driver open-source che sia compatibile con i driver proprietari di 3Dconnexion.



#### Installare da repo 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Si noti, tuttavia, che la versione 0.6 disponibile su Ubuntu 20.04 (e probabilmente quelle precedenti) non sembra funzionare. Devi quindi compilare spacenavd dal sorgente come spiegato di seguito.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```


:   spacenav ha bisogno di queste autorizzazioni





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Riavvia spnavd e FreeCAD





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

-   Scaricare i seguenti file:
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) (latest version)
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) (get latest libspnav version)
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) (get latest libspnav version)
-   Scompattare gli archivi in una cartella nella propria directory /home.
-   Entrare nella directory spacenavd-x.x ed eseguire i seguenti comandi:

:   
    
```python
    ./configure
    make
    
```
    

-   Se questo ha successo, eseguire i seguenti comandi **come root** (o con prefisso sudo).

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
    

-   Ora entrare nella directory denominata libspnav-x.x.x ed eseguire i seguenti comandi:

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
    

-   Consultare la directory libspnav-x.x.x/examples/. Se si desidera provare il proprio dispositivo, compilare ed eseguire uno dei due esempi.

-   Seguire lo stesso procedimento per compilare e installare spnavcfg. Ricordarsi di eseguire spnavcfg come root, altrimenti non verrà salvata nessuna impostazione!



#### Avvio di spacenavd come servizio systemd all\'avvio 

Se vuoi avviare spacenavd all\'avvio usando systemd, procedi come segue:

-   Vai alla directory in cui hai clonato il repository spacenavd (alla radice del repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", se vuoi avviarlo subito.

Questo è necessario solo per l\'installazione dal sorgente.



#### Riavviare spacenavd 

Se talvolta navigatore smette di funzionare, è bene riavviare il conducente. Per riavviarlo, andare al terminale ed eseguire:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Dopo avere riavviare FreeCAD. Su alcune distro è necessario a ogni avvio.



#### Problemi noti 

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

### MacOS

Su macOS i dispositivi di input 3Dconnexion sono supportati, purché FreeCAD sia costruito e utilizzato su un sistema con i driver 3Dconnexion installati. Potrebbe essere necessario 3DxWare 10.7.2 o superiore per macOS 12 Monterey.

### Windows

A partire dalla versione 0.13, il mouse 3D è supportato sotto windows. È necessario avere installato i driver 3Dconnexion. Nella versione 1.0 di FreeCAD è stata introdotta una [nuova integrazione con i dispositivi 3Dconnexion](https://github.com/FreeCAD/FreeCAD/pull/12929). Se compilato con tale integrazione, è supportato solo l\'hardware recente: per supportare i dispositivi più vecchi gli utenti dovranno auto-compilarli con la variabile cMake FREECAD_3DCONNEXION_SUPPORT impostata su \"Raw Input\". Gli utenti Windows devono essere consapevoli che il driver di 3Dconnexion (\"non\" il codice in FreeCAD) contiene un pacchetto di telemetria che comunica le informazioni sul software installato a 3Dconnexion.



#### Problemi noti 

-   In FreeCAD versione 1.0 e successive la modifica delle impostazioni nella finestra di configurazione 3DX potrebbe non produrre i risultati attesi ([issue](https://github.com/FreeCAD/FreeCAD/issues/14044)). Per risolvere questo problema:
    1.  Arrestare il driver (eseguendo Stop 3DxWare).
    2.  Andare in **..<utente>\AppData\Roaming\3Dconnexion\3DxWare\Cfg** ed eliminare il file **FreeCAD.xml**.
    3.  Avviare il driver (eseguendo Start 3DxWare).
    4.  Eseguire FreeCAD e verificare se è possibile modificare le impostazioni di [Spaceball Motion](#Spaceball_Motion.md).

## Setting up FreeCAD 


{{VersionPlus/it|1.0}}

: Il manipolatore 3Dconnexion può essere configurato nella sua app driver (software 3DxWare).


{{VersionMinus/it|0.21}}

: se viene rilevata un Spaceball, è possibile utilizzare le seguenti schede nella [finestra di dialogo Personalizza](Interface_Customization/it.md) per modificare le impostazioni:

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



### Risoluzione dei problemi 

Controlla se l\'installazione di FreeCAD si collega alla libreria spacenav. Il modo migliore per verificarlo è eseguire FreeCAD dal terminale della riga di comando `FreeCAD --log-file /tmp/freecad.log` e chiuderlo immediatamente. Quindi apri il file **/tmp/freecad.log** e cerca i messaggi:


`Connected to spacenav daemon`

oppure


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

Se nessuno di essi appare, la build di FreeCAD non si collega alla libreria Spacenav. Se viene visualizzato il primo messaggio, in pratica funziona. Quest\'ultimo messaggio indica che probabilmente c\'è un problema con il demone spacenav.



## Relazioni

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > [3rd Party](Category_3rd%20Party.md) > 3Dconnexion input devices/it
