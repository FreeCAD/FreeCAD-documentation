---
 GuiCommand:
   Name: Std SendToPythonConsole
   Name: Std: Wyślij do konsoli Python
   MenuLocation: Edycja , Wyślij do konsoli Python
   Workbenches: wszystkie
   Shortcut: **Ctrl** + **Shift**+**P**
   Version: 0.19
---

# Std SendToPythonConsole/pl



## Opis

Polecenie **Wyślij do konsoli Pyton** tworzy w [Konsoli Python](Python_console/pl.md) zmienne odnoszące się do wybranego obiektu i jego wybranych kształtów podrzędnych, wraz z kilkoma innymi użytecznymi odniesieniami. Zmienne i związany z nimi kod mogą być wykorzystane podczas tworzenia kodu środowiska Python.

W zależności od wybranego obiektu i jego wybranych kształtów podrzędnych, jeśli takie istnieją, tworzone są następujące zmienne:

+++
| Nazwa zmiennej  | Obiekty, do których się odwołano                                                                                                                               |
+=================+================================================================================================================================================================+
|  | Dokument zawierający wybrany obiekt                                                                                                                            |
| {{Incode|doc}}  |                                                                                                                                                                |
|              |                                                                                                                                                                |
+++
|  | Wybrany obiekt odnośnika *(tworzony tylko wtedy, gdy wybrany obiekt jest odnośnikiem)*                                                                         |
| {{Incode|lnk}}  |                                                                                                                                                                |
|              |                                                                                                                                                                |
+++
|  | W zależności od wybranego obiektu:                                                                                                                             |
| {{Incode|obj}}  | Sam zaznaczony obiekt *(jeśli zaznaczony obiekt nie jest odnośnikiem)*                                                                                         |
|              | Obiekt powiązany *(jeśli wybrany obiekt jest odnośnikiem)*                                                                                                     |
+++
|  | W zależności od typu {{Incode|obj}}:                                                                                                             |
| {{Incode|shp}}  | Właściwość {{Incode|Shape}} obiektu {{Incode|obj}} *(dla obiektów wywodzących się z klasy {{Incode|Part::Feature}})* |
|              | Właściwość {{Incode|Mesh}} obiektu {{Incode|obj}} *(dla obiektów typu Mesh)*                                                       |
|                 | Właściwość {{Incode|Points}} obiektu {{Incode|obj}} *(dla obiektów Points)*                                                        |
+++
|  | Pierwszy wybrany kształt podrzędny *(tworzony tylko wtedy, gdy wybrany jest co najmniej jeden kształt podrzędny)*                                              |
| {{Incode|sub}}  |                                                                                                                                                                |
|              |                                                                                                                                                                |
+++
|  | Lista zawierająca wszystkie kształty podrzędne *(tworzona tylko w przypadku wybrania dwóch lub więcej kształtów podrzędnych)*                                  |
| {{Incode|subs}} |                                                                                                                                                                |
|              |                                                                                                                                                                |
+++

>>> ### Begin command Std_SendToPythonConsole
>>> try:
>>>     del(doc,lnk,obj,shp,sub,subs)
>>> except Exception:
>>>     pass
>>> 
>>> doc = App.getDocument("Unnamed")
>>> lnk = doc.getObject("Link")
>>> obj = lnk.getLinkedObject()
>>> shp = obj.Shape
>>> sub = obj.getSubObject("Edge10")
>>> subs = [obj.getSubObject("Edge10"),obj.getSubObject("Face3"),obj.getSubObject("Vertex5"),]
>>> ### End command Std_SendToPythonConsole



*Przykładowe dane wyjściowe: wybrano krawędź, ścianę i wierzchołek [łącza](Std_LinkMake/pl.md) do [sześcianu](Part_Box/pl.md).*



## Użycie

1.  Wybierz pojedynczy obiekt albo jeden lub więcej kształtów podrzędnych należących do pojedynczego obiektu.
2.  Polecenie można wywołać na kilka sposobów:
    -   Wybierz opcję **Edycja → <img src="images/Std_SendToPythonConsole.svg" width=16px> Wyślij do konsoli Python** z menu.
    -   Wybierz opcję **<img src="images/Std_SendToPythonConsole.svg" width=16px> Wyślij do konsoli Python** z menu kontekstowego okna [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **Ctrl** + **Shift** + **P**.
3.  W razie potrzeby otwiera się [Konsola Pythona](Python_console/pl.md).
4.  [Konsola Python](Python_console/pl.md) zostaje przekierowana na klawiaturę.



## Uwagi

-   Wszystkie wcześniej utworzone zmienne są usuwane po każdym uruchomieniu polecenia.

-   Jeśli zaznaczony obiekt jest Łączem *({{Incode|App::Link}})*, a Obiekt połączony pochodzi z klasy {{Incode|Part::Feature}}, zmienna {{Incode|shp}} będzie kształtem obiektu połączonego. Jeśli odnośnik został przekształcony lub przeskalowany i chcesz uzyskać dostęp do przeskalowanego/przekształconego kształtu, możesz to zrobić za pomocą tego kodu:

:   
    
```pythonlnk_shp = Part.getShape(lnk)```
    





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SendToPythonConsole/pl
