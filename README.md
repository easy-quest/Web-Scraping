Начиная
Легко начать работу с запросами Pull Github для Custom Code. Просто выполните следующие шаги, чтобы начать.

Установите расширение изнутри VS-кода или загрузите его с рынка.
Откройте желаемый репозиторий GitHUB в VS-коде.
На панели активности появится новый просмотрлетлет, который показывает список запросов и проблем по тяги.
Используйте кнопку на просмотру, чтобы войти в GitHub.
Вам может потребоваться настроить настройку githubpullrequests.remotes, по умолчанию расширение будет искать PRS для начала происхождения и выше по потоку. Если у вас есть разные пульты, добавьте их в список удалений.

Вы должны быть хороши, чтобы пойти!


Языки, которые символ «#» не должен использоваться для привлечения предложений о завершении проблем.


Github Pull запросы: Queries
Указывает, какие запросы следует использовать в Github Pull запрашивает дерево. Каждый объект запроса имеет метку, которая будет показана в дереве и поисковой запрос с использованием синтаксиса поиска GitHub. Переменная ${user} Может использоваться для указания зарегистрированного пользователя в поисках. По умолчанию эти запросы определяют категории "Waiting For My Review", "Assigned To Me" and "Created By Me". Если вы хотите сохранить их, убедитесь, что они все еще в массиве, когда вы измените настройку.