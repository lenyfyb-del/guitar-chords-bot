import aiohttp
import asyncio
import logging
from bs4 import BeautifulSoup
import random

logger = logging.getLogger(__name__)

# Популярные песни для случайного выбора
POPULAR_SONGS = [
    ("Pink Floyd", "Comfortably Numb"),
    ("Led Zeppelin", "Stairway to Heaven"),
    ("The Beatles", "Hey Jude"),
    ("Nirvana", "Smells Like Teen Spirit"),
    ("Queen", "Bohemian Rhapsody"),
    ("Guns N' Roses", "Sweet Child o' Mine"),
    ("David Bowie", "Space Oddity"),
    ("The Rolling Stones", "Satisfaction"),
    ("Jimi Hendrix", "Purple Haze"),
    ("AC/DC", "Back in Black"),
    ("Imagine Dragons", "Radioactive"),
    ("The Who", "Baba O'Riley"),
    ("Metallica", "Enter Sandman"),
    ("Black Sabbath", "Paranoid"),
    ("Deep Purple", "Smoke on the Water"),
    ("Земфира", "Светлая"),
    ("Чайф", "Белый танец"),
    ("Кино", "Видели ночь"),
    ("Кипелов", "Я свободен"),
    ("Калинов Мост", "Жить хорошо"),
]

async def search_chords(artist: str, song_title: str) -> str:
    """
    Поиск аккордов на Ultimate Guitar
    """
    try:
        # Подготавливаем поисковый запрос
        search_query = f"{artist} {song_title}"
        url = f"https://www.ultimate-guitar.com/search.php?search_type=title&value={search_query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    logger.warning(f"Search failed with status {response.status}")
                    return None
                
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                # Ищем первый результат с аккордами
                results = soup.find_all('a', {'class': 'ug-item'}, limit=5)
                
                if not results:
                    logger.info(f"No results found for {artist} - {song_title}")
                    return None
                
                # Пробуем каждый результат
                for result in results:
                    song_url = result.get('href')
                    if not song_url or 'chords' not in song_url.lower():
                        continue
                    
                    # Полный URL
                    if not song_url.startswith('http'):
                        song_url = 'https://www.ultimate-guitar.com' + song_url
                    
                    # Получаем страницу с аккордами
                    async with session.get(song_url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as chord_response:
                        if chord_response.status != 200:
                            continue
                        
                        chord_html = await chord_response.text()
                        chord_soup = BeautifulSoup(chord_html, 'html.parser')
                        
                        # Ищем текст песни и аккорды
                        content = chord_soup.find('pre', {'class': 'js-tab-content'})
                        
                        if content:
                            chords_text = content.get_text()
                            
                            # Форматируем вывод
                            result_text = f"""
<b>🎸 Найденные аккорды:</b>

<b>Исполнитель:</b> {artist}
<b>Песня:</b> {song_title}

<pre>{chords_text[:1500]}</pre>

<b>🔗 Полная версия:</b> <a href="{song_url}">Ultimate Guitar</a>
"""
                            return result_text
                
                return None
                
    except asyncio.TimeoutError:
        logger.error("Request timeout while searching for chords")
        return None
    except Exception as e:
        logger.error(f"Error searching chords: {e}")
        return None

async def get_random_song() -> str:
    """
    Получить случайную популярную песню с аккордами
    """
    artist, song_title = random.choice(POPULAR_SONGS)
    return await search_chords(artist, song_title)
