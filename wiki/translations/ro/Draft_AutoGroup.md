# Draft AutoGroup/ro
---
- GuiCommand:   Name:Draft AutoGroup   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft → Utilities → AutoGroup   SeeAlso:---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument permite setarea unui grup sau derivat ca [ Proiect VisGroup](Proiect_VisGroup.md), [Arch Site](Arch_Site.md), [Arch Building](Arch_Building.md) sau [ Arch Floor](Floor_Arch.md) , ca grup activ automat. Când este setat un grup auto, toate obiectele noi create în [ Draft Workbench](Draft_Workbench.md) sau [ Arch Workbench](Arch_Workbench.md) vor fi plasate în acel grup.


</div>

This command was originally intended for groups, hence its name, but was redesigned in FreeCAD version 0.19 when a layer system was introduced. Because handling layers is now the default for the command the rest of this page will primarily focus on layers.

![](images/Draft_tray_menu.png ) 
*The layer menu of the Draft Tray*

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Selectați meniul Schiță → Utilități → **<img src="images/Draft_AutoGroup.png" width=16px> [AutoGroup](Draft_AutoGroup.md)
** sau faceți clic pe butonul de autogrupare din bara de instrumente sau faceți clic cu butonul din dreapta pe un obiect Group în vizualizarea arborescentă → Utilitare → **<img src="images/Draft_AutoGroup.png" width=16px> [AutoGroup](Draft_AutoGroup.md)**
2.  Alegeți grupul dorit din caseta drop-down contextuală


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Când setarea AutoGroup este setată, butonul devine verde, înseamnă că este activată gruparea automată. Puteți să faceți clic pe acesta pentru a schimba grupul sau a dezactiva.
-   Când gruparea automată este activă, orice nou obiect Draft sau Arch creat va fi plasat în acel grup (cu excepția cazului în care Modul de construcție a proiectului este activat, caz în care acesta merge la grupul de construcție).
-   Aceasta funcționează numai atunci când creați obiecte de tip Proiect sau Arch din butoanele GUI. Nu când le folosiți din Python. Acest lucru este posibil, astfel încât scripturile Python să poată face gruparea pe care o doresc, indiferent de ce autogrupează.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   This command can optionally also handle groups: **Edit → Preferences... → Draft → General settings → General Draft Settings → Show groups in layers list drop-down button**.

## Scrip-Programare 

See also: _.


<div class="mw-translate-fuzzy">

În script-urile python, folosirea Draft de auto-grupare se face pur și simplu cu comanda de mai jos:


</div>


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

layer = Draft.make_layer()
Gui.draftToolBar.setAutoGroup(layer.Name)

Draft.autogroup(polygon1)
Draft.autogroup(polygon2)
Draft.autogroup(polygon3)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AutoGroup/ro
