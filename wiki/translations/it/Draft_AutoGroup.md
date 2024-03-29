---
 GuiCommand:
   Name: Draft AutoGroup
   Name/it: Gruppo automatico
   Empty: 1
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Version: 0.17
   SeeAlso: Draft_Layer/it, Std Group/it
---

# Draft AutoGroup/it



## Descrizione

Il comando **Draft Gruppo automatico** modifica il [Draft Livello](Draft_Layer/it.md) (layer) attivo o, [opzionalmente](#Preferenze.md), il [ Gruppo](Std_Group/it.md) attivo o l\'oggetto simil-gruppo [Arch](Arch_Workbench/it.md). I nuovi oggetti [Draft](Draft_Workbench/it.md) e [Arch](Arch_Workbench/it.md) vengono automaticamente posizionati in questo livello attivo o gruppo.

Questo comando era originariamente destinato ai gruppi, da cui il nome, ma è stato riprogettato nella versione 0.19 di FreeCAD quando è stato introdotto un sistema a livelli (layer). Poiché la gestione dei livelli è ora l\'impostazione predefinita per il comando, il resto di questa pagina si concentrerà principalmente su di essi

![](images/Draft_tray_menu.png ) 
*Il menu dei livelli della barra di Draft*



## Utilizzo

1.  Facoltativamente selezionare il livello che si vuole rendere attivo nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante ![](images/Draft_tray_button_layer.png ) nella [Barra di Draft](Draft_Tray/it.md). Questo pulsante può avere un aspetto diverso. Se è presente un livello attivo, verrà visualizzato il nome del livello e un\'icona del livello con il **Line Color** e il **Shape Color** del livello.
    -   Se si ha selezionato un livello: seleziona l\'opzione **<img src="images/button_right.svg" width=16px> Attiva questo livello** dal menu contestuale [Vista ad albero](Tree_view/it.md).
3.  Se non si ha ancora selezionato un livello, si apre il menu dei livelli. Effettuare una delle seguenti operazioni:
    -   Selezionare **Nessuno** per lavorare senza un livello attivo.
    -   Selezionare un livello esistente da rendere attivo.
    -   Selezionare **Aggiungi nuovo livello** per creare un nuovo livello. La selezione di questa opzione non modificherà il livello attivo.
4.  Se il livello attivo è stato modificato, il pulsante nella [Barra di Draft](Draft_Tray/it.md) viene aggiornato.



## Note

-   È anche possibile creare un nuovo [livello](Draft_Layer/it.md) facendo clic con il pulsante destro del mouse sul contenitore del livello nella [Vista ad albero](Tree_view/it.md) e selezionando **<img src="images/Draft_NewLayer.svg" width=16px> Aggiungi nuovo livello** opzione dal menu contestuale.
-   Se la [Modalità di costruzione Draft](Draft_ToggleConstructionMode/it.md) è attivata, il [livello](Draft_Layer/it.md) attivo viene ignorato.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Questo comando può opzionalmente gestire anche i gruppi: **Modifica → Preferenze... → Draft → Generale → Includi gruppi nell'elenco dei livelli**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Se [Draft](Draft_Workbench/it.md) è attivo, l\'oggetto dell\'applicazione FreeCADGui ha una proprietà `draftToolBar`. Questo oggetto `draftToolBar` ha una proprietà `autogroup`, che contiene il nome dell\'autogroup attivo, o è `None` se nessun autogroup è attivo. Per modificare il gruppo automatico attivo utilizza il metodo `setAutoGroup` dell\'oggetto `draftToolBar`. Per inserire gli oggetti nell\'autogroup attivo utilizza il metodo `autogroup` del modulo Draft.


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
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AutoGroup/it
