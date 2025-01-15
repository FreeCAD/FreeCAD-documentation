# Flatpak/ru
## Установка



### Стабильная версия 

Если вы хотите выполнить установку на уровне пользователя или у вас нет привилегий sudo, добавьте флаг `--user` к следующим командам:


{{code|lang=bash|code=
# add flathub repo just to be sure as it might not be enabled if it is your first time using flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.freecad.FreeCAD
}}



## Тестовые версии 

Если вы хотите выполнить установку на уровне пользователя или у вас нет привилегий sudo, добавьте флаг `--user` к следующим командам:


{{code|lang=bash|code=
# flathub-beta repo is not enabled by default
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak install flathub-beta org.freecad.FreeCAD
}}



## Запуск

Вы можете запустить flatpak, используя файл desktop или используя следующую команду:


{{code|lang=bash|code=
flatpak run org.freecad.FreeCAD
}}

Параллельно могут быть установлены различные ветки. Чтобы выбрать, какую из них запускать, используйте флаг `--branch`:


{{code|lang=bash|code=
flatpak run --branch=beta org.freecad.FreeCAD
}}

Чтобы запустить определенный исполняемый файл (например, `FreeCADCmd` для запуска без графического интерфейса) из flatpak, используйте флаг `--command`:


{{code|lang=bash|code=
flatpak run --command=FreeCADCmd org.freecad.FreeCAD
}}



## Репзиторий

-   <https://github.com/flathub/org.freecad.FreeCAD>



### Поставщик(и) ПО 

-   [adrianinsaval](https://github.com/adrianinsaval)
-   [hfiguiere](https://github.com/hfiguiere)



## Сопутствующая информация 

-   Пакеты [AppImage](AppImage.md)
-   Пакеты [Snap](Snap.md)



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Testing](Category_Testing.md) > Flatpak/ru
