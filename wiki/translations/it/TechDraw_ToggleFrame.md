---
- GuiCommand:/it
   Name:TechDraw ToggleFrame
   Name/it:Attiva o disattiva la cornice
   MenuLocation:TechDraw → Attiva o disattiva la cornice
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vista](TechDraw_View/it.md), [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)
---

# TechDraw ToggleFrame/it


</div>

## Descrizione

Lo strumento attiva o disattiva la visualizzazione della vista di cornici, etichette e vertici.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*Vista della proiezione di un solido con cornici attive e disattivate*

## Utilizzo

1.  Se nel documento ci sono più pagine di disegno, è necessario selezionare la pagina desiderata nella struttura.
2.  Premere il pulsante **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md)
**
3.  Se le strutture delle viste sono visibili, scompaiono. Se le strutture delle viste non sono visibili, appaiono.
4.  È possibile avere diversi stati di visualizzazione della struttura per le diverse Viste. Se ciò accade, premere una o due volte il pulsante **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Attiva o disattiva la cornice](TechDraw_ToggleFrame/it.md)** per risincronizzare le viste.

## Background

The dotted view frame and the vertex dots are just for reference, they aren\'t actually part of the drawing, so you won\'t see them once you export the page as PDF or SVG.

The suggested workflow is to use **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Turn View Frames On/Off](TechDraw_ToggleFrame.md)** to deactivate the frame surrounding the view, and also the additional dots. With the dots, use the measurement tools to select the correct edges to measure, then toggle the frame (and dots) off to see the final result. Not satisfied? Toggle the frame (and dots) on again, select other vertices and create new measurements, then toggle the frame off again.

You can adjust the size of the vertex dots in the [TechDraw Preferences/Scale tab](TechDraw_Preferences#Scale.md). Please do not set their size to zero, just small or big enough so it\'s comfortable for you to pick them up.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Per ora lo strumento non ha un\'interfaccia di programmazione.


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/it
