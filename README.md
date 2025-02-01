# diploma_work
<!-- Опишите задачу и структуру проекта. 
Укажите, как запускать тесты. 
Так же добавьте в него ссылку на финальный проект. -->
<h1 align="center">Дипломная работа Skypro &#129302; Архитектура фреймворка</h1>
<h2>О проекте &#128161;</h2>
<b>Продукт: <a href="https://asproagile.ru/">Аспро.Agile</a></b>
<p>Задача — автоматизация UI- и API-тестов финального проекта.</p>
<ul>
    <li>
        <a href="https://drive.google.com/file/d/1rd6PYzz3EAOw7v5MpxgpJCs2R7BAVMB9/view?usp=drive_link">Тест план финального проекта</a>
    </li>
    <li>
        <a href="https://drive.google.com/file/d/1BGyCN-h3T8O38qQdZDWe3dgklFOpZZ79/view?usp=drive_link">Отчет о тестировании финального проекта</a>
    </li>
</ul>
<h3>Структура проекта &#128196;</h3>
<ul>
    <li>
        allure-result — папка с отчетами о прогонах автотестов.
    </li>
    <li>
        pages
        <ul>
            <li>
                auth.py — класс для работы со страницей и токеном авторизации в ui-тестах.
                </li>
                <li>
                config.py — конфигурационный файл для хранения значений id, токенов и данных авторизации и т.п.
                </li>
                <li>
                task_api.py — класс для работы с задачами с помощью api.
                </li>
                <li>
                task.py — класс для работы со страницей бэклогаAgile-проекта в ui-тестах.
            </li>
        </ul>
    </li>
    <li>
        test
        <ul>
                <li>
                test_api.py — файл с API-тестами.
                </li>
                <li>
                test_ui.py — файл с UI-тестами.
                </li>
        </ul>
    </li>
</ul>

<h3>Команды для работы с проектом &#9000;</h3>
<table>
    <tr>
        <th>Запуск всех тестов</th>
        <th><pre>pytest</pre></th>
    </tr>
    <tr>
        <th>Запуск только API-тестов</th>
        <th><pre>pytest -m api_test</pre></th>
    </tr>
    <tr>
        <th>Запуск только UI-тестов</th>
        <th><pre>pytest -m ui_test</pre></th>
    </tr>
    <tr>
        <th>Запуск тестов с записью результатов тестирования в Allure</th>
        <th><pre>pytest --alluredir allure-result</pre></th>
    </tr>
    <tr>
        <th>Конвертация результатов теста в отчет</th>
        <th><pre>allure serve allure-result</pre></th>
    </tr>
</table>
