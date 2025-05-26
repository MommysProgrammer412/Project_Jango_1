from django import template

register = template.Library()

@register.filter(name='format_price')
def format_price(value, currency='₽'):
    """Форматирует цену добавляя знак рубля"""
    # Преобразуем значение в число, если оно пришло строкой
    try:
        numeric_value = float(value)
        formatted_number = '{:,.0f}'.format(numeric_value).replace(',', ' ')
        # Добавляем символ рубля
        return f"{formatted_number} {currency}"
    except (ValueError, TypeError):
        # Если не удалось преобразовать в число, возвращаем исходное значение
        return value

@register.simple_tag(name='format_name')
def format_name(name):
    if not name:
        return ""
    return f'Мастер {name.capitalize()}'

@register.simple_tag(name='format_position')
def format_position(position, param1, param2):
    if not position:
        return ""
    return f'Должность: {position.capitalize()} {param1} {param2}'