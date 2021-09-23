# OpenSCAD CSG/it
 {{TOCright}}

## Importazione

### Elementi supportati 

-   primitive: cubo, sfera, cilindro, rettangolo, circonferenza, poligono, poliedro
-   booleane: unione, differenza, intersezione
-   estrusione lineare, rivoluzione
-   importazione (dxf, stl, off) (senza scalatura o trasformazione dell\'originale)
-   matrici multiple
-   colore

### Elementi non supportati 

-   proiezioni
-   superficie
-   renderizzazione (ignorata)
-   operazioni in generale: minkowski, glide, path, subdiv, hull

## Esportazione

### Elementi supportati 

-   primitive: parallelepipedo, cilindro, Cono, Toro
-   booleane: differenza, fusione, intersezione

### Ripiego

Qualsiasi oggetto derivato da Part::Feature che non è (ancora) supportato viene grigliato (mesh) ed esportato come un elemento poliedrico

## Correlazioni

-   [Ambiente OpenSCAD](OpenSCAD_Workbench/it.md)
-   [Importazione e Esportazione](Import_Export/it.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)


 {{OpenSCAD Tools navi}}

[Category:File\_Formats](Category:File_Formats.md)
