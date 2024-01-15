---
 GuiCommand:
   Name: SheetMetal AddCornerRelief
   Name/pl: Arkusz Blachy: Dodaj podcięcie narożnika
   MenuLocation: SheetMetal , Dodaj podcięcie narożnika
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **C** **R**
---

# SheetMetal AddCornerRelief/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> **Dodaj podcięcie narożnika** dodaje podcięcie w narożniku. Podcięcie jest zwykle tworzone w narożnikach, w których spotykają się dwa zagięcia, ale polecenie może również utworzyć podcięcie w otwartym narożniku.

Polecenie może utworzyć tylko jedno podcięcie naraz.

<img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width:300px;"> 
*Domyślny narożnik z dwoma zagięciami → Narożnik z dodatkowym podcięciem narożnym.*

<img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width:300px;"> 
*Domyślny otwarty narożnik → Otwarty narożnik z dodatkowym podcięciem.*



## Użycie

1.  Wybierz jedną lub więcej krawędzi.
2.  Aktywuj polecenie <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> **Wykonaj podcięcie narożnika** używając jednej z poniższych opcji:
    -   Przycisk **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Wykonaj podcięcie narożnika**.
    -   Opcja menu **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Wykonaj podcięcie narożnika**.
    -   Skrót klawiaturowy: **C** + **R**.



## Kształt podcięcia 

Kształt narożnego podcięcia można zmienić, zmieniając wartości jego właściwości:

Wartość właściwości **SzkicPodcięcia** może być wybrana z listy: {{value|Okrąg}} (domyślnie), {{value|Skalowany-Okrąg}}, {{value|Kwadrat}}, {{value|Skalowany-Kwadrat}}, {{value|Szkic}}.

-    {{value|Okrąg}}i {{value|Kwadrat}} używają wartości właściwości **Rozmiar** do skalowania podcięcia.

-    {{value|Skalowany-Okrąg}}i {{value|Skalowany-Kwadrat}} używają wartości właściwości **Współczynnik rozmiaru** do skalowania podcięcia.

-    {{value|Szkic}}aktywuje użycie szkicu wymienionego we właściwości **Szkic** do zdefiniowania kształtu podcięcia.

<img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width:200px;"> 
*Podcięcie okrągłe ''(ustawienia domyślne)'' → Podcięcie kwadratowe ''(ustawienia domyślne)'' → Podcięcie oparte na szkicu*



## Bliższe spojrzenie na rozmiary podcięć 

Aby zorientować się, jak i gdzie umieszczone jest podcięcie, rozkładamy domyślny narożnik bez podcięcia.

<img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width:200px;">



*Domyślny narożnik z dwoma zagięciami → Narożnik z rozwiniętą bryłą → Narożnik w widoku z góry.*

Następnym krokiem jest otwarcie rozwiniętego szkicu, utworzenie okręgu przez trzy punkty i dodanie wymiaru promienia.
Teraz dodajemy narożne podcięcie, tworzymy odpowiednią rozwiniętą bryłę i ponownie otwieramy pierwszy rozwinięty szkic.
Dodanie koncentrycznego okręgu o promieniu {{Value|3 mm}} pokazuje, że dowiedzieliśmy się, jak umieszczony jest wewnętrzny okrąg, ponieważ nowy okrąg idealnie pasuje do wycięcia rozwiniętej bryły z podcięciem.

<img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width:300px;">



*Domyślny narożnik z rozłożonym szkicem → Narożnik z domyślnym podcięciem i tym samym rozłożonym szkicem.*

Próba ustawienia właściwości **Rozmiar** na wartość poniżej określonego {{Value|1,67 mm}} spowoduje błąd. Każda wartość powyżej powinna działać poprawnie.

Przełączenie na Skalowany-Okrąąg i utworzenie kolejnej rozwiniętej bryły pokazuje, że {{Value|1,67 mm}} jest również podstawą dla właściwości **Współczynnik rozmiaru**.



## Uwagi

-   Współczynnik **k** określa, gdzie w grubości arkusza znajduje się oś neutralna.

*(Dobrze byłoby wiedzieć, czy współczynnik ten jest zgodny ze standardem ISO czy ANSI \...)*



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Podcięcia narożnika środowiska Arkusz Blachy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Cecha bazowa|Link|hidden**: Cecha bazowa. Łącze do cechy nadrzędnej.

-    **_Body|LinkHidden|hidden**: Ukryte łącze do elementu nadrzędnego.


{{Properties_Title|Parametry}}

-    **SzkicPodcięcia|Enumeration**: *Typ podcięcia narożnika* {{value|Okrąg}} (domyślnie), {{value|Skalowany-Okrąg}}, {{value|Kwadrat}}, {{value|Skalowany-Kwadrat}}, {{value|Szkic}}.

-    **Rozmiar|Length**: *Rozmiar kształtu*. Wartość domyślna: {{value|3,00 mm}}.

-    **Współczynnik rozmiaru|Float**: *Współczynnik rozmiaru kształtu*. Wartość domyślna: {{value|1,50}}.

-    **Obiekt bazowy|LinkSub**: *Obiekt bazowy*. Łącza do pary krawędzi definiujących pozycję Podcięcia Narożnika.

-    **WspółczynnikK|FloatConstraint**: *Pozycja osi neutralnej*. Wartość domyślna: {{value|0,50}}.


{{Properties_Title|Parametry1}}

-    **Szkic|Link**: *Szkic podcięcia narożnika*.

-    **OdsunięcieX|Distance**: *Szczelina od strony pierwszej*. Wartość domyślna: {{value|0,00 mm}}.

-    **OdsunięcieY|Distance**: *Szczelina od strony drugiej*. Wartość domyślna: {{value|0,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/pl
