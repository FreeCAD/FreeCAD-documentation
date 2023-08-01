---
- GuiCommand:
   Name:Path Fixture
   Name/it:Fissaggio
   Workbenches:[Path](Path_Workbench/it.md)
   MenuLocation:Path - Comandi parziali - Fissaggio
   Shortcut:**P** **F**
   SeeAlso:
---

# Path Fixture/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento imposta il dispositivo di coordinate dell\'offset del lavoro del controllore CNC della macchina. Questo strumento imposta un punto di fissaggio (G53-G59) per le successive operazioni


</div>


<div class="mw-translate-fuzzy">

Target Work Offset Coordinates typically include: Fixtures G53 to G59. The G-Code is simply the Fixture (G53, G54, etc\...). The coordinate offset fixtures represent:

-   G53 -\> Machine coordinate system.
-   G54 -\> Scratchpad coordinate system.
-   G55 to G59.9 -\> Coordinate fixtures allowing work offsets, relative to Homing switches located on the CNC machine, to be used.


</div>


<div class="mw-translate-fuzzy">

The G59 Fixture is used to expand available fixtures. The degree of expansion implemented is CNC machine specific, and this command allows provides for G59.1 to G59.9.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Path_Fixture.png" width=16px> [Fissaggio](Path_Fixture/it.md)
**
2.  Impostare il fissaggio desiderato. Seleziona il Fix Offset lavoro desiderato dal menu a tendina.


</div>



## Proprietà

-    **Fixture**: Imposta il punto di fissaggio corrente

-    **Active**: Definisce se questo comando è attivo o meno quando viene inserito in un composto

## Notes

## Limitations

## Scripting


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Fixture/it
