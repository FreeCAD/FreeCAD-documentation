# Raytracing templates/pl
## Wprowadzenie

Do środowiska pracy [Raytracing](Raytracing_Workbench/pl.md) dołączone są szablony dla povray i luxrender, ale można łatwo stworzyć własne. Wystarczy utworzyć plik sceny dla danego renderera, a następnie edytować go ręcznie za pomocą edytora tekstu, wstawiając specjalne znaczniki, które program FreeCAD rozpozna i w których wstawi jego zawartość (dane kamery i obiektów).

Szablony własne {{Version/pl|0.18}} można umieścić we właściwej ścieżce


```python
~/.FreeCAD/data/Mod/Raytracing/Templates
```

## Povray

Pliki scen Povray *(z rozszerzeniem .pov)* można tworzyć ręcznie za pomocą edytora tekstowego *(povray został stworzony przede wszystkim z myślą o wykorzystaniu jako język skryptowy)*, ale także za pomocą szerokiej gamy aplikacji 3D, takich jak [blender](http://www.blender.org). Na stronie [Povray](http://www.povray.org/) można znaleźć dalsze informacje oraz listę aplikacji zdolnych do tworzenia plików typu .pov.

Gdy plik .pov jest już gotowy, należy otworzyć go w edytorze tekstu i wykonać dwie operacje:

1.  usunąć informacje o kamerze, ponieważ FreeCAD umieści w nim własne dane kamery. Aby to zrobić, znajdź blok tekstowy, taki jak ten: camera { ... }, zawierający parametry kamery, i usuń go *(lub wstaw \"//\" przed każdą linią, aby je wykomentować)*.
2.  Wstaw gdzieś następujący wiersz://RaytracingContent. W tym miejscu FreeCAD wstawi swoją zawartość *(dane z kamery i obiektów)*. Możesz na przykład umieścić tę linię na samym końcu pliku.

Zauważ, że FreeCAD doda również pewne deklaracje, które możesz wykorzystać w swoim szablonie, po znaczniku //RaytracingContent. Są to:

-   cam_location: położenie kamery
-   cam_look_at: położenie punktu docelowego kamery
-   cam_sky: wektor górny kamery.
-   cam_angle: kąt kamery.

Można tego użyć, na przykład, do umieszczenia lampy nad aparatem: 
```python
light_source {
 cam_location + cam_angle * 100
 color rgb <10, 10, 10>
}
```

## Luxrender

Pliki scen Luxrender *(z rozszerzeniem.lxs)* mogą być albo pojedynczymi plikami, albo głównym plikiem .lxs, który zawiera pliki definicji świata *(.lxw)*, definicji materiałów *(.lxm)* i definicji geometrii *(.lxo)*. Można pracować z obydwoma stylami, ale można też łatwo przekształcić grupę 4 plików w pojedynczym pliku .lxs, kopiując zawartość każdego pliku .lxw, .lxm i .lxo i wklejając ją w miejscu, w którym dany plik jest wstawiany do głównego pliku .lxs.

Pliki scen Luxrender są trudne do wytworzenia ręcznie, ale są łatwe do wytworzenia za pomocą wielu aplikacji 3D, takich jak [blender](http://www.blender.org). Na stronie domowej [Luxrender](http://www.luxrender.net) znajdziesz więcej informacji i wtyczki do głównych aplikacji 3D.

Jeśli będziesz pracował z oddzielnymi plikami .lxw, .lxm i .lxo, pamiętaj, że końcowy plik .lxs wyeksportowany przez FreeCAD może znajdować się w innej lokalizacji niż plik szablonu, a zatem pliki te mogą nie zostać znalezione przez Luxrender w czasie renderowania. W takim przypadku powinieneś albo skopiować te pliki do lokalizacji swojego pliku końcowego, albo edytować ich ścieżki w wyeksportowanym pliku .lxs.

Jeśli eksportujesz plik sceny z blendera i chcesz scalić wszystko w jeden plik, będziesz musiał wykonać jeden krok przed eksportem: Domyślnie, eksporter luxrender w blenderze eksportuje wszystkie geometrie siatek jako oddzielne pliki .ply, zamiast umieszczać geometrię siatki bezpośrednio w pliku .lxo. Aby zmienić to działanie, musisz wybrać każdą ze swoich siatek w blenderze, przejść do zakładki \"mesh\" i ustawić opcję \"eksportuj jako\" na \"luxrender mesh\" dla każdej z nich.

Po przygotowaniu pliku sceny, aby przekształcić go w szablon FreeCAD, należy wykonać następujące czynności:

1.  Znajdź pozycję kamery, pojedynczy wiersz zaczynający się od LookAt, i usuń go *(lub umieść znak \"#\" na początku wiersza, aby go wykomentować)*.
2.  W tym miejscu wstaw następujący wiersz:#RaytracingCamera
3.  W odpowiednim miejscu, na przykład tuż za końcem definicji materiałów, przed informacją o geometrii lub na samym końcu, tuż przed ostatnią linią WorldEnd, wstaw następującą linię: #RaytracingContent.

W tym miejscu FreeCAD wstawi swoje własne obiekty.

Zauważ, że w luxrender, obiekty przechowywane w pliku sceny mogą definiować macierze transformacji, które wykonują operacje lokalizacji, obracania lub skalowania. Te macierze mogą układać się w stos i wpływać na wszystko, co nastąpi po nich, więc umieszczając swój tag #RaytracingContent na końcu pliku, możesz zobaczyć obiekty FreeCAD, na które ma wpływ macierz transformacji umieszczona wcześniej w szablonie . Aby upewnić się, że tak się nie stanie, umieść swój tag #RaytracingContent przed jakimkolwiek innym obiektem geometrii obecnym w szablonie. Sam FreeCAD nie zdefiniuje żadnej z tych macierzy transformacji.


{{TechDraw Tools navi/pl}}


{{Userdocnavi/pl}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](Category_TechDraw.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing templates/pl
