---
 GuiCommand:
   Name/es: Fixtura de trayectoria
   Workbenches: Path Workbench
   MenuLocation: Trayectoria , Comandos Parciales , Fixtura
   Shortcut: **P** **F**
   SeeAlso: 
---

# CAM Fixture/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta coloca un punto de fixtura (G53-G59) para las siguientes operaciones


</div>

Target Work Offset Coordinates typically include: Fixtures G53 to G59. The G-code is simply the Fixture (G53, G54, etc\...). The coordinate offset fixtures represent:

-   G53 → Machine coordinate system.
-   G54 → Scratchpad coordinate system.
-   G55 to G59.9 → Coordinate fixtures allowing work offsets, relative to Homing switches located on the CNC machine, to be used.

The G59 Fixture is used to expand available fixtures. The degree of expansion implemented is CNC machine specific, and this command allows provides for G59.1 to G59.9.



## Utilización


<div class="mw-translate-fuzzy">

1.  Presiona el boton **<img src="images/Path_Fixture.png" width=16px> [Fixtura](Path_Fixture.md)
**
2.  Coloca la fixtura deseada


</div>



## Propiedades

-    **Fixtura**: Coloca el actual punto como fixtura

-    **Activar**: Define si este comando esta activo o no cuando es introducido a un compuesto.

## Notes

## Limitations

## Scripting


<div class="mw-translate-fuzzy">





</div>


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Fixture/es
