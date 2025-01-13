---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/es: Hoja de cálculo Establecer Alias
   MenuLocation: -
   Workbenches: Spreadsheet_Workbench/es
   Shortcut: **Ctrl**+**Shift**+**A**
   Version: 0.17
---

# Spreadsheet SetAlias/es



## Descripción


<div class="mw-translate-fuzzy">

La herramienta **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Hoja de cálculo EstablecerAlias](Spreadsheet_SetAlias/es.md)** abre un cuadro de diálogo para configurar un alias para una celda. En lugar de utilizar el nombre de celda exacto como A2, B3 o C4, se puede utilizar un nombre personalizado.


</div>



## Uso


<div class="mw-translate-fuzzy">

1.  Asegúrese de que haya una **[<img src=images/Spreadsheet_CreateSheet.svg style="width:16px"> [hoja de cálculo](Spreadsheet_CreateSheet/es.md)** activa abierta para que el botón esté habilitado.
2.  Seleccione una celda.
3.  Presione el botón **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Hoja de cálculo EstablecerAlias](Spreadsheet_SetAlias/es.md)**.
4.  Ingrese un alias:
    -   Solo caracteres alfanuméricos y guiones bajos (`A` a `Z`, `a` a `z`, `0` a {{ incode\|9}} y `_`) están permitidos.
    -   El primer carácter debe ser una letra.
    -   No se permite el uso de 1 o 2 letras mayúsculas seguidas de 1 a 5 números, por ejemplo `AB123`, ya que se considera una dirección de celda.
    -   No se permiten secuencias de caracteres que sean unidades. Por ejemplo, `W` es un alias no válido ya que es la unidad de [Watt](https://en.wikipedia.org/wiki/Watt). Dado que FreeCAD admite muchas unidades, es mejor evitar alias cortos. Consulte [Expresiones](Expressions#Units.md).
    -   El uso de las constantes matemáticas `pi` y `e` como alias generará errores y debe evitarse.
    -   No utilice espacios en los alias, ya que también provocarán errores.


</div>





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/es
