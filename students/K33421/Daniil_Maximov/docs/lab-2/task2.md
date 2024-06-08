# Задание 2

Лабораторная:

<a href="https://github.com/TonikX/ITMO_ICT_WebDevelopment_tools_2023-2024" class="external-link" target="_blank">Текст работы</a>


???+ question "Задание"

    **Задача 2. Параллельный парсинг веб-страниц с сохранением в базу данных.**

    **Задача:** Напишите программу на Python для параллельного парсинга нескольких веб-страниц с сохранением данных в базу данных с использованием подходов threading, multiprocessing и async. Каждая программа должна парсить информацию с нескольких веб-сайтов, сохранять их в базу данных.
    
    **Подробности задания:**
    1. Напишите три различных программы на Python, использующие каждый из подходов: threading, multiprocessing и async.
    2. Каждая программа должна содержать функцию parse_and_save(url), которая будет загружать HTML-страницу по указанному URL, парсить ее, сохранять заголовок страницы в базу данных и выводить результат на экран.
    3. Используйте базу данных из лабораторной работы номер 1 для заполенния ее данными. Если Вы не понимаете, какие таблицы и откуда Вы могли бы заполнить с помощью парсинга, напишите преподавателю в общем чате потока.
    4. Для threading используйте модуль threading, для multiprocessing - модуль multiprocessing, а для async - ключевые слова async/await и модуль aiohttp для асинхронных запросов.
    5. Создайте список нескольких URL-адресов веб-страниц для парсинга и разделите его на равные части для параллельного парсинга.
    6. Запустите параллельный парсинг для каждой программы и сохраните данные в базу данных.
    7. Замерьте время выполнения каждой программы и сравните результаты.
    
    **Дополнительные требования:**
    - Сделайте документацию, содержащую описание каждой программы, используемые подходы и их особенности.
    - Включите в документацию таблицы, отображающие время выполнения каждой программы.
    - Прокомментируйте результаты сравнения времени выполнения программ на основе разных подходов.

=== "async"

    ```Python title="async_worker.py"
    --8<-- "lab-2/task2/async_worker.py"
    ```

=== "multiprocess"

    ```Python title="multiprocess_worker.py"
    --8<-- "lab-2/task2/multiprocess_worker.py"
    ```

=== "threading"

    ```Python title="threading_worker.py"
    --8<-- "lab-2/task2/threading_worker.py"
    ```




=== "results"

    **Задача 1. Различия между threading, multiprocessing и async в Python.**


    | Worker              | Time (seconds)     |
    |-----------------------|--------------------|
    | AsyncWorker         | 1.4784667491912842 |
    | MultiprocessWorker  | 7.75731086730957   |
    | ThreadingWorker     | 7.163795232772827  |