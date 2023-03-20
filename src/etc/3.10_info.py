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

# Detecting and deconstructing different structures in your data


def get_name(user: dict):
    match user:
        case {"location": {"city": city, "country": country}}:
            return f"{city}, {country}"
        case {"location": location}:
            return location


v1 = {"location": "seoul, south korea"}
v2 = {"location": {"city": "seoul", "country": "south korea"}}

print(get_name(user=v1))

# Using different kinds of patterns
