# 🎸 Guitar Chords Bot для Telegram

Telegram-бот для поиска аккордов гитары для песен на английском, русском и украинском языках.

## ✨ Возможности

- 🎸 **Поиск аккордов по исполнителю и названию трека**
- 🎲 **Случайные популярные аккорды**
- 📖 **Интеграция с Ultimate Guitar**
- 🌍 **Поддержка песен на разных языках**
- ⚡ **Быстрый поиск в реальном времени**

## 📋 Требования

- Python 3.9+
- pip
- Интернет соединение
- Telegram Bot Token (получи в @BotFather)

## 🚀 Быстрый старт (Локально)

### 1. Клонируем репозиторий
```bash
git clone https://github.com/lenyfyb-del/guitar-chords-bot.git
cd guitar-chords-bot
```

### 2. Создаём виртуальное окружение
```bash
python -m venv venv

# На Windows:
venv\Scripts\activate

# На Linux/Mac:
source venv/bin/activate
```

### 3. Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

### 4. Настраиваем токен

**⚠️ ВАЖНО: Если ты использовал старый токен - отмени его!**

- Напиши в Telegram: @BotFather
- Команда: `/revoke`
- Выбери бота и подтверди отмену токена
- Команда: `/newbot`
- Следуй инструкциям, получи новый токен

Затем:
```bash
# Отредактируй .env файл
nano .env
# или используй редактор (вставь новый токен вместо ТУТ_ВСТАВЬ_НОВЫЙ_ТОКЕН)
```

### 5. Запускаем бота
```bash
python bot.py
```

Если всё работает, увидишь:
```
INFO:root:🎸 Бот запущен!
```

## 🖥️ Деплой на VPS (Ubuntu/Debian)

### 1. Подключаемся к VPS по SSH
```bash
ssh user@your_vps_ip
```

### 2. Обновляем систему
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 3. Клонируем проект
```bash
cd /home/user
git clone https://github.com/lenyfyb-del/guitar-chords-bot.git
cd guitar-chords-bot
```

### 4. Создаём окружение
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Настраиваем .env
```bash
nano .env
# Вставляем новый токен (Ctrl+X, затем Y, Enter для сохранения)
```

### 6. Создаём systemd сервис (для автозагрузки)
```bash
sudo nano /etc/systemd/system/guitar-bot.service
```

Вставляем:
```ini
[Unit]
Description=Guitar Chords Telegram Bot
After=network.target

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/guitar-chords-bot
Environment="PATH=/home/user/guitar-chords-bot/venv/bin"
ExecStart=/home/user/guitar-chords-bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Сохраняем: `Ctrl+X`, `Y`, `Enter`

### 7. Включаем и запускаем сервис
```bash
sudo systemctl daemon-reload
sudo systemctl enable guitar-bot
sudo systemctl start guitar-bot

# Проверяем статус:
sudo systemctl status guitar-bot
```

### 8. Просмотр логов
```bash
# Живые логи:
sudo journalctl -u guitar-bot -f

# Последние 50 строк:
sudo journalctl -u guitar-bot -n 50
```

## 🔄 Обновление на VPS
```bash
cd /home/user/guitar-chords-bot
git pull origin main
sudo systemctl restart guitar-bot
```

## 📝 Структура проекта
```
guitar-chords-bot/
├── bot.py           # Основной код бота
├── parser.py        # Парсер Ultimate Guitar
├── requirements.txt # Зависимости Python
├── .env            # Переменные окружения (НЕ коммитим!)
├── .gitignore      # Игнорируемые файлы
└── README.md       # Этот файл
```

## 🐛 Решение проблем

### "ModuleNotFoundError: No module named 'telegram'"
```bash
pip install -r requirements.txt
```

### "TELEGRAM_TOKEN не найден в .env"
Проверь, что в .env файле правильно указан токен:
```bash
cat .env
```

### Бот не отвечает на VPS
```bash
# Проверяем статус:
sudo systemctl status guitar-bot

# Смотрим ошибки:
sudo journalctl -u guitar-bot -n 100

# Перезагружаем:
sudo systemctl restart guitar-bot
```

### Ошибка при парсинге
- Проверь интернет соединение
- Ultimate Guitar может блокировать запросы - измени User-Agent в parser.py
- Попробуй вручную открыть ultimate-guitar.com

## 🔐 Безопасность

⚠️ **НИКОГДА** не коммитьте .env файл с реальным токеном!

Проверить, не случайно ли был закоммичен токен:
```bash
git log --all --full-history -- .env
```

Если был закоммичен - срочно отмени токен в @BotFather!

## 📄 Лицензия

MIT

## 👨‍💻 Автор

Guitar Chords Bot - 2026

---

**Вопросы?** Создавай Issue в репозитории! 🎸
