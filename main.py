from flask import Flask, render_template, request
from random import choices

# https://www.sysadmintutorials.com/build-ultimate-free-password-generator-python-flask/

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        quantity = int(request.form["quantity"])
        include_adverb = "adverb" in request.form
        include_verb = "verb" in request.form
        include_adjective = "adjective" in request.form
        include_animal = "animal" in request.form
        enable_starts_with = "enable_starts_with" in request.form
        try:
            starts_with = request.form["starts_with"]
        except:
            starts_with = ""

        phrase_list = generate_name_list(
            include_adverb,
            include_verb,
            include_adjective,
            include_animal,
            quantity,
            starts_with,
        )

        return render_template(
            "index.html",
            phrase_list=phrase_list,
            include_adverb=include_adverb,
            include_verb=include_verb,
            include_adjective=include_adjective,
            include_animal=include_animal,
            default_quantity=quantity,
            enable_starts_with=enable_starts_with,
            starts_with=starts_with,
        )

    return render_template(
        "index.html",
        include_adverb=True,
        include_verb=True,
        include_adjective=True,
        include_animal=True,
        default_quantity=1,
        starts_with="",
    )


def generate_name_list(
    include_adverb,
    include_verb,
    include_adjective,
    include_animal,
    quantity,
    starts_with,
):
    if include_adverb:
        adverbs = get_words("adverb", quantity, starts_with)
    if include_verb:
        verbs = get_words("verb", quantity, starts_with)
    if include_adjective:
        adjectives = get_words("adjective", quantity, starts_with)
    if include_animal:
        animals = get_words("animal", quantity, starts_with)

    phrase_list = []
    for i in range(0, quantity):
        string = ""
        string = f"{string} {adverbs[i]}" if include_adverb else string
        string = f"{string} {verbs[i]}" if include_verb else string
        string = f"{string} {adjectives[i]}" if include_adjective else string
        string = f"{string} {animals[i]}" if include_animal else string
        phrase_list += [string]
    return phrase_list


def get_words(word_type: str, quantity: int, start_letter: str):
    inFile = open(f"./resources/{word_type}.txt", "r")
    word_list = inFile.read().splitlines()
    if start_letter:
        word_list = [x for x in word_list if x.lower().startswith(start_letter.lower())]
    return choices(word_list, k=quantity)


if __name__ == "__main__":
    app.run(debug=True)
