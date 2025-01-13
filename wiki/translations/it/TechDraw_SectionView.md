---
 GuiCommand:
   Name: TechDraw_SectionView
   Name/it: TechDraw Vista di sezione
   MenuLocation: TechDraw , Viste TechDraw , Inserisci Vista di sezione
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_ComplexSection/it, TechDraw_View/it
---

# TechDraw SectionView/it



## Descrizione

Lo strumento **TechDraw Vista di sezione** inserisce una vista in sezione trasversale basata sulla vista di una parte esistente.

<img alt="" src=images/TechDraw_section_ANSI.png  style="width:350px;">
<img alt="" src=images/TechDraw_section_ISO.png  style="width:350px;"> 
*Sezione di una vista già posizionata, che mostra i fori interni e la superficie di taglio tratteggiati.<br>
L'immagine in alto mostra il formato della freccia ANSI.<br>
L'immagine in basso mostra il formato della freccia ISO.
*



## Utilizzo

1.  Selezionare una vista della parte nella [Vista 3D](3D_view/it.md) o nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_SectionView.svg" width=16px> [Inserisci Vista di sezione](TechDraw_SectionView/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_SectionView.svg" width=16px> Inserisci Vista di sezione** dal menu.
3.  Si apre un pannello delle attività che aiuterà a calcolare le varie proprietà. Vengono calcolati valori ragionevoli per la direzione della vista, ma questi possono essere modificati.

![](images/TechDraw_Section_Taskview.png ) 
*La scheda Azioni per definire il taglio in sezione di una vista*



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Nelle proprietà della **Base View** si può modificare l\'aspetto della linea di sezione.

Una Vista di Sezione, formalmente un oggetto {{Incode|TechDraw::DrawViewSection}}, deriva da un oggetto [Part View](TechDraw_View/it#Properties_Part_View.md), formalmente un oggetto {{Incode|TechDraw::DrawViewPart}} ed eredita tutti le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Appearance}}

-    **Section Line Stretch|FloatConstraint**: regola la lunghezza della linea di sezione. {{Value|1.0}} è la lunghezza normale, {{Value|1.1}} sarebbe più lungo del 10%, {{Value|0.9}} sarebbe più corto del 10%. {{Version/it|1.0}}


{{TitleProperty|Cut Operation}}

-    **Fuse Before Cut|Bool**: Fonde le forme di origine prima di eseguire il taglio in sezione.

-    **Trim After Cut|Bool**: Ritaglia inoltre la forma risultante dopo il taglio della sezione per rimuovere eventuali pezzi indesiderati. {{Version/it|0.21}}

-    **Use Previous Cut|Bool**Utilizza la forma di taglio dalla vista di base invece dell\'oggetto originale. {{Version/it|1.0}}


{{TitleProperty|Cut Surface Format}}

-    **Cut Surface Display|Enumeration**: Aspetto della superficie tagliata. Opzioni:

    -   
        {{Value|Hide}}
        
        : Nasconde la superficie tagliata, verrà visualizzato solo il contorno.

    -   
        {{Value|Color}}
        
        : Colora la superficie tagliata utilizzando l\'impostazione **Cut Surface Color** nelle [Preferenze TechDraw](TechDraw_Preferences/it.md).

    -   
        {{Value|SvgHatch}}
        
        : Tratteggia la sezione tagliata utilizzando un [tratteggio](TechDraw_Hatch/it.md)

    -   
        {{Value|PatHatch}}
        
        : Tratteggia la sezione tagliata utilizzando un [tratteggio geometrico](TechDraw_GeometricHatch/it.md)

-    **File Hatch Pattern|File**: Percorso completo del file del modello di tratteggio SVG.

-    **File Geom Pattern|File**: Percorso completo del file di pattern PAT.

-    **Svg Included|FileIncluded**: Percorso completo del file del modello di tratteggio SVG incluso.

-    **Pat Included|FileIncluded**: Percorso completo del file di pattern PAT incluso.

-    **Name Geom Pattern|String**: Nome del modello PAT da utilizzare.

-    **Hatch Scale|Float**: Regolazione della dimensione del modello di tratteggio.

-    **Hatch Rotation|Float**: Rotazione del modello di tratteggio in gradi in senso antiorario. {{Version/it|0.21}}

-    **Hatch Offset|Vector|Hidden**: Offset del modello di tratteggio. {{Version/it|0.21}}


{{TitleProperty|Section}}

-    **Section Symbol|String**: l\'identificatore di questa sezione.

-    **Base View|Link**: la vista su cui si basa questa sezione.

-    **Section Normal|Vector**: un vettore che descrive la direzione normale al piano di taglio.

-    **Section Origin|Vector**: un vettore che descrive un punto sul piano di taglio. In genere il baricentro della parte originale.

-    **Section Direction|Enumeration**: la direzione nella vista di base per questa sezione. Opzioni: {{Value|Aligned}}, {{Value|Right}}, {{Value|Left}}, {{Value|Up}} or {{Value|Down}}.



### Vista


{{TitleProperty|Cut Surface}}

-    **Cut Surface Color|Color**: colore solido per l\'evidenziazione della superficie. Utilizzato se **Cut Surface Display** è impostato su {{Value|Color}}.

-    **Show Cut Surface|Bool|Hidden**: mostra/nasconde la superficie tagliata.


{{TitleProperty|Surface Hatch}}

-    **Geom Hatch Color|Color**: il colore del modello di tratteggio geometrico.

-    **Hatch Color|Color**: il colore del modello di tratteggio Svg.

-    **Hatch Cut Surface|Bool|Hidden**: tratteggia la superficie tagliata.

-    **Weight Pattern|Float**: spessore della linea del modello di tratteggio geometrico.



## Note

-   **Section Line Format**: sono supportati due formati di linea di sezione (come illustrato sopra) e controllati dall\'impostazione delle preferenze \"Standard linea di sezione\" nella scheda Annotazione. L\'opzione {{Value|ANSI}} utilizza \"frecce che tirano\" (noto anche come \"formato tradizionale\" in alcune aree) e l\'opzione {{Value|ISO}} utilizza \"frecce che spingono\" (noto anche come \"formato freccia di riferimento \").
-   **Fuse Before Cut**: l\'operazione di sezione a volte non riesce a tagliare le forme sorgente. Se **Fuse Before Cut** è true, le forme di origine vengono unite in un\'unica forma prima che venga tentata l\'operazione di sezione. Se si riscontrano problemi con il funzionamento della sezione, prova a invertire questo valore.
-   **Trim After Cut**: l\'operazione di taglio della sezione a volte lascia dietro di sé una porzione della forma sorgente. Se **Trim After Cut** è true, viene eseguita un\'operazione di taglio aggiuntiva sul risultato del primo taglio che dovrebbe rimuovere eventuali pezzi indesiderati.
-   **Cut Surface Display**: la superficie tagliata può essere nascosta, dipinta in un colore solido, tratteggiata utilizzando un modello Svg (predefinito) o tratteggiata utilizzando un modello PAT. Vedere [Tratteggio](TechDraw_Hatching/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Vista di sezione può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite le seguenti funzioni:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)

doc.recompute()
```



## Esempi

Per ulteriori informazioni sulle Viste di sezione e su alcuni casi d\'uso, dare un\'occhiata a: [Esempi di sezione TechDraw](TechDraw_Section_Examples/it.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/it
