def parse_names(names):
    splitted_names = names.split(" / ")
    name_pt = splitted_names[0]
    name_en = splitted_names[1] if len(splitted_names) > 1 else ""
    return name_pt, name_en


def split_name_code(name_ligapokemon):
    names = name_ligapokemon.split(" (")[0]
    name_pt, name_en = parse_names(names)

    code = name_ligapokemon.split(" (")[1].split("/")[0]

    return {"name_pt": name_pt, "name_en": name_en, "code": code}
