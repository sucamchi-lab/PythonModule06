if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXEPTION")
    import alchemy.grimoire.dark_spellbook

    result = alchemy.grimoire.dark_spellbook.dark_spell_record(
        "Poison", "bats, arsenic, eyeball")
    print(f"Testing record dark spell: {result}")
