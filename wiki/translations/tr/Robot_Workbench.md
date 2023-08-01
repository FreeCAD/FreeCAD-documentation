# Robot Workbench/tr
**The Robot Workbench is unmaintained. If you have experience with the topic and are interested in maintaining it, please state your intention in the developer's section of the [https://forum.freecadweb.org/index.php FreeCAD forum].

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository.
**

## Giriş

<img alt="Robot workbench icon" src=images/Workbench_Robot.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

[Robot Tezgahı](Robot_Workbench/tr.md), [Kuka](http://kuka.com/) gibi bir standart [6 eksenli endüstriyel robot](Robot_6-Axis.md) \'u simüle etmek için kullanılan bir araçtır.


</div>

Aşağıdaki görevleri yapabilirsiniz:

-   Bir robot ve iş parçaları ile bir simülasyon ortamı kurun.
-   Hareket yörüngelerini oluşturun ve doldurun.
-   Bir CAD parçasının özelliklerini bir yörüngeye ayırın.
-   Robot hareketini simüle edin ve mesafeye ulaşın.
-   Yörüngeyi bir robot program dosyasına aktarın.


<div class="mw-translate-fuzzy">

Başlamak için [Robot klavuzunu](Robot_tutorial/tr.md) deneyin ve [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py) örneğindeki programlama arayüzünü görün.


</div>


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Araçlar

Burada bir robot kurulumu oluşturmak için kullanabileceğiniz temel komutlar.

### Robotlar

6 Eksenli robotları oluşturma ve yönetme araçları


<div class="mw-translate-fuzzy">

-   ![ 30px](images/_Robot_CreateRobot.png ) [Robot Oluştur](Robot_CreateRobot/tr.md): Sahneye yeni bir robot yerleştirin
-   ![ 30px](images/_Robot_Simulate.png ) [ Robot Simülasyon](Robot_Simulate/tr.md) : Simülasyon iletişim kutusunu açar ve simüle etmenizi sağlar
-   ![ 30px](images/_Robot_Export.png ) [ Robot Dışa aktar](Robot_Export/tr.md): Bir robot program dosyasını dışa aktarın
-   ![ 30px](images/_Robot_SetHomePos.png ) [ Ana konum ayarla](Robot_SetHomePos/tr.md): Bir robotun ana konumunu ayarlayın
-   ![ 30px](images/_Robot_RestoreHomePos.png ) [ Ana konuma dön](Robot_RestoreHomePos.md): robotu ana konumuna getirir.


</div>

### Yörüngeler

Yörüngeleri oluşturmak ve değiştirmek için araçlar. Parametrik ve parametrik olmayan iki tür vardır.


<div class="mw-translate-fuzzy">

#### Parametrik olmayan yörüngeler 

-   ![ 30px](images/_Robot_CreateTrajectory.png ) [Yörünge oluştur](Robot_CreateTrajectory/tr.md): Sahneye yeni bir boş yörünge nesnesi ekler
-   ![ 30px](images/_Robot_SetDefaultOrientation.png ) [ Varsayılan yönlendirmeyi ayarla](Robot_SetDefaultOrientation/tr.md): Oryantasyon yol noktalarını varsayılan olarak oluşturulacak şekilde ayarlayın
-   ![ 30px](images/_Robot_SetDefaultValues.png ) [Varsayılan değerleri ayarla](Robot_SetDefaultValues/tr.md) Yol noktası oluşturma için varsayılan değerleri ayarlayın.
-   ![ 30px](images/_Robot_InsertWaypoint.png ) [ Bir yol noktası ekleyin](Robot_InsertWaypoint/tr.md): Geçerli robot konumundan bir yörüngeye bir yol noktası ekleyin
-   ![ 30px](images/_Robot_InsertWaypointPre.png ) [ Bir yol noktası ekle](Robot_InsertWaypointPre/tr.md): Geçerli fare konumundan bir yörüngeye bir yol noktası ekleyin


</div>


<div class="mw-translate-fuzzy">

#### Parametrik yörüngeler 

-   ![ 30px](images/_Robot_Edge2Trac.png ) [ Kenarlardan bir yörünge oluşturun](Robot_Edge2Trac.md): Kenarları yörüngeye çeviren yeni bir nesne yerleştirin
-   ![ 30px](images/_Robot_TrajectoryDressUp.png ) [ Bir yörüngeyi giydir](Robot_TrajectoryDressUp.md): Yörüngenin bir veya daha fazla özelliğini geçersiz kılmanıza izin verir
-   ![ 30px](images/_Robot_TrajectoryCompound.png ) [ Trajectory \...](Robot_TrajectoryCompound.md): Bazı tek yörüngelerin dışında bir bileşik oluşturun


</div>

## Betik


<div class="mw-translate-fuzzy">

Robot yer değiştirmelerini modellemek için kullanılan işlevlerin açıklaması için [Robot API örneği](Robot_API_example/tr.md) bölümüne bakınız.


</div>

## Kılavuzlar

-   [ Robot 6 Eksen](Robot_6-Axis/tr.md)
-   [ Robot Simülasyonu için VRML Hazırlığı](VRML_Preparation_for_Robot_Simulation/tr.md)


<div class="mw-translate-fuzzy">


{{docnav/tr|[FEM tezgahı](FEM_Workbench/tr.md)|[Standart Menü](Standard_Menu/tr.md)}}


{{Robot Tools navi/tr}}


{{Userdocnavi/tr}}


</div>


{{Robot Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Robot](Category_Robot.md) > Robot Workbench/tr
