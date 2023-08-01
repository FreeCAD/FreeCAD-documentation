# Macro ObjectInfo/ru
{{Macro/ru
|Name=Macro ObjectInfo
|Translate=Macro ObjectInfo
|Description=предоставляет информацию о выбранном объекте
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=Это не макрос, а один WorkBench, распакуйте ZIP-файл и вставьте полный каталог в каталог пользователя Mod. [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=[Arch Survey|<img src=images/Arch_Survey.svg style="width:24px"> [Arch Survey](Arch_Survey/ru.md)
}}

## Описание

Этот WorkBench позволяет узнать объем информации о площади поверхности, центре масс и моменте интерции выбранного объекта.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Установка

Если вы работаете в Linux, вам нужно создать папку с именем «Mod» в скрытой папке .FreeCAD, которая находится в вашей домашней папке. Затем создайте папку с именем \"Info\" в папке \"Mod\" и извлеките в нее содержимое архива. На Windows я понятия не имею, где это будет. Используйте ту же процедуру для Windows в C:\\Program Files\\FreeCAD\\Mod.

## Использование

Затем запустите FreeCAD, откройте свой файл STEP и переключитесь на рабочую среду \"Info\" с помощью переключателя рабочей среды или перейдя в меню View → Workbench. Теперь выберите твёрдое тело и нажмите на иконку «Информация»; левая панель задач покажет некоторую информацию о модели, в том числе объем, площадь поверхности, центр масс и момент пересечения.

## код


{{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Ссылки

Пользователь FreeCAD создал удобный модуль «Информация», который вы можете получить здесь: <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

С форума[Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro ObjectInfo/ru
