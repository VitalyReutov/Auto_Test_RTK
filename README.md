# Auto_Test_RTK

Использовались техника выделения классов эквивалентности и техника граничных значений, так как поля ввода имеют валидацию на длину значения.
Таблица с тест-кейсами и баг-рпеортами размещена по адресу
https://docs.google.com/spreadsheets/d/1RXvfHWaKbedxsHsljw1nFU9uubnEja_spuBCe4tOyBU/edit?usp=sharing

Все тесты разбиты на 3 файла: регистрация, авторизация и восстановление пароля
Запускать тесты командой в терминале: python3 -m pytest -v --driver Chrome --driver-path /Users/vitaly/Downloads/chromedriver  {имя файла}
