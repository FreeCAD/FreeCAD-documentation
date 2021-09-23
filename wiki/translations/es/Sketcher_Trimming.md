---
- GuiCommand:/es
   Name:Sketcher Trimming
   Name/es:Croquizador Recortar
   MenuLocation:Croquis → Croquizador Geometrías → Recortar borde
   Workbenches:[Croquizador](Sketcher_Workbench/es.md)
   Version:0.12
   SeeAlso:[Croquizador Extender borde](Sketcher_Extend/es.md)
---

# Sketcher Trimming/es

## Descripción

Esta herramienta recorta un borde hasta el borde más cercano que se superpone.

![](images/SketcherTrimExample1.png ) ![](images/SketcherTrimExample2.png ) ![](images/SketcherTrimExample3.png )

## Utilización

1.  Pulse el **<img src=images/Sketcher_Trimming.svg style="width:16px"> [Recortar](Sketcher_Trimming/es.md)**. El puntero del ratón se convierte en una cruz blanca con un símbolo de recorte rojo.
2.  Haga clic en el borde que desea recortar.
3.  El segmento de línea se recortará hasta la(s) línea(s) más cercana(s) que se superponga(n). Si hay otros elementos del boceto a ambos lados de la posición en la que se ha hecho clic, se recortará el trozo en el que se ha hecho clic.
4.  Si se pulsa **Esc** o se presiona el botón derecho del ratón, se terminará la función.

## Limitaciones

-    {{VersionMinus/es|0.18}}Los arcos de hipérbola, los arcos de parábola y las B-splines no se pueden recortar.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/es
