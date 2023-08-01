# Arch Survey/cs
---
- GuiCommand:   Name: Arch Survey   Name/cs: Architektura Přehled    Workbenches: [MenuLocation: Arch - Survey   SeeAlso: [[Macro FCInfo/cs|FcInfo (macro)](Arch_Workbench/cs___Architektura]].md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Přehled spustí speciální přehledový mód, který umožňuje rychle zjistit rozměry a informace z modelu a přenést tyto informace do jiných aplikací. Když už jste v přehledovém módu, kliknutí na jiný subelement 3D objektu posbírá následující informace v závislosti na co jste klikli:


</div>

-   Jestli jste klikli na hranu, dostanete její délku
-   Jestli jste klikli na vrchol, dostanete jeho výšku (souřadnici na ose Z)
-   Jestli jste klikli na plochu, dostanete její plošnou výměru
-   Jestli dvojkliknete na cokoliv, vyberete celý objekt a dostanete jeho objem

Když jsou informace posbírány, stanou se 3 věci:

-   Nad element je umístěno návěští, které zobrazuje hodnotu (s \"a\" pro plochu, \"l\" pro délku, \"z\" pro výšku nebo \"v\" pro objem)
-   Numerická hodnota je zkopírována do schránky, takže ji můžete vložit do jiné aplikace
-   Ve výstupním okně FreeCADu je vytištěn řádek. Po ukončení přehledového módu mohou být tyto řádky zkopírovány a následně vloženy do jiné aplikace (hodnoty jsou odděleny čárkou, což usnadňuje jejich přenos do tabulkového programu)

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*Obrázek nahoře ukazuje co se stane při spuštění přehledového módu.*


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Stiskněte tlačítko **<img src="images/Arch_Survey.png" width=16px> [Architektura Přehled](Arch_Survey/cs.md)
**
2.  Klikejte na vrcholy, hrany, plochy nebo dvojklikněte pro výběr celého objektu
3.  Stiskněte klávesu**ESC** nebo tlačítko **'''Zrušit'''** pro ukončení přehledového módu a odstranění všech návěští.


</div>

## Options

-   You can add a custom label to any line in the Task dialog by clicking that line, then adding a text in the description field, then press the **set description** button.
-   Once you are done, before closing, you can export the contents of the Task dialog by pressing the \"export CSV\" button. The resulting CSV file can then be opened in any spreadsheet application such as Excel or LibreOffice Calc. The values and units will be separated in the resulting CSV file, and the totals are written as SUM() functions.

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Přehledový mód nemůže být použit přímo ze skriptů Pythonu, ale získání stejných informací z jakéhokoliv objektu založeného na [Dílu](Part_Workbench/cs.md) je snadno reprodukovatelné podle následujícího skriptu:


</div>


```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Survey/cs
