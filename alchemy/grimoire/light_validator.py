def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredient = [item.lower()
                          for item in light_spell_allowed_ingredients()]
    ingredient_list = [item.strip().lower()
                       for item in ingredients.split(",") if item.strip()]

    if any(ingredient in allowed_ingredient for ingredient in ingredient_list):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
