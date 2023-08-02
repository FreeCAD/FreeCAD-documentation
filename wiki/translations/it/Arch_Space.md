---
- GuiCommand:
   Name: Arch_Space
   Name/it: Spazio
   MenuLocation: Arch -> Spazio
   Workbenches: Arch_Workbench/it
   Shortcut: **S** **P**
   Version: 0.14
   SeeAlso: Arch_Wall/it, Arch_Structure/it
---

# Arch Space/it

## Descrizione

Lo strumento Spazio consente di definire un volume vuoto, basato su una forma solida, oppure definendo i suoi confini, o con un mix di entrambi. Se è basato esclusivamente sui confini, il volume viene calcolato a partire dai confini dati, e sottraendo lo spazio interno ai confini. L\'oggetto spazio definisce sempre un volume solido. Può anche essere visualizzata la superficie di un oggetto spazio, calcolata intersecando un piano orizzontale nel centro di massa del volume dello spazio.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;"> 
*Oggetto spazio creato da un oggetto solido esistente, poi sono aggiunte due facce della parete come confini.*



## Utilizzo

-   Selezionare un oggetto solido esistente o le facce che lo delimitano.
-   Premere il pulsante **<img src="images/Arch_Space.svg" width=16px> [Spazio](Arch_Space/it.md)**, oppure i tasti **S**, **P**.



### Limitazioni

-   Attualmente, le proprietà boundaries non sono modificabile tramite GUI.
-   Per seguire l\'evoluzione dello strumento consultare la pagina [Arch Space](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275) nel forum.



## Proprietà

-    {{PropertyData/it|Base}}: L\'oggetto base, se esiste (deve essere un solido).

-    {{PropertyData/it|Boundaries}}: Un elenco di confini opzionali.

-    {{PropertyData/it|Area}}: L\'area del pavimento calcolata in questo spazio.

-    {{PropertyData/it|FinishFloor}}: La finitura del pavimento di questo spazio.

-    {{PropertyData/it|FinishWalls}}: La finitura delle pareti di questo spazio.

-    {{PropertyData/it|FinishCeiling}}: La finitura del soffitto di questo spazio.

-    {{PropertyData/it|Group}}: Gli oggetti che sono inclusi in questo spazio, come arredo.

-    {{PropertyData/it|SpaceType}}: Il tipo di questo spazio.

-    {{PropertyData/it|FloorThickness}}: Lo spessore della finitura del pavimento.

-    {{PropertyData/it|NumberOfPeople}}: Il numero di persone che di solito occupano questo spazio.

-    {{PropertyData/it|LightingPower}}: La potenza elettrica necessaria per illuminare questo spazio in Watt.

-    {{PropertyData/it|EquipmentPower}}: La potenza elettrica necessaria per gli apparecchi di questo spazio in Watt.

-    {{PropertyData/it|AutoPower}}: Se True, Equipment Power viene compilata automaticamente dalla potenza degli apparecchi inclusi in questo spazio.

-    {{PropertyData/it|Conditioning}}: Il tipo di aria condizionata di questo spazio.

-    {{PropertyData/it|Internal}}: Specifica se questo spazio è interno o esterno.

-    {{PropertyView/it|Text}}: Il testo da mostrare. Usare \$area, \$label, \$tag, \$floor, \$walls, \$ceiling per inserire i rispettivi dati.

-    {{PropertyView/it|FontName}}: Il nome del carattere.

-    {{PropertyView/it|TextColor}}: Il colore del testo.

-    {{PropertyView/it|FontSize}}: La dimensione del testo.

-    {{PropertyView/it|FirstLine}}:La dimensione della prima riga di testo (moltiplica la dimensione del carattere 1 = stessa dimensione, 2 = doppia dimensione, ecc.).

-    {{PropertyView/it|LineSpacing}}: Lo spazio tra le righe di testo.

-    {{PropertyView/it|TextPosition}}: La posizione del testo. Lasciare (0,0,0) per la posizione automatica.

-    {{PropertyView/it|TextAlign}}: La giustificazione del testo.

-    {{PropertyView/it|Decimals}}: Il numero di decimali da utilizzare per i testi calcolati.

-    {{PropertyView/it|ShowUnit}}: Mostra il suffisso dell\'unità di misura o no.



## Opzioni

-   Per creare zone che raggruppano più spazi, utilizzare [Parte di edificio](Arch_BuildingPart/it.md) e impostare il tipo di IFC su \"Spatial Zone\"
-   L\'oggetto spazio ha le stesse modalità di visualizzazione degli altri oggetti Arch e Part, con una modalità in più chiamata **Footprint**, che visualizza solo la faccia inferiore dello spazio.

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Spazio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Crea un oggetto `Space` con gli `objects` dati, o con un `baseobj`, che può essere.
    -   un oggetto del documento, nel qual caso diventa la forma base dell\'oggetto spazio, o
    -   un elenco di oggetti selezionati restituiti da `FreeCADGui.Selection.getSelectionEx()`, o
    -   una lista di tuple `(object, subobjectname)`

Esempio: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

Dopo aver creato un oggetto spazio, ad esso si possono aggiungere delle facce selezionate con il seguente codice: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

I confini possono anche essere rimossi, selezionando nuovamente le facce indicate: 
```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```


{{docnav/it
|[Piano di sezione](Arch_SectionPlane.md)
|[Scale](Arch_Stairs/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_SectionPlane.svg
|IconR=Arch_Stairs.svg
|IconC=Workbench_Arch.svg
}}



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/it
