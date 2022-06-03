---
- GuiCommand   */es
   Name   *PartDesign Migrate
   Name/es   *DiseñoPiezas Migración
   MenuLocation   *Diseño Piezas → Migración
   Workbenches   *[DiseñoPiezas](PartDesign_Workbench/es.md)
   Version   *0.17
---

# PartDesign Migrate/es

## Descripción

El ambiente de trabajo de DiseñoPiezas en FreeCAD v0.17 introduce nuevas herramientas y elementos que no son reconocidos por las versiones anteriores de FreeCAD (0.16 y anteriores). Los documentos de FreeCAD creados en versiones anteriores pueden seguir siendo abiertos y editados. Para beneficiarse de las nuevas características, deben ser migrados a través del menú DiseñoPiezas → Migrar.


{{Version/es|0.17}}

## Utilización

1.  Abrir un documento de FreeCAD que fue creado con FreeCAD {{VersionMinus/es|0.16}}
2.  Cambiar al **<img src="images/Workbench_PartDesign.svg" width=16px> [DiseñoPieza](PartDesign_Workbench/es.md)** ambiente de trabajo.
3.  Ve al menú **Diseño Pieza** → **Migrar**.
4.  Si la migración funciona, un <img alt="" src=images/Std_Part.svg  style="width   *24px;"> [Contenedor de piezas](Std_Part/es.md) se creará que contendrá uno o más <img alt="" src=images/PartDesign_Body.svg  style="width   *24px;"> [Cuerpos](PartDesign_Body/es.md), cada uno de los cuales albergará una cadena de características.

## Limitaciones

-   Antes de iniciar el proceso de migración, compruebe si el modelo se construyó con las opciones de refinamiento automático activadas (en **Edición → Preferencias → Diseño Piezas → General**), y configure sus preferencias en consecuencia. Esto puede determinarse fácilmente alternando sucesivamente la visibilidad de las características en el árbol del modelo. Si no quedan aristas residuales entre características como Almohadillas y Bolsillos, las opciones de refinamiento automático se desactivaron.
-   Si un documento que se va a migrar sólo contiene croquis y operaciones de DiseñoPieza , es probable que el proceso de migración tenga éxito. Algunas operaciones, como los chaflanes y los filetes, pueden requerir una reconstrucción.
-   Si el documento a migrar tiene un flujo de trabajo mixto Pieza/Diseño de Pieza/Borrador, lo más probable es que la conversión falle o, en el mejor de los casos, produzca resultados inesperados, y sea necesario migrarlo manualmente.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate/es
