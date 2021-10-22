# <img alt="" src=images/MOOC_workbench_icon.svg  style="width:240px;">  MOOC Workbench/it
*align=center|The FreeCAD MOOC External Workbench Icon*

## Descrizione


{{TOCright}}


<div class="mw-translate-fuzzy">

MOOC è un [ambiente esternoh](External_workbenches/it.md) con cui è possibile seguire tutorial interattivi e fare la valutazione del proprio lavoro direttamente nell\'interfaccia di FreeCAD.


</div>

-   Currently only in French (and hard-coded).
-   Only compatible with FreeCAD Py3 and Qt5 (PySide2)
-   LGPLv2 (or similar) code funded by Europe through IMT and EESAB.
-   Modular: This workbench was created with the intention that the addition of tutorials and evaluations was modular. In other words, one has to add a tutorial in the {{FileName|lessons}} folder or an evaluation in the {{FileName|exercises}} folder to show up in the respective tool.


<div class="mw-translate-fuzzy">

Le esercitazioni **Interattive** (anche chiamate Player) sono esercizi guidati step-by-step con verifiche oggettive. Si avvia direttamente in FreeCAD e consente di avanzare passo dopo passo nella modellazione di un oggetto. L\'utente ha un testo, un video e soprattutto il controllo che gli obiettivi sono stati raggiunti.


</div>

<img alt="" src=images/MOOC_Player_Dialog_Context.png  style="width:1024px;"> 
*align=center|MOOC Player Dialog within FreeCAD GUI* ![](images/MOOC_Player_Dialog.png ) 
*MOOC Player Dialog close up*


<div class="mw-translate-fuzzy">

**Valutazioni** (anche chiamato Grader) sono costituite da un piccolo programma che controlla determinati criteri di un documento di FreeCAD, ad esempio la presenza di un corpo parte, uno schizzo o il volume finale.


</div>

<img alt="" src=images/MOOC_Grader_Dialog.png  style="width:1024px;"> 
*align=center|The MOOC Grader Dialog*

## Installazione


<div class="mw-translate-fuzzy">

Questo ambiente può essere facilmente installato e aggiornato dal [Addon Manager](AddonManager/it.md) disponibile in FreeCAD 0.17 e superiore. Per gli utenti di FreeCAD 0.16 e per altri metodi di installazione, fare riferimento alla pagina [Installare componenti aggiuntivi](Installing/it#Installare_componenti_aggiuntivi.md).


</div>

## Limitations

ATM this workbench is only available in the French language.

## Technical Details 

From a technical point of view, the workbench is composed of:

-   an \"API\" that contains the code that analyzes the document ({{FileName|MoocChecker.py}})
-   the code that executes the tutorials in the \"lessons\" folder ({{FileName|MoocPlayer.py}})
-   the code that executes the evaluations in the \"exercises\" folder ({{FileName|MoocGrader.py}})

## Roadmap

-   internationalization of the workbench
-   Integration of videos in FreeCAD (PySide2.QtWebEngineWidgets?)
-   request the integration of the workbench in the list of the addon manager DONE

## Link


<div class="mw-translate-fuzzy">

-   Codice sorgente ospitato su Framagit: [1](https://framagit.org/freecad-france/mooc-workbench)
-   Official complete [2](https://framagit.org/freecad-france/mooc-workbench#mooc-workbench)


</div>

## Ambienti aggiuntivi 

Gli ambienti di FreeCAD sono facili da programmare in [Python](Python/it.md), quindi ci sono molte persone che sviluppano ambienti aggiuntivi al di fuori degli sviluppatori principali di FreeCAD.

La pagina [Ambienti complementari](external_workbenches/it.md) contiene alcune informazioni e tutorial su alcuni di loro, e il progetto [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) mira a raccoglierli e renderli facilmente installabili dall\'interno di FreeCAD.

Sono in fase di sviluppo ulteriori nuovi ambienti.


 

_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > MOOC Workbench/it
