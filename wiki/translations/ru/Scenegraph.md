# Scenegraph/ru
## Введение


<div class="mw-translate-fuzzy">

Геометрия которая появляется в [трёхмерных видах](3D_view/ru.md) FreeCAD, получается с помощью библиотек [Coin3d](https://ru.wikipedia.org/wiki/Coin3D). Coin3D это реализация стандарта [OpenInventor](https://ru.wikipedia.org/wiki/Open_Inventor). [OpenCASCADE](https://ru.wikipedia.org/wiki/Open_Cascade_Technology) тоже поддерживает схожую функциональность, но при создании FreeCAD было решено не использовать встроенный в OpenCASCADE просмотрщик, а скорее перейти на более производительный Coin3D. Для изучения этой библиотеки рекомендуется книга [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).


</div>

## Описание


<div class="mw-translate-fuzzy">

[OpenInventor](https://ru.wikipedia.org/wiki/Open_Inventor) это язык описания [трёхмерной сцены](https://ru.wikipedia.org/wiki/Граф_сцены). Сцена, описанная в OpenInventor, затем отрисовывается OpenGL на вашем экране. Об этом заботится Coin3D, поэтому программисту не надо иметь дело со сложными вызовами OpenGL, он может просто предоставить корректный (работающий) код OpenInventor. Большим преимуществом является то, что OpenInventor это широко известный и хорошо задокументированный стандарт.


</div>


<div class="mw-translate-fuzzy">

Одну из главных работ, которую FreeCAD делает за вас, это перевод информации о геометрии OpenCASCADE в формат языка OpenInventor.


</div>


<div class="mw-translate-fuzzy">

OpenInventor записывает трехмерную сцену в форме [древа сцен](https://ru.wikipedia.org/wiki/Граф_сцены), как показано ниже:


</div>

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">



*
Рисунок, взятый с сайта [http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/ Inventor mentor]*


</div>


<div class="mw-translate-fuzzy">

Дерево сцен в openInventor описывает все части трёхмерной сцены, такие как геометрия, цвета, материалы, освещение, и т.д. и организует все эти данные в удобной и четкой структуре. Все что угодно может быть сгруппировано в субструктуры, позволяя вам организовывать содержание вашей сцены тем способом, который вам нравится. Вот пример файла в формате openInventor:


</div>


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}

Как вы можете видеть, его структура проста. Вы используете разделители (separator), организуя ваши данные в блоки, это немного похоже на то, как вы организуете ваши файлы в папках. Каждый оператор влияет на то, что будет дальше, например, первые два пункта в вашем корневом разделителе это поворот и перенос(трансляция), как они повлияют на следующий элемент, который тоже является разделителем. В этом сепараторе определяется материал и другое преобразование. Поэтому наш цилиндр будет подвержен обеим трансформациям, то что было применено непосредственно к нему, так и то что было применено к родительскому разделителю.


<div class="mw-translate-fuzzy">

Мы также обладаем множество элементов других типов для организации нашей сцены, таких как группы, переключатели и аннотации. Мы можем задать очень сложные материалы для ваших объектов, с цветами, текстурой, теневыми режимами и прозрачностью. Мы также можем задать освещение, камеры, и даже движение. Можно даже встроить кусочки сценариев в openInventor файлы, для задания более сложного поведения.


</div>


<div class="mw-translate-fuzzy">

Если вы заинтересованы в получении дополнительной информации о openInventor, отправляйтесь напрямую к самому известному руководству: [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html).


</div>


<div class="mw-translate-fuzzy">

В FreeCAD, как правило. не нужно напрямую взаимодействовать с древом сцен openInventor. Каждый объект в документе FreeCAD, будь то полигональная модель (mesh), форма детали, или что-нибудь ещё, автоматически преобразуется в код OpenInventor и вставляется в основное дерево сцен, которое вы видите в окне [трёхмерного просмотра](3D_view/ru.md). Это древо сцен непрерывно обновляется, когда вы модифицируете, добавляете или удаляете объекты. В самом деле каждый объект (в пространстве App) обладает поставщиком визуального отображения (соответствующий объект в пространстве Gui), ответственного за выдачу кода OpenInventor.


</div>

Но есть множество преимуществ, которые будут возможны при прямом доступе. Например, мы временно можем изменить внешний вид объекта, или мы можем добавить в сцену объекты, которые не обладают реальным представлением в документе FreeCAD, такие как геометрия построений, помощники, графические подсказки или инструменты, такие как манипуляторы или отображающаяся на экране информация.


<div class="mw-translate-fuzzy">

FreeCAD обладает несколькими инструментами для просмотра и изменения openInventor кода. На пример, нижеследующий код на python отобразит openInventor представление выбранного объекта:


</div>


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```


<div class="mw-translate-fuzzy">

А также мы обладаем модулем python открывает полный доступ к управлению чем угодно в Coin3D, такому как ваше дерево сцен в FreeCAD. Также читайте об этом на странице [Pivy](Pivy/ru.md).


</div>

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository can be found at <https://github.com/MariwanJ/COIN3D_Snippet>. {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Scenegraph/ru
