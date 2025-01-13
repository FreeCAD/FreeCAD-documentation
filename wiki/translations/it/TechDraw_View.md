---
 GuiCommand:
   Name: TechDraw View
   Name/it: TechDraw Vista
   MenuLocation: TechDraw , Viste TechDraw , Inserisci Vista
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_ProjectionGroup/it, TechDraw_SpreadsheetView/it, TechDraw_ArchView/it, TechDraw_Symbol/it, TechDraw_Image/it
---

# TechDraw View/it



## Descrizione

Lo strumento **TechDraw Vista** aggiunge una rappresentazione di uno o più oggetti ad una pagina di disegno. {{Version/it|1.0}}: Può creare un [Elemento del gruppo di proiezione (una singola vista)](#Properties_Projection_Group_Item.md), un [Gruppo di proiezione](TechDraw_ProjectionGroup/it.md), una [Vista del foglio di calcolo](TechDraw_SpreadsheetView/it.md), una [Vista di Arch](TechDraw_ArchView/it.md), un [Simbolo](TechDraw_Symbol/it.md) o una [Vista immagine](TechDraw_Image/it.md).

In {{VersionMinus/it|0.21}} lo strumento può creare solo una [Part View](#Properties_Part_View.md), che è molto simile a un elemento del gruppo di proiezione.

![](images/TechDraw_View_example.png ) 
*Vista di un solido con linee nascoste*



## Utilizzo dell\'Elemento del Gruppo di Proiezione e del Gruppo di Proiezione 

1.  Facoltativamente ruotare la [vista 3D](3D_view/it.md). La direzione della telecamera nella vista 3D può essere utilizzata per impostare la direzione di proiezione della vista primaria.
2.  Selezionare uno o più oggetti con una proprietà **Shape** nella vista 3D o [Vista ad albero](Tree_view/it.md). È inoltre possibile selezionare [Std Parti](Std_Part/it.md) o [Std Gruppi](Std_Group/it.md) che contengono tali oggetti. Quando si seleziona nella vista 3D, la prima faccia selezionata può essere utilizzata per impostare la direzione di proiezione della vista primaria. Non selezionare gli oggetti selezionando una faccia nella vista 3D se desidera utilizzare la direzione corrente della telecamera.
3.  Se nel documento sono presenti più pagine di disegno: facoltativamente aggiungere la pagina desiderata alla selezione selezionandola nella [Vista ad albero](Tree_view/it.md).
4.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_View.svg" width=16px> [Inserisci Vista](TechDraw_View/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_View.svg" width=16px> Inserisci Vista** dal menu.
5.  Se nel documento sono presenti più pagine di disegno e se nessuna pagina è visualizzata nell\'[Area della vista principale](Main_view_area/it.md) e non si ha ancora selezionato una Pagina, si apre la finestra di dialogo **Scelta Pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
6.  Si apre il pannello delle azioni **Vista Parte**. {{Version/it|1.0}}
7.  Facoltativamente regolare i parametri:
    -   **Scala**: selezionare {{Value|Pagina}}, {{Value|Automatico}} o {{Value|Personalizzato}}. Se è selezionata l\'ultima opzione: inserire il numeratore e il denominatore della scala.
    -   **Direzione**: utilizzare i pulsanti disponibili per regolare la direzione di proiezione e la rotazione della vista primaria:
        -   Il pulsante **[#.## #.## #.##]** al centro mostra la direzione di proiezione corrente. Il valore iniziale dipende dalla [preferenza](TechDraw_Preferences/it#General.md) **Usa direzione telecamera 3D** . Premere il pulsante per regolare manualmente la direzione e la rotazione della vista.
        -   Premere il pulsante **<img src="images/Arrow-up.svg" width=16px>**, **<img src="images/Arrow-down.svg" width=16px>**, **<img src="images/Arrow-left.svg" width=16px>** o il pulsante **<img src="images/Arrow-right.svg" width=16px>** per ruotare la direzione di proiezione di 90° attorno all\'asse orizzontale o verticale della vista.
        -   Premere il pulsante **<img src="images/Arrow-cw.svg" width=16px>** o il pulsante **<img src="images/Arrow-ccw.svg" width=16px>** per ruotare la vista di 90 ° attorno alla direzione di proiezione.
        -   Premere il pulsante **<img src="images/TechDraw_ProjFront.svg" width=16px>** per impostare la direzione di proiezione della vista primaria sulla [vista frontale](Std_ViewFront/it.md) standard.
        -   Premere il pulsante **<img src="images/TechDraw_CameraOrientation.svg" width=16px>** per impostarlo sulla prima faccia selezionata, se disponibile, oppure sulla direzione corrente della telecamera.
    -   **Proiezioni secondarie**: crea facoltativamente proiezioni secondarie oltre alla vista primaria. È necessario specificare almeno una proiezione secondaria affinché tutti i controlli in questa sezione possano essere visualizzati.
8.  Dopo aver modificato alcuni parametri, può essere necessario premere il pulsante **Applica** per aggiornare le viste.
9.  Premere il pulsante **OK**.
10. Viene inserito un [Elemento gruppo di proiezioni](#Properties_Projection_Group_Item.md) o, se sono presenti una o più proiezioni secondarie, un [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md).

![](images/TechDraw_View_Taskpanel.png ) 
*Vista Parte [pannello azioni](Task_panel/it.md)*



## Utilizzo di altri tipi di visualizzazione 


{{Version/it|1.0}}

1.  Facoltativamente, selezionare un [Foglio di calcolo](Spreadsheet_CreateSheet/it.md) nella [Vista ad albero](Tree_view/it.md) o un [Arch Piano di sezione](Arch_SectionPlane/it.md) nella [Vista 3D](3D_view/it.md) o nella vista ad albero.
2.  Seguire i passaggi 3, 4 e 5 come spiegato [sopra](#Usage_Projection_Group_Item_and_Projection_Group.md).
3.  Se non si ha selezionato un Foglio di calcolo o un Arch piano di sezione:
    1.  Si apre una finestra di dialogo di avviso.
    2.  Selezionare la casella di controllo **Non mostrare più questo messaggio** per evitare questa finestra di dialogo in futuro.
    3.  Premere il pulsante **OK**.
    4.  Si apre un browser di file.
    5.  Selezionare un file SVG o un\'immagine.
4.  È stato inserito una [Vista Foglio di calcolo](TechDraw_SpreadsheetView/it.md), un [Vista Arch](TechDraw_ArchView/it.md), un [Simbolo](TechDraw_Symbol/it.md) o un [Vista Immagine](TechDraw_Image/it.md).
5.  In caso di Vista di un Foglio di calcolo: regolare l\'intervallo di celle della visualizzazione modificando le sue proprietà **Cell Start** e **Cell End**.
6.  In caso di Vista di un Simbolo o di un\'Immagine: facoltativamente modificare la sua proprietà **Scale** per regolarne le dimensioni.



## Proprietà Part View 

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Una Vista Parte, formalmente un oggetto {{Incode|TechDraw::DrawViewPart}}, ha le seguenti proprietà:



### Dati


{{TitleProperty|Base}}

-    **X|Distance**: la posizione orizzontale della vista sulla pagina. (1)

-    **Y|Distance**: la posizione verticale della vista sulla pagina. (1)

-    **Lock Position|Bool**: impedisce alle viste di essere trascinate nella GUI quando `True`. La vista può ancora essere spostata modificando le proprietà X,Y. (1)

-    **Rotation|Angle**: rotazione in senso antiorario della vista sulla pagina in gradi. (1)

-    **Scale Type|Enumeration**: il tipo di scala. Opzioni: (1)

    -   
        {{Value|Page}}
        
        : utilizza l\'impostazione di scala della [Pagina predefinita](TechDraw_PageDefault/it.md).

    -   
        {{Value|Automatic}}
        
        : adatta la visualizzazione alla pagina.

    -   
        {{Value|Custom}}
        
        : utilizza la scala definita da **Scale**.

-    **Scale|FloatConstant**: la vista verrà visualizzata sulla pagina in rapporto Scala:1 rispetto all\'origine. (1)

-    **Caption|String**: didascalia di testo breve opzionale. (1)


{{TitleProperty|Cosmetics}}

-    **Cosmetic Vertexes|TechDraw::PropertyCosmeticVertexList|Hidden**
    

-    **Cosmetic Edges|TechDraw::PropertyCosmeticEdgeList|Hidden**
    

-    **Center Lines|TechDraw::PropertyCenterLineList|Hidden**
    

-    **Geom Formats|TechDraw::PropertyGeomFormatList|Hidden**
    


{{TitleProperty|HLR Parameters}}

-    **Coarse View|Bool**: Se `True`, TechDraw utilizzerà un\'approssimazione del poligono per calcolare la geometria del disegno. Se `False`, TechDraw utilizzerà un algoritmo di precisione. CoarseView può essere molto più veloce per i modelli complessi. La qualità del disegno risulta ridotta, poiché ogni curva viene approssimata come una serie di brevi segmenti di linea. I vertici non vengono visualizzati in CoarseView poiché ogni breve segmento comporterebbe due nuovi vertici e la visualizzazione diventerebbe ingombrante. Le quote lineari possono essere aggiunte a CoarseView, ma è improbabile che siano utili.

-    **Smooth Visible|Bool**: Linee smussate visibili attivate/disattivate.

-    **Seam Visible|Bool**: Linee di giuntura visibili (seme) attivate/disattivate.

-    **Iso Visible|Bool**: Linee isometriche visibili (u,v) attivate/disattivate.

-    **Hard Hidden|Bool**: Linee nascoste attivate/disattivate.

-    **Smooth Hidden|Bool**: Linee nascoste attivate/disattivate.

-    **Seam Hidden|Bool**: Linee di giuntura (seme) nascoste attivate/disattivate.

-    **Iso Hidden|Bool**: Linee isometriche nascoste(u,v) attivate/disattivate.

-    **Iso Count|Integer**: Numero di linee isometriche(u,v) da disegnare su ciascuna faccia.

-    **Scrub Count|Integer**: Numero di volte in cui FreeCAD dovrebbe tentare di pulire il risultato HLR. {{Version/it|0.21}}


{{TitleProperty|Projection}}

-    **Source|LinkList**: collegamenti agli oggetti disegnabili da rappresentare.

-    **XSource|XLinkList**: collegamenti agli oggetti disegnabili in un file esterno.

-    **Direction|Vector**: questo vettore controlla la direzione da cui si sta visualizzando l\'oggetto. +X è destra, -X è sinistra, +Y è posteriore, -Y è anteriore (guardando nello schermo), +Z è su e -Z è giù. Quindi una vista frontale è (0,-1,0) e una vista isometrica è (1,-1,1).

-    **XDirection|Vector**: questo vettore controlla la rotazione della vista attorno alla direzione.

-    **Perspective|Bool**: `True` per proiezione prospettica, `False` per proiezione ortogonale.

-    **Focus|Distance**: distanza dalla fotocamera al piano di proiezione per proiezioni prospettiche. Deve essere regolato per adattarsi all\'oggetto. Troppo lontano si perde la prospettiva, troppo vicino l\'oggetto risulta distorto.



### Vista


{{TitleProperty|Base}}

-    **Keep Label|Bool**: mostra sempre l\'etichetta della vista se `True`. (1)

-    **Stack Order|Integer**: sopra o sotto giro rispetto ad altre visualizzazioni. (1) {{Version/it|0.21}}


{{TitleProperty|Broken View}}

-    **Break Line Style|Enumeration**: Imposta lo stile della linea di interruzione, se applicabile. {{Version/it|1.0}}

-    **Break Line Type|Enumeration**: Regola il tipo di rappresentazione della linea di interruzione sulle viste interrotte, se applicabile: {{Value|None}}, {{Value|ZigZag}} o {{Value|Simple}}. {{Version/it|1.0}}


{{TitleProperty|Decoration}}

-    **Arc Center Marks|Bool**: Attiva/disattiva i contrassegni centrali dell\'arco circolare.

-    **Center Scale|Float**: Regola la dimensione del contrassegno centrale dell\'arco circolare, se abilitato.

-    **Horiz Center Line|Bool**: Mostra una linea centrale orizzontale attraverso la Vista.

-    **Show All Edges|Bool**: Mostra temporaneamente le linee invisibili.

-    **Vert Center Line|Bool**: Mostra una linea centrale verticale attraverso la Vista.


{{TitleProperty|Faces}}

-    **Face Color|Color**: Imposta il colore delle facce. {{Version/it|1.0}}

-    **Face Transparency|Percent**: Imposta la trasparenza delle facce. {{Version/it|1.0}}


{{TitleProperty|Highlight}}

-    **Highlight Adjustment|Float**: regola la rotazione dei dettagli evidenziati, se applicabile.

-    **Highlight Line Color|Color**: imposta il colore della linea evidenziata, se applicabile.

-    **Highlight Line Style|Enumeration**: imposta lo stile della linea evidenziata, se applicabile.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: non ancora implementato.

-    **Hidden Width|Length**: lo spessore delle linee nascoste, se abilitato.

-    **Iso Width|Length**: lo spessore delle linee isometriche di superficie (u,v) e delle linee di quota.

-    **Line Width|Length**: lo spessore delle linee visibili. Vedere [Gruppi di linee](TechDraw_LineGroup/it.md).


{{TitleProperty|Section Line}}

-    **Include Cut Line|Bool**: Mostra/nasconde la linea di taglio della sezione, se applicabile. {{Version/it|1.0}}

-    **Section Line Color|Color**: Imposta il colore della linea di sezione, se applicabile.

-    **Section Line Marks|Bool**: Mostra/nasconde i contrassegni ai cambi di direzione per la sezione complessa, se applicabile. {{Version/it|0.21}}

-    **Section Line Style|Enumeration**: Imposta lo stile della linea di sezione, se applicabile.

-    **Show Section Line|Bool**: Mostra/nasconde la linea di sezione, se applicabile.

\(1\) queste proprietà sono comuni a tutti i tipi di Viste.



## Proprietà dell\'Elemento del gruppo di proiezione 

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un Elemento del Gruppo di Proiezione, formalmente un oggetto {{Incode|TechDraw::DrawProjGroupItem}}, deriva da un oggetto [Part View](#Properties_Part_View.md), formalmente un oggetto {{Incode|TechDraw::DrawViewPart}} ed eredita tutti le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati 


{{TitleProperty|Base}}

-    **Type|Enumeration**: Il tipo di vista ({{Value|Front}}, {{Value|Left}}, ecc.).

-    **Rotation Vector|Vector**: Deprecato utilizzare invece **XDirection**.



## Properties Gruppo di Proiezione 

Vedere [TechDraw Gruppo di Proiezione](TechDraw_ProjectionGroup/it#Properties.md).



## Proprietà Vista Foglio di calcolo 

Vedere [TechDraw Vista Foglio di calcolo](TechDraw_SpreadsheetView/it#Properties.md).



## Proprietà Vista di Arch 

Vedere [TechDraw Vista di Arch](TechDraw_ArchView/it#Properties.md).



## Proprietà Simbolo 

Vedere [TechDraw Simbolo](TechDraw_Symbol/it#Properties.md).



## Proprietà Vista Immagine 

Vedere [TechDraw Immagine](TechDraw_Image/it#Properties.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

È possibile creare una Vista Parte con [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando le seguenti funzioni:


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/it
