# validator.py

# Список запрещённых подстрок (для примера)
FORBIDDEN_WORDS = ["spam", "hack", "bad"]

def validate_code(code: str) -> bool:
    code = code.strip()
    
    if not code:
        return False

    # Правило 1: длина ровно 8 символов (как у промокода)
    if len(code) != 8:
        return False

    # Правило 2: только латиница и цифры
    if not code.isalnum():
        return False
    
    # Правило 3: только латинские буквы (не кириллица!)
    has_latin = all(
        ('a' <= c.lower() <= 'z') or c.isdigit() 
        for c in code
    )
    if not has_latin:
        return False

    # Правило 4: не начинается с цифры
    if code[0].isdigit():
        return False

    # Правило 5: нет запрещённых слов (регистронезависимо)
    code_lower = code.lower()
    for word in FORBIDDEN_WORDS:
        if word in code_lower:
            return False

    return True


def calculate_stats(codes: list) -> str:
    total = len(codes)
    
    # Считаем, сколько кодов начинаются на каждую букву
    starts_with = {}
    for c in codes:
        first_letter = c[0].upper()
        starts_with[first_letter] = starts_with.get(first_letter, 0) + 1

    top_letters = sorted(
        starts_with.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:3]  # топ-3 буквы

    letters_str = ", ".join(f"{letter}: {count}" for letter, count in top_letters)

    result = (
        f"Всего валидных кодов: {total}\n"
        f"Самые частые первые буквы: {letters_str if letters_str else 'нет'}"
    )
    return result
