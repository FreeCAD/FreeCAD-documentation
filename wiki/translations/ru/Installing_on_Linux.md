# Installing on Linux/ru
{{TOCright}}

## Обзор

The installation of FreeCAD on the most well-known Linux systems has been now endorsed by the community, and FreeCAD should be directly available via the package manager available on your distribution. The FreeCAD team also provides some:

-   \"Official\" packages when new releases are made
-   Experimental _, and [Ubuntu Snaps](Ubuntu_Snap.md) for testing bleeding-edge features.


<div class="mw-collapsible mw-collapsed toccolours">

## Ubuntu и Ubuntu подобные системы 

Многие дистрибутивы Linux базируются на Ubuntu и используют их репозитории. Кроме официальных вариантов (Kubuntu, Lubuntu и Xubuntu), существуют неофициальные дистрибутивы, такие как Mnint, Voyager и другие. Приведенные ниже опции установки должны быть совместимыми с этими системами.


<div class="mw-collapsible-content">

### Официальная версия 

FreeCAD доступен в репозиториях Ubuntu Universe и может быть установлен через **Центр управления программным обеспечением** или через терминал:


```python
sudo apt install freecad
```


**Note:**

the Ubuntu Universe package may be outdated as the packaging may lag behind the latest stable source code. In this case, it is suggested to install the package from the `-stable` PPA below. In addition, installing the `-daily` package can be done to test the development branch.

### Стабильная PPA версия 

Персанальный Архив Пакетов (Personal Package Archive (PPA)) для стабильной версии FreeCAD поддерживается сообществом FreeCAD на Launchpad community. Launchpad репозиторий называется как [FreeCAD Stable Releases](https://launchpad.net/~freecad-maintainers/+archive/freecad-stable) .

#### С помощью графического интерфеса 

Установка стабильного PPA с помощью графического интерфейса (GUI):

:   1\. Navigate to **Ubuntu Software → Software & Updates → Software Sources → Other Software**
:   2\. Click on **Add**, then copy and paste the following line

    :   
        
```python
        ppa:freecad-maintainers/freecad-stable
        
```
        





:   3\. Add the source, close the dialog, and reload your software sources, if asked.

Now you can find and install the last stable FreeCAD version from the **Ubuntu Software Center**.

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

As FreeCAD is in constant development, you may wish to install the **daily** package to keep with the latest improvements and bug fixes. The repository is also hosted on Launchpad and is called [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/freecad-daily).

This version is compiled daily from the official master repository. Please beware that although it will contain new features and bug fixes, it may also have newer bugs, and be unstable.

Add the daily PPA to your software sources, update the package lists, and install the daily package: 
```python
sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
sudo apt-get update
sudo apt-get install freecad-daily
```

Every day you can update to the latest daily: 
```python
sudo apt-get update
sudo apt-get install freecad-daily
```


**Note:**

in some cases new code or dependencies added to FreeCAD will cause packaging errors; if this happens, a daily package may not be generated until the maintainers manually fix the problems. If you wish to continue testing the latest code, you should get the source code and compile FreeCAD directly; for instructions see [compiling](compiling.md).

Запустите ежедневную (PPA) версию FreeCAD:

:   
    
```python
    freecad-daily
    
```
    


**Note:**

it is possible to install both the `-stable` and `-daily` packages in the same system. This is useful if you wish to work with a stable version, and still be able to test the latest features in development. Notice that the executable for the daily version is `freecad-daily`, but for the stable version it is just `freecad`.


</div>


</div>

## Debian и прочие базирующиеся на нём системы 

Начиная с Debian Lenny, FreeCAD доступен прямо из программных репозиториев Debian и может быть установлен через synaptic или просто через:


```python
sudo apt-get install freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## OpenSUSE

FreeCAD is typically installed with YAST (abbr. Yet another Setup Tool) the Linux operating system setup and configuration tool, or in any terminal/console (root rights required) with:

:   
    
```python
    zypper install FreeCAD
    
```
    


**Note:**

This procedure only covers the installation of officially released **stable** FreeCAD program versions, depending on the installed links to the program package repositories of your OS version. The openSUSE package *may be outdated* as the packaging may lag behind the latest stable source code. In this case, it is suggested to install the package manually from the below indicated (Expand) source repositories.


<div class="mw-collapsible-content">

A vast release program for FreeCAD package builds are offered. Please visit for a survey:

**[Survey of repositories on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD)**

Generally for selecting the correct openSUSE distribution needed it is necessary to click on the particular **View** button.

### Stable

The stable package version: [Stable repositories on openSUSE](https://software.opensuse.org/package/FreeCAD). The correct openSUSE distribution version must be selected in the lower part of the web page.

Note: openSUSE has several options to choose from when downloading FreeCAD. To view these options, visit [Survey of stable repositories on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=FreeCAD).

### Development

Latest development releases AKA **unstable**: [Unstable repositories listings on openSUSE](https://software.opensuse.org/download.html?project=science%3Aunstable&package=FreeCAD)

It is recommended to grab the binary packages directly. Then select the correct distribution for your installed openSUSE OS.


</div>


</div>

## Gentoo

FreeCAD может быть скомпилирован/установлен просто вызовом:


```python
emerge freecad
```


<div class="mw-collapsible mw-collapsed toccolours">

## Fedora

FreeCAD has been included in the official Fedora packages since Fedora 20. It can be installed from the command line with:


```python
sudo dnf install freecad
```


<div class="mw-collapsible-content">

On older Fedora releases, that was:


```python
sudo yum install freecad
```

The gui packages managers can also be used. Search for \"freecad\". The official release package version tends to be well behind the FreeCAD releases. [Package: freecad](http://rpms.remirepo.net/rpmphp/zoom.php?rpm=freecad) shows the versions included in the Fedora repositories over time and versions.

More current versions can be obtained by downloading one of the [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/)releases from the github repository. These work fine on Fedora.

If you want to keep up with the absolute latest daily builds, FreeCAD is also available on [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). To install the build from there, in a terminal session, enter:


```python
sudo dnf copr enable @freecad/nightly
sudo dnf install freecad
```

That leaves the copr repository active, so


```python
sudo dnf upgrade
```

or equivalent, will update to the latest FreeCAD build, along with updates from any of the other active repos. If you want something a bit more stable, you can disable \@freecad/nightly again after the initial install. The copr repository only keeps builds from the past 2 weeks. This is not a solution if you want to pick a specific older version.


<div class="mw-translate-fuzzy">

Инструкции также доступны в [компиляция FreeCAD самостоятельно](Compile_on_Linux/ru.md), включая сценарий специально для Fedora. С небольшим изменением, чтобы проверить конкретную фиксацию из git, любая версия начиная примерно с FreeCAD 0.15 может быть построена на любом дистрибутиве начиная с Fedora 21.


</div>


</div>


</div>

## Arch

Installing FreeCAD on Arch Linux and derivatives (ex. Manjaro):


```python
pacman -S freecad
```

## Другие

If you find out that your system features FreeCAD but is not documented in this page, please tell us on the [forum](http://forum.freecadweb.org/viewforum.php?f=21)!

Many alternative, non-official FreeCAD packages are available on the net, for example for systems like slackware or fedora. A search on the net can quickly give you some results.

### Ручная установка в системах, основанных на .deb 

If for some reason you cannot use one of the above methods, you can always download one of the .deb packages available on the [Download](Download.md) page.
{{DownloadUnixStable}}

Once you downloaded the .deb corresponding to your system version, if you have the _ package installed (usually it is), you just need to navigate to where you downloaded the file, and double-click on it. The necessary dependencies will be taken care of automatically by your system package manager. Alternatively you can also install it from the terminal, navigating to where you downloaded the file, and type:


```python
sudo dpkg -i Name_of_your_FreeCAD_package.deb
```

changing Name\_of\_your\_FreeCAD\_package.deb by the name of the file you downloaded.

After you installed FreeCAD, a startup icon will be added in the \"Graphic\" section of your Start Menu.

### Установка в других Linux/Unix системах 

Many common Linux distros now include a precompiled FreeCAD as part of the standard packages. This is often out of date, but is a place to start. Check the standard package managers for your system. One of the following (partial) list of commands could install the official version of FreeCAD for your distro from the terminal. These probably need administrator privileges.


```python
apt-get install freecad
dnf install freecad
emerge freecad
slackpkg install freecad
yum install freecad
zypper install freecad
```

The package name is case sensitive, so try \FreeCAD\ as well as \freecad\. If that does not work for you, either because your package manager does not have a precompiled FreeCAD version available, or because the available version is too old for your needs, you can try downloading one of the [.AppImage](https://github.com/FreeCAD/FreeCAD/releases/) releases from the github repository. These tend to work on most 64 bit Linux distributions, without any special installation. Just make sure the downloaded file is marked as executable, then run it.


<div class="mw-translate-fuzzy">

Если и этого недостаточно, и вы не можете найти другой источник предварительно скомпилированного пакета для вашей ситуации, вам потребуется [скомпилировать FreeCAD самостоятельно](Compile_on_Linux/ru.md).


</div>

### Установка Windows Версии в Linux 

Смотрите страницу: [Установка в Windows](Installing_on_Windows/ru.md).

## Следующий Шаг 

После того, как вы установили FreeCAD, пора [приступить к работе](Getting_started.md)!







_ _

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Installing on Linux/ru
