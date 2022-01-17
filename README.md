
Проект staff_editor позволяет легко отслеживать и вносить изменения в структуру любого предприятия. 
Благодаря staff_editor любой авторизованный пользователь может узнать наполнение того или иного подразделения и пренадлежность сотрудника к отделу или занимаемую им должности. 
Проект является хорошо масштабируемым блягодаря представлениям, реализованным при помощи mixins.
В работе использвал фреймворк Django 4 и библиотеку django-crispy-forms.
В качестве СУБД использовал Postgresql.

Далее представлена информация о структуре проекта.

Проектирование информационных обьектов:
1.Список обьектов, таблиц:
1) Подрразделение(отдел) Department
2) Должность Position
3) Пользователь Employee

2.Характеристики информационных обьектов
1) Department: Название, Сотрудники
2) Position: Название, Сотрудники
3) Employee: Фио,текущий отдел, текущая должность

3.Связи между таблицами 
1) у отдого одела может быть много сотрудников. 
2) В одной должности может быть много сотрудников
3) У одого ссотрудника одна должность и однин отдел

4. Страницы сайта
1) Справочник должностей 
2) Список пользователей 
3) Карточки сотрудников
4) Страницы регистрации и авторизации
5) Формы добавления/редактирования/удаления пользователя/должности/отдела

5.Подробнее о структуре сайта(Содержание)
1)Главная страница: преветственное сообщение, кнопки: -'log in', 'sign in'
2)После аторизации появляются следующие кнопки: -'Подразделения' -'Должности' -'Сотрудники'
3)При переходе на страницу пользователи возвращается список ФИО сотрудников, напроттив каждого сотрудника кнопка 'Подробнее'
При нажатии на которую возвразается карточа данного соотрудника
4) На странице карточки сотрудника отображается следующая информация:
-ФИО -Текущая должность(с сылкой на него) -Текущее подразделение(с сылкой на него) + кнопки -'Изменить' 
5)При переходе по ссылке 'Подразделения'/'Должности' возвразается список подразделений/должностей + конопки -'Добавить', + напротив каждого подразделения кнопка -'подробнее'
6)При переходе по ссылке 'Подробнее' возвращается список сотрудников данного подразделения/должности