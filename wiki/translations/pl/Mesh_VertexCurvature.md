---
- GuiCommand:
   Name:Mesh VertexCurvature
   Name/pl:Siatka: Krzywizna siatki
   MenuLocation:Siatki → Wykres krzywizny
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Informacje o krzywiźnie](Mesh_CurvatureInfo/pl.md)
---

# Mesh VertexCurvature/pl



## Opis

Polecenie **Wykres krzywizny** tworzy obiekty krzywizny dla obiektów siatki. Obiekt krzywizny wyświetla krzywiznę siatki używając różnych kolorów dla części wypukłej, płaskiej i wklęsłej.

![](images/Mesh_VertexCurvature_example.png ) 
*Przykład obiektu krzywizny siatki*



## Użycie

1.  Wybierz jeden lub więcej obiektów siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_VertexCurvature.svg" width=16px> [Krzywizna siatki](Mesh_VertexCurvature/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_VertexCurvature.svg" width=16px> Wykres krzywizny**.
    -   Wybierz opcję **<img src="images/Mesh_VertexCurvature.svg" width=16px> Wykres krzywizny** z menu podręcznego [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).



## Właściwości

Dla obiektu krzywizny siatki następujące właściwości są dostępne w [edytorze właściwości](Property_editor/pl.md). Wybierz opcję **Wyświetl wszystko** z menu kontekstowego Edytora właściwości, aby wyświetlić ukryte właściwości.



### Dane


{{TitleProperty|Podstawa}}

-    **Etykieta|String**: edytowalna przez użytkownika nazwa obiektu, dowolny ciąg znaków UTF8.

-    **Pochodzenie|Link**: link do obiektu siatki.



#### Ukryte dane 


{{TitleProperty|Podstawa}}

-    **Curv Info|CurvatureList**: lista informacji o krzywiźnie.

-    **Expression Engine|ExpressionEngine**: lista wyrażeń.

-    **Label2|String**: opis obiektu edytowalny przez użytkownika, dowolny ciąg znaków UTF8, który może zawierać nowe linie.

-    **Visibility|Bool**: jeśli opcja jest ustawiona na wartość {{TRUE/pl}}, obiekt pojawi się w oknie [widoku 3D](3D_view/pl.md).



### Widok


{{TitleProperty|Podstawa}}

-    **Display Mode|Enumeration**: {{value|Krzywizna bezwzględna}} *(domyślnie)*, {{value|Krzywizna średnia}}, {{value|Krzywizna Gaussa}}, {{value|Krzywizna maksymalna}}, {{value|Krzywizna minimalna}}.

-    **On Top When Selected|Enumeration**: {{value|Wyłączone}} *(domyślnie)*, {{value|Włączone}}, {{value|Objekt}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Kształt}}, {{value|Ramka otaczająca}} *(domyślnie)*.

-    **Show In Tree|Bool**: jeśli opcja jest ustawiona na wartość {{TRUE/pl}}, obiekt pojawi się w oknie [Widoku drzewa](Tree_view/pl.md).

-    **Visibility|Bool**: jeśli opcja jest ustawiona na wartość {{TRUE/pl}}, obiekt pojawi się w oknie [Widoku 3D](3D_view/pl.md).



#### Wyświetl ukryte 


{{TitleProperty|Podstawa}}

-    **Texture Material|Material**: [Materiał](App_Material/pl.md) związany z obiektem.





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh VertexCurvature/pl
