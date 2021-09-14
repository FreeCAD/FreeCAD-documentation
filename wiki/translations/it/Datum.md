# Datum/it



## Introduzione

In FreeCAD la parola **Datum** viene normalmente utilizzata per fare riferimento alla geometria ausiliaria (di riferimento) in [PartDesign](PartDesign_Workbench/it.md). Questi elementi geometrici non faranno parte della [Forma](Shape/it.md) (Shape) finale del [Corpo](Body/it.md) (Body), ma possono essere usati come riferimenti e supporti per gli [schizzi](Sketch/it.md) e altri tipi di [Funzioni](Feature/it.md) (Feature).

I seguenti elementi corrispondono agli elementi derivati dalla classe `Part::Datum`, a sua volta derivata da [Part Feature](Part_Feature/it.md):

-   [Punto di riferimento di PartDesign](PartDesign_Point/it.md)
-   [Linea di riferimento di PartDesign](PartDesign_Line/it.md)
-   [Piano di riferimento di PartDesign](PartDesign_Plane/it.md)
-   [Sistema di coordinate di PartDesign](PartDesign_CoordinateSystem/it.md)

I seguenti elementi sono derivati direttamente da [Part Feature](Part_Feature.md):

-   [PartDesign Forma legata](PartDesign_ShapeBinder/it.md)
-   [PartDesign Forma legata secondarie](PartDesign_SubShapeBinder/it.md)

## Utilizzo

1.  Passare nell\'ambiente [PartDesign](PartDesign_Workbench/it.md).
2.  Premere **<img src=images/PartDesign_Body.svg style="width:16px"> [Crea un corpo](PartDesign_Body/it.md)**.
3.  Selezionare l\'origine del corpo e renderla visibile premendo la barra **Spazio** sulla tastiera.
4.  Premere **<img src=images/PartDesign_Plane.svg style="width:16px"> [Piano di riferimento](PartDesign_Plane/it.md)** per aprire la scheda [Azioni](task_panel/it.md) per il piano.
5.  Nella [vista 3D](3D_view/it.md), fare clic su uno dei piani standard, ad esempio il piano XY. Quindi premere **OK** per chiudere il pannello delle azioni.
6.  Ora nella <img src=images/PartDesign_NewSketch.svg style="width:vista ad albero](tree_view/it.md), selezionare il piano di riferimento appena creato, quindi premere **[16px"> [Crea uno schizzo](PartDesign_NewSketch/it.md)**.
7.  Creare un contorno chiuso, quindi utilizzare **<img src=images/PartDesign_Pad.svg style="width:16px"> [Pad](PartDesign_Pad/it.md)** per estrudere lo schizzo e creare un solido iniziale.

Ora si può spostare e ruotare il piano di riferimento come si desidera, modificandone le proprietà nell\'[editor delle proprietà](property_editor/it.md) e Schizzo e Pad seguiranno il suo nuovo [Posizionamento](Placement/it.md).

È possibile aggiungere altri tipi di riferimenti da utilizzare con altri schizzi e funzioni.

## Note


<div class="mw-translate-fuzzy">

Quando sono apparsi nella v0.17, gli oggetti di riferimento erano destinati ad essere utilizzati all\'interno dei [Corpi](PartDesign_Body/it.md) di PartDesign. Tuttavia, poiché sono utili oggetti \"di riferimento\" con diversi [metodi di associazione](Part_Attachment/it.md), è stato proposto che siano disponibili al di fuori di [PartDesign](PartDesign_Workbench/it.md). In questo modo, saranno utilizzabili in gli ambienti di lavoro come geometria di supporto, in particolare nel contesto della creazione di [assemblaggi](Assembly/it.md).

-   [Create and display local coordinate system](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datum objects in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Structure toolbar and datums](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Local CS cannot be used in Part Wb?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


</div>


{{PartDesign Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
