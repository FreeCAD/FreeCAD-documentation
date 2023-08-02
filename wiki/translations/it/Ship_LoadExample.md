---
- GuiCommand:
   Name: Ship Load‏‎
   Name/it: Carica esempio
   MenuLocation: Ship design -> Carica un esempio di geometria di una nave
   Workbenches: Ship Workbench/it
   Shortcut: 
   SeeAlso: 
---

# Ship LoadExample/it


</div>

## Description

### Introduzione

FreeCAD-Ship lavora su delle **entità Ship** che devono essere create preventivamente sulla base delle geometrie fornite. La geometria deve essere un solido, o un insieme di solidi, e deve rispettare i seguenti criteri:

-   Deve essere fornita tutta la geometria dello scafo (comprese le barche simmetriche).
-   La geometria di dritta, di tribordo, deve essere posizionata nel dominio *Y negativa*.
-   L\'origine (0,0,0) si trova nel punto di intersezione della **sezione maestra** (Punto medio tra la perpendicolare di poppa e quella di prua) e la **linea di base**.

Ship works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid, or set of solids. The following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![](images/FreeCAD-Ship-SignCriteria.jpg ) ![Schematic view of sign criteria](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

Descrizione dei requisiti della forma base


</center>

In order to help new users, Ship includes a geometries examples loader, with the following to choose from:

-   Series 60 from Iowa University
-   Wigley Canonical Ship
-   Series 60 Catamaran
-   Wigley Catamaran

## Caricare una geometria della Serie 60 

Per aiutare i nuovi utenti, Ship include una serie di esempi di geometrie, dove si può scegliere tra i seguenti elementi:

-   Serie 60 della Iowa University
-   Canonica imbarcazione Wigley
-   Catamarano Serie 60
-   Catamarano Wigley


<div class="mw-translate-fuzzy">

Eseguendo lo strumento (Caricare una geometria modello di nave) si apre una finestra di dialogo. Selezionare **Series 60 da Iowa Università** e premere il pulsante OK. Lo strumento carica un nuovo documento con la geometria **s60_IowaUniversity**


</div>


**<center>'''Attenzione, prima di modificare qualsiasi cosa!'''</center>
<center>Ora si sta lavorando con il file originale del modello.</center>
<center>Per preservare l'esempio originale, senza modificarlo, '''è necessario salvarlo come nuovo file, prima di apportare delle modifiche'''</center>**

## Tutorial

-   [/it\|Tutorial Ship s60, prima parte ](FreeCAD-Ship_s60_tutorial.md)
-   [Tutorial Ship s60, seconda parte](FreeCAD-Ship_s60_tutorial_(II)/it.md)



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship LoadExample/it
