# Selection view/pl
## Wprowadzenie




[Widok wyboru](selection_view/pl.md) jest panelem [interfejsu](interface/pl.md) domyślnie znajdującym się poniżej widoku złożonego. Podobnie jak [edytor właściwości](property_editor/pl.md), pokazuje on więcej informacji o aktualnie wybranych obiektach.

Wyboru można dokonać poprzez zaznaczenie obiektu w [Widoku 3D](3D_view/pl.md) lub w [Widoku drzewa](Tree_view/pl.md). Wiele obiektów można zaznaczyć przytrzymując **Ctrl**.

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Widok wyboru oznaczony cyfrą 5, w standardowym [Interfejsie użytkownika](interface/pl.md).*



## Zaznaczanie obiektów 

Widok drzewa tego przykładu zawiera dwie [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części, z kilkoma cechami każda, oraz prosty [Stożek](Part_Cone/pl.md) środowiska Część. Drzewo wygląda następująco.

![](images/FreeCAD_Selection_Tree_view.png )

Widok wyboru jest pusty, jeśli żaden obiekt nie jest zaznaczony w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md).

<img alt="" src=images/FreeCAD_Selection_view_empty.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_empty_3D.png  style="width:" height="286px;">

Po wybraniu obiektu pojawi się on na liście obiektów wraz z dokumentem, do którego należy. Wyświetlony zostanie zarówno wewnętrzny kod tylko do odczytu {{Incode|Name}}, jak i zmienny kod użytkownika {{Incode|Label}}.


`Name`

może zawierać tylko podstawowe znaki alfanumeryczne `[_0-9a-zA-Z]`, podczas gdy `Label` może zawierać dowolny symbol, w tym spacje i znaki akcentowane. 
```python
Document#Name (Label)
```

<img alt="" src=images/FreeCAD_Selection_view_one_object.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_one_object_3D.png  style="width:" height="286px;">

Po wybraniu różnych obiektów zostaną one wyświetlone w widoku. Jeśli obiekty te znajdują się wewnątrz typu kontenera, na przykład [Zawartość](PartDesign_Body/pl.md), środowiska Projekt Części wyświetlana nazwa zostanie podana w sposób hierarchiczny, czyli `Document#Parent.Child`. W takim przypadku nie tylko element podrzędny, ale cały element nadrzędny zostanie podświetlony w widoku 3D. 
```python
Document#Body.Feature. (Feature_label)
```

<img alt="" src=images/FreeCAD_Selection_view_many_objects.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_many_objects_3D.png  style="width:" height="286px;">

Poszczególne elementy zawartości, tj. wierzchołki, krawędzie i ściany, mogą być zaznaczane i będą również wyświetlane w sposób hierarchiczny. 
```python
Document#Body.Feature.Vertex (Feature_label)
Document#Body.Feature.Edge (Feature_label)
Document#Body.Feature.Face (Feature_label)
```

<img alt="" src=images/FreeCAD_Selection_view_many_objects_subelements.png  style="width:" height="286px;"> <img alt="" src=images/FreeCAD_Selection_view_many_objects_subelements_3D.png  style="width:" height="286px;">



## Pasek wyszukiwania 

Jeśli masz wiele obiektów w dokumencie i nie możesz wybrać tego, który chcesz z [widoku 3D](3D_view/pl.md) lub z [widok drzewa](Tree_view/pl.md), możesz wpisać częściową nazwę obiektu w polu wyszukiwania. Zostaną przeszukane wszystkie nazwy w dokumencie i wyświetlona zostanie lista tych, które częściowo pasują do wpisanego tekstu. Po znalezieniu szukanego obiektu można go kliknąć, aby go zaznaczyć.



## Działania

Kliknięcie prawym przyciskiem myszy elementu na liście powoduje wyświetlenie różnych poleceń.

-    **Wybierz tylko**: odznacza wszystko i zaznacza tylko obiekt nadrzędny, który zawiera dany element.

-    **Odznacz**: całkowicie usuwa zaznaczenie wszystkich obiektów.

-    **Powiększenie do dopasowania**: odznacza wszystko i zaznacza tylko obiekt nadrzędny, który zawiera dany element. Ponadto [Widok 3D](3D_view/pl.md) jest przesuwany i powiększany tak, aby obiekt nadrzędny był wyśrodkowany na ekranie. Jest to przydatne podczas wybierania jednego obiektu w widoku drzewa, a następnie szybkiego ustawiania na nim ostrości kamery w widoku 3D.

-    **Przejdź do wyboru**: odznacza wszystko i zaznacza tylko obiekt nadrzędny, który zawiera wybrany element. W tym przypadku [widok drzewa](Tree_view/pl.md) jest dostosowywany i rozszerzany, aby pokazać dokładnie, gdzie wybrany obiekt znajduje się w drzewie. Jest to przydatne, gdy obiekty w widoku 3D znajdują się wewnątrz wielu obiektów kontenera w widoku drzewa, na przykład [Część](Std_Part/pl.md), [Grupa](Std_Group/pl.md), [Zawartość](PartDesign_Body/pl.md) środowiska Projekt Części, [Budowla](Arch_BuildingPart/pl.md) środowiska Architektura i podobnych. Gdy masz setki brył, łatwiej jest wybrać obiekt w widoku 3D, a następnie wybrać **Widok drzewa**, aby natychmiast zlokalizować obiekt w widoku drzewa, a następnie przejść do edycji jego właściwości w [Edytor właściwości](Property_editor/pl.md).

-    **Zaznacz do przeliczenia**: zaznacza wybrany obiekt jako \"Dotknięty\", co oznacza, że jego właściwości zostaną zaktualizowane następnym razem, gdy dokument zostanie [przeliczony](Std_Refresh/pl.md).

-    **Do konsoli Python**: tworzy zmienną `obj`, która przechowuje odniesienie do obiektu nadrzędnego. Jest to przydatne podczas pisania skryptów i testowania poleceń w [konsoli Python](Python_console/pl.md). Zamiast używać pełnej nazwy obiektu, łatwiej jest użyć krótszej i bardziej kompaktowej nazwy `obj`.



## Wskazany obiekt 

Począwszy od wersji 0.19, dostępne jest pole wyboru **lista obiektów wskazanych**. Jeśli jest ono zaznaczone, pojawi się dodatkowa lista pokazująca wszystkie elementy podrzędne *(wierzchołki, krawędzie i ściany)*, które można wybrać jednym kliknięciem, nawet te, które znajdują się za *(ukryte przez)* innymi obiektami.

<img alt="" src=images/FreeCAD_Selection_view_pick_hidden.png  style="width:" height="300px;"> <img alt="" src=images/FreeCAD_Selection_view_pick_hidden_3D.png  style="width:" height="300px;">


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Selection view/pl
