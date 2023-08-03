# Drawing Openbrowser/it
---
 GuiCommand:   Name: Drawing Openbrowser   Name/it: Apri browser   Workbenches: Drawing Workbench/it   Drawing, Complete|MenuLocation: Drawing , Apri Browser   Shortcut: none---

### Descrizione

Questo comando consente di visualizzare una [pagina di disegno](Drawing_Landscape_A3/it.md) selezionata utilizzando il browser web interno di FreeCAD. Il normale visualizzatore di una pagina di disegno di FreeCAD si basa sul [modulo interno di rendering SVG di Qt](http://qt-project.org/doc/qt-5.0/qtsvg/svgrendering.html), che supporta solo un piccolo sottoinsieme di tutte le specificazioni SVG. Per questo, alcune funzionalità SVG più avanzate, come il riempimenti a motivo o i testi multilinea non sono supportati da questo visualizzatore. Il browser web interno di FreeCAD, invece, è costruito su [webkit](http://en.wikipedia.org/wiki/WebKit), che è uno dei migliori render SVG disponibili e visualizza correttamente la pagina con tutte le sue caratteristiche.

### Utilizzo

1.  Creare una [Pagina di disegno](Drawing_Landscape_A3/it.md)
2.  Aggiungere delle [proiezioni](Drawing_View/it.md) o altro contenuto alla pagina
3.  [Aggiornare](Std_Refresh/it.md) se la pagina di disegno non viene aperta
4.  Premere il pulsante **<img src="images/Drawing_Openbrowser.png" width=16px> [Apri browser](Drawing_Openbrowser/it.md)
**

### Limitazioni

-   Una pagina aperta nel browser web non si aggiorna automaticamente alle modifiche. È necessario aggiornarla manualmente utilizzando: tasto destro del mouse → ricarica.


{{docnav/it
|[Ritaglio](Drawing_Clip/it.md)
|[Viste ortogonali](Drawing_Orthoviews/it.md)
|[Drawing](Drawing_Workbench/it.md)
|IconL=Drawing_Clip.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Orthoviews.png
}}


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Openbrowser/it
