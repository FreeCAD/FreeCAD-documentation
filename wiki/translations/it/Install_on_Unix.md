


<div class="mw-translate-fuzzy">





</div>

## Descrizione


{{TOCright}}

L\'installazione di FreeCAD sui più noti sistemi Linux è stata ora approvata dalla comunità e FreeCAD dovrebbe essere direttamente disponibile tramite il gestore di pacchetti disponibile per la propria distribuzione. Il team di FreeCAD fornisce anche alcuni:

-   Pacchetti \"ufficiali\" quando vengono rilasciate nuove versioni
-   Repository sperimentali [Personal Package Archive](https://help.ubuntu.com/community/PPA) (PPA), [AppImages](AppImage.md), e [Ubuntu Snaps](Ubuntu_Snap.md) per testare le ultime funzioni sviluppate.


<div class="mw-collapsible mw-collapsed toccolours">

## Ubuntu e sistemi basati su Ubuntu 

Molte distribuzioni Linux sono basate su Ubuntu e condividono i suoi repository. Per altre varianti ufficiali (Kubuntu, Xubuntu e Lubuntu), ci sono distro non ufficiali come per Linux Mint, Voyager e altri. Le opzioni di installazione riportate in seguito dovrebbero essere compatibili con tali sistemi.


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

### Repository ufficiale di Ubuntu 


</div>

FreeCAD è disponibile nel repository ufficiale di Ubuntu e può essere installato tramite **Software Center** o dal terminale:


```python
sudo apt install freecad
```


**Nota:**

il pacchetto del repository di Ubuntu potrebbe essere obsoleto rispetto all\'ultimo codice sorgente stabile. In questo caso, si consiglia di installare il pacchetto dal PPA `-stable` sottostante. Inoltre, l\'installazione del pacchetto `-daily` può essere eseguita per testare il ramo di sviluppo.


<div class="mw-translate-fuzzy">

### PPA stabile 


</div>


<div class="mw-translate-fuzzy">

Il Personal Package Archive (PPA) per la versione stabile di FreeCAD è mantenuto dalla comunità di FreeCAD su Launchpad. Il repository Launchpad viene chiamato [FreeCAD Stable Releases](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable) .


</div>

#### Interfaccia grafica 

Installare il PPA stabile tramite l\'interfaccia utente grafica (GUI):


<div class="mw-translate-fuzzy">


:   1\. Navigare verso **Software per Ubuntu → Software e Aggiornamenti → Codice sorgente → Altro Software**
:   2\. Cliccare su **Aggiungi**, quindi copiare e incollare la riga seguente


</div>


:   

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Aggiungere il sorgente, chiudere la finestra di dialogo e ricaricare i sorgenti del software, se richiesto.

Ora si può trovare e installare l\'ultima versione stabile di FreeCAD da **Ubuntu Software Center**.

#### Riga di comando 

Installare il PPA stabile tramite l\'interfaccia della riga di comando (CLI):

:   1\. Aggiungere il PPA al proprio sorgenti software:

    :   
        
```python
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        
```
        





:   2\. Recuperare gli elenchi dei pacchetti aggiornati:

    :   
        
```python
        sudo apt update
        
```
        





:   3\. Quindi installare FreeCAD insieme alla sua documentazione offline:

    :   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Nota:**

a causa di problemi di pacchettizzazione, in alcune versioni di Ubuntu il pacchetto `freecad-doc` è entrato in conflitto con l\'installazione di FreeCAD o con una delle sue dipendenze; in questo caso, rimuovere il pacchetto `freecad-doc` e installare solo il pacchetto `freecad`. Se il pacchetto `freecad-doc` non esiste, ignoralo.

#### Verificare l\'installazione 

:   4\. Una volta che il PPA stabile è stato aggiunto ai sorgenti usando uno dei metodi sopra, il pacchetto `freecad` installerà questa versione PPA su quella fornita dal repository di Ubuntu Universe. Si può vedere le versioni disponibili con il seguente comando `apt-cache`:
:   
    
```python
    apt-cache policy freecad
    
```
    





:   L\'output dovrebbe essere simile al seguente (ovviamente le informazioni sulla versione varieranno):


```python
freecad:
  Installed: (none)
  Candidate: 2:0.18.4+dfsg1~201911060029~ubuntu18.04.1
  Version table:
     2:0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
        500 http://ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
     0.16.6712+dfsg1-1ubuntu2 500
        500 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
ubuntu@ubuntu:~$ apt-cache policy freecad-doc
```


:   5\. Richiamare la versione stabile (PPA) di FreeCAD dall\'interfaccia grafica (GUI) o dalla riga di comando (CLI). Quest\'ultimo metodo è il seguente:
:   
    
```python
    ./freecad
    
```
    

### PPA per le versioni di sviluppo (Daily) 

Dato che FreeCAD è in costante sviluppo, si potrebbe voler installare il pacchetto **daily** per essere aggiornati sugli ultimi miglioramenti e correzioni di bug. Il repository è anche ospitato su Launchpad e viene chiamato [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

Questa versione viene compilata quotidianamente dal repository principale ufficiale. Tienere presente che, sebbene contenga nuove funzioni e correzioni di bug, potrebbe anche avere bug più recenti ed essere instabile.

Aggiungere il PPA daily alle sorgenti software, aggiornare gli elenchi dei pacchetti e installare il pacchetto daily: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

È possibile aggiornare quotidianamente la versione daily: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Nota:**

in alcuni casi il nuovo codice o le dipendenze aggiunte a FreeCAD causano errori di pacchettizzazione; se ciò accade, il pacchetto daily potrebbe non essere generato fino a quando i manutentori non risolvono manualmente i problemi. Se si desidera continuare a testare il codice più recente, bisogna scaricare il codice sorgente e compilare FreeCAD direttamente; per le istruzioni vedere [compilazione](compiling/it.md).

Esegui la versione daily (PPA) di FreeCAD:

:   
    
```python
    freecad-daily
    
```
    


**Nota:**

è possibile installare entrambi i pacchetti `-stable` e `-daily` nello stesso sistema. Ciò è utile se si desidera lavorare con una versione stabile ed essere comunque in grado di testare le ultime funzioni in fase di sviluppo. Notare che l\'eseguibile per la versione giornaliera è `freecad-daily`, ma per la versione stabile è solo `freecad`.


</div>


</div>

## Debian e altri sistemi basati su Debian 

A partire da Debian Lenny, FreeCAD è disponibile direttamente nei repository di software Debian e può essere installato tramite Synaptic o semplicemente con:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD is typically installed with YAST (abbr. Yet another Setup Tool) the Linux operating system setup and configuration tool, or in any terminal/console (root rights required) with:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Note:**

This procedure only covers the installation of officially released **stable** FreeCAD program versions, depending on the installed links to the program package repositories of your OS version. The openSUSE package *may be outdated* as the packaging may lag behind the latest stable source code. In this case, it is suggested to install the package manually from the below indicated (Expand) source repositories.


<div class="mw-collapsible-content">

A vast release program for FreeCAD package builds are offered. Please visit for a survey:

**[Survey of repositories on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Generally for selecting the correct openSUSE distribution needed it is necessary to click on the particular **View** button.

### Stable

The stable package version: [Stable repositories on openSUSE](https://software.opensuse.org/package/FreeCAD). The correct openSUSE distribution version must be selected in the lower part of the web page.

Note: openSUSE has several options to choose from when downloading FreeCAD. To view these options, visit [Survey of stable repositories on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Sviluppo

Latest development releases AKA **unstable**: [Unstable repositories listings on openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

It is recommended to grab the binary packages directly. Then select the correct distribution for your installed openSUSE OS.


</div>


</div>

## Gentoo

FreeCAD si può costruire/installare semplicemente eseguendo:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD has been included in the official Fedora packages since Fedora 20. It can be installed from the command line with:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

On older Fedora releases, that was:


```python
sudo yum install freecad
```

The gui packages managers can also be used. Search for \"freecad\". The official release package version tends to be well behind the FreeCAD releases. [Package: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) shows the versions included in the Fedora repositories over time and versions.

More current versions can be obtained by downloading one of the [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)releases from the github repository. These work fine on Fedora.

If you want to keep up with the absolute latest daily builds, FreeCAD is also available on [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). To install the build from there, in a terminal session, enter:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

That leaves the copr repository active, so


```python
sudo dnf upgrade
```

or equivalent, will update to the latest FreeCAD build, along with updates from any of the other active repos. If you want something a bit more stable, you can disable \@freecad/nightly again after the initial install. The copr repository only keeps builds from the past 2 weeks. This is not a solution if you want to pick a specific older version.

Instructions are also available on [compile FreeCAD yourself](Compile_on_Linux.md), including a script specifically for Fedora. With a minor change, to checkout the specific commit from git, any version since about FreeCAD 0.15 can be built on any distribution since Fedora 21.


</div>


</div>

## Arch

Installing FreeCAD on Arch Linux and derivatives (ex. Manjaro):


```python
pacman -S freecad
```

## Altri

Se scoprite che il vostro sistema è dotato di FreeCAD, ma in questa pagina non è documentato, per favore comunicatelo tramite il [forum](http://forum.freecadweb.org/viewforum.php?f=21)!

Sulla rete sono disponibili diversi pacchetti alternativi non ufficiali di FreeCAD, ad esempio per sistemi come Slackware o Fedora. Una ricerca in rete può dare rapidamente buoni risultati.

### Installazione manuale in sistemi basati su .deb 

Se per qualche motivo non è possibile utilizzare uno dei metodi di cui sopra, si può sempre scaricare uno dei pacchetti .deb disponibili nella pagina [Download](Download.md).
{{DownloadUnixStable}}

Dopo aver scaricato la versione .deb corrispondente al proprio sistema, se è installato il pacchetto [Gdebi](wikipedia:Debian#GDEBI.md) (di solito lo è), basta spostarsi nella cartella del file scaricato e fare doppio clic su di esso. Le dipendenze necessarie sono installate automaticamente dal gestore del sistema. In alternativa è possibile installare il pacchetto dal terminale; spostarsi nella cartella che contiene il file e digitare:


```python
sudo dpkg -i Name_of_your_FreeCAD_package.deb
```

sostituendo a Name\_of\_your\_FreeCAD\_package.deb il nome del file scaricato

Terminata l\'installazione di FreeCAD, nella sezione \"Grafica\" del Menu Start viene aggiunta l\'icona per avviarlo.

### Installazione in altri sistemi Linux/Unix 

Many common Linux distros now include a precompiled FreeCAD as part of the standard packages. This is often out of date, but is a place to start. Check the standard package managers for your system. One of the following (partial) list of commands could install the official version of FreeCAD for your distro from the terminal. These probably need administrator privileges.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
```

The package name is case sensitive, so try \FreeCAD\ as well as \freecad\. If that does not work for you, either because your package manager does not have a precompiled FreeCAD version available, or because the available version is too old for your needs, you can try downloading one of the [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) releases from the github repository. These tend to work on most 64 bit Linux distributions, without any special installation. Just make sure the downloaded file is marked as executable, then run it.


<div class="mw-translate-fuzzy">

Se ciò non basta, e non è possibile individuare un\'altra fonte di un pacchetto precompilato per la propria situazione, è necessario [compilare FreeCAD](Compile_on_Linux/Unix/it.md) da soli.


</div>

### Installing Windows Version on Linux 

See the [Installing on Windows](Installing_on_Windows.md) page.

## Next Step 

Appena terminata l\'installazione di FreeCAD, è ora di [iniziare](Getting_started/it.md)!


<div class="mw-translate-fuzzy">





</div>




[Category:Common Questions{{\#translation:}}](Category:Common_Questions.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
