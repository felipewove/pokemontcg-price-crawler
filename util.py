def split_name_code(name_ligapokemon):
    names = " ".join(name_ligapokemon.split(" ")[:-1])
    name_pt, name_en = NameUtil.parse_names(names)

    code = name_ligapokemon.split(" (")[-1].split("/")[0]

    return {"name_pt": name_pt, "name_en": name_en, "code": code}


def parse_price(raw_price):
    """
    Receives "R$ XX,XX\xa0" and returns "XX.XX"
    """
    sanitized_price = MoneyUtil.sanitize(raw_price)
    price = MoneyUtil.remove_currency(sanitized_price)
    return price.replace(",", ".")


class MoneyUtil:
    def sanitize(bad_string):
        """
        Because LigaPokemon shows its value with a &nbsp; at the end
        Receives "R$ XX,XX\xa0" and returns "R$ XX,XX"
        """
        return bad_string[:-1]

    def remove_currency(raw_price):
        """
        Receives "R$ XX,XX" and returns "XX,XX"
        """
        return raw_price.split(" ")[-1]


class NameUtil:
    def parse_names(names):
        splitted_names = names.split(" / ")
        name_pt = splitted_names[0]
        name_en = splitted_names[1] if len(splitted_names) > 1 else name_pt
        return name_pt, name_en
