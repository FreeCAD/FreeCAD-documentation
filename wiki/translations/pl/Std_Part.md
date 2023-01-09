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


**[<img src=images/Std_Part.svg style="width:16px"> [Std: Część](Std_Part.md)**

*(wewnętrznie nazywany [App: Część](App_Part.md))* jest to uniwersalny kontener, który gromadzi wspólnie grupę obiektów, dzięki czemu można je przesuwać razem jako całość w oknie [widoku 3D](3D_view/pl.md).

Element **Std: Część** został opracowany jako podstawowy element konstrukcyjny do tworzenia [zespołów](Assembly/pl.md) mechanicznych. W szczególności, ma on za zadanie uporządkować obiekty, które mają kształt [części TopoShape](Part_TopoShape/pl.md), jak [Część: Bryły pierwotne](Part_Primitives/pl.md), [Projekt Części: Zawartość](PartDesign_Body/pl.md) i inne [cechy Części](Part_Feature/pl.md). Std: Część dostarcza [obiekt Odniesienie położenia](#Odniesienie_położenia.md) z lokalnymi osiami X, Y i Z oraz płaszczyznami standardowymi, które mogą być używane jako odniesienie do położenia obiektów zamkniętych. Ponadto Std: Część mogą być zagnieżdżone wewnątrz innych Std: Część w celu utworzenia dużego zespołu z mniejszych podzespołów.

Chociaż jest on przeznaczony głównie dla brył, Std: Część może być użyty do zarządzania dowolnym obiektem, który posiada właściwość [Umiejscowienie](Placement/pl.md), więc może również zawierać [cechy siatki](Mesh_Feature/pl.md), [szkice](Sketch/pl.md) i inne obiekty pochodzące z klas [App: GeoFeature](App_GeoFeature.md).

Nie należy mylić elementu **[<img src=images/PartDesign_Body.svg style="width:16px"> [Projekt Części: Zawartość](PartDesign_Body/pl.md)** z częścią **[<img src=images/Std_Part.svg style="width:16px"> [Std: Część](Std_Part/pl.md)**. Pierwszym z nich jest określony obiekt używany w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), przeznaczony do modelowania [pojedynczej, ciągłej bryły](PartDesign_Body/pl#Single_contiguous_solid.md) za pomocą funkcji [właściwości](PartDesign_Feature.md). Z drugiej strony [Std: Część](Std_Part/pl.md) nie jest używana do modelowania, a jedynie do rozmieszczania różnych obiektów w przestrzeni z zamiarem tworzenia [złożeń](assembly.md).

Narzędzie **[<img src=images/Std_Part.svg style="width:16px"> [Std: Część](Std_Part/pl.md)** nie jest zdefiniowane przez konkretne środowisko pracy, lecz przez system bazowy, a więc znajduje się na pasku **narzędzi struktury**, który jest dostępny we wszystkich [Środowiskach pracy.](Workbenches/pl.md) Aby dowolnie grupować obiekty bez względu na ich położenie, należy użyć funkcji **[<img src=images/Std_Group.svg style="width:16px"> [Std: Group](Std_Group/pl.md)**. Obiekt ten nie ma wpływu na rozmieszczenie elementów, które zawiera, w zasadzie jest to tylko folder, który jest używany do utrzymania widoku drzewa w sposób zorganizowany.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Z lewej: elementy wewnątrz Std: Część w [widoku drzewa](Tree_view/pl.md). <br>Z prawej: obiekty umieszczone w przestrzeni, odnoszące się do odniesienia położenia Std: Części.*



## Użycie

1.  Naciśnij przycisk **[<img src=images/Std_Part.svg style="width:16px"> [Utwórz Część](Std_Part/pl.md)**.
2.  Zostanie utworzona pusta część, która automatycznie stanie się *[aktywna](Std_Part/pl#Status_aktywności.md)*.
3.  Aby dodać obiekty do nowo utworzonej pozycji Części, zaznacz ją w [widoku drzewa](Tree_view/pl.md), a następnie przeciągnij je i upuść nad Częścią.
4.  Aby usunąć obiekty z części, przeciągnij je poza część, na etykietę dokumentu u góry [widoku drzewa](Tree_view/pl.md).
5.  Obiekty można także dodawać i usuwać, edytując właściwość **Grupa** części.



## Uwagi

-   Dany obiekt może należeć tylko do jednej pozycji Części.
-   Operacje 3D, takie jak [operacje logiczne](Part_Boolean/pl.md) środowiska Część, nie mogą być stosowane do części. Na przykład nie można wybrać dwóch części i wykonać operacji [Scalenie](Part_Fuse/pl.md) lub [Cięcie](Part_Cut/pl.md).



## Właściwości

[Std: Część](Std_Part/pl.md) jest wewnętrznie nazywana [App: Part](App_Part.md) *(klasa App::Part)*, i pochodzi z [App: GeoFeature](App_GeoFeature.md) *(klasa App::GeoFeature)*, ioraz dziedziczy wszystkie jego właściwości. Posiada również kilka dodatkowych właściwości. W szczególności właściwości, które pomagają zarządzać informacjami w kontekście złożenia, na przykład **Typ**, **Id**, **Licencja**, **LicencjaURL** i **Grupa**.

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawowe}}

-    **Typ|String**: opis dla obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Materiał|Link**: materiał wybrany dla tego obiektu.

-    **Meta|Map|Ukryte**: wprowadza dodatkowe informacje meta. Domyślnie jest ona pusta. {}.

-    **Id|String**: numer identyfikacyjny lub numer części dla obiektu. Domyślnie jest to pusty łańcuch znaków {{value|""}}.

-    **Uid|UUID|Hidden**: [uniwersalny, niepowtarzalny identyfikator](https://en.wikipedia.org/wiki/Universally_unique_identifier) *(UUID)* *(liczba 128-bitowa)* obiektu. Jest on nadawany w czasie tworzenia.

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

-    **Etykieta2|String|Ukryte**: dłuższy, edytowalny przez użytkownika opis tego obiektu, jest to dowolny ciąg znaków UTF8, który może zawierać znaki nowej linii. Domyślnie jest to pusty łańcuch {{value|""}}.

-    **Silnik wyrażeń|ExpressionEngine|Ukryte**: lista wyrażeń. Domyślnie jest ona pusta {{value|[]}}.

-    **Widoczność|Bool|Ukryte**: określa, czy obiekt ma być wyświetlany, czy nie.

-    **Odniesienie położenia|Link|Ukryte**: obiekt [App: Odniesienie położenia](App_OriginGroupExtension/pl.md), który jest pozycyjnym odniesieniem dla wszystkich elementów wymienionych w **Grupie**.

-    **Grupa|LinkList**: lista obiektów, których dotyczą odniesienia. Domyślnie jest pusta {{value|[]}}.

-    **_ Group Touched|Bool|Ukryte**: określa czy grupa jest poddana edycji, czy nie.



### Widok


{{TitleProperty|Opcje wyświetlania}}

-    **Tryb wyświetlania|Enumeration**: {{value|Grupa}}.

-    **Wyświetl w drzewie|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt pojawia się w widoku [Widok drzewa](Tree_view/pl.md). W przeciwnym razie jest on niewidoczny..

-    **Widoczność|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt pojawia się w oknie [widoku 3D](3D_view/pl.md). W przeciwnym razie jest niewidoczny. Domyślnie właściwość ta może być włączana i wyłączana przez naciśnięcie klawisza **Spacja** na klawiaturze.


{{TitleProperty|Wybieranie}}

-    **Na wierzchu po wybraniu|Enumeration**: {{value|Wyłączone}} *(domyślnie)*, {{value|Wyłączone}}, {{value|Objekt}}, {{value|Element}}.

-    **Styl wyboru|Enumeration**: {{value|Kształt}} *(domyślnie)*, {{value|BoundBox}}. Jeśli opcja ma wartość {{value|Kształt}}, cały kształt *(wierzchołki, krawędzie i ściany)* zostanie podświetlony w oknie [widoku 3D](3D_view/pl.md). Jeśli wartość to {{value|Ramka otaczająca}}, podświetlone zostanie tylko pole ograniczające.



## Szczegółowe wyjaśnienia 



### Status aktywności 

Otwarty dokument może zawierać wiele części. Ale tylko jedna Część może być aktywna. Aktywna Część zostanie wyświetlona w [widoku drzewa](Tree_view/pl.md) przy zastosowaniu koloru tła określonego w [edytorze preferencji](Preferences_Editor/pl#Kolory.md) przez wartość **Aktywny kontener** *(domyślnie, jasnoniebieski)*. Etykieta aktywnej części zostanie również wyświetlona pogrubionym tekstem.

Aby uaktywnić lub dezaktywować Część:

-   Kliknij dwukrotnie na jej pozycję w [widoku drzewa](Tree_view/pl.md), lub
-   Otwórz menu kontekstowe *(klikając prawym przyciskiem myszy)* i wybierz **Przełącz aktywność części**.

![](images/Std_Part_active.png )



*Dokument z dwiema Częściami Std, wśród których aktywna jest druga część.*



### Odniesienie położenia 

Początek układu współrzędnych składa się z trzech standardowych osi *(X, Y, Z)* oraz trzech standardowych płaszczyzn *(XY, XZ i YZ)*. [Szkic](Sketch/pl.md) i inne obiekty mogą być dołączone do tych elementów w trakcie ich tworzenia.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Z lewej: Początek układu współrzędnych Części w [widoku drzewa](Tree_view/pl.md). <br>Z prawej: reprezentacja początku układu współrzędnych w oknie [widoku 3D](3D_view/pl.md).*


**Uwaga:**

Początek układu współrzędnych jest obiektem [App: Odniesienie położenia](App_OriginGroupExtension.md) *(klasa `App::Origin`)*, podczas gdy osie i płaszczyzny są obiektami odpowiednio typu `App::Line` oraz `App::Plane`. Każdy z tych elementów może być ukryty i nieujawniany indywidualnie przy użyciu klawisza **spacja**. Jest to przydatne przy tworzeniu innych obiektów, aby wybrać właściwe odniesienie.


**Uwaga 2:**

Wszystkie elementy składowe Części są powiązane z jej początkiem, co oznacza, że Część może być przesuwana i obracana w odniesieniu do globalnego układu współrzędnych, bez wpływu na rozmieszczenie jej elementów składowych.



### Zarządzanie wyświetlaniem 

Parametr wyświetlania Części ma pierwszeństwo określania wyświetlania dowolnego obiektu, który zawiera. Jeśli wyświetlanie Części zostanie ukryte, to obiekty, które zawiera będą również ukryte, nawet jeśli ich indywidualna właściwość {{PropertyView/pl|Widoczność}} jest ustawiona na `True`. Jeśli Część jest widoczna, to właściwość każdego obiektu **Widoczność** określa, czy obiekt jest prezentowany na ekranie okna [widoku 3D](3D_view/pl.md) czy nie.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*Parametr widoczności Std Części określa, czy zgrupowane pod nią obiekty są prezentowane w oknie [widoku 3D](3D_view/pl.md), czy też nie. <br>Po lewej: Część została ukryta, więc żaden z obiektów nie będzie widoczny w oknie [widoku 3D](3D_view/pl.md). <br>Po prawej: Część jest widoczna, więc każdy obiekt kontroluje indywidualnie swoje właściwości w zakresie wyświetlania.*



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty tworzone skryptami](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Element Std: Part ([App Part](App_Part.md)) jest tworzony przy pomocy metody `addObject()` dokumentu. Gdy istnieje element Part, inne obiekty mogą być do niego dodane za pomocą metod `addObject()` lub `addObjects()` tej Części.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
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
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

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
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Part/pl
