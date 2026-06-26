from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients_dark(ingredients: str) -> str:
    allowed_ingredients = [item.lower()
                           for item in dark_spell_allowed_ingredients()]
    ingr_list = [item.lower() for item in ingredients.split(",")]

    if any(ingredient in allowed_ingredients for ingredient in ingr_list):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
