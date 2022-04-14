# Тесты для курса ННГУ по глубокому обучению.

## Описание

Это решение запускает тесты для проекта [Depth Estimation](https://paperswithcode.com/paper/high-quality-monocular-depth-estimation-via).
[Исходный код](https://github.com/ialhashim/DenseDepth) примера.

Решение для работы использует уже обученую модель [NYU Depth V2](https://drive.google.com/file/d/19dfvGvDfCRYaqxVKypp1fRHwK7XtSjVu/view?usp=sharing).

## Требования

- Ubuntu (Вероятно, под WSL тоже заработает)
- python 3
- Docker без *sudo*

## Запуск

### Простой запуск примера:

```
python3 run.py
```

Запустится докер с обученной моделью. Построится коллаж из тестовых картинок после обработки. Результат будет записан в `test.png` в рабочей директории.

### Дополнительные возможности:

Модель поддерживает картинки в формате `png` разрешением 640х480 с тремя каналами 

Скрипт `run.py` имеет два аргумета `--tests` и `--out`. В них можно опционально передать директорию с тестовыми картинками и жиректорию для записи результата.

Запуск:

```
python3 run.py --tests <path-to-tests> --out <path-to-out>
```

## Сборка образа

Для сборки образа необходиа обученная модель [NYU Depth V2](https://drive.google.com/file/d/19dfvGvDfCRYaqxVKypp1fRHwK7XtSjVu/view?usp=sharing).

Её необходимо скачать и положить в директорию с `Dockerfile`, а затем запустить сборку образа:

```
docker build .
```
