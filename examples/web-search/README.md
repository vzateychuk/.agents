# Web Search Extension for pi

## Установка
```bash
uv pip install -r requirements.txt
```

## Использование
Чтобы искать в Интернете, вызовите:
```bash
pi --extend web-search search-web "how to learn ai"
```

Или используйте в скрипте:
```python
from extension import handle_query
print(handle_query("how to learn ai"))
```

## Поиск через разные системы
- **DuckDuckGo Instant Answer API** (по умолчанию).
- **Google Custom Search API** (замените `extension.py` и используйте API ключ).
- **Brave Search API** (без ключа).

## Примеры результатов
```
🔍 **Web Search:**
✅ **Result:** AI is the simulation of human intelligence...
🌐 **Source:** [https://ai.google](https://ai.google)
```