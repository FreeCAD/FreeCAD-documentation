---
- GuiCommand:/it
   Name:Ship Outline
   Name/it:Contorno   MenuLocation:Ship design → Disegno del contorno
   Icon:Ship_OutlineDraw.svg
   Workbenches:[Ship](Ship_Workbench/it.md)
   Shortcut:
   SeeAlso:
---

# Ship Outline/it


</div>


**Warning. This tool is outdated and will be removed from the module. You can instead consider the [Cross-sections](Part_CrossSections.md) tool to compute the intersections, and the [Drawing workbench](Drawing_Workbench.md) to plot them**


<div class="mw-translate-fuzzy">

## Introduzione

Da fare


</div>

Plots the ship hull outline draw

## Disegno delle linee 

Ship fornisce uno strumento che rende semplice ottenere un Piano delle linee dal disegno delle linee della nave


<div class="mw-translate-fuzzy">

![Outline draw tool.](images/FreeCAD-Ship-OutlineDrawIco.png )


<center>

Icona dello strumento per disegnare il contorno


</center>


</div>

Il disegno delle linee è un insieme di sezione sui 3 assi, che alla fine mostreranno la geometria dello scafo in un Piano delle linee. Dobbiamo fornire le linee per le 3 seguenti viste:

-   Body Plan (utilizzando le sezioni trasversali)
-   Sheer Plan (usando le sezioni longitudinali)
-   Half-Breadth Plan (usando le sezioni delle linee d\'acqua)


<div class="mw-translate-fuzzy">

### Sezioni trasversali 

Di solito devono essere eseguite 21 sezioni trasversali equidistanti tra le perpendicolari. Per eseguire questa operazione FreeCAD-Ship fornisce uno strumento automatico, è sufficiente selezionare **Transversal** come tipo di sezione, andare nel dialogo **Auto create** e impostare **21** nel campo delle sezioni, poi premere **Create sections**.


</div>

![Outline draw transversal sections preview.](images/S60OutlineTransversal.png )


<center>

Anteprima della vista delle sezioni trasversali


</center>

Viene compilata la tabella delle sezioni e si crea un nuovo oggetto chiamato OutlineDraw che permette di visualizzare l\'anteprima delle sezioni adottate. Di solito si producono delle sezioni più ravvicinate nelle zone prossime alla poppa e alla prua, dove la curvatura più pronunciata; per fare questo basta andare alla fine della tabella e fare **doppio clic** nella riga vuota, aggiungere un nuovo valore e premere Invio per confermare. Aggiungere manualmente le seguenti due sezioni:

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m

Secondo la complessità della geometria dello scafo, l\'anteprima delle sezioni può richiedere del tempo per essere elaborata.


<div class="mw-translate-fuzzy">

### Sezioni longitudinali 

Devono essere aggiunte due sezioni longitudinali, quindi selezionare **Longitudinal** come tipo di sezione, andare nel dialogo **Auto create** e impostare **2** nel campo delle sezioni, poi premere **Create sections**. Viene compilata la tabella delle sezioni e viene aggiornata l\'anteprima.


</div>


<div class="mw-translate-fuzzy">

### Linee d\'acqua 

Di solito servono 6 linee d\'acqua tra la linea di base e la linea di galleggiamento, quindi selezionare **Waterlines** come tipo di sezione, andare nel dialogo **Auto create** e impostare **5** nel campo delle sezioni (La linea d\'acqua Z = 0 m non è inclusa automaticamente, se è necessaria può essere aggiunta manualmente in un secondo momento), quindi premere **Create sections**. Viene compilata la tabella delle sezioni e viene aggiornata l\'anteprima.


</div>

Devono essere aggiunte diverse linee d\'acqua supplementari:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m


<div class="mw-translate-fuzzy">

### Tracciare il piano di costruzione 

Selezionare una scala **1:100** e premere **Accept** per fare in modo che lo strumento generi le sezioni 3D in un nuovo oggetto.


</div>

![Resultant sections.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Sezioni risultanti.


</center>

Per disegnare queste sezioni si può utilizzare il modulo [Drawing](Drawing_Workbench/it.md):

![Outline draw plot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Proiezione dei piani.


</center>

### Tutorial

La lettura di queste guide permette di conoscere il funzionamento di questo modulo.

-   [Tutorial Ship s60, prima parte ](FreeCAD-Ship_s60_tutorial/it.md)
-   [Tutorial Ship s60, seconda parte](FreeCAD-Ship_s60_tutorial_(II)/it.md)





{{Ship_Tools_navi

}}

---
[documentation index](../README.md) > Ship Outline/it
