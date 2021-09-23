# Macro Loft/cs
{{Macro
|Name=Macro Loft
|Icon=FCCreaLoft.png
|Description=Vytvoří vybrané dráty s loft wit.
|Author=Mario52
|Version=00.04
|Date=2019-07-03
|Download=[https://www.freecadweb.org/wiki/images/2/29/FCCreaLoft.png ToolBar Icon]
|SeeAlso= [32px|FCTexture](File:FCTexture.png.md) [Macro_Texture](Macro_Texture/cs.md)
|FCVersion=All
}}

## Popis

speciálně napsané pro snadné lofting s liniemi vytvořenými [ Macro Texture](Macro_Texture/cs.md) (ale mohou být vhodné a použity pro společné loft)
{{Codeextralink|https://gist.githubusercontent.com/mario52a/c477f892233d6abe02df5e97af828ff4/raw/d633193c577e8257ef458b8c1824d1047c3c6613/Macro_FCCreaLoft.FCMacro}}

<img alt="" src=images/Texture_001_Logo.png  style="width:480px;"> 
*Texture_001_Logo*


<div class="mw-translate-fuzzy">

## Použijte

Zkopírujte makro a ikonu do adresáře maker.


</div>

-   ****Sort |****: Třídit položky dat.
-   ****Reverse****: Obrácení pořadí dat.
-   \'\'\' **Reset** / **Upgrade** \'\'\': Toto tlačítko tolik funkcí:
-   \# Je-li výběr v 3D zobrazen, zobrazí se toto tlačítko **Upgrade**.
    Vyberte objekt v zobrazení 3Dview nebo Combo a klepnutím na toto tlačítko aktualizujete údaje v makru, změní se tlačítko **Reset**.
-   \# Je-li vybrán jeden nebo více objektů před spuštěním makra, zobrazí se toto tlačítko **Reset**.
    V okně makra jsou zobrazeny všechny vybrané objekty. \'Třídit**\'nebo** Obrátit \'\' zobrazené údaje, toto tlačítko **Reset** se používá k návratu k původní objednávce.
    Pokud kliknete na 3DView nebo nevyberete všechny objekty tlačítko se používá pro reset na makro.
    Pokud přidáváte jeden nebo více objektů v seznamu, použije se toto tlačítko.
-   ****Select all****: Vyberte všechny objekty v dokumentu.
-   **SpinBox**: Zvyšte skok x Elements (výchozí 1 všechny objekty jsou používány).
-   ****Quit****: Ukončete makro.
-   **CheckBox** Pokud je CheckBox zaškrtnuto, zobrazí se průběh práce, pokud není pouze práce ProgressBar (tato metoda je rychlejší) (ve výchozím nastavení je zaškrtnuto).
-   ****Launch the Lofting****: Spusťte Lofting a resetujte makro. Zobrazí se číslo výběru a reálné číslo se zvýší, pokud se použije skok spinBoxu

### Rozhraní

<img alt="FCCreaLoft002" src=images/Macro_FCCreaLoft_01.png  style="width:400px;"> 

## Skript

Ikony pro nástroj Toolbar <img alt="" src=images/FCCreaLoft.png  style="width:64px;">

Stáhněte makro na Gist [**Macro\_FCCreaLoft.FCMacro**](https://gist.github.com/mario52a/c477f892233d6abe02df5e97af828ff4)

## Odkazy

Diskuse na fóru [Texture](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893&start=10)

The [Macro Texture](Macro_Texture/cs.md)

## Verze

ver 00.00 : 06/02/2016

ver 00.02 : 09/02/2016 : Add button \"Select all\" and little option displayed in the button Launch (number selections) and (real number loft)

ver 00.03 : 09/02/2016 : minor (display on button)

ver 00.04 : 03/07/2019 : adapt to Python 3

---
[documentation index](../README.md) > Macro Loft/cs
