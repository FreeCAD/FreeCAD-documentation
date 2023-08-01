---
- GuiCommand:/it
   Name:Draft OrthoArray
   Name/it:Serie ortogonale
   MenuLocation:Modifiche → Strumenti serie → Serie ortogonale
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version:0.19
   SeeAlso:[Serie polare](Draft_PolarArray/it.md), [Serie circolare](Draft_CircularArray/it.md), [Serie su tracciato](Draft_PathArray/it.md), [Serie di link su tracciato](Draft_PathLinkArray/it.md), [Serie su punti](Draft_PointArray/it.md), [Serie di link su punti](Draft_PointLinkArray/it.md)
---

# Draft OrthoArray/it



## Descrizione

Il comando <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Serie ortogonale** crea una serie (array) ortogonale (3 assi) da un oggetto selezionato. Il comando può facoltativamente creare una Serie di [Link](App_Link/it.md), che è più efficiente di una normale Serie.

Il comando può essere utilizzato su oggetti 2D creati con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche su molti oggetti 3D come quelli creati con gli ambienti [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Serie ortogonale*



## Utilizzo

1.  Facoltativamente selezionare un oggetto.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_OrthoArray.svg" width=16px> [Serie ortogonale](Draft_OrthoArray/it.md)**.
    -   Selezionare l\'opzione **Modifiche → Strumenti serie → <img src="images/Draft_OrthoArray.svg" width=16px> Serie ortogonale** dal menu.
3.  Si apre il pannello attività **Serie ortogonale**. Vedi [Opzioni](#Opzioni.md) per maggiori informazioni.
4.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto.
5.  Immettere i parametri richiesti nel pannello delle attività.
6.  Per completare il comando, eseguire una delle seguenti operazioni:
    -   Fare clic nella [Vista 3D](3D_view/it.md).
    -   Premere **Enter**.
    -   Premere il pulsante **OK**.



## Opzioni

-   Inserire il **Numero di elementi** per le direzioni X, Y e Z. Questo numero deve essere almeno {{Value|1}} per ogni direzione.
-   Immettere **Intervalli X** per specificare lo spostamento degli elementi nella direzione X. Per una serie rettangolare i valori Y e Z devono essere {{Value|0}}.
-   Immettere **Intervalli Y** per specificare lo spostamento degli elementi nella direzione Y. Per una serie rettangolare i valori X e Z devono essere {{Value|0}}.
-   Immettere **Intervalli Z** per specificare lo spostamento degli elementi nella direzione Z. Per una serie rettangolare i valori X e Y devono essere {{Value|0}}.
-   Premere il pulsante **Reset X, Y o Z** per reimpostare lo spostamento nella direzione data ai valori predefiniti.
-   Se la casella di controllo **Fusione** è selezionata, gli elementi sovrapposti nella serie vengono fusi. Questo non funziona per le Serie di link.
-   Se la casella **Serie di link** è spuntata, viene creato una Serie di Link invece di un normale serie. Una Serie di link è più efficiente perché i suoi elementi sono oggetti [App Link](App_Link/it.md).
-   Premere **Esc** o il pulsante **Annulla** per interrompere il comando.



## Note

-   Una Serie ortogonale può essere trasformata in una [Serie polare](Draft_PolarArray/it.md) o in una [Serie circolare](Draft_CircularArray/it.md) modificandone la proprietà **Array Type**.
-   Una Serie di link non può essere trasformata in una serie normale o viceversa. Il tipo di serie deve essere deciso al momento della creazione.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Il comando Serie ortogonale, il comando [Serie polare](Draft_PolarArray/it.md) e il comando [Serie circolare](Draft_CircularArray/it.md) creano lo stesso oggetto. Questo oggetto è derivato da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà (ad eccezione di alcune proprietà della vista che non sono ereditate dagli serie di link). Le seguenti proprietà sono aggiuntive se non diversamente specificato:



### Dati


{{TitleProperty|Link}}

Le proprietà in questo gruppo sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Circular array}}

Le proprietà in questo gruppo sono nascoste per le serie ortogonali e le serie polari.

-    **Number Circles|Integer**: specifica il numero di strati circolari. Deve essere almeno {{Value|2}}.

-    **Radial Distance|Distance**: specifica la distanza tra gli strati circolari.

-    **Symmetry|Integer**: specifica il numero di linee di simmetria. Questo numero cambia la distribuzione degli elementi nella serie.

-    **Tangential Distance|Distance**: specifica la distanza tra gli elementi nello stesso strato circolare. Deve essere maggiore di zero.


{{TitleProperty|Objects}}

-    **Array Type|Enumeration**: specifica il tipo di serie, che può essere {{value|ortho}}, {{value|polar}} o {{value|circular}}.

-    **Axis Reference|LinkGlobal**: specifica l\'oggetto e il bordo da utilizzare al posto delle proprietà **Axis** e **Center**. Non utilizzato per le serie ortogonali.

-    **Base|Link**: specifica l\'oggetto da duplicare nella serie.

-    **Count|Integer**: (read-only) specifica il numero totale di elementi nella serie. {{VersionMinus/it|0.20}}: disponibile solo per le serie di link.

-    **Expand Array|Bool**: specifica se espandere la serie nella [Vista ad albero](Tree_view/it.md) per abilitare la selezione dei suoi singoli elementi. Disponibile solo per le serie di link.

-    **Fuse|Bool**: specifica se gli elementi sovrapposti nella serie sono fusi o meno. Non utilizzato per le serie di link.


{{TitleProperty|Orthogonal array}}

Le proprietà in questo gruppo sono nascoste per le serie circolari e polari.

-    **Interval X|VectorDistance**: specifica l\'intervallo tra gli elementi nella direzione X.

-    **Interval Y|VectorDistance**: specifica l\'intervallo tra gli elementi nella direzione Y.

-    **Interval Z|VectorDistance**: specifica l\'intervallo tra gli elementi nella direzione Z.

-    **Number X|Integer**: specifica il numero di elementi nella direzione X. Deve essere almeno {{Value|1}}.

-    **Number Y|Integer**: specifica il numero di elementi nella direzione Y. Deve essere almeno {{Value|1}}.

-    **Number Z|Integer**: specifica il numero di elementi nella direzione Z. Deve essere almeno {{Value|1}}.


{{TitleProperty|Polar array}}

Le proprietà in questo gruppo sono nascoste per le serie circolari e ortogonali.

-    **Angle|Angle**: specifica l\'apertura dell\'arco circolare. Usa {{value|360&#176;}} per un cerchio completo.

-    **Interval Axis|VectorDistance**: specifica l\'intervallo tra gli elementi nella direzione **Axis**.

-    **Number Polar|Integer**: specifica il numero di elementi nella direzione polare.


{{TitleProperty|Polar/circular array}}

Le proprietà in questo gruppo sono nascoste per le serie ortogonali.

-    **Axis|Vector**: specifica la direzione dell\'asse della serie.

-    **Center|VectorDistance**: specifica il punto centrale della serie. L\'asse della serie passa per questo punto. Per le serie circolari è un offset dal **Placement** dell\'oggetto **Base**.



### Vista


{{TitleProperty|Link}}

Le proprietà in questo gruppo, ad eccezione della proprietà ereditata, sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: questa è una proprietà ereditata che appare nel gruppo Selezione per altre serie

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

Le proprietà in questo gruppo, ad eccezione della proprietà ereditata, sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: questa è una proprietà ereditata.


{{TitleProperty|Display Options}}

Le proprietà in questo gruppo sono proprietà ereditate. Vedere [Part Feature](Part_Feature#Properties.md) per ulteriori informazioni.

-    **Bounding Box|Bool**: questa proprietà non è ereditata dalle serie di link.

-    **Modalità di visualizzazione|Enumeration**: per le serie di link può essere {{value|Link}} o {{value|ChildView}}. Per altre serie può essere: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} o {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

Le proprietà in questo gruppo non vengono ereditate dalle serie di link.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).



### Serie parametrica 

Per creare una serie ortogonale parametrica usare il metodo `make_array` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeArray`. Il metodo `make_array` può creare Serie ortogonali, [Serie polari](Draft_PolarArray/it.md) e [Serie circolari](Draft_CircularArray/it.md). Per ogni tipo di serie sono disponibili uno o più wrapper.

Il metodo principale:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

I wrapper per le serie ortogonali sono:


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

I wrapper per le serie rettangolari sono:


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`è l\'oggetto da disporre in serie. Può anche essere la `Label` (string) di un oggetto nel documento corrente.

-    `v_x`, `v_y` e `v_z` sono i vettori tra i punti base degli elementi nelle rispettive direzioni.

-    `d_x`, `d_y` e `d_z` sono le distanze tra i punti base degli elementi nelle rispettive direzioni.

-    `n_x`, `n_y` e `n_z` sono i numeri degli elementi nelle rispettive direzioni.

-   Se `use_link` è `True` gli elementi creati sono [App Links](App_Link/it.md) invece di normali copie.

-    `array`viene restituito con l\'oggetto serie creato.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```



### Serie non parametrica 

Per creare una serie ortogonale non parametrica usare il metodo `array` del modulo Draft. Questo metodo restituisce `None`.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/it
