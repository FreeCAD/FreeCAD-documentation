# Std Workbench/it
---
- GuiCommand:/it   Name:Std_Workbench   Name/it:Ambiente   Empty:1   MenuLocation:[Workbenches:Tutti   SeeAlso:[[Workbenches/it| Ambienti di lavoro](Std_View_Menu/it___Visualizza]]_→_Ambiente_→.md)---


</div>

## Descrizione

Il comando **Ambienti** attiva l\'[ambiente di lavoro](Workbenches/it.md) selezionato inclusa la sua interfaccia utente grafica (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*L'elenco a discesa Workbench è indicato dal numero 10 nell'[interfaccia](interface/it.md) standard*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare un ambiente dall\'elenco a discesa \"Workbench\" nella barra degli strumenti degli ambienti. Questa opzione non è disponibile se l\'ambiente in uso è `<none>` (nessun ambiente).
    -   Seleziona un ambiente di lavoro dal sottomenu **Visualizza → Ambienti**.

## Note


<div class="mw-translate-fuzzy">

-   Ulteriori [ambienti aggiuntivi](External_Workbenches/it.md) possono essere scaricati con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md).


</div>

## Preferenze

-   L\'ambiente di avvio può essere modificato nelle preferenze: **Modifica → Preferenze... → Generale → Generale → Avvio**. Vedere la pagina [Editor delle preferenze](Preferences_Editor/it#Generale.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per cambiare l\'ambiente usare il metodo `activWorkbench` del modulo FreeCADGui. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  {{Interface navi}}

---
[documentation index](../README.md) > Std Workbench/it
