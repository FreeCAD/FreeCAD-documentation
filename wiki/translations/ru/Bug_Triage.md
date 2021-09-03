





{{TOCright}}

## Для чего {#для_чего}


{{ColoredParagraph|Triageː

1a :  the sorting of and allocation of treatment to patients and especially battle and disaster victims according to a system of priorities designed to maximize the number of survivors

1b :  the sorting of patients (as in an emergency room) according to the urgency of their need for care

2:  the assigning of priority order to projects on the basis of where funds and other resources can be best used, are most needed, or are most likely to achieve success
}}

Сортировка ошибок важна для организации и приоритизации ошибок / функций/исправлений по сравнению с FreeCAD Bug Tracker. Если эта задача игнорируется, проект может пострадать от так называемого \"Bloat Bugtracker\", который в основном состоит из накопления и разложения пропущенных билетов. Сортировка также помогает идентифицировать дубликаты билетов, которые, как правило, накапливаются, особенно если существует давняя нерешенная проблема, о которой команда FC знает, но не имеет необходимых ресурсов, независимо от причины.

## Как происходит сортировка {#как_происходит_сортировка}

### Статус Тикета {#статус_тикета}

#### New

Per MantisBT docsː {{ColoredText|This is the landing status for new issues. Issues stay in this status until they areː assigned, acknowledged, confirmed or resolved. }}

In other words, **NEW** status indicates several thingsː

1.  Ticket hasn\'t been confirmed.
2.  Ticket is still in process, i.e. Triage/Devs still evaluating/clarifying details of ticket from OP.
3.  FreeCAD team hasn\'t decided what to do with this ticket yet.

All current [open FreeCAD tickets with **NEW** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=10&hide_status=80).

#### Подтвержден

#### Обратная связь {#обратная_связь}

Тикеты обозначаются в этом состоянии, когда OP просит предоставить дополнительную информацию.

Тикет находится на рассмотрении в зависимости от участия ОП. Например, в тикете отсутствует информация о версии FC; или, возможно, требуется определенное имя или версия сторонней библиотеки и т. Д\... Разработчикам необходимо устанавливать этот статус при каждом ответе на запрос, чтобы указать, что запрос находится на рассмотрении. Это важно из-за возможности того, что ОП пренебрегает ответом, что имеет высокую вероятность того, что тикет условно говоря \"протухнет\" в трекере.

Когда OP ответит, статус билета автоматически изменится на \"Новый\". Затем билет необходимо пересмотреть, чтобы решить, что необходимо.

Продолжение обсуждения данной темы в [FreeCAD форуме](https://forum.freecadweb.org/viewtopic.php?f=10&t=23005).

All current [open FreeCAD tickets with **FEEDBACK** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=20&hide_status=80) in the FC bugtracker.

#### Подтверждён

Когда тикет подтвержден, он был либоː

-   ошибка, которая была воспроизведена
-   функция, которая была отмечена зеленым цветом, чтобы считаться действительной.

Теперь он готов для назначения разработчику или разработчиком.

All current [open FreeCAD tickets with **CONFIRMED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=40&hide_status=80) in the FC tracker.

#### Назначено

Само собой разумеется, что эти билеты были назначены конкретному разработчику.

All current [open FreeCAD tickets with **ASSIGNED** status](https://freecadweb.org/tracker/view_all_set.php?type=1&temporary=y&status=50&hide_status=80) in the FC tracker.

#### Решено

Эти тикеты были разрешены, но еще не закрыты, скорее всего, потому, что им нужно подтверждение того, что тикет был исправлен.

------------------------------------------------------------------------

### Ticket Resolutioɲ {#ticket_resolutioɲ}

#### Open

Self-explanatory, all tickets remain as \'open\' if they are still relevant at the discretion of the FC team.

#### Fixed

Tickets that have been fixed.

#### Unable to reproduce {#unable_to_reproduce}

Tickets deemed un-reproducible

#### Duplicate

Tickets that are or have a duplicate ticket.

#### No change required {#no_change_required}

Tickets were it has been ascertained that no modifications are necessary.

#### Won\'t fix {#wont_fix}

FC team has rejected the ticket request for whatever reason stated.

#### Not fixable {#not_fixable}

#### Reopened

Tickets that have been closed me then re-opened for a relevant reason. Most likely that the issue has resurfaced or wasn\'t totally fixed.

#### Suspended

### Приоритет Тикета {#приоритет_тикета}

#### Immediatə

#### Urgent

#### High

#### Normal

#### Low

#### None

### Степень важности Тикета {#степень_важности_тикета}

#### Block

#### Crash

#### Major (Важный) {#major_важный}

#### Minor (Незначительный) {#minor_незначительный}

#### Tweak

#### Текст

#### Trivial

#### Feature

## Tagging Tickets {#tagging_tickets}

An important methodology to track tickets by a certain subject/theme/category. It\'s important that **Existing Tags** be used to tag issues **before** new tags are created. If duplicate or superfluous tags are created the bug tracker admin is responsible to remove them and if possible retag said tickets.

## Related

[Bugtracker](Tracker.md)







[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Administration{{\#translation:}}](Category:Administration.md)
