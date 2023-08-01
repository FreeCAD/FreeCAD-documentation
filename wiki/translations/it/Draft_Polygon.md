---
- GuiCommand:
   Name: Draft Polygon
   Name/it: Poligono
   MenuLocation: Drafting - Poligono
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut: **P** **G**
   Version: 0.7
---

# Draft Polygon/it



## Descrizione

Il comando <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> **Poligono** crea un poligono regolare nel [piano di lavoro](Draft_SelectPlane/it.md) corrente da un centro e un raggio. Il raggio può essere definito selezionando un punto.

Un Poligono può essere cambiato da inscritto a circoscritto modificando la sua proprietà **Draw Mode**. Gli angoli di un poligono possono essere raccordati (arrotondati) o smussati modificandone rispettivamente **Fillet Radius** o **Chamfer Size**.

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;"> 
*Poligono regolare definito da due punti, centro e raggio*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Polygon.svg" width=16px> [Draft Polygon](Draft_Polygon/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Polygon.svg" width=16px> Poligono** dal menu.
    -   Usare la scorciatoia da tastiera: **P** poi **G**.
2.  Si apre il pannello attività **Poligono**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Regolare il numero desiderato di **Lati**.
4.  Scegliere il primo punto, il centro del poligono, nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
5.  Scegliere il secondo punto nella [Vista 3D](3D_view/it.md), o inserire un **Raggio**.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate del centro, inserire le componenti X, Y e Z, e premere **Enter** dopo ciascuna. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempito** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, il poligono creato avrà **Make Face** impostato su `True` e avrà una faccia piena.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando si riavvierà al termine, consentendo di continuare a creare poligoni.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un Poligono può essere modificato con il comando [Modifica](Draft_Edit/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento di coordinate e raggi: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.
-   Se l\'opzione **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Usa le primitive Part quando disponibili** è selezionata, il comando creerà un [Part Poligono regolare](Part_RegularPolygon/it.md) invece di un Draft Poligono.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Poligono è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia del poligono. Il valore sarà {{value|0.0}} se **Make Face** se `False`.

-    **Chamfer Size|Length**: specifica la lunghezza degli smussi agli angoli del poligono.

-    **Draw Mode|Enumeration**: specifica se il poligono è {{value|inscritto}} in un cerchio o {{value|circoscritto}} attorno a un cerchio.

-    **Faces Number|Integer**: specifica il numero di lati del poligono.

-    **Fillet Radius|Length**: specifica il raggio dei raccordi agli angoli del poligono.

-    **Make Face|Bool**: specifica se il poligono forma o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto.

-    **Radius|Length**: specifica il raggio del cerchio che definisce il poligono.



### Viste


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del poligono. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Draft Poligono utilizzare il metodo `make_polygon` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makePolygon`.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Crea un oggetto `polygon` con il numero specificato di facce (`nfaces`) e basato su un cerchio di `radius` in millimetri.
-   Se `inscribed` è `True`, il poligono è inscritto nel cerchio, altrimenti sarà circoscritto.
-   Se `placement` è `None` il poligono viene creato all\'origine e uno dei suoi vertici giace sull\'asse X.
-   Se `face` è `True`, il poligono formerà una faccia, cioè apparirà pieno.

Esempio: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/it
