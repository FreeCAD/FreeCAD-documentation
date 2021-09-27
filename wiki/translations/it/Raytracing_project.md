# Raytracing project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


**(2020) This page refers to an attempt to update the [Raytracing Workbench](Raytracing_Workbench.md), proposed around 2012. Its original author never completed the implementation so this information is outdated, and should not be considered current.

New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], a complete Python replacement for the [Raytracing Workbench](Raytracing_Workbench.md).
**


{{TOCright}}

Questo è il progetto di sviluppo per l\'implementazione di un modulo Raytracing in FreeCAD (Rendere realistici gli oggetti tramite il tracciato di raggi di luce). Esso segue le regole della metodologia _ (Development roadmap).


<div class="mw-translate-fuzzy">

## Finalità e principi 

Lo scopo di questo progetto è quello di aggiornare il modulo di renderizzazione corrente <img alt="" src=images/Raytracing.png  style="width:16px;"> [Raytracing](Raytracing_Workbench/it.md) che ora utilizza [POV-Ray](http://www.povray.org/) (un renderizzatore parziale che dà risultati soddisfacenti) e permettere di utilizzare renderizzatori più moderni come [Lux Render](http://www.luxrender.net/en_GB/index), [Yafaray](http://www.yafaray.org/), [Indigo](http://www.indigorenderer.com/).


</div>

Scopo di questo progetto è anche quello di fornire una interfaccia generica che permetta di utilizzare più back-end (stadi finali) di renderizzazione per visualizzarne le caratteristiche all\'interno di FreeCad. Una interfaccia di programmazione più generica permetterà di creare più facilmente i plugin di rendering.

L\'interfaccia consentirà di utilizzare sia i renderizzatori open source che i renderizzatori proprietari esterni per generare file di scena compatibili e avviare un processo separato in background. Il risultato potrà quindi essere visualizzato in anteprima direttamente all\'interno FreeCAD aprendo il file temporaneo di output (se disponibile).

Ogni renderizzatore sarà un plugin all\'interno di una interfaccia generica e fornirà materiali e modalità di renderizzazione compatibili.

## Risultati

Una eccellente visualizzazione realistica! Produrre risultati di alta qualità degli oggetti dei documenti di FreeCAD e fornire una interfaccia molto semplice con i parametri preimpostati per consentire l\'avvio rapido dell rendering e delle anteprime.

L\'interfaccia utente dovrebbe consentire di realizzare situazioni complesse e, possibilmente, di visualizzarle in anteprima in modo da permettere di cambiare e modificare le luci e le posizioni. Tuttavia, l\'obiettivo è di fornire una suite di rendering completa di tutte le funzionalità.

## Riflessioni

\'Dovrà\' essere creata una libreria dei materiali per ogni plugin di rendering con i parametri preimpostati. Le proprietà del materiale potranno essere modificate.

Avere i parametri della scena preimpostati dovrebbe consentire anche agli utenti poco esperti di rendering di produrre delle belle immagini in breve tempo.

## Organizzazione

L\'interfaccia generica è attualmente in fase di creazione e, per testarla, [Lux Render](http://www.luxrender.net/en_GB/index), che è un renderizzatore unbiased (accurato), sarà il primo renderizzatore ad essere implementato.

Il lavoro attuale è realizzato interamente da mrlukeparry sul suo ramo di renderizzazione [Github Render Branch](https://github.com/mrlukeparry/FreeCAD_sf_master/tree/raytracing).

**Attualmente è possibile renderizzare oggetti con Lux Render:**

![](images/LuxRenderOutput.png )

Nell\'immagine precedente è visualizzata una Parte creata da uno Schizzo di PartDesign e poi renderizzata con il nuovo Modulo Render in fase di sviluppo in Lux Render. Lux Render permette di creare gradevoli effetti, come ad esempio la profondità di campo [DOF (Depth of Field)](http://wiki.blender.org/index.php/Doc:FR/2.4/Manual/Render/Camera/Depth_Of_Field), per migliorare il realismo.

## Azioni successive 

-   Creare l\'Astrazione per fornire l\'interfaccia ai renderizzatori (Fatto)
-   Implementare una interfaccia per descrivere i materiali generici e collezionarli (Fatto)
-   Implementare un\'interfaccia per descrivere i parametri di renderizzazione preimpostati (Fatto)
-   Implementare una funzione per memorizzare tutte queste informazioni in modo permanente (In corso)
-   Creare un modulo di ambiente per visualizzare l\'output (Fatto)
-   Creare gli strumenti dell\'ambiente di lavoro per modificare le proprietà dei renderizzatori (Fatto)
-   Creare gli strumenti dell\'ambiente di lavoro per esplorare, modificare e applicare le caratteristiche dei materiali alla parte (Fatto)
-   Creare degli script automake (In corso)
-   Rimuovere eventuali dipendenze dalla GUI di Raytracing/App
    -   La struttura dei dati di Bounding Box non dovrebbe utilizzare coin3d SbBox3f (Fatto)
    -   Per quale motivo QWidget incluso in QProcess? (Risolto)
-   Testare la compatibilità con Windows (In corso)
    -   Aggiornare Libpack per includere QT 4.7 - QT 4.8
    -   Eliminare avvisi ed errori del compilatore
-   Implementare il salvataggio delle proprietà dei materiali (Fatto)
-   Sistemare l\'interfaccia QML (In corso)
-   Creare dei Modelli di rendering, di Materiali e di Impostazioni predefinite
-   Creare un modello di conversione di scena da Blender a Lux
-   Convertire i materiali di LuxBlender .lbm (http://www.luxrender.net/lrmdb/en/material/) in materiali di rendering utili
-   Creare Python bindings per i materiali di rendering, camere, luci
-   Creare un oggetto documento di RenderCamera
-   Permettere che il modello scena sia importato nella operazioni di rendering.
-   Directory definite dall\'utente per le impostazioni, per i materiali e i modelli
-   Migliorare il View Provider
-   Convertire Povray/YafaRay per utilizzare la nuova infrastruttura del modulo di rendering
-   Testare il tutto



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing project/it
