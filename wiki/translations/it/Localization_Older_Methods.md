# Localization Older Methods/it
{{docnav/it
|[Branding](Branding/it.md)
|[Extra python module](Extra_python_modules/it.md)
}}

Questa è una raccolta di vecchie tecniche di localizzazione utilizzate da FreeCAD in passato. Mostra alcuni dei processi interni, **ma da ora in poi dovrebbero essere utilizzate le tecniche descritte nella pagina [Localizzazione](Localisation/it.md).**

### Traduzione con Qt-Linguist (forma antiquata - OBSOLETA) 

Le seguenti informazioni non devono più essere utilizzate ed è probabile che diventino obsolete. Sono mantenute qui in modo che i programmatori possano conoscere come funzionano.

-   Aprire tutte le cartelle della lingua di FreeCAD mostrate sotto
-   Verificare che non esista un file .ts con il proprio codice lingua (\"fr\" per francese, \"de\" per tedesco, ecc \...)
-   Se esiste, è possibile scaricare tale file, se si desidera modificare, rivedere, o migliorare la traduzione (fare clic sul file, quindi scaricare)
-   Se non esiste, scaricare il file .ts senza codice lingua (o qualsiasi altro .ts disponibile)
-   Rinominare quel file con il proprio codice lingua
-   Aprirlo con il programma Qt-Linguist
-   Eseguire la traduzione (Qt Linguist è molto facile da usare)
-   Una volta completato, salvare il file
-   [Inviarci i file](http://www.freecadweb.org/tracker/main_page.php) in modo che possiamo includerli nel codice sorgente del freecad per consentire anche gli altri utenti di beneficiarne.

\'\'\' File di traduzione disponibili \'\'\'

-   I seguenti collegamenti sono tutti diretti a sourceforge che non è più utilizzato da FreeCAD. Ora il codice è ospitato su <https://github.com/FreeCAD/FreeCAD>.
-   [FreeCAD main GUI](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Gui/Language/)
-   [Complete Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Complete/Gui/Resources/translations/)
-   [Drawing Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Drawing/Gui/Resources/translations/)
-   [Draft Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Draft/Resources/translations/)
-   [Reverse Engineering Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/ReverseEngineering/Gui/Resources/translations/)
-   [FEM Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Fem/Gui/Resources/translations/)
-   [Robot Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Robot/Gui/Resources/translations/)
-   [Image Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Image/Gui/Resources/translations/)
-   [Sketcher Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Sketcher/Gui/Resources/translations/)
-   [Mesh Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Mesh/Gui/Resources/translations/)
-   [Test Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Test/Gui/Resources/translations/)
-   [Points Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Points/Gui/Resources/translations/)
-   [Raytracing Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Raytracing/Gui/Resources/translations/)
-   [Part Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Part/Gui/Resources/translations/)
-   [PartDesign Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/PartDesign/Gui/Resources/translations/)
-   [Assembly Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/Assembly/Gui/Resources/translations/)
-   [MeshPart Workbench](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Mod/MeshPart/Gui/Resources/translations/)
-   C\'è un ottimo post sul forum sul vecchio modo di tradurre, ma è in tedesco. Vedere <http://forum.freecadweb.org/viewtopic.php?f=13&t=19496&start=60#p152655>

## Preparare i propri moduli o applicazioni per la traduzione 

### Prerequisiti

Per realizzare la traduzione del modulo dell\'applicazione servono delle utility fornite con *Qt*. Esse si possono scaricare da [Trolltech-Website](http://www.trolltech.com/products/qt/downloads), ma sono anche contenute in [LibPack](Third_Party_Libraries/it#LibPack.md):

qmake: Genera i file del progetto
lupdate: Estrae o aggiorna i testi originali del progetto tramite la scansione del codice sorgente
Qt-Linguist: *Qt-Linguist* è molto facile da usare, agevola la traduzione con pratiche funzioni e dispone di un frasario per le espressioni più comuni.

### Setup del progetto 

Per iniziare la localizzazione del proprio progetto andare alla GUI-Part del modulo e digitare sulla riga di comando:


```python
qmake -project
```

Questo esegue la scansione della directory del progetto alla ricerca dei file contenenti stringhe di testo e crea un file di progetto come nel seguente esempio:


```python
 ######################################################################
 # Automatically generated by qmake (1.06c) Do 2. Nov 14:44:21 2006
 ######################################################################
 
 TEMPLATE = app
 DEPENDPATH += .\Icons
 INCLUDEPATH += .
 
 # Input
 HEADERS += ViewProvider.h Workbench.h
 SOURCES += AppMyModGui.cpp \
            Command.cpp \
            ViewProvider.cpp \
            Workbench.cpp
 TRANSLATIONS += MyMod_de.ts
```

È possibile aggiungere manualmente i file qui. La sezione TRANSLATIONS contiene un elenco di file con la traduzione per ogni lingua. Nell\'esempio precedente *MyMod\_de.ts* è la traduzione in tedesco.

Ora è necessario eseguire lupdate per estrarre tutte le stringhe letterali nella propria GUI. Eseguire lupdate dopo le modifiche del codice sorgente è sempre una operazione sicura in quanto non cancella mai stringhe dai file di traduzione. Aggiunge solo le nuove stringhe.

Ora è necessario aggiungere i file .ts al proprio progetto VisualStudio. Specificare per essi il seguente metodo di costruzione personalizzato:


```python
 python ..\..\..\Tools\qembed.py "$(InputDir)\$(InputName).ts"
                 "$(InputDir)\$(InputName).h" "$(InputName)"
```

Nota: Inserire questo comando in un\'unica riga, l\'interruzione di riga è finalizzata solo alla visualizzazione.

Compilando il file Gui.cpp*. In questo esempio potrebbe essere *AppMyModGui.cpp*. Aggiungere lì la riga:


```python
new Gui::LanguageProducer("Deutsch", <Modul>_de_h_data, <Modul>_de_h_len);
```

per pubblicare la traduzione nell\'applicazione.

### Configurare i file python per la traduzione 

Per facilitare la localizzazione dei file .py è possibile utilizzare lo strumento *pylupdate4* che accetta uno o più file .py. Con l\'opzione -ts si può preparare / aggiornare uno o più file .ts. Ad esempio per preparare un file .ts per la traduzione in francese è sufficiente inserire nella riga di comando:


```python
pylupdate4 *.py -ts YourModule_fr.ts 
```

lo strumento pylupdate esegue la scansione dei file .py per le funzioni translate() o tr() e crea un file YourModule\_fr.ts. Si può tradurre questo file con QLinguist e produrre il file YourModule\_fr.qm con QLinguist o con il comando:


```python
lrelease YourModule_fr.ts
```

Attenzione che lo strumento pylupdate4 non è molto efficace nel riconoscere le funzioni translate(), esse devono essere formattate in modo molto specifico (vedere come esempio i file del modulo Draft). All\'interno del file, è possibile impostare un traduttore come questo (dopo il caricamento delle QApplication però PRIMA di creare qualsiasi widget Qt):


```python
translator = QtCore.QTranslator()
translator.load("YourModule_"+languages[ln])
QtGui.QApplication.installTranslator(translator)
```

Facoltativamente, è possibile anche creare il file XML Draft.qrc con questo contenuto:


```python
<RCC>
<qresource prefix="/translations" > 
<file>Draft_fr.qm</file> 
</qresource> 
</RCC> 
```

e eseguire pyrcc4 Draft.qrc -o qrc\_Draft.py che crea un grande file Python contenente tutte le risorse. Questo metodo funziona anche per inserire i file di icona in un file di risorse


{{docnav/it
|[Marchiatura](Branding/it.md)
|[Moduli python aggiuntivi](Extra_python_modules/it.md)
}}


 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Localization Older Methods/it
