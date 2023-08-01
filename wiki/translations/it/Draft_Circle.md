---
- GuiCommand:/it
   Name:Draft Circle
   Name/it:Cerchio
   MenuLocation:Drafting → Cerchio
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**C** **I**
   Version:0.7
   SeeAlso:[Arco](Draft_Arc/it.md), [Arco da 3 punti](Draft_Arc_3Points/it.md)
---

# Draft Circle/it



## Descrizione

Il comando <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Cerchio** crea un cerchio nel [piano di lavoro](Draft_SelectPlane/it.md) corrente da un centro e un raggio. Il raggio può essere definito selezionando un punto.

Un Cerchio può essere trasformato in un arco impostando le sue proprietà **First Angle** e **Last Angle** su valori diversi.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Cerchio definito da due punti, centro e raggio*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Circle.svg" width=16px> [Cerchio](Draft_Circle/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Circle.svg" width=16px> Cerchio** dal menu.
    -   Usare la scorciatoia da tastiera: **C** poi **I**.
2.  Si apre il pannello delle attività **Cerchio**. Vedi [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto, il centro del cerchio, nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere il secondo punto nella [Vista 3D](3D_view/it.md), o inserire un **Raggio**.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate del centro, inserire le componenti X, Y e Z, e premere **Enter** dopo ciascuna. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempimento** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, il cerchio creato avrà **Make Face** impostato su `True` e avrà una faccia piena.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando si riavvierà al termine, consentendo di continuare a creare cerchi.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premi **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un Cerchio può essere modificato con il comando [Modifica](Draft_Edit/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento di coordinate e raggi: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.
-   Se l\'opzione **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Usa le primitive di Part quando disponibili** è selezionata, il comando creerà un [Part Cerchio](Part_Circle/it.md) invece di un Draft Cerchio.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Cerchio è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia del cerchio. Il valore sarà {{value|0.0}} se **Make Face** se `False` o la faccia non può essere creato.

-    **First Angle|Angle**: specifica l\'angolo iniziale del cerchio, normalmente {{value|0&#176;}}.

-    **Last Angle|Angle**: specifica l\'angolo finale del cerchio, normalmente {{value|0&#176;}}.

-    **Make Face|Bool**: specifica se il cerchio crea o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se **First Angle** e **Last Angle** hanno lo stesso valore. Notare che {{value|0&#176;}} e {{value|360&#176;}} non sono considerati uguali.

-    **Radius|Length**: specifica il raggio del cerchio.



### Vista


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del cerchio. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Draft Cerchio usare il metodo `make_circle` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeCircle`.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```

-   Crea un oggetto `circle` dal dato `radius` in millimetri.
    -   
        `radius`
        
        può anche essere un `Part.Edge`, di cui l\'attributo `Curve` deve essere un `Part.Circle`.
-   Se `placement` è `None` il cerchio viene creato all\'origine.
-   Se `face` è `True` e il cerchio è chiuso, diventa una faccia e appare riempita.
-   Se `startangle` e `endangle` sono dati in gradi e hanno valori diversi, sono usati e l\'oggetto appare come un [Arco](Draft_Arc/it.md).

Esempio: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/it
