# Installing on Windows/it
{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}

Si può installare FreeCAD su Windows scaricando uno degli installer seguenti:


{{DownloadWindowsStable}}

Dopo aver scaricato il file .exe (NSIS Installer), fare doppio clic su di esso per avviare il processo di installazione automatica.

Più avanti sono riportate ulteriori informazioni sul alcune opzioni tecniche.
Tuttavia, la maggior parte degli utenti ha solo bisogno dei precedenti file .exe. Al termine dell\'installazione leggere la pagina [Per iniziare](Getting_started/it.md).

## Semplice installazione con NSIS Installer 

Il modo più semplice per **installare FreeCAD su Windows** è utilizzare il pacchetto di installazione scaricabile sopra. Questa pagina descrive l\'utilizzo e le funzionalità di \"NSIS Installer\" per ulteriori opzioni di installazione.

Se si desidera scaricare una versione di sviluppo (che potrebbe essere instabile), vedere la pagina [Download](Download/it.md).

## Chocolatey

Tuttavia, si consiglia vivamente di utilizzare un gestore di pacchetti come Chocolatey per mantenere aggiornato il software. È possibile installare Chocolatey seguendo [queste istruzioni](https://chocolatey.org/install) e quindi aprire un terminale PowerShell come amministratore ed eseguire:


```python
choco install freecad
```

di tanto in tanto si può aggiornare il proprio software con


```python
choco upgrade freecad
```

per ottenere l\'ultima versione disponibile sul repository Chocolatey. In caso di problemi con il pacchetto chocolatey, è possibile contattare i manutentori su [questa pagina](https://chocolatey.org/packages/freecad).

## Installazione da riga di comando 

Con l\'utilità da riga di comando *msiexec.exe*, sono disponibili funzionalità aggiuntive come l\'installazione non interattiva e l\'installazione amministrativa. Vedere sotto gli esempi.

### Installazione non interattiva 

L\'installazione si avvia con il comando:


```python
msiexec /i FreeCAD<version>.msi
```

L\'installazione può essere avviata a livello di programmazione. Ulteriori parametri possono essere passati alla fine della riga di comando, ad esempio:


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

### Limitazione dell\'interfaccia utente 

Il livello di interfaccia visualizzabile dall\'installatore può essere impostato con le opzioni /q

-   /qn - Senza interfaccia
-   /qb - Interfaccia di base - visualizza solo una finestra di dialogo di avanzamento con il pulsante Annulla
-   /qb! - Come /qb, ma nasconde il pulsante Annulla
-   /qr - Interfaccia ridotta - visualizza tutte le finestre di dialogo che non richiedono interazione da parte dell\'utente (salta tutte le finestre modali)
-   /qn+ - Come /qn, ma visualizza la finestra \"Completed\" alla fine

### Directory di destinazione 

La proprietà TARGETDIR determina la directory principale di installazione di FreeCAD.

Ad esempio, si può specificare una diversa unità di installazione con


```python
TARGETDIR=R:\FreeCAD25
```

La cartella di destinazione predefinita (TARGETDIR di default) è \[WindowsVolume\\Programm Files\\\]FreeCAD.

### Installazione per tutti gli utenti 

Aggiungendo


```python
ALLUSERS=1
```

si realizza una installazione usabile da tutti gli utenti. Per impostazione predefinita, un\'installazione non interattiva (/i) rende il pacchetto utilizzabile solo dall\'utente corrente (quello che esegue l\'installazione); un\'installazione interattiva presenta una finestra di dialogo che assume come valore predefinito \"tutti gli utenti\" se l\'utente che esegue l\'installazione ha i permessi necessari.

### Selezione delle funzioni 

Varie proprietà permettono la selezione delle funzioni da installare, reinstallare, o rimuovere.

Il set di funzioni dell\'installatore di FreeCAD è:

-   DefaultFeature - Installa il software appropriato, più le librerie di base
-   Documentation - Installa la documentazione
-   Source code - Installa il codice sorgente
-   \... ToDo

Inoltre, ALL specifica (installa) tutte le funzioni.

Tutte le funzioni dipendono da DefaultFeature, quindi installando qualsiasi funzione si installano automaticamente anche le funzione di default.

Le seguenti proprietà controllano le operazioni di installazione o di rimozione:

-   ADDLOCAL - Elenco delle funzioni da installare sulla macchina locale.
-   REMOVE - Elenco delle funzioni da eliminare dalla macchina locale.
-   ADDDEFAULT - Elenco delle funzioni aggiunte nella loro configurazione di default (che è locale per tutte le funzioni di FreeCAD).
-   REINSTALL - Elenco delle funzioni da reinstallare o riparare.
-   ADVERTISE - Elenco delle funzioni per cui fornire un avviso di installazione.

Ci sono alcune altre proprietà aggiuntive disponibili, vedere la documentazione MSDN per i dettagli.

Con queste opzioni, aggiungendo


```python
ADDLOCAL=Extensions
```

installa l\'interprete e registra le estensioni, ma non installa niente altro.

## Disinstallazione

Si può disinstallare FreeCAD con:


```python
msiexec /x FreeCAD<version>.msi
```

Per la disinstallazione, non è necessario disporre del file MSI; in alternativa, può anche essere specificato il codice del pacchetto o del prodotto.

Per trovare il codice del prodotto, esplorare le proprietà del collegamento per la disinstallazione che FreeCAD installa nel menu di Avvio.

## Installazione Amministrativa 

Si può iniziare una installazione \"amministrativa\" (da rete) con:


```python
msiexec /a FreeCAD<version>.msi
```

I file vengono decompressi nella directory di destinazione (che dovrebbe essere una directory in rete), ma non vengono apportate altre modifiche al sistema locale.

Inoltre, viene generato un altro file .msi (più piccolo) nella directory di destinazione, che i clienti possono utilizzare per eseguire un\'installazione locale (le future versioni potrebbero anche offrire di mantenere alcune funzioni sull\'unità di rete).

Attualmente non esiste alcuna interfaccia per le installazioni amministrative.

La directory di destinazione deve essere specificata nella riga di comando.

Non esiste una specifica procedura di disinstallazione, basta cancellare la directory di destinazione se non è più utilizzata da nessun client.

## Advertisement - Annunciare FreeCAD 

Con


```python
msiexec /jm FreeCAD<version>.msi
```

è possibile, all\'inizio, \"annunciare\" FreeCAD a una macchina (con /jm oppure ad un utente con /ju).

In questo modo, le icone appaiono nel menu Start e le estensioni vengono registrate senza che il software venga effettivamente installato.

Il primo uso di una funzione provoca l\'installazione della funzione stessa.

L\'installatore di FreeCAD attualmente supporta solo l\'annuncio per le voci del menu di avvio, ma non supporta l\'annuncio per i comandi di avvio veloce.

## Installazione automatica su un gruppo di macchine 

Utilizzando i criteri di gruppo di Windows, è possibile automatizzare l\'installazione di FreeCAD su un gruppo di macchine.

Per effettuare questa operazione, attenersi alla seguente procedura:

1.  Accedere al controller di dominio.
2.  Copiare il file MSI in una cartella condivisa a cui è consentito l\'accesso a tutti i computer di destinazione
3.  Aprire il componente MMC \"Active Directory users and computers\"
4.  Passare al gruppo di computer che necessitano di FreeCAD
5.  Aprire Proprietà
6.  Aprire Criteri di gruppo - Group Policies
7.  Aggiungere un nuovo criterio, e editarlo - new policy
8.  In Computer Configuration/Software Installation, sceglire New/Package
9.  Selezionare il file MSI attraverso il percorso di rete
10. Facoltativamente, selezionare che si desidera che FreeCAD venga disinstallato se il computer lascia il campo di applicazione del criterio.

La propagazione dei criteri di gruppo richiede in genere un po \'di tempo - per distribuire in modo affidabile il pacchetto, tutte le macchine dovrebbero essere riavviate.

## Installazione su Linux con Crossover Office 

È possibile installare la versione Windows di FreeCAD su un sistema Linux utilizzando *CXOffice 5.0.1*.

Eseguire *msiexec* dalla riga di comando di CXOffice.

Supponendo che il pacchetto di installazione si trovi nella directory \"software\", nell\'unità \"Y:\":


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD viene eseguito, ma è stato riferito che OpenGL non funziona, come succede con altri programmi che girano sotto [http://es.wikipedia.org/wiki/Wine Wine](http://es.wikipedia.org/wiki/Wine_Wine.md), quali ad esempio [Google SketchUp](http://es.wikipedia.org/wiki/Google_SketchUp.md).


{{docnav/it
|[Funzionalità](Feature_list/it.md)
|[Installare in Linux](Installing_on_Linux/it.md)
}}

---
[documentation index](../README.md) > Installing on Windows/it
