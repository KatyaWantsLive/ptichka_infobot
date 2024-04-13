# Кейс: Телеграм бот *"Птичка"*
## Описание
Телеграмм-бот созданный для автоматизации процесса информирования жителей Сургута о правилах сдачи, помощи в определении типа вторсырья, графиках работы пунктов, проводимых мероприятиях. 

## Презентация
[Вход при помощи впн](https://pitch.com/v/tgbot-93tced)
(На презентацию принесем пдф)

## Команда "Азимут"
### Участники: 
- Старинская Светлана 
- Пачганов Алексей

## Доступные команды
### Для пользователя
- О нас
  - Как мы работаем
  - Мероприятия
- Контакты
  - Cотрудничество
  - Вопросы
- Помощь с сортировкой
  - Правила сдачи
  - Типы вторсырья
  - Классификация типа по фото

### Для администратора
- Создать рассылку
- Внести изменения
  - Мероприятия
  - Пункты

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/functions.png)

## Структура Базы данных

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/dbgraph.png)

## Классификатор вторсырья
### Классы:
- Металл
- Пластик
### Параметры обучения:
- Предобученная модель: Resnet18
- Функция потерь: CrossEntropy
- Оптимизатор: SGD
### Соотношение классов:
- Tensor 0 - Plastic 
- Tensor 1 - Metal

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/labels.png)

### Изображения в датасете:

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/tensors.png)

### Точность:

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/accuracy.png)

### Пример ответа:

![](https://github.com/KatyaWantsLive/ptichka_infobot/blob/main/metal.png)

## Cтек технологий
### Софт:
- Архитектуры функций: Figma
- БД: dbdiogram
- Нейронная сеть: Google Colab 
- Бот: Visual Studio Code
### Язык:
- Python
### Фреймворки:
- PyTorch
### Библиотеки:
- Aiogram
- NumPy
- MatPlotLib
- Pandas
- Pillow
- SQLAlchemy
  
## Запуск

Python версия 3.12

Клонирование репозитория:

```bash
git clone https://github.com/KatyaWantsLive/ptichka_infobot
cd ptichka_infobot
```

Работа с виртуальным окружением:

```bash
python3 -m venv venv
source venv\Scripts\activate.bat
```

Токен нужно получить у @BotFather и подставить его в значение TOKEN:

```bash
echo "TELEGRAM_BOT_TOKEN = ""
DB_PATH = "db/db.sqlite3" > .env
```

Обновление pip, установка зависимостей и запуск:

```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 ptichka_infobot/main.py
```



