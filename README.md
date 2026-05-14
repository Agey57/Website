# News Project (Второе задание: Модели)

Django-проект для новостного сайта. Выполнено второе обязательное задание курса.

## Структура
- **news/**: Приложение с моделями Article, Tag, Scope.
  - Article: заголовок, текст, дата, изображение (ManyToMany с тегами через Scope).
  - Scope: связь article-tag с is_main и unique constraint.
- Миграции: применены (проверить `python manage.py migrate`).
- Admin: настроен, media-uploads работают.
- Views: articles_list (пока базовая).

## Запуск
1. `pip install -r requirements.txt` (или `django==5.2.14`).
2. `python manage.py makemigrations news && python manage.py migrate`.
3. `python manage.py createsuperuser`.
4. `python manage.py runserver` — сайт на http://127.0.0.1:8000/, admin на /admin/.

## Файлы для проверки
- models.py: модели с отношениями.
- settings.py: MEDIA_URL/ROOT, INSTALLED_APPS.
- urls.py: подключены.

Готово для зачёта!
