# Installing on Linux/ru
## Обзор


<div class="mw-translate-fuzzy">

Установка FreeCAD на наиболее известных системах Linux теперь поддерживается сообществом и FreeCAD должен быть доступен напрямую через диспетчер пакетов вашего дистрибутива. Команда FreeCAD также предоставляет:

-   «Официальные» пакеты при выпуске новых релизов доступны через [Snap packages](Ubuntu_Snap/ru.md), [AppImages](AppImage/ru.md), [Flatpaks](Flatpak.md) и [PPA](#Stable_PPA_version.md)
-   Экспериментальные сборки доступны через [PPA](#Development_PPA_.28Daily.29.md) daily repository, [AppImages](AppImage/ru.md), [Ubuntu Snaps](Ubuntu_Snap/ru.md).


</div>


<div class="mw-collapsible mw-collapsed toccolours">



## Ubuntu и Ubuntu подобные системы 

Многие дистрибутивы Linux базируются на Ubuntu и используют их репозитории. Кроме официальных вариантов (Kubuntu, Lubuntu и Xubuntu), существуют неофициальные дистрибутивы, такие как Mint, Voyager и другие. Приведенные ниже опции установки должны быть совместимыми с этими системами.


<div class="mw-collapsible-content">



### Официальная версия 

FreeCAD доступен в репозиториях Ubuntu Universe и может быть установлен через **Центр управления программным обеспечением** или через терминал:


```python
sudo apt install freecad
```


**Примечание:**

пакет Ubuntu Universe может быть устаревшим, так как упаковка может отставать от последнего стабильного исходного кода. В этом случае рекомендуется установить пакет из PPA `-stable` ниже. Кроме того, для тестирования ветки разработки можно установить пакет `-daily`.



### Стабильная PPA версия 

**Предупреждение:** FreeCAD PPA в настоящее время не поддерживается и [ищет добровольцев](https://forum.freecadweb.org/viewtopic.php?f=42&t=69055&start=20). Пожалуйста, используйте альтернативу (snap, appimage), пока проблема не будет устранена!

Персанальный Архив Пакетов (Personal Package Archive (PPA)) для стабильной версии FreeCAD поддерживается сообществом FreeCAD на Launchpad community. Launchpad репозиторий называется как [FreeCAD Stable Releases](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable) .



#### С помощью графического интерфеса 

Установка стабильного PPA с помощью графического интерфейса (GUI):

:   1\. Перейдите на **Ubuntu Software → Software & Updates → Software Sources → Other Software**
:   2\. Кликните на **Add**, затем скопируйте и вставьте следующую строку

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Добавьте источник, закройте диалоговое окно, и перезагрузите свои источники софта, если нужно.

Теперь вы можете найти и установить последнюю стабильную версию FreeCAD из **Ubuntu Software Center**.



#### Через командную строку 

Установите стабильный PPA через коммандную строку:

:   1\. Добавьте PPA в свои источники программного обеспечения:

    :   
        
```python
        sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
        
```
        





:   2\. Извлеките обновленные списки пакетов:

    :   
        
```python
        sudo apt update
        
```
        





:   3\. Затем установите FreeCAD вместе с комплектом оффлайн документации:

    :   
        
```python
        sudo apt install freecad freecad-doc
        
```
        


**Note:**

из-за проблем с упаковкой в некоторых версиях Ubuntu у пакета `freecad-doc` возникают коллизии с пакетом самого FreeCAD или одной из его зависимостей; в этом случае удалите пакет `freecad-doc` и установите только пакет `freecad`. Если пакет `freecad-doc` не существует, проигнорируйте его установку.



#### Проверка Установки 

:   4\. Как только вы добавите стабильный PPA в свои исходные файлы одним из вышеперечисленных методов, пакет `freecad` установит эту версию PPA поверх версии, предоставленной репозиторием Ubuntu Universe. Вы можете просмотреть доступные версии с помощью следующей команды `apt-cache` :
:   
    
```python
    apt-cache policy freecad
    
```
    





:   Результат должен выглядеть примерно так (конечно, информация о версии будет отличаться):


```python
freecad:
  Installed: (none)
  Candidate: 2:0.18.4+dfsg1~201911060029~ubuntu18.04.1
  Version table:
     2:0.18.4+dfsg1~201911060029~ubuntu18.04.1 500
        500 http://ppa.launchpad.net/freecad-maintainers/freecad-stable/ubuntu bionic/main amd64 Packages
     0.16.6712+dfsg1-1ubuntu2 500
        500 http://archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
ubuntu@ubuntu:~$ apt-cache policy freecad-doc
```


:   5\. Вызовите стабильную (PPA) версию FreeCAD через графический интерфейс или через командную строку. Последний метод заключается в следующем:
:   
    
```python
    ./freecad
    
```
    

### Development PPA (Daily) 

Поскольку FreeCAD находится в постоянном развитии, вы можете установить пакет **daily**, чтобы быть в курсе последних улучшений и исправлений ошибок. Репозиторий также размещен на Launchpad и называется [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

Эта версия компилируется ежедневно из официального главного репозитория. Имейте в виду, что хотя он будет содержать новые функции и исправления ошибок, он также может содержать новые ошибки и быть нестабильным.

Добавьте PPA типа \"daily\" к вашим источникам программного обеспечения, обновите списки пакетов и установите ежедневный пакет: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Каждый день вы можете обновлять до последней ежедневной: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Примечание:**

в некоторых случаях новый код или зависимости, добавленные в FreeCAD, вызывают ошибки упаковки; в этом случае пакет \"daily\" может не создаваться до тех пор, пока майнтайнеры не исправят проблемы вручную.

Запустите ежедневную (PPA) версию FreeCAD:

:   
    
```python
    freecad-daily
    
```
    


**Примечание:**

в одной системе можно установить как пакеты `-stable`, так и `-daily`.Это полезно, если вы хотите работать со стабильной версией и при этом иметь возможность тестировать новейшие функции в разработке. Обратите внимание, что исполняемый файл для ежедневной версии - это `freecad-daily`, а для стабильной версии это просто `freecad`.


</div>


</div>



## Debian и прочие базирующиеся на нём системы 

Начиная с Debian Lenny, FreeCAD доступен прямо из программных репозиториев Debian и может быть установлен через synaptic или просто через:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD обычно устанавливается через YAST (сокр. Yet another Setup Tool, Еще один инструмент установки), инструмент установки и настройки операционной системы Linux, или в терминале/консоли (нужны права root) с помощью:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Примечание:**

Эта процедура распространяется только на установку официально выпущенных **стабильных** версий программы FreeCAD, в зависимости от установленных ссылок на репозитории программных пакетов вашей версии ОС. Пакет openSUSE «может быть устаревшим», так как упаковка может отставать от последнего стабильного исходного кода.В этом случае рекомендуется установить пакет вручную из отмеченных (Expand) репозиториев исходников.


<div class="mw-collapsible-content">

Предлагается обширная программа выпуска для сборок пакетов FreeCAD. Посетите для обзора:

**[1](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Обычно для выбора правильного дистрибутива openSUSE необходимо щелкнуть по особой кнопке **View**.



### Стабильная версия 

Стабильная версия пакета: [Стабильные репозитории на openSUSE](https://software.opensuse.org/package/FreeCAD). Требуемая версия дистрибутива openSUSE должна быть выбрана в нижней части веб-страницы.

Примечание: openSUSE имеет несколько вариантов на выбор при загрузке FreeCAD. Чтобы просмотреть эти варианты, посетите [Обзор стабильных репозиториев на openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).



### В разработке 

Последние выпуски разработчика **unstable**: [Списки нестабильных репозиториев в openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

Рекомендуется загружать бинарные пакеты напрямую. Затем выберите правильный дистрибутив для установленной вами ОС openSUSE.


</div>


</div>

## Gentoo

FreeCAD может быть скомпилирован/установлен просто вызовом:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD выл включён в официальные пакеты начиная с Fedora 20. Он может быть установлен из командной строки:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

Для предыдущих выпусков Fedora:


```python
sudo yum install freecad
```

Также может быть использован менеджер пакетов с графическим интерфейсом. Задайте поиск \"freecad\". Версия пакета официального релиза как правило сильно отстает от релизов FreeCAD. [Package: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) показывает версии, включенные в репозитории Fedora с течением времени и версии.

Более свежие версии можно получить, загрузив один из [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)релизов из репозитория github. Они отлично работают на Fedora.

Если вы хотите быть в курсе самых последних ежедневных сборок, FreeCAD также доступен на [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/)Чтобы установить сборку оттуда введите в терминале:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

Это оставляет copr хранилище активным, так что


```python
sudo dnf upgrade
```

или эквивалентной, обновится до последней сборки FreeCAD вместе с обновлениями из любых других активных репозиториев. Если вы хотите что-то более стабильное, вы можете отключить \@freecad/nightly снова после первоначальной установки. Репозиторий copr сохраняет только сборки за последние 2 недели. Это не подходит, если вы хотите выбрать более старую конкретную версию.

Инструкции также доступны на [компиляция FreeCAD самостоятельно](Compile_on_Linux/ru.md), включая сценарий специально для Fedora. С небольшим изменением, чтобы проверить конкретную фиксацию из git, любая версия начиная примерно с FreeCAD 0.15 может быть построена на любом дистрибутиве начиная с Fedora 21.


</div>


</div>

## Arch

Установка FreeCAD в Arch Linux и производных (например, Manjaro):


```python
pacman -S freecad
```



## Прочие

Если Вы обнаружите, что Ваша система использует FreeCAD, но не описана на этой странице, пожалуйста сообщите нам на [форум](http://forum.freecadweb.org/viewforum.php?f=21)!

В сети доступны многие альтернативные, неофициальные пакеты FreeCAD, например для систем вроде slackware или fedora. Поиск в сети быстро даст Вам какие-нибудь результаты.



### Установка в других Linux/Unix системах 

Многие распространенные дистрибутивы Linux теперь включают в себя скомпилированный FreeCAD как часть стандартных пакетов. Он часто устаревший, но хорошая стартовая точка. Проверьте стандартные менеджеры пакетов для вашей системы. С помощью одного из следующих (частичных) списков команд можно установить официальную версию FreeCAD для вашего дистрибутива из терминала. Для этого вероятно потребуются права администратора.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
pacman -Sy freecad
```

Имя пакета чувствительно к регистру, поэтому попробуйте \FreeCAD\, а также \freecad\. Если это не работает для вас, либо из-за того, что у вашего менеджера пакетов нет предварительно скомпилированной версии FreeCAD, либо из-за того, что доступная версия устарела для ваших нужд, вы можете попробовать загрузить один из [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) релизов из репозитория github. Они работают на большинстве 64-битных дистрибутивов Linux без какой-либо специальной установки. Просто убедитесь, что загруженный файл помечен как исполняемый, а затем запустите его.

Если и этого недостаточно, и вы не можете найти другой источник предварительно скомпилированного пакета для вашей ситуации, вам потребуется [скомпилировать FreeCAD самостоятельно](Compile_on_Linux/ru.md).



## Следующий Шаг 

После того, как вы установили FreeCAD, пора [приступить к работе](Getting_started.md)!



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Developer Documentation](Category_Developer Documentation.md) > Installing on Linux/ru
