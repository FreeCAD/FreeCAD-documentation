# Compile on Docker/it
}





{{TOCright}}



## Presentazione

Tra le opzioni per la compilazione e l\'installazione di FreeCAD, c\'è la possibilità di utilizzare Docker. Questo metodo è utile principalmente per gli sviluppatori di FreeCAD che utilizzano computer Linux o Mac OS.



### Vantaggi

Tutte le dipendenze di FreeCAD sono già installate, compatibili tra loro e configurate in modo appropriato, consentendo di iniziare a sviluppare molto rapidamente.

-   Le dipendenze sono contenute all\'interno del contenitore docker, impedendo ad eventuali pacchetti indesiderati di contaminare la tua workstation e prevenendo eventuali conflitti tra versioni.
-   Il codice sorgente e le directory di compilazione sono al di fuori del contenitore docker. Ciò ti consente di utilizzare i tuoi editor preferiti, i sistemi di controllo delle versioni, gli strumenti di sviluppo e così via, senza doverli configurare nel contenitore docker. Puoi semplicemente usarli normalmente, direttamente dalla tua postazione di lavoro. (Inoltre, significa che non è necessario ricostruire il contenitore docker ogni volta che si desidera creare FreeCAD.)
-   Per coloro che usano oscure distribuzioni \*nix per le quali le [istruzioni non sono disponibili](Compile_on_Linux/it#Ottenere_le_dipendenze.md) per recuperare le dipendenze, tutto ciò che si deve installare sulla workstation è docker, che è comunemente disponibile in molte distribuzioni.
-   Fornisce un ambiente di sviluppo statico e immutabile. Personalmente lo trovo utile durante lo sviluppo per ridurre il numero di potenziali variabili che potrebbero causare un problema. Si è sicuri di non aver alterato qualcosa di esoterico nell\'ambiente tra le build. Per gli sviluppatori che collaborano ed utilizzano lo stesso contenitore docker, si può essere certi di lavorare tutti sullo stesso ambiente, il che riduce gli errori di comunicazione causati dalle differenze nell\'ambiente.



## Repository Docker 

-   Originario: <https://gitlab.com/daviddaish/freecad_docker_env>
-   Ufficiale: <https://GitHub.com/FreeCAD/Docker>



## Prerequisiti

-   10GB di spazio libero
-   Docker



## Installazione



### Scarica i sorgenti 

Il modo migliore per ottenere il codice sorgente di FreeCAD è clonare il [repository Git](https://github.com/FreeCAD/FreeCAD). Per questo è necessario il programma `git` che può essere facilmente installato nella maggior parte delle distribuzioni Linux e Mac OS, e può anche essere ottenuto dal [sito ufficiale](http://git-scm.com/).

Questo collocherà una copia dell\'ultima versione del codice sorgente di FreeCAD in una nuova directory chiamata `freecad_source`.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git ~/my_code/freecad_source
}}

Per ulteriori informazioni sull\'utilizzo di Git e sul contributo del codice al progetto, vedere [Gestione del codice sorgente](Source_code_management/it.md).

#### Archivio dei sorgenti 

In alternativa si può scaricare il sorgente dall\'[archivio](https://github.com/FreeCAD/FreeCAD/releases/latest), in un file `.zip` o `.tar.gz` e scompattarlo nella directory desiderata.



### Creare la cartella di compilazione 

Creare una directory per contenere il sorgente di FreeCAD compilato.


{{Code|lang=bash|code=
mkdir ~/my_code/freecad_build
}}



### Prelevare l\'immagine Docker 

Prelevare l\'immagine Docker. (Immagine ufficiale in arrivo.)


{{Code|lang=bash|code=
docker pull registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



### Consentire l\'accesso al tuo gestore di finestre 

Affinché FreeCAD possa avviare la sua GUI dall\'interno del contenitore Docker, è necessario concedere le autorizzazioni di accesso a Docker al gestore delle finestre. Nella maggior parte delle distribuzioni Linux, questo è il sistema X Window. È possibile utilizzare il comando seguente per consentire l\'accesso generale a X, fino al riavvio o alla disconnessione dal computer.


{{Code|lang=bash|code=
xhost +
}}

Se si è connessi a qualsiasi sistema non affidabile, ad esempio tramite `ssh`, questo ti renderà vulnerabile al codice dannoso. Chiudere tutte le connessioni `ssh` o cercare autorizzazioni xhost più sicure, ciò esula dallo scopo di questo tutorial.



#### Utenti Mac OS 

Per coloro che utilizzano Mac OS, il sistema X Window potrebbe non essere installato. Il progetto XQuartz è un progetto open source di lunga durata che ti consentirà di aggiungerlo al tuo computer. [Lo trovi qui](https://www.xquartz.org/).



### Lanciare l\'immagine the docker 

Assegnare le variabili di ambiente in modo che il contenitore Docker monti il ​​codice sorgente di FreeCAD e crei la directory. Inoltre, si può montare una cartella aggiuntiva per contenere tutti i file che si desidera utilizzare a scopo di test. Nello snippet sottostante, è stata lasciata come home directory per semplice impostazione predefinita.


{{Code|lang=bash|code=
fc_source=~/my_code/freecad_source
fc_build=~/my_code/freecad_build
other_files=~/
}}

Avviare l\'immagine Docker.


{{Code|lang=bash|code=
docker run -it --rm \
-v $fc_source:/mnt/source \
-v $fc_build:/mnt/build \
-v $other_files:/mnt/files \
-e "DISPLAY" -e "QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
registry.gitlab.com/daviddaish/freecad_docker_env:latest
}}



### Compilare FreeCAD 

È possibile creare FreeCAD utilizzando lo script di compilazione installato o utilizzando il metodo preferito.


{{Code|lang=bash|code=
/root/build_script.sh
}}



### Eseguire FreeCAD 

Una volta che FreeCAD è stato compilato, può essere eseguito normalmente.


{{Code|lang=bash|code=
/mnt/build/bin/FreeCAD
}}

Puoi trovare le directory allegate nella cartella `/mnt`.



## Discussioni

-   [Docker env build container](https://forum.freecadweb.org/viewtopic.php?f=4&t=42954)
-   [VSCode setup with Docker (1)](https://forum.freecadweb.org/viewtopic.php?f=10&t=48266)
-   [VSCode setup with Docker (2)](https://forum.freecadweb.org/viewtopic.php?p=427812#p427812)



## Correlazioni

-   [AppImage](AppImage.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > Compile on Docker/it
