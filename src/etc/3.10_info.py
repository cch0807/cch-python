# Structural Pattern Matching(a.k.a Switch)

# Matching literal patterns
def literal_match(lang: str):
    match lang:
        case "korean":
            return "Great !"
        case "english":
            return "Very nice!"
        case _:
            return "Which language do you speak?"


literal_match(lang="english")
