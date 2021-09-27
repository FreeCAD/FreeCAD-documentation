# Document structure/pl
{{TOCright}}

![](images/Screenshot_treeview.jpg ) Dokument FreeCADa zawiera wszystkie obiekty twojej sceny. Może zawierać grupy i obiekty wykonane w dowolnym Środowisku pracy. Dlatego możesz przełączać się między nimi, ciągle pracując z tym samym dokumentem. Dokument jest tym co zostaje zapisane na dysku kiedy zachowujesz swoją pracę. Możesz także uruchomić kilka dokumentów jednocześnie i kilka widoków tego samego dokumentu.

W środku dokumentu obiekty mogą być łączone w grupy i posiadać unikalną nazwę. Zarządzanie grupami, obiektami i nazwami obiektów dokonywane jest głównie z poziomu drzewa widoku *(Tree view)*. **Uwaga:** Jak wszystko w programie FreeCAD, można dokonać tego przez interpreter _, łączyć obiekty w grupy, usuwać obiekty lub grupy przez kliknięcie prawym przyciskiem na [drzewo](Tree_view.md) lub obiekt, zmieniać nazwy przez podwójne kliknięcie na ich nazwy lub dokonywać innych operacji - zależnie od Środowiska pracy.

Wewnątrz dokumentu FreeCAD mogą znajdować się obiekty różnych typów. Każde Środowisko pracy może tworzyć własne typy obiektów, np <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> _ tworzy obiekty Part, <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft](Draft_Workbench/pl.md) także tworzy obiekty Part, itp.

Jeśli w FreeCAD jest przynajmniej jeden dokument otwarty, zawsze jest jeden i tylko jeden aktywny dokument. Jest to dokument, który pojawia się w bieżącym widoku 3D, dokument nad którym aktualnie pracujesz.

## Aplikacja i Interfejs Użytkownika 

Jak niemal wszystko w programie FreeCAD, interfejs użytkownika *(Gui)* jest odseparowany od programu bazowego *(App)*. Dotyczy to także dokumentów. Dokumenty złożone są z dwóch części:
dokument Aplikacji, który zawiera nasze obiekty i dokument Widoku, który zawiera reprezentację naszych obiektów na ekranie.

Myśl o tym jako o dwóch miejscach, gdzie są zdefiniowane obiekty. Ich parametry konstrukcyjne *(to sześcian? stożek? o jakim rozmiarze?)* są zmagazynowane w dokumencie Aplikacji, podczas gdy ich reprezentacja graficzna *(jest narysowany przy pomocy czarnych linii? z niebieskimi ścianami?)* są zmagazynowane w dokumencie Widoku. Dlaczego tak jest? Ponieważ FreeCAD może być także uruchamiany BEZ interfejsu graficznego, np. wewnątrz innych programów i musimy mieć nadal możliwość manipulowania naszymi obiektami, pomimo że nic nie jest ryzowane na ekranie.

Kolejną rzeczą zawartą w dokumencie Widoku są widoki 3D. Jeden dokument może być otwarty w kilku widokach, więc możesz kontrolować obiekt w kilku punktach widoku w tym samym czasie. Może chcesz zobaczyć widok z góry i z przodu twojej pracy w tym samym czasie? Wtedy masz dwa widoki tego samego dokumentu, oba zmagazynowane w dokumencie Widoku,. Tworzenie nowych lub zamykanie widoków może być dokonywane przez menu Widoku lub kliknięcie prawym przyciskiem w zakładkę widoków.

## Tworzenie skryptów 

Dokumenty mogą być łatwo tworzone, otwierane and modyfikowane przez interpreter [Python](Python/pl.md). Na przykład: 
```python
FreeCAD.ActiveDocument
``` Zwróci aktualny *(aktywny)* dokument 
```python
FreeCAD.ActiveDocument.Blob
``` Uzyskanie dostępu do obiektu nazwanego \"Blob\" w twoim dokumencie 
```python
FreeCADGui.ActiveDocument
``` Zwróci dokument widoku powiązany z aktualnym dokumentem 
```python
FreeCADGui.ActiveDocument.Blob
``` Uzyskanie dostępu do graficznej reprezentacji *(widoku)* naszego obiektu Blob 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Zwróci aktualny widok

---
[documentation index](../README.md) > Document structure/pl
