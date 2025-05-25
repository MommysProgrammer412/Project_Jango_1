from .data import MENU_ITEMS

def menu_context(request):
    return {'menu_items': MENU_ITEMS}