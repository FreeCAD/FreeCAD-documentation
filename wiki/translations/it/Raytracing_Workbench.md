# Raytracing Workbench/it

 


{{VeryImportantMessage|L'ambiente Raytracing è essenzialmente obsoleto. Nuovi sviluppi stanno avvenendo nel [https://github.com/FreeCAD/FreeCAD-render Render Workbench], che è inteso come suo sostituto. Questo ambiente è completamente programmato in Python, quindi è molto più facile da estendere.

Tuttavia, le informazioni in questa pagina sono generalmente utili anche per il nuovo ambiente, poiché entrambi i moduli funzionano sostanzialmente allo stesso modo.
}}

<img alt="L\'icona di Raytracing" src=images/Workbench_Raytracing.svg  style="width:128px;">

## Introduzione


{{TOCright}}

Il modulo <img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> Raytracing viene utilizzato per generare immagini fotorealistiche dei modelli elaborandole con un renderer esterno.

Il modulo Raytracing lavora con dei [modelli](Raytracing_templates/it.md), che sono file di progetto che definiscono una scena per il modello 3D. È possibile posizionare luci e geometrie come i piani terra e contiene anche i segnaposto per la posizione della telecamera e per le informazioni sul materiale degli oggetti nella scena. Il progetto può quindi essere esportato in un file pronto per il rendering o essere eseguito direttamente in FreeCAD.

Attualmente sono supportati due renderizzatori: [POV-Ray](POV-Ray.md) e [LuxRender](LuxRender.md). Per poter eseguire il rendering direttamente da FreeCAD, sul sistema deve essere installato almeno uno di questi renderer, e deve essere configurato il suo percorso nelle preferenze di FreeCAD per Raytracing. Senza alcun renderer installato, si può comunque esportare un file della scena e utilizzarlo successivamente in uno di questi renderer, o su una macchina diversa.

L\'ambiente Raytracing è essenzialmente obsoleto. Nuovi sviluppi stanno avvenendo nel [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), che è inteso come suo sostituto. Questo nuovo ambiente è completamente programmato in Python, quindi è molto più facile estenderlo rispetto all\'ambiente corrente che è programmato in C++. Tuttavia, le informazioni in questa pagina sono generalmente utili anche per il nuovo banco di lavoro, poiché entrambi i moduli funzionano sostanzialmente allo stesso modo.

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

## Flusso di lavoro tipico 

1.  Creare o aprire un progetto di FreeCAD, aggiungere alcuni oggetti solidi sul modulo [Part](Part_Workbench/it.md) o [PartDesign-based](PartDesign_Workbench/it.md); i mesh non sono ancora supportati
2.  Creare un progetto Raytracing (luxrender o povray)
3.  Selezionare gli oggetti che si desidera aggiungere al progetto raytracing e aggiungerli con lo strumento \"Inserisci Parte\"
4.  Esportare o elaborare direttamente


</div>

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">


*Flusso di lavoro del Raytracing Workbench; il workbench prepara un file di progetto da un determinato modello e quindi chiama un programma esterno per produrre il rendering effettivo della scena. Il renderer esterno può essere usato indipendentemente da FreeCAD.*

## Strumenti

### Strumenti di progetto 

Questi sono gli strumenti principali per esportare il proprio lavoro 3D su renderer esterni.

-   <img alt="" src=images/Raytrace_New.svg  style="width:32px;"> [Nuovo progetto PovRay](Raytracing_New/it.md): inserisce un nuovo progetto PovRay nel documento.
-   <img alt="" src=images/Raytrace_Lux.svg  style="width:32px;"> [Nuovo progetto LuxRender](Raytracing_Lux/it.md): inserisce un nuovo progetto LuxRender nel documento.
-   <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:32px;"> [Inserisci parte](Raytracing_InsertPart/it.md): inserisce una vista di una parte in un progetto di raytracing.
-   <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:32px;"> [Reset camera](Raytracing_ResetCamera/it.md): abbina la posizione della telecamera di un progetto di raytracing alla vista corrente.
-   <img alt="" src=images/Raytrace_ExportProject.svg  style="width:32px;"> [Esporta progetto\...](Raytracing_ExportProject/it.md): esporta un progetto di raytracing in un file di scena per il rendering in un renderer esterno.
-   <img alt="" src=images/Raytrace_Render.svg  style="width:32px;"> [Render](Raytracing_Render/it.md): esegue il rendering di un progetto raytracing con un renderer esterno.

### Utilità

Questi sono degli strumenti di supporto per eseguire manualmente azioni specifiche.

-   <img alt="" src=images/Raytracing_WriteView.svg  style="width:32px;"> [Esporta la vista in PovRay\...](Raytracing_WriteView/it.md): scrive la vista 3D attiva con la fotocamera e tutto il suo contenuto in un file PovRay.
-   <img alt="" src=images/Raytracing_WriteCamera.svg  style="width:32px;"> [Esporta la camera in PovRay\...](Raytracing_WriteCamera/it.md): esporta la posizione della telecamera della vista 3D attiva in un file in formato POV-Ray.
-   <img alt="" src=images/Raytracing_WritePart.svg  style="width:32px;"> [Esporta la parte in PovRay\...](Raytracing_WritePart/it.md): scrive la Parte selezionata (oggetto) come un file POV-Ray.

## Preferenze

-   <img alt="" src=images/Preferences-raytracing.svg  style="width:32px;"> [Preferenze](Raytracing_Preferences/it.md): preferenze disponibili per gli strumenti Raytracing.

## Tutorials

-   [Basic Raytracing tutorial](Raytracing_tutorial/fr.md)
-   [Intermediate Raytracing tutorial](Tutorial_FreeCAD_POV_ray/fr.md)

### Creare manualmente un file povray 

Gli strumenti di utilità descritti prima consentono di esportare la corrente vista 3D e tutto il suo contenuto in un file [Povray](http://www.povray.org/). In primo luogo, è necessario caricare un documento o crearne uno e poi orientare la vista 3D come si desidera. Dopo, scegliere **Utilità → Esporta la vista \...** nel menu di Raytracing.

![](images/FreeCAD_Raytracing.jpg )

Nella finestra di dialogo **Esporta pagina**, selezionare la destinazione per salvare il file \*.pov. Successivamente aprire il file in [Povray](http://www.povray.org/) e generare la renderizzazione: ![](images/Povray.jpg )

Come è noto, le applicazioni di renderizzazione possono produrre immagini di grandi dimensioni e ottima qualità: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">

## Script

Vedere [Esempio di API Raytracing](Raytracing_API_example/it.md) per informazioni sulla scrittura di scene a livello di codice.

### Link

### POV-Ray 

-   [Pagina POV-Ray in questa wiki](POV-Ray.md)
-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://en.wikipedia.org/wiki/POV-Ray>

### LuxRender

-   [Pagina LuxRender in questa wiki](LuxRender.md)
-   <http://www.luxrender.net/>

### Render per future implementazioni 

-   <http://www.yafaray.org/>
-   <http://www.mitsuba-renderer.org/>
-   <http://www.kerkythea.net/>
-   <http://www.artofillusion.org/>

## Esportare in Kerkythea 

Sebbene l\'esportazione diretta nel formato XML di Kerkythea non sia ancora supportata, è possibile esportare gli oggetti come file Mesh (.obj) e poi importarli in Kerkythea.

-   se si utilizza Kerkythea per Linux, ricordarsi di installare il pacchetto WINE (necessario per far funzionare Kerkythea in Linux)
-   è possibile convertire i modelli in mesh con l\'aiuto dell\'ambiente Mesh e poi esportare questi mesh, come file .obj
-   Se l\'esportazione della mesh ha provocato errori (capovolgimento di normali, buchi \...) puoi tentare la fortuna con [netfabb studio basic](http://www.netfabb.com/downloadcenter.php?basic=1)

:   Gratuito per uso personale, disponibile per Windows, Linux e Mac OSX.
:   Ha strumenti di riparazione standard che ripareranno il tuo modello nella maggior parte dei casi.

-   un altro buon programma per l\'analisi/riparazione di mesh è [Meshlab](http://sourceforge.net/projects/meshlab/)

:   Open Source, disponibile per Windows, Linux e Mac OSX.
:   Ha strumenti di riparazione standard che ripareranno il tuo modello nella maggior parte dei casi (riempire i fori, riorientare le normali, ecc.)

-   è possibile utilizzare \"make compound\" e poi \"make single copy\" oppure è possibile fondere i solidi in un gruppo prima di convertirli in mesh
-   ricordatevi di impostare in Kerkythea un fattore di importazione di 0.001 per obj-modeler, in quanto Kerkythea si aspetta che il file obj sia in m (ma l\'unità standard in FreeCAD è il mm)

:   Within WIndows 7 64-bit Kerkythea does not seem to be able to save these settings.
:   So remember to do that each time you start Kerkythea

-   se si importano più oggetti in Kerkythea è possibile utilizzare la funzione \"File → Unisci\" di Kerkythea

## Sviluppo

Queste pagine si riferiscono al nuovo ambiente, programmato in Python, destinato a sostituire l\'attuale ambiente Raytracing.

-   [Render Workbench](https://github.com/FreeCAD/FreeCAD-render)
-   [Render Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=25933) (announcement only, no discussion)
-   [FreeCAD Renderer Workbench improvements](https://forum.freecadweb.org/viewtopic.php?t=39168)

**Obsoleto**

Queste pagine si riferiscono all\'ambiente in sostituzione, programmato in C++, proposto intorno al 2012, che non è mai stato completato.

-   [Progetto Raytracing](Raytracing_project/it.md)
-   [Progetto Render](Render_project/it.md)





{{Raytracing Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
