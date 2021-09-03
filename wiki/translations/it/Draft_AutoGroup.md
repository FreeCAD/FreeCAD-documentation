---
- GuiCommand:/it
   Name:Draft AutoGroup
   Name/it:AutoGruppo
   MenuLocation:Draft → Utilità → AutoGruppo
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version:0.17
   SeeAlso:[Gruppo](Std_Group/it.md), [VisGroup](Draft_VisGroup/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Gruppo Automatico imposta un [Gruppo](Std_Group/it.md) standard selezionato, o un elemento correlato come un [VisGroup](Draft_VisGroup/it.md), un [Sito](Arch_Site/it.md), un [Edificio](Arch_Building/it.md) o una [Parte di edificio](Arch_BuildingPart/it.md), come gruppo automatico attivo. Quando viene impostato un gruppo automatico, i nuovi oggetti vengono automaticamente spostati nel gruppo indicato al momento della creazione.


</div>

This command was originally intended for groups, hence its name, but was redesigned in FreeCAD version 0.19 when a layer system was introduced. Because handling layers is now the default for the command the rest of this page will primarily focus on layers.

![](images/Draft_tray_menu.png )


<div class="mw-translate-fuzzy">


*Il vassoio di Draft che imposta il gruppo automatico attivo facendo clic sull'icona della cartella e scegliendo un gruppo
*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un **<img src="images/Group.svg" width=16px> [Gruppo](Std_Group/it.md)**, o un **<img src="images/Group.svg" width=16px> [Gruppo costruzione](Draft_ToggleConstructionMode/it.md)**, o un **<img src="images/Draft_VisGroup.svg" width=16px> [VisGroup](Draft_VisGroup/it.md)** nella vista ad albero.
2.  Premere il pulsante **<img src="images/Draft_AutoGroup_off.svg" width=16px> None**, o andare nel menu {{MenuCommand|Draft → Utilità → <img src="images/Draft_AutoGroup.svg" width=16px> [AutoGruppo](Draft_AutoGroup/it.md)}}. Se non è selezionato nessun gruppo, un menu a discesa mostra i gruppi idonei da usare, o \"None\".
3.  Il pulsante cambia e appare il nome del gruppo automatico attivo, ad esempio, **<img src="images/Draft_AutoGroup_on.svg" width=16px> Gruppo**.


</div>

## Notes


<div class="mw-translate-fuzzy">

Note:

-   Il pulsante **<img src="images/Draft_AutoGroup.svg" width=16px> [AutoGruppo](Draft_AutoGroup/it.md)** è presente nella [barra di Draft](Draft_Tray/it.md), che appare solo negli ambienti [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md).
-   Prima di utilizzare questo strumento deve esistere almeno un **<img src="images/Group.svg" width=16px> [Gruppo](Std_Group/it.md)**, o un **<img src="images/Group.svg" width=16px> [Gruppo costruzione](Draft_ToggleConstructionMode/it.md)**, o un **<img src="images/Draft_VisGroup.svg" width=16px> [VisGroup](Draft_VisGroup/it.md)**.
-   Per cambiare il gruppo automatico, selezionare un altro gruppo nella vista ad albero e fare clic su **<img src="images/Draft_AutoGroup_on.svg" width=16px> Gruppo**. Se nessun gruppo è selezionato, si può scegliere \"None\" per disattivare il raggruppamento automatico.
-   Quando il raggruppamento automatico è attivo, i nuovi oggetti [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md) sono posizionati in quel gruppo tranne quando la **<img src="images/Draft_Construction.svg" width=16px> [Modalità costruzione](Draft_ToggleConstructionMode/it.md)**è attiva, nel qual caso la nuova geometria verrà posizionata nel gruppo Costruzione.
-   Il raggruppamento automatico funziona solo per gli oggetti creati dall\'interfaccia utente grafica; gli oggetti creati a livello di programmazione da [macro](macros/it.md) o dalla console [Python](Python/it.md) non vengono posizionati automaticamente nei gruppi. L\'utente ha sempre la possibilità di eseguire il raggruppamento a livello di programmazione, indipendentemente dalle impostazioni di raggruppamento automatico.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   This command can optionally also handle groups: {{MenuCommand|Edit → Preferences... → Draft → General settings → General Draft Settings → Show groups in layers list drop-down button}}.

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'aggiunta di oggetti al gruppo automatico attivo può essere eseguita in [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


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


<div class="mw-translate-fuzzy">





</div>


 
