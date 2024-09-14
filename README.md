# Movie-review-classifier

## Описание
Этот репозиторий содержит модель, подготовленную в рамках тестового задания для junior-специалистов
по направлению Data Science АО "Гринатом". 

**С демо модели можно ознакомиться по [ссылке](https://huggingface.co/spaces/wlwla/Movie-review-classifier)**

## Начало работы
### Требования
Для успешного запуска проекта необходимы:
- Python 3.12.x и выше
- Необходимые зависимости
- Файл `.pth` с весами модели

### Подготовка окружения

Для развертывания сервиса выполните следующие шаги:

1. Клонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/wlwlaa/Movie-review-classifier.git
```

2. Перейдите в папку проекта:
```bash
cd Movie-review-classifier
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### Запуск проекта

1.  Запустите файл app.py:
```bash
python app.py
```
2. Перейдите по указаннному в консоли URL адресу в браузере:
```bash
127.0.0.1:7860
```

## Модель
### Описание
В этом проекте моделью является fine-tuned трансформер [DistilBERT base uncased finetuned SST-2](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english). Это упрощенная версия классифкатора BERT, предоставляя меньший размер и меньшие вычислительные затраты, при этом, сохраняя высокую точность.

### Метрики
Ключевые метрики:
- **F1 score**: 0.9564
- **Accuracy**: 0.9564


## Датасет
Для дообучения использовался [Large Movie Review Dataset v1.0](https://ai.stanford.edu/~amaas/data/sentiment/), включающий в себя 50,000 различных отзывов к фильмам с оценкой от 1 до 10. Данные были предварительно очищены от "шума", перемешаны и разделены на обучающую/тестовую выборку в отношении 80/20.

## Обучение
Обучение производилось в среде Google Colab Pro на ускорителе Nvidia L4.
Подробнее с процессом обучения можно ознамиться в файле [`Greenatom.ipynb`](https://github.com/wlwlaa/Movie-review-classifier/blob/main/Greenatom.ipynb), находящимся в репозитории.

## Лицензия
Проект распространятся под лицензией Apache 2.0 - подробнее в файле [LICENSE](https://github.com/wlwlaa/Movie-review-classifier/blob/main/LICENSE).