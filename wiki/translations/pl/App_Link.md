# App Link/pl

 {{TOCright}}

## Wprowadzenie

<img alt="" src=images/Link.svg  style="width:32px;">

[App: Link](App_Link/pl.md), lub formalnie `App::Link`, jest typem obiektu, który odwołuje się lub łączy z innym obiektem, w tym samym dokumencie lub w innym. Jest on specjalnie zaprojektowany do efektywnego powielania pojedynczego obiektu wiele razy, co pomaga w tworzeniu skomplikowanych [złożeń](assembly/pl.md) z mniejszych złożeń podrzędnych i z wielu ponownie używanych komponentów jak wkręty, nakrętki i tym podobne elementy złączne.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Uproszczony schemat zależności pomiędzy głównymi obiektami w programie. Obiekt `App::Link* jest głównym składnikiem systemu, nie zależy on od żadnego środowiska pracy, a może być użyty z większością obiektów stworzonych we wszystkich środowiskach pracy.`

## Użycie

1.  Wybierz obiekt w [widoku drzewa](tree_view/pl.md) lub oknie [widoku 3D](3D_view.md) dla którego chcesz stworzyć Łącze.
2.  Naciśnij przycisk**<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)**. Stworzony obiekt ma tę samą ikonę jak oryginalny obiekt, ale została nałożona na niego strzałka informująca, że jest on Łączem.

Zobacz stronę [Std: LinkMake](Std_LinkMake.md) dla pełnych informacji, włącznie z [tworzeniem skryptów](Std_LinkMake/pl#Tworzenie_skrypt.C3.B3w.md).

## Właściwości

[App: Link](App_Link/pl.md) *(klasa`App::Link`)* pochodzi z [App: DocumentObject](App_DocumentObject/pl.md) *(klasa`App::DocumentObject`)*, przez co współdzieli większość właściwości tej ostatniej.

Zobacz pełną listę właściwości na stronie [Std: LinkMake](Std_LinkMake/pl.md).


{{Std Base

}} {{Document objects navi}} 
