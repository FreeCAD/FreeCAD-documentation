---
 GuiCommand:
   Name: Draft Hatch
   Name/pl: Rysunek Roboczy: Kreskowanie
   MenuLocation: Kreślenie , Kreskowanie
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **H** **A**
   Version: 0.20
   SeeAlso: Draft_Pattern/pl
---

# Draft Hatch/pl



## Opis

Polecenie <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> **Kreskowanie** środowiska Rysunek Roboczy tworzy kreskowanie na powierzchniach planarnych wybranego obiektu.



## Użycie

1.  Wybierz obiekt z powierzchniami. Tylko planarne powierzchnie obiektu zostaną zakreskowane.
2.  Istnieje kilka sposobów, aby wywołać to polecenie:
    -   Naciśnij przycisk **<img src="images/Draft_Hatch.svg" width=16px> '''Kreskowanie'''**.
    -   Wybierz z menu opcję **Kreślenie → <img src="images/Draft_Hatch.svg" width=16px> Kreskowanie**.
    -   Użyj skrótu klawiaturowego: **H**, a następnie **A**.
3.  Otworzy się panel zadań **Kreskowanie**. Zobacz [Opcje](#Opcje.md), aby uzyskać więcej informacji.
4.  Naciśnij przycisk **OK**, aby zakończyć polecenie.



## Opcje

-   Naciśnij przycisk **...**, aby wybrać plik **PAT** z wzorem. Zobacz [Uwagi](#Uwagi.md).
-   Wybierz **Wzór** z pliku. Obecnie zaleca się unikanie wzorów z przerywanymi liniami.
-   Określ **Skalę** dla wzoru.
-   Określ **Obrót** dla wzoru.
-   Naciśnij klawisz **Esc** lub przycisk **Anuluj**, aby przerwać polecenie.



## Wyrównanie wzoru 

Gdy obliczany jest wzór kreskowania dla ściany, domyślnie jest on tymczasowo odwzorowany na globalną płaszczyznę XY. Dla powierzchni z prostymi krawędziami pierwsza prosta krawędź określa, jak to będzie realizowane. Pierwszy punkt tej krawędzi jest umieszczany na początku, a sama krawędź jest wyrównywana do osi X. Jeśli utworzysz [linię łamaną](Draft_Wire/pl.md) z myślą o tym, możesz kontrolować, w jaki sposób wzór kreskowania jest wyrównany do konturu ściany

Jeśli wszystkie powierzchnie wybranego obiektu znajdują się na globalnej płaszczyźnie XY, można wyłączyć to domyślne zachowanie, ustawiając właściwość **Translate** kreskowania projektu na wartość {{FALSE/pl}}. Wzór kreskowania jest wtedy wyrównany do położenia odniesienia i osi X globalnego układu współrzędnych. W przypadku powierzchni na płaszczyźnie XY o prostych krawędziach właściwość **Translate** może być użyta do przełączania między wzorcami bezwzględnymi *(po lewej na obrazku)* i względnymi *(po prawej na obrazku)*.

<img alt="" src=images/Draft_Hatch_alignment.png  style="width:400px;"> 
*
Dwie zakreskowane figury z linii łamanych.<br>.
Figury zostały narysowane w kierunku przeciwnym do ruchu wskazówek zegara, zaczynając od lewego dolnego punktu.<br>
Dla szkicu kreskowania po lewej stronie właściwość Translate jest ustawiona na wartość {{False/pl*.<br>
Dla szkicu kreskowania po prawej stronie jest ona ustawiona na wartość {{True/pl}}.
}}



## Uwagi

-   Na razie radzimy pobrać plik PAT. Wiele z nich można znaleźć w Internecie. Można na przykład wyszukać w sieci **acad.pat** lub **acadiso.pat**.
-   Mały plik PAT jest instalowany z programem FreeCAD: **<program_folder>/data/Mod/TechDraw/PAT/FCPAT.pat**, gdzie **<program_folder>** jest folderem instalacyjnym programu FreeCAD:
    -   W systemie Linux jest to zazwyczaj **/usr/share/freecad**.
    -   W systemie Windows jest to zazwyczaj **C:\Program Files\FreeCAD**.
    -   W systemie macOS jest to zazwyczaj **/Applications/FreeCAD**.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Preferencje](Draft_Preferences/pl.md) środowiska Rysunek Roboczy.

Zastosowanie mają następujące preferencje:

-   Plik PAT: **Przybory → Edycja parametrów → BaseApp → Preferences → Mod → TechDraw → PAT → FilePattern**.
-   Wzór: **Przybory → Edycja parametrów → BaseApp → Preferences → Mod → TechDraw → PAT → NamePattern**.
-   Skala: **Przybory → Edycja parametrów → BaseApp → Preferences → Mod → Draft → HatchPatternScale**.
-   Obrót: **Przybory → Edycja parametrów → BaseApp → Preferences → Mod → Draft → HatchPatternRotation**.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Kreskowanie wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Kreskowanie}}

-    **Podstawowe|Link**: określa obiekt, którego ściany zostaną zakreskowane.

-    **Plik|Plik**: określa plik wzoru PAT.

-    **Wzór|Ciąg znaków**: określa nazwę wzoru.

-    **Obrót|Kąt**: określa obrót wzoru.

-    **Skala|Float**: określa skalę wzoru.

-    **Przesunięcie|Bool**: określa, czy podczas procesu kreskowania powierzchnie są tymczasowo przeliczane na globalną płaszczyznę XY. Ustawienie tej wartości na {{FALSE/pl}} może dać błędne wyniki dla powierzchni innych niż XY.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć kreskowanie, użyj metody `make_hatch` modułu Rysunek Roboczy.


```python
hatch = make_hatch(baseobject, filename, pattern, scale, rotation)
```

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
rectangle.MakeFace = True
filename = App.getHomePath() + "data/Mod/TechDraw/PAT/FCPAT.pat"
pattern = "Horizontal5"
hatch = Draft.make_hatch(rectangle, filename, pattern, scale=50, rotation=45)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Hatch/pl
