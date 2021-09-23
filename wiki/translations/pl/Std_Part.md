---
- GuiCommand:/pl
   Name:Std Part
   Name/pl:Std: Część
   MenuLocation:brak
   Workbenches:wszystkie
   Version:0.17
   SeeAlso:[Grupa](Std_Group.md), [Zawartość](PartDesign_Body/pl.md)
---

# Std Part/pl

## Opis


**<img src=images/Std_Part.svg style="width:16px"> [Std: Część](Std_Part.md)**

*(wewnętrznie nazywany [App: Część](App_Part.md))* jest to uniwersalny kontener, który gromadzi wspólnie grupę obiektów, dzięki czemu można je przesuwać razem jako całość w oknie [widoku 3D](3D_view/pl.md).

Element **Std: Część** został opracowany jako podstawowy element konstrukcyjny do tworzenia [zespołów](Assembly/pl.md) mechanicznych. W szczególności, ma on za zadanie uporządkować obiekty, które mają kształt [części TopoShape](Part_TopoShape/pl.md), jak [Część: Bryły pierwotne](Part_Primitives/pl.md), [Projekt Części: Zawartość](PartDesign_Body/pl.md) i inne [cechy Części](Part_Feature/pl.md). Std: Część dostarcza [obiekt Odniesienie położenia](#Odniesienie_położenia.md) z lokalnymi osiami X, Y i Z oraz płaszczyznami standardowymi, które mogą być używane jako odniesienie do położenia obiektów zamkniętych. Ponadto Std: Część mogą być zagnieżdżone wewnątrz innych Std: Część w celu utworzenia dużego zespołu z mniejszych podzespołów.

Chociaż jest on przeznaczony głównie dla brył, Std: Część może być użyty do zarządzania dowolnym obiektem, który posiada właściwość [Umiejscowienie](Placement/pl.md), więc może również zawierać [cechy siatki](Mesh_Feature/pl.md), [szkice](Sketch/pl.md) i inne obiekty pochodzące z klas [App: GeoFeature](App_GeoFeature.md).

Nie należy mylić elementu **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:Projekt Części: Zawartość](PartDesign_Body/pl.md)** z częścią **[16px"> [Std: Część](Std_Part/pl.md)**. Pierwszym z nich jest określony obiekt używany w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), przeznaczony do modelowania [pojedynczej, ciągłej bryły](PartDesign_Body/pl#Single_contiguous_solid.md) za pomocą funkcji [właściwości](PartDesign_Feature.md). Z drugiej strony [Std: Część](Std_Part/pl.md) nie jest używana do modelowania, a jedynie do rozmieszczania różnych obiektów w przestrzeni z zamiarem tworzenia [złożeń](assembly.md).

Narzędzie **<img src=images/Std_Part.svg style="width:16px"> <img src=images/Std_Group.svg style="width:Std: Część](Std_Part/pl.md)** nie jest zdefiniowane przez konkretne środowisko pracy, lecz przez system bazowy, a więc znajduje się na pasku **narzędzi struktury**, który jest dostępny we wszystkich [Środowiskach pracy.](Workbenches/pl.md) Aby dowolnie grupować obiekty bez względu na ich położenie, należy użyć funkcji **[16px"> [Std: Group](Std_Group.md)**. Obiekt ten nie ma wpływu na rozmieszczenie elementów, które zawiera, w zasadzie jest to tylko folder, który jest używany do utrzymania widoku drzewa w sposób zorganizowany.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )


*Z lewej: elementy wewnątrz Std: Część w [widoku drzewa](Tree_view/pl.md). <br>Z prawej: obiekty umieszczone w przestrzeni, odnoszące się do pochodzenia ''(Origin)'' Std: Część.*

## Użycie

1.  Naciśnij przycisk **<img src=images/Std_Part.svg style="width:16px"> [Std: Część](Std_Part/pl.md)**. Zostanie utworzona pusta część, która automatycznie stanie się *[aktywna](Std_Part/pl#Status_aktywności.md)*.
2.  Aby dodać obiekty do nowo utworzonej pozycji Części, zaznacz ją w [widoku drzewa](Tree_view/pl.md), a następnie przeciągnij je i upuść nad Częścią.
3.  Aby usunąć obiekty z części, przeciągnij je poza część, na etykietę dokumentu u góry [widoku drzewa](Tree_view/pl.md).

## Uwagi

-   Od wersji programu v0.19, dany obiekt może należeć tylko do jednej pozycji Części.
-   Kliknij dwukrotnie w pozycję Część w [widoku drzewa](Tree_view/pl.md) lub otwórz menu kontekstowe *(klikając prawym przyciskiem myszy)* i wybierz **Przełącz aktywność części** aby uaktywnić lub dezaktywować wybraną Część. Jeśli aktywna jest inna część, jej aktywność zostanie wyłączona. Aby uzyskać więcej informacji, zobacz akapit [status aktywności](Std_Part/pl#Status_aktywności.md).

## Ograniczenia

-   Aktualnie metody [Draft: Przyciąganie](Draft_Snap/pl.md) nie działają na wybranych kontenerach części ani na obiektach znajdujących się wewnątrz nich.
-   Część nie ma kształtu topologicznego, dlatego też operacje przestrzenne, takie jak [Część: Działania logiczne na bryłach](Part_Boolean/pl.md), nie mogą być bezpośrednio użyte na samej części. Na przykład nie można wybrać dwóch Części i wykonać za ich pomocą operacji [Część: Suma](Part_Fuse/pl.md) lub [Część: Wytnij](Part_Cut/pl.md).
    -   Te operacje logiczne działają tylko na zawartych obiektach, o ile pochodzą one z obiektu [Część: funkcjonalność](Part_Feature/pl.md) i mają [kształt topologiczny](Part_TopoShape/pl.md).

## Właściwości

[Std: Część](Std_Part/pl.md) jest wewnętrznie nazywana [App: Part](App_Part.md) *(klasa App::Part)*, i pochodzi z [App: GeoFeature](App_GeoFeature.md) *(klasa App::GeoFeature)*, dlatego też posiada większość właściwości tej ostatniej.

Oprócz właściwości opisanych w [App: GeoFeature](App_GeoFeature.md), klasa App Part posiada pewne właściwości, które pomagają w zarządzaniu informacjami w kontekście zespołu, na przykład: **Typ**, **Id**, **Licencja**, **LicencjaURL**, **Kolor**, oraz **Grupa**.

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).

### Dane


{{TitleProperty|Podstawowe}}

-    **Typ|String**: opis dla obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Id|String**: numer identyfikacyjny lub numer części dla obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Licencja|String**: pole do określenia licencji dla obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **LicencjaURL|String**: pole do podania adresu strony internetowej z licencją lub umową dla tego obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Kolor|Color**: tupla czterech zmiennoprzecinkowych wartości RGBA white color.

-    **Umieszczenie|Placement**: ustawienie obiektu w oknie [widoku 3D](3D_view.md). Umieszczenie jest określone przez punkt *(wektor)* `Baza` i `Obrót` *(oś i kąt)*. Patrz: [Umiejscowienie](Placement.md).

    -   
        **Kąt**
        
        : kąt obrotu wokół **Osi**. Domyślnie jest to {{value|0°}} *(zero stopni)*.

    -   
        **Oś**
        
        : wektor jednostkowy, który określa oś obrotu dla położenia. Każdy komponent jest wartością zmiennoprzecinkową pomiędzy {{value|0}} a {{value|1}}. Jeśli jakaś wartość znajduje się powyżej {{value|1}}, wektor jest normalizowany tak, że jego wielkość wynosi {{value|1}}. Domyślnie ustawiono dodatnią oś Z, {{value|(0, 0, 1)}}.

    -   
        **Pozycja**
        
        : wektor ze współrzędnymi przestrzennymi punktu bazowego. Domyślnie, jest to punkt startowy {{value|(0, 0, 0)}}.

-    **Etykieta|String**: edytowalna przez użytkownika nazwa obiektu, jest to dowolny ciąg znaków w standardzie UTF8.

-    **Grupa|LinkList**: lista obiektów, których dotyczą odniesienia. Domyślnie jest pusta {{value|[]}}.

#### Dane Właściwości ukryte 

-    **Materiał|Map**: mapa z właściwościami materiałów. Domyślnie jest ona pusta {}.

-    **Meta|Map**: mapa z dodatkowymi meta informacjami. Domyślnie jest ona pusta {}.

-    **Uid|UUID**: [uniwersalny identyfikator](https://en.wikipedia.org/wiki/Universally_unique_identifier) *(UUID)* *(128-bitowy numer)* obiektu. Numer ten jest przypisywany podczas tworzenia obiektu.

-    **Etykieta2|String**: dłuższy, edytowalny przez użytkownika opis tego obiektu. Jest to dowolny ciąg znaków w standardzie UTF8, który może zawierać nowe linie. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Silnik wyrażenia|ExpressionEngine**: lista wyrażeń. Domyślnie, jest ona pusta {{value|[]}}.

-    **Widoczność|Bool**: parametr określający czy obiekt ma być widoczny, czy też nie.

-    **Origin|Link**: the [App: Origin](App_Origin.md) obiekt, który jest odniesieniem położenia dla wszystkich elementów wymienionych w **Grupie**.

-    **_ Grupa Dotknięta|Bool**: parametr określający czy grupa jest wzruszona, czy też nie.

### Widok

App: Część ma tylko pięć podstawowych właściwości [App: FeaturePython](App_FeaturePython.md), i nie ma właściwości ukrytych.


{{TitleProperty|Podstawowe}}

-    **Tryb wyświetlania|Enumeration**: {{value|Grupa}}.

-    **Na górze po wybraniu|Enumeration**: {{value|Wyłączone}} *(domyślnie)*, {{value|Włączone}}, {{value|Obiekt}}, {{value|Element}}.

-    **Styl wyboru|Enumeration**: {{value|Kształt}} *(domyślnie)*, {{value|Pole ograniczające}}. Jeśli wartość opcji jest następująca {{value|Kształt}}, cały kształt *(wierzchołki, krawędzie i powierzchnie)* zostanie podświetlony w oknie [widoku 3D](3D_view/pl.md). Jeśli wybrano wartość {{value|Pole ograniczające}}, to tylko ramka ograniczająca zostanie podświetlona.

-    **Pokaż w drzewku|Bool**: Jeśli ustawiono wartość `True`, obiekt pojawia się w [widoku drzewa](Tree_view.md). W przeciwnym razie, jest on określony jako niewidoczny.

-    **Widoczność|Bool**: Jeśli ustawiono wartość `True`, obiekt pojawia się w oknie [widoku 3D](3D_view/pl.md). W przeciwnym razie będzie niewidoczny. Domyślnie, właściwość ta, może być włączana i wyłączana, poprzez naciśnięcie klawisza **Spacja** na klawiaturze.

## Koncepcja złożeń 

Std: Część ma być podstawowym elementem konstrukcyjnym do tworzenia złożeń. W przeciwieństwie do [Projekt części: Zawartość](PartDesign_Body/pl.md), zespół ma być zbiorem oddzielnych, rozróżnialnych elementów, które są w jakiś sposób połączone w świecie fizycznym, na przykład za pomocą nacisku, śrub lub kleju.

Przykłady, które mogą być częściami:

-   Drewniany stół, który składa się z pojedynczych drewnianych przedmiotów *(nóg, blatu)*, które są łączone za pomocą kleju lub metalowych wkrętów.
-   Łożysko kulkowe, które składa się z wielu stalowych kulek, pierścienia wewnętrznego, koszyka, uszczelki i pierścienia zewnętrznego.
-   Zespół śruby z podkładką i odpowiednią nakrętką.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Z lewej: trzy pojedyncze sąsiadujące bryły, z których każda została wymodelowana za pomocą obiektu [Projekt Części: Zawartość](PartDesign_Body/pl.md). <br> Z prawej: poszczególne bryły złożone razem w Std: Część, aby utworzyć zespół.*

Ogólnie rzecz biorąc, podczas importowania pliku STEP do programu, główny zespół i jego podzespoły będą importowane jako kontenery części, a każdy z nich będzie zawierał podstawową [funkcjonalność części](Part_Feature/pl.md).

## Szczegółowe wyjaśnienia 

### Status aktywności 

Otwarty dokument może zawierać wiele części. Aktywna Część zostanie wyświetlona w [widoku drzewa](Tree_view/pl.md) przy zastosowaniu koloru tła określonego w [edytorze preferencji](Preferences_Editor/pl#Kolory.md) przez wartość **Aktywny kontener** *(domyślnie, jasnoniebieski)*. Etykieta aktywnej części zostanie również wyświetlona pogrubionym tekstem.

Aby uaktywnić lub dezaktywować Część:

-   Kliknij dwukrotnie na jej pozycję w [widoku drzewa](Tree_view/pl.md), lub
-   Otwórz menu kontekstowe *(klikając prawym przyciskiem myszy)* i wybierz **Przełącz aktywność części**.


**Uwagi:**

-    {{emphasis|Aktywny status}}Części opracowano w v0.17 równolegle z {{emphasis|aktywnym statusem}} [Projekt części: Zawartość](PartDesign_Body.md), jednakże od v0.19 status ten nie ma rzeczywistego przeznaczenia dla Części.

-   Nawet gdy część jest aktywna, nowo wytworzone obiekty nie są automatycznie umieszczane w jej wnętrzu. W tym przypadku, po prostu przeciągnij wybrane nowe obiekty i upuść je do żądanej Części.

-   W danym momencie może być aktywna tylko pojedyncza Część.

![](images/Std_Part_active.png )


*Dokument z dwiema Częściami Std, wśród których aktywna jest druga część.*

### Odniesienie położenia 

Początek układu współrzędnych składa się z trzech standardowych osi *(X, Y, Z)* oraz trzech standardowych płaszczyzn *(XY, XZ i YZ)*. [Szkic](Sketch/pl.md) i inne obiekty mogą być dołączone do tych elementów w trakcie ich tworzenia.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )


*Z lewej: Początek układu współrzędnych Części w [widoku drzewa](Tree_view/pl.md). <br>Z prawej: reprezentacja początku układu współrzędnych w oknie [widoku 3D](3D_view/pl.md).*


**Uwaga:**

Początek układu współrzędnych jest obiektem [App Origin](App_Origin.md) *(klasa `App::Origin`)*, podczas gdy osie i płaszczyzny są obiektami odpowiednio typu `App::Line` oraz `App::Plane`. Każdy z tych elementów może być ukryty i nieujawniany indywidualnie przy użyciu klawisza **spacja**. Jest to przydatne przy tworzeniu innych obiektów, aby wybrać właściwe odniesienie.


**Uwaga 2:**

Wszystkie elementy składowe Części są powiązane z jej początkiem, co oznacza, że Część może być przesuwana i obracana w odniesieniu do globalnego układu współrzędnych, bez wpływu na rozmieszczenie jej elementów składowych.

### Zarządzanie wyświetlaniem 

Parametr wyświetlania Części ma pierwszeństwo określania wyświetlania dowolnego obiektu, który zawiera. Jeśli wyświetlanie Części zostanie ukryte, to obiekty, które zawiera będą również ukryte, nawet jeśli ich indywidualna właściwość {{PropertyView/pl|Widoczność}} jest ustawiona na `True`. Jeśli Część jest widoczna, to właściwość każdego obiektu **Widoczność** określa, czy obiekt jest prezentowany na ekranie okna [widoku 3D](3D_view/pl.md) czy nie.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) *Parametr widoczności Std Części określa, czy zgrupowane pod nią obiekty są prezentowane w oknie [widoku 3D](3D_view/pl.md), czy też nie. <br>Po lewej: Część została ukryta, więc żaden z obiektów nie będzie widoczny w oknie [widoku 3D](3D_view/pl.md). <br>Po prawej: Część jest widoczna, więc każdy obiekt kontroluje indywidualnie swoje właściwości w zakresie wyświetlania.*

### Dziedziczenie

Obiekt [Std: Część](Std_Part/pl.md) jest formalnie instancją klasy `App::Part`, której rodzicem jest podstawowa klasa [App GeoFeature](App_GeoFeature/pl.md) *(`App::GeoFeature`)*, i jest wzbogacona o rozszerzenie Origin.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Uproszczony schemat relacji między głównymi obiektami w programie. Klasa `App::Part* jest prostym kontenerem, który ma swoją pozycję w przestrzeni 3D i posiada zdefiniowany punkt początku w układzie współrzędnych ''(Origin)'', kontrolujący położenie zgrupowanych pod nim obiektów.`

## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty tworzone skryptami](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć w [Część: właściwość](Part_Feature/pl.md).

Element Std: Part ([App Part](App_Part.md)) jest tworzony przy pomocy metody `addObject()` dokumentu. Gdy istnieje element Part, inne obiekty mogą być do niego dodane za pomocą metod `addObject()` lub `addObjects()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::Part", "Part")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

Nie można utworzyć skryptu `App::Part`. Można jednak dodać zachowanie `App::Part` do obiektu skryptowego `Part::FeaturePython` za pomocą następującego kodu:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension('App::OriginGroupExtensionPython')
        obj.Origin = FreeCAD.ActiveDocument.addObject('App::Origin', 'Origin')

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension('Gui::ViewProviderOriginGroupExtensionPython')
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject('Part::FeaturePython', 'Group', group.MyGroup(), group.ViewProviderMyGroup(), True)
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Part/pl
