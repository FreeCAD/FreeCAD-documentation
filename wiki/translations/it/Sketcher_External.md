---
 GuiCommand:
   Name: Sketcher External
   Name/it: Sketcher Geometria esterna
   MenuLocation: Schizzo , Strumenti Sketcher , Crea geometria esterna
   Workbenches: Sketcher Workbench/it
   Shortcut: **G** **X**
   SeeAlso: Sketcher_ToggleConstruction/it
---

# Sketcher External/it



## Descrizione


{{VersionMinus/it|1.0}}

: lo strumento <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Sketcher Geometria esterna](Sketcher_External/it.md) proietta bordi e/o vertici appartenenti a oggetti esterni allo schizzo sul piano dello schizzo. La geometria proiettata è chiamata \"geometria esterna\". Rimane parametricamente collegato ai suoi oggetti sorgente. I bordi della geometria esterna sono contrassegnati con un [colore](Sketcher_Preferences/it#Appearance.md) (magenta predefinito) e un tipo di linea ({{Version/it|1.0}}) dedicati. Similmente alla geometria di costruzione, la geometria esterna non è visibile all\'esterno dello schizzo, ma ha lo scopo di aiutare a definire i vincoli e altre geometrie all\'interno dello schizzo stesso.


{{VersionPlus/it|1.1}}

: Vedere <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Proiezione](Sketcher_Projection/it.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*Le due linee magenta sono una geometria esterna collegata ai bordi di un [Pad](PartDesign_Pad/it.md) preesistente. Sono usate per vincolare i cerchi.*



## Utilizzo

Vedere anche: [Aiuti per il disegno](Sketcher_Workbench/it#Drawing_aids.md).

1.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Sketcher_External.svg" width=16px> [Crea geometria esterna](Sketcher_External/it.md)**.
    -   Selezionare l\'opzione **Schizzo → Strumenti Sketcher → <img src="images/Sketcher_External.svg" width=16px> Crea geometria esterna** dal menu.
    -   Fare clic con il pulsante destro del mouse nella [Vista 3D](3D_view/it.md) e selezionare l\'opzione **<img src="images/Sketcher_External.svg" width=16px> Crea geometria esterna** dal menu contestuale.
    -   Usare la scorciatoia da tastiera: **G** quindi **X**.
2.  Il cursore si trasforma in una croce con l\'icona dello strumento.
3.  Selezionare un bordo esterno o un vertice. Vedere [Note](#Note.md).
4.  Viene creata la geometria esterna.
5.  Questo strumento viene sempre eseguito in modalità continua: opzionalmente continuare a selezionare i bordi esterni e/o i vertici.
6.  Per terminare, fare clic con il pulsante destro del mouse o premere **Esc** oppure avviare un altro strumento di creazione di geometrie o vincoli.



## Note

-   È possibile selezionare solo bordi e vertici di oggetti all\'interno dello stesso sistema di coordinate. Lo schizzo e l\'oggetto devono trovarsi nello stesso [Corpo](PartDesign_Body/it.md), o nella stessa [Parte](Std_Part/it.md), o entrambi nel sistema di coordinate globali. Se necessario, utilizzare un [Binder](PartDesign_SubShapeBinder/it.md) per portare una copia dell\'oggetto nel sistema di coordinate corrente.
-   Le dipendenze circolari non sono consentite. Non è possibile collegarsi a un oggetto che dipende dallo schizzo stesso.
-   I collegamenti agli elementi di altri schizzi sono possibili e incoraggiati, poiché sono più affidabili dei collegamenti alla geometria (solida) generata. Quest\'ultimo può soffrire del [Problema di denominazione topologica](Topological_naming_problem/it.md). Vedere [Consigli per modelli stabili](Feature_editing/it#Advice_for_creating_stable_models.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/it
