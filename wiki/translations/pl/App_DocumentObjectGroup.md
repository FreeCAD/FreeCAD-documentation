# App DocumentObjectGroup/pl
## Wprowadzenie

<img alt="" src=images/Folder.svg  style="width:32px;">

**Obiekt grupy dokumentu** lub formalnie `App::DocumentObjectGroup` to prosty element, który umożliwia grupowanie dowolnego typu [obiektów dokumentu](App_DocumentObject/pl.md) w widoku drzewa, bez względu na ich rodzaj danych.

Został opracowany, aby zorganizować obiekty w [widoku drzewa](Tree_view/pl.md) w sposób logiczny dla użytkownika.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Schemat uproszczony relacji między podstawowymi obiektami w programie. Klasa `App::DocumentObjectGroup* ma rozszerzenie, które pozwala grupować dowolny rodzaj obiektu. Samo Grupowanie nie ma wielu właściwości.`



## Użycie

1.  Kliknij przycisk **[<img src=images/Std_Group.svg style="width:16px"> [Std Grupa](Std_Group/pl.md)** na pasku narzędzi struktury. Utworzona zostanie pusta Grupa.
2.  Aby dodać obiekty do Grupy, zaznacz je w [widoku drzewa](Tree_view/pl.md) i przeciągnij je na Grupę.
3.  Aby usunąć obiekty z Grupy, przeciągnij je z Grupy na etykietę dokumentu na górze [widoku drzewa](Tree_view/pl.md).

Zobacz stronę [Std: Grupa](Std_Group/pl.md) dla uzyskania pełnych informacji, włącznie z sekcją [tworzeniem skryptów](Std_Group/pl#Tworzenie_skrypt.C3.B3w.md).



## Właściwości

**Obiekt grupy dokumentu** *(klasa `App::DocumentObjectGroup`)* jest pochodną podstawowego [App Obiekt dokumentu](App_DocumentObject/pl.md) *(klasa `App::DocumentObject`)*, dlatego dzieli wszystkie jego właściwości.

Zobacz właściwości na stronie [Std Grupa](Std_Group/pl.md).


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > App DocumentObjectGroup/pl
