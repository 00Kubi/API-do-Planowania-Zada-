# API do Planowania Zadań

API do planowania zadań z obsługą zależności i zadań cyklicznych stworzono przy użyciu Flask. Umożliwia ono użytkownikom zarządzanie zadaniami, w tym ich tworzenie, edytowanie, usuwanie oraz odczytywanie.

## Spis Treści
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Endpointy API](#endpointy-api)
- [Przykłady Użycia](#przykłady-użycia)
- [Podsumowanie](#podsumowanie)

## Wymagania
- Python 3.6+
- Flask

## Instalacja
Aby zainstalować wszystkie wymagane biblioteki, użyj poniższego polecenia:

```bash
pip install Flask
```

## Użycie
Aby uruchomić aplikację, wykonaj polecenie:

```bash
python app.py
```

API będzie dostępne pod adresem `http://127.0.0.1:5000`.

## Endpointy API

### 1. Trasa Główna
- **GET /**  
  Zwraca powitanie.
  - **Odpowiedź:**
    ```json
    {
      "message": "Witaj w API do planowania zadań!"
    }
    ```

### 2. Tworzenie Zadania
- **POST /tasks**  
  Tworzy nowe zadanie.
  - **Body:**
    ```json
    {
      "title": "Zadanie 1",
      "description": "Opis zadania 1",
      "dependencies": [],
      "interval": "daily"
    }
    ```
  - **Odpowiedź:**
    ```json
    {
      "task_id": 1
    }
    ```

### 3. Odczyt Wszystkich Zadań
- **GET /tasks**  
  Zwraca listę wszystkich zadań.
  - **Odpowiedź:**
    ```json
    [
      {
        "task_id": 1,
        "title": "Zadanie 1",
        "description": "Opis zadania 1",
        "dependencies": [],
        "interval": "daily",
        "created_at": "2024-10-21T19:11:54.000000"
      }
    ]
    ```

### 4. Odczyt Konkretnego Zadania
- **GET /tasks/{task_id}**  
  Zwraca szczegóły zadania o podanym ID.
  - **Odpowiedź:**
    ```json
    {
      "task_id": 1,
      "title": "Zadanie 1",
      "description": "Opis zadania 1",
      "dependencies": [],
      "interval": "daily",
      "created_at": "2024-10-21T19:11:54.000000"
    }
    ```

### 5. Aktualizacja Zadania
- **PUT /tasks/{task_id}**  
  Aktualizuje istniejące zadanie.
  - **Body:**
    ```json
    {
      "title": "Zaktualizowany tytuł",
      "description": "Zaktualizowany opis",
      "dependencies": [],
      "interval": "weekly"
    }
    ```
  - **Odpowiedź:**
    ```json
    {
      "message": "Zadanie zaktualizowane!"
    }
    ```

### 6. Usunięcie Zadania
- **DELETE /tasks/{task_id}**  
  Usuwa zadanie o podanym ID.
  - **Odpowiedź:**
    ```json
    {
      "message": "Zadanie usunięte!"
    }
    ```

### 7. Zwrócenie Zadań do Wykonania
- **GET /tasks/due**  
  Zwraca listę zadań, które są gotowe do wykonania.
  - **Odpowiedź:**
    ```json
    [
      {
        "task_id": 1,
        "title": "Zadanie 1"
      }
    ]
    ```

## Przykłady Użycia

### Tworzenie Zadania
```bash
curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Zadanie 1", "description": "Opis zadania 1", "dependencies": [], "interval": "daily"}'
```

### Odczyt Wszystkich Zadań
```bash
curl -X GET http://127.0.0.1:5000/tasks
```

### Odczyt Konkretnego Zadania
```bash
curl -X GET http://127.0.0.1:5000/tasks/1
```

### Aktualizacja Zadania
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"title": "Zaktualizowany tytuł"}'
```

### Usunięcie Zadania
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

### Odczyt Zadań do Wykonania
```bash
curl -X GET http://127.0.0.1:5000/tasks/due
```

## Podsumowanie
API do planowania zadań umożliwia użytkownikom łatwe zarządzanie swoimi zadaniami, w tym ich tworzenie, aktualizowanie i usuwanie, a także śledzenie zadań cyklicznych. Możesz rozwijać to API, dodając więcej funkcji, takich jak autoryzacja użytkowników, przechowywanie danych w bazie danych czy integracja z systemami powiadomień.