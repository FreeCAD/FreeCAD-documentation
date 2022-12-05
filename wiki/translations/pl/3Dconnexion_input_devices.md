# <img alt="kontroler SpaceNavigator firmy 3Dconnexion" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/pl


{{TOCright}}

## Instalacja sterowników 

### Linux

FreeCAD używa sterowników z projektu [Spacenav](http://spacenav.sourceforge.net/). Jest to projekt mający na celu stworzenie otwartego sterownika, który jest kompatybilny z zamkniętym sterownikiem firmy 3Dconnexion.

#### Instalacja z repozytorium 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Należy jednak pamiętać, że wersja 0.6 dostępna na Ubuntu 20.04 *(i prawdopodobnie starsze wersje)* nie działa. Należy wtedy skompilować spacenavd ze źródła, jak wyjaśniono poniżej.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```

Spacenav potrzebuje tych uprawnień:

:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Uruchom ponownie spnavd i FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```

#### Kompilacja Spacenav z pliku źródłowego 

Rozwiązanie to jest zalecane, jeśli dystrybucja może zawierać nieaktualną wersję.

-   Pobierz następujące pliki:
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) *(najnowsza wersja)*,
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) *(pobierz najnowszą wersję libspnav)*,
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) *(pobierz najnowszą wersję libspnav)*,
-   Rozpakuj archiwa do folderu w swoim katalogu domowym.
-   Wejdź do katalogu spacenavd-x.x i wykonaj następujące polecenia:

:   
    
```python
    ./configure
    make
    
```
    

-   Jeśli operacja przebiegła pomyślnie, wykonaj następujące polecenia **jako root** *(lub za pośrednictwem sudo)*.

:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Instaluje demona spacenav, konfiguruje go do automatycznego ładowania przy starcie systemu i uruchamia demona bez konieczności ponownego uruchamiania.
-   Teraz należy sprawdzić, czy urządzenie zostało prawidłowo wykryte. Gdy urządzenie jest odłączone od zasilania, wykonaj poniższe polecenie, a następnie podłącz je do komputera.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Jeżeli rezultat wygląda tak, jak poniżej, można kontynuować.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    

-   Teraz wejdź do katalogu o nazwie libspnav-x.x.x i wykonaj następujące polecenia:

:   
    
```python
    ./configure
    make
    
```
    

-   Jeśli `make` nie powiedzie się z następującym błędem: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... to musisz zainstalować libgtkmm-2.4-dev. W Ubuntu robi się to w następujący sposób:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Jeśli operacja przebiegła pomyślnie, wykonaj następujące polecenia **jako root** *(lub za pośrednictwem sudo)*.

:   
    
```python
    make install
    
```
    

-   Poszukaj w katalogu libspnav-x.x.x.x/examples/. Jeśli chcesz przetestować swoje urządzenie, skompiluj i uruchom jeden z dwóch przykładów.

-   W ten sam sposób należy skompilować i zainstalować spnavcfg. Upewnij się, że uruchamiasz `spnavcfg` jako root, w przeciwnym razie ustawienia nie zostaną zapisane!

#### Uruchamianie spacenavd jako usługi systemd przy starcie systemu 

Jeśli chcesz uruchamiać spacenavd przy starcie systemu za pomocą systemd, wykonaj następujące operacje:

-   Przejdź do katalogu, w którym sklonowałeś repozytorium spacenavd *(do katalogu głównego repozytorium)*,

-    `sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service`.

-    `sudo systemctl enable spacenavd-local.service`.

-    `sudo systemctl start spacenavd-local.service`, jeśli chcesz uruchomić go od razu.

Jest to konieczne tylko w przypadku instalacji ze źródła.

#### Restartowanie spacenavd 

Jeśli czasami nawigator przestaje działać, dobrze jest zrestartować sterownik. Aby go zrestartować, przejdź do terminala i wykonaj polecenie:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Następnie uruchom ponownie program FreeCAD. W niektórych dystrybucjach jest to konieczne przy każdym starcie systemu.

## Znane problemy 

Jeden z użytkowników zgłosił [na forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327), że widzi następującą sytuację: {{code|  Spacenav daemon 0.6
  failed to open config file /etc/spnavrc: No such file or directory. using defaults.
  adding device.
  device name: 3Dconnexion SpacePilot
  using device: /dev/input/event5
  No protocol specified
  failed to open X11 display ":0.0"}} Rozwiązanie, które zadziałało w jego przypadku:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```

### OSX

Urządzenia wejściowe 3Dconnexion są obsługiwane w systemie OS X, pod warunkiem, że program FreeCAD jest kompilowany i używany w systemie z zainstalowanymi sterownikami 3Dconnexion. Możesz potrzebować 3DxWare 10.7.2 lub nowszego dla Mac OSX Monterey.

### Windows

Począwszy od wersji 0.13, mysz 3D jest obsługiwana w systemie Windows. Musisz mieć zainstalowane sterowniki 3Dconnexion.

#### Znane problemy 

Występuje problem polegający na tym, że program 3Dconnexion wysyła do programu FreeCAD zduplikowane zdarzenia przewijania, co powoduje przeskakiwanie widoku. Aby to naprawić:

1.  Otwórz Właściwości 3Dconnexion. Możesz dwukrotnie kliknąć jego ikonę na pasku zadań, obok zegara Windows.
2.  Kliknij przycisk Ustawienia zaawansowane.
3.  Otwórz program FreeCAD lub przełącz się do już otwartego okna programu FreeCAD.
4.  Przełącz się z powrotem do Ustawień zaawansowanych 3Dconnexion. Upewnij się, że w nagłówku jest napisane \"FreeCAD\".
5.  Usuń zaznaczenie wszystkich pól na stronie.

ref: <https://freecadweb.org/tracker/view.php?id=1893>

## Konfiguracja programu FreeCAD 

Obsługa myszy 3D została wykonana za pomocą projektu spnav w systemie Linux i na bardzo niskim poziomie w systemie Windows. Oznacza to, że nie było obsługi żadnych ustawień urządzenia, ponieważ w systemie Linux nie ma dobrego wsparcia, a w systemie Windows jest to nadpisane. Dlatego do okna *Dostosuj* dodano dwie dodatkowe strony.

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">

### Ruch Spaceball 

Na tej karcie można skonfigurować niektóre z ogólnych ustawień myszy przestrzennej. Należą do nich:

-   Czułość globalnie - suwak umożliwiający ustawienie czułości globalnej
-   Dominacja - jeśli włączysz tryb dominujący, pod uwagę będą brane tylko osie o największym ruchu
-   Odwróć YZ - ta opcja umożliwia odwrócenie osi Y i Z w myszy 3D.
-   Włącz przesunięcia *(Włącz przesunięcia)* - prosty sposób na włączenie/wyłączenie przesunięć
-   Włącz obroty - łatwy sposób na włączenie/wyłączenie obrotu
-   Kalibruj - umożliwia kalibrację nawigatora przestrzeni. Naciska się go, gdy nawigator nie jest poruszany.
-   Ustaw na domyślne - usuwa wszystkie ustawienia i ustawia je na domyślne.

Oprócz tego dla każdej osi można ustawić:

-   Włączone - włączanie / wyłączanie osi
-   Odwróć - odwracanie ruchu na osiach.
-   Czułość - suwak z możliwością ustawienia czułości.

### Przyciski Spaceball 

Gdy otworzysz tę kartę po raz pierwszy, będzie ona pusta i niedostępna. Aby ją uaktywnić, należy nacisnąć jeden z klawiszy spacji myszy. Po jego naciśnięciu po lewej stronie pojawi się lista przycisków, a po prawej lista dostępnych poleceń.

Aby połączyć określone polecenie z przyciskiem, wybierz przycisk po lewej stronie, a jego polecenie po prawej stronie. Aby usunąć polecenia z przycisku, naciśnij przycisk **Wyczyść**.

### Rozwiązywanie problemów 

Sprawdź, czy Twoja instalacja FreeCAD łączy się z biblioteką spacenav. Najlepszym sposobem sprawdzenia tego jest uruchomienie programu FreeCAD z wiersza poleceń terminala `FreeCAD --log-file /tmp/freecad.log` i natychmiastowe zamknięcie go ponownie. Następnie otwórz plik **/tmp/freecad.log** i poszukaj komunikatów:


`Connected to spacenav daemon`

lub


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

Jeśli nie pojawi się żaden z nich, oznacza to, że Twój program FreeCAD nie jest połączony z biblioteką spacenav. Jeśli pojawi się pierwszy z tych komunikatów, oznacza to, że program w zasadzie działa. Drugi komunikat oznacza, że prawdopodobnie wystąpił problem z demonem spacenav.

## Powiązane

-   Wątek na forum [spacenav na windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Wątek na forum [Space navigator pomylenie os](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > 3Dconnexion input devices/pl
