---
- GuiCommand:/it
   Name:Std ToggleVisibility
   Name/it:Mostra/Nascondi
   Empty:1
   MenuLocation:Visualizza → Mostra/Nascondi
   Workbenches:Tutti
   Shortcut:**Spazio**
   SeeAlso:[Mostra la selezione](Std_ShowSelection/it.md), [Nascondi la selezione](Std_HideSelection/it.md), [Commuta tutti gli oggetti](Std_ToggleObjects/it.md), [Mostra tutti gli oggetti](Std_ShowObjects/it.md), [Nascondi tutti gli oggetti](Std_HideObjects/it.md)
---


</div>

## Descrizione

The **Std ToggleVisibility** command toggles the visibility of selected objects in [3D views](3D_view.md).

## Utilizzo


<div class="mw-translate-fuzzy">

### Utilizzo 

Questo comando serve a rendere visibili o a nascondere nella vista i componenti del documento.
Esso è accessibile in diversi modi:

-   La barra spaziatrice.
-   La console Python.
-   La struttura del progetto.
-   La scheda Vista.
-   Il menu Visualizza.
-   La vista dell\'area di lavoro.

Esempio di elementi visibili e di elementi nascosti: <img alt="" src=images/Mostra1.png  style="width:750px;">  Nella struttura ad albero gli elementi nascosti sono in grigio, quelli visibili in nero e quelli selezionati sono evidenziati.
Nell\'area di lavoro appaiono solo gli elementi che nella struttura sono indicati in nero.
Nella console Python l\'elemento (\"Revolution006\") prima è nascosto (Visibility=False), poi è visibile (Visibility=True).
Nella scheda Vista l\'elemento (\"Revolution006\") è visibile (Visibility true).

#### Barra spaziatrice 

Selezionare un elemento e premere {{KEY/it|Spazio}} sia per mostrarlo che per nasconderlo.

#### Console Python 

Inserire il comando ( in questo caso: *Gui.getDocument(\"test\_ok\_3p\").getObject(\"Revolution006\").Visibility=False)*, poi premere {{KEY/it|Invio}}

#### Dal menu principale 

-   Direttamente con **Visualizza → Nascondi**, oppure
-   dal menu **Visualizza → Visibilità → Sottomenu** e scegliendo nel sottomenu l\'azione desiderata.

Il secondo modo permette anche di stabilire se l\'elemento può essere selezionato.

#### Nella struttura del progetto 

Selezionare gli elementi con il tasto destro del mouse,
oppure selezionare e poi aprire il menu contestuale da tastiera (tasto in basso a destra, a fianco di Ctrl).

#### Nella scheda Vista 

Si può operare su un solo elemento per volta. Selezionare un elemento, aprire la scheda delle sue Proprietà Vista e modificare il valore.

#### Nell\'area di lavoro 

Selezionare gli elementi con il tasto destro del mouse e scegliere la voce che interessa tra quelle del menu che viene aperto.

### Note

Quando si applica **Nascondi** a un elemento già nascosto l\'elemento diventa visibile.
Per selezionare più elementi tenere premuto il tasto {{KEY/it|Crtl}} durante l\'operazione.

### Casi particolari 

Nei documenti con molti oggetti, dove è difficile individuare un elemento nella struttura, può essere utile nascondere un oggetto nella vista grafica e poi utilizzare **Visualizza → Visibilità → Attiva/disattiva tutti gli oggetti** per rendere visibile solo l\'oggetto desiderato. Questa procedura usata in combinazione con gli altri comandi di selezione globale, **Mostra tutti gli oggetti** e **Visualizza tutti gli oggetti**, evita noiose operazioni di selezione.

### Esempi

Console Python: ![](images/Mostra2.png ) 

Menu principale: <img alt="" src=images/Mostra3.png  style="width:750px;"> 

Struttura del progetto: ![](images/Mostra4.png ) 

Scheda Vista: ![\|left](images/Mostra5.png ) 

Area di lavoro: ![\|left](images/Mostra6.png ) 


</div>

## Note 

-   Invisible objects are displayed with a greyed out label and a greyed out icon in the [Tree view](Tree_view.md).
-   Objects nested in a [Std Part](Std_Part.md), or a [Std Link](Std_LinkMake.md) to a [Std Group](Std_Group.md), or a LinkGroup, and [features](PartDesign_Feature.md) of a [PartDesign Body](PartDesign_Body.md) will only be visible in [3D views](3D_view.md) if their parent is visible as well. This means that a feature in a PartDesign Body that is nested in a Std Part will only be visible in 3D views if the feature itself, the PartDesign Body, and the Std Part are all visible. And if the Std Part is in turn nested in another Std Part, then that last object must also be visible.
-   If the visibility of a [Std Group](Std_Group.md) (or an object derived from it such as an [Arch BuildingPart](Arch_BuildingPart.md)) is changed, the visibility of its nested objects will change accordingly. But their visibility can be changed independently as well.
-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Use the `show` and `hide` methods of an object to change its visibility.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True:
  obj.hide()
else:
  obj.show()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
