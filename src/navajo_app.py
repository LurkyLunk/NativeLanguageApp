import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dictionary of Navajo words and their English translations
navajo_dictionary = {
    "hello": {"translation": "Yá'át'ééh", "pronunciation": "placeholder"},
    "goodbye": {"translation": "Hózhǫ́ǫ́go", "pronunciation": "placeholder"},
    "thank you": {"translation": "Ahéhee'", "pronunciation": "placeholder"},
    "yes": {"translation": "Ahe'", "pronunciation": "placeholder"},
    "no": {"translation": "Dóó", "pronunciation": "placeholder"},
    "water": {"translation": "Tó", "pronunciation": "placeholder"},
    "sun": {"translation": "Tááłá'", "pronunciation": "placeholder"},
    "moon": {"translation": "Tł'ízíłání", "pronunciation": "placeholder"},
    "tree": {"translation": "Chʼil", "pronunciation": "placeholder"},
    "rock": {"translation": "Tsé", "pronunciation": "placeholder"},
    "fire": {"translation": "Doo", "pronunciation": "placeholder"},
    "earth": {"translation": "Naaki", "pronunciation": "placeholder"},
    "wind": {"translation": "Binii", "pronunciation": "placeholder"},
    "rain": {"translation": "Tłʼiish", "pronunciation": "placeholder"},
    "snow": {"translation": "Azee'", "pronunciation": "placeholder"},
    "mountain": {"translation": "Dził", "pronunciation": "placeholder"},
    "dog": {"translation": "łééchąąʼí", "pronunciation": "placeholder"},
    "horse": {"translation": "Bááh", "pronunciation": "placeholder"},
    "sheep": {"translation": "Dibé", "pronunciation": "placeholder"},
    "cow": {"translation": "Daaztsaastsoh", "pronunciation": "placeholder"},
    "corn": {"translation": "Naadaałtsʼoosii", "pronunciation": "placeholder"},
    "potato": {"translation": "Hashké", "pronunciation": "placeholder"},
    "bread": {"translation": "Dááko", "pronunciation": "placeholder"},
    "butterfly": {"translation": "Tséłchííʼ", "pronunciation": "placeholder"},
    "bird": {"translation": "Dibéyázhí", "pronunciation": "placeholder"},
    "cat": {"translation": "Mósí", "pronunciation": "placeholder"},
    "fish": {"translation": "łóóʼ", "pronunciation": "placeholder"},
    "bear": {"translation": "Shash", "pronunciation": "placeholder"},
    "deer": {"translation": "Bįįh", "pronunciation": "placeholder"},
    "rabbit": {"translation": "Gah", "pronunciation": "placeholder"},
    "eagle": {"translation": "Atsá", "pronunciation": "placeholder"},
    "snake": {"translation": "Tsísnajinii", "pronunciation": "placeholder"},
    "spider": {"translation": "Naʼashǫǫʼii", "pronunciation": "placeholder"},
    "star": {"translation": "Sitsoii", "pronunciation": "placeholder"},
    "sky": {"translation": "Yá", "pronunciation": "placeholder"},
    "cloud": {"translation": "Tłʼiish", "pronunciation": "placeholder"},
    "river": {"translation": "Tó Łitso", "pronunciation": "placeholder"},
    "ocean": {"translation": "Tó Hózhǫ́ǫ́gi", "pronunciation": "placeholder"},
    "flower": {"translation": "Chʼil łitso", "pronunciation": "placeholder"},
    "grass": {"translation": "Tłʼiish dzilígíí", "pronunciation": "placeholder"},
    "fruit": {
        "translation": "Hózhǫǫgi bił dah yisdzoh",
        "pronunciation": "placeholder",
    },
    "vegetable": {
        "translation": "Hózhǫǫgi bił dah yisdzoh",
        "pronunciation": "placeholder",
    },
    "car": {"translation": "Chidí", "pronunciation": "placeholder"},
    "airplane": {"translation": "Tsidi", "pronunciation": "placeholder"},
    "train": {"translation": "Choochoo", "pronunciation": "placeholder"},
    "book": {"translation": "Tłʼiish", "pronunciation": "placeholder"},
    "pen": {"translation": "Biih bitooʼ", "pronunciation": "placeholder"},
    "paper": {"translation": "Tłʼiish yishtłizh", "pronunciation": "placeholder"},
    "school": {"translation": "Shinálí", "pronunciation": "placeholder"},
    "home": {"translation": "Kin", "pronunciation": "placeholder"},
    "morning": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "evening": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "night": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "today": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "yesterday": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "tomorrow": {"translation": "Hózhǫǫgi", "pronunciation": "placeholder"},
    "food": {"translation": "Chʼiyáán", "pronunciation": "placeholder"},
    "drink": {"translation": "Tłʼiish", "pronunciation": "placeholder"},
    "man": {"translation": "Hastiin", "pronunciation": "placeholder"},
    "woman": {"translation": "Asdzáá", "pronunciation": "placeholder"},
    "child": {"translation": "Ashkii / Atsáá", "pronunciation": "placeholder"},
}


choctaw_dictionary = {
    "hello": {"translation": "Halito", "pronunciation": "placeholder"},
    "goodbye": {"translation": "Chinchokma'shki", "pronunciation": "placeholder"},
    "thank you": {"translation": "Yakoke", "pronunciation": "placeholder"},
    "yes": {"translation": "Enh", "pronunciation": "placeholder"},
    "no": {"translation": "Keyu", "pronunciation": "placeholder"},
    "water": {"translation": "Oka", "pronunciation": "placeholder"},
    "sun": {"translation": "Hashi", "pronunciation": "placeholder"},
    "moon": {"translation": "Hashi Ninak Waya", "pronunciation": "placeholder"},
    "tree": {"translation": "Itti", "pronunciation": "placeholder"},
    "rock": {"translation": "Tali", "pronunciation": "placeholder"},
    "fire": {"translation": "Lukfi", "pronunciation": "placeholder"},
    "earth": {"translation": "Ofi' Toklo", "pronunciation": "placeholder"},
    "wind": {"translation": "Anowa", "pronunciation": "placeholder"},
    "rain": {"translation": "Osi", "pronunciation": "placeholder"},
    "snow": {"translation": "Tashka", "pronunciation": "placeholder"},
    "mountain": {"translation": "Nanih Waiya", "pronunciation": "placeholder"},
    "dog": {"translation": "Ofi", "pronunciation": "placeholder"},
    "horse": {"translation": "Soksi", "pronunciation": "placeholder"},
    "sheep": {"translation": "Fuswa", "pronunciation": "placeholder"},
    "cow": {"translation": "Hattakshi", "pronunciation": "placeholder"},
    "corn": {"translation": "Tanchi", "pronunciation": "placeholder"},
    "potato": {"translation": "Kanchi", "pronunciation": "placeholder"},
    "bread": {"translation": "Tanchi Poya", "pronunciation": "placeholder"},
    "butterfly": {"translation": "Shukha Anumpa", "pronunciation": "placeholder"},
    "bird": {"translation": "Foshi", "pronunciation": "placeholder"},
    "cat": {"translation": "Katos", "pronunciation": "placeholder"},
    "fish": {"translation": "Nani", "pronunciation": "placeholder"},
    "bear": {"translation": "Nita", "pronunciation": "placeholder"},
    "deer": {"translation": "Issi", "pronunciation": "placeholder"},
    "rabbit": {"translation": "Kowi", "pronunciation": "placeholder"},
    "eagle": {"translation": "Foshi Koba", "pronunciation": "placeholder"},
    "snake": {"translation": "Sinti", "pronunciation": "placeholder"},
    "spider": {"translation": "Choba", "pronunciation": "placeholder"},
    "star": {"translation": "Hashi Lowa", "pronunciation": "placeholder"},
    "sky": {"translation": "Lusa", "pronunciation": "placeholder"},
    "cloud": {"translation": "Achufa", "pronunciation": "placeholder"},
    "river": {"translation": "Bok Chito", "pronunciation": "placeholder"},
    "ocean": {"translation": "Bok Chito Shupan", "pronunciation": "placeholder"},
    "flower": {"translation": "Shola", "pronunciation": "placeholder"},
    "grass": {"translation": "Kancha", "pronunciation": "placeholder"},
    "fruit": {"translation": "Pila", "pronunciation": "placeholder"},
    "vegetable": {"translation": "Chukfi Pila", "pronunciation": "placeholder"},
    "car": {"translation": "Takolo", "pronunciation": "placeholder"},
    "airplane": {"translation": "Hashi Pisa", "pronunciation": "placeholder"},
    "train": {"translation": "Osi Pisa", "pronunciation": "placeholder"},
    "book": {"translation": "Holitopa", "pronunciation": "placeholder"},
    "pen": {"translation": "Shola", "pronunciation": "placeholder"},
    "paper": {"translation": "Holitopa", "pronunciation": "placeholder"},
    "school": {"translation": "Chukma", "pronunciation": "placeholder"},
    "home": {"translation": "Chukka", "pronunciation": "placeholder"},
    "morning": {"translation": "Hushi", "pronunciation": "placeholder"},
    "evening": {"translation": "Nittak Himona", "pronunciation": "placeholder"},
    "night": {"translation": "Nitti", "pronunciation": "placeholder"},
    "today": {"translation": "Himak Nitak", "pronunciation": "placeholder"},
    "yesterday": {"translation": "Bissi", "pronunciation": "placeholder"},
    "tomorrow": {"translation": "Safo", "pronunciation": "placeholder"},
    "food": {"translation": "Anowa", "pronunciation": "placeholder"},
    "drink": {"translation": "Inhola", "pronunciation": "placeholder"},
    "man": {"translation": "Hattak", "pronunciation": "placeholder"},
    "woman": {"translation": "Hokma", "pronunciation": "placeholder"},
    "child": {"translation": "Talowa", "pronunciation": "placeholder"},
}

# Curriculum: List of lists. Each list is a "level" and contains words that the user should learn in that level.
curriculum = [
    ["hello", "goodbye", "yes", "no"],
    ["water", "sun", "moon", "tree"],
    # More levels...
]

# The user's current level
current_level = 0

# The words the user has learned
learned_words = []


# Function to translate a word from English to the selected language
def translate_word(word, language):
    if language == "Navajo":
        dictionary = navajo_dictionary
    elif language == "Choctaw":
        dictionary = choctaw_dictionary
    else:
        return "Invalid language", None

    if word in dictionary:
        return dictionary[word]["translation"], dictionary[word]["pronunciation"]
    else:
        return "Translation not found", None


# Function to generate a random word and its translation in the selected language
def generate_random_word(language):
    if language == "Navajo":
        dictionary = navajo_dictionary
    elif language == "Choctaw":
        dictionary = choctaw_dictionary
    else:
        return "Invalid language", None, None

    random_word = random.choice(list(dictionary.keys()))
    translation = dictionary[random_word]["translation"]
    pronunciation = dictionary[random_word]["pronunciation"]
    return random_word, translation, pronunciation


# Function to get the next word in the curriculum
def get_next_word():
    global current_level
    global learned_words

    # If the user has learned all words in the current level, move to the next level
    if set(learned_words) == set(curriculum[current_level]):
        current_level += 1
        learned_words = []

    # Get a word that the user has not learned yet
    word = random.choice(curriculum[current_level])
    while word in learned_words:
        word = random.choice(curriculum[current_level])

    learned_words.append(word)
    return word


root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")  # Use the "clam" theme

root.configure(bg="lightgray")

language_var = tk.StringVar(value="Navajo")

navajo_button = ttk.Radiobutton(
    root, text="Navajo", variable=language_var, value="Navajo"
)
navajo_button.pack()

choctaw_button = ttk.Radiobutton(
    root, text="Choctaw", variable=language_var, value="Choctaw"
)
choctaw_button.pack()

word_label = ttk.LabelFrame(
    root, text="Enter an English word to translate or learn a new word:"
)
word_label.pack(padx=20, pady=20)

word_entry = ttk.Entry(word_label)
word_entry.pack(padx=20, pady=20)


def translate():
    word = word_entry.get()
    language = language_var.get()
    translation, pronunciation = translate_word(word, language)
    messagebox.showinfo(
        "Translation", f"Translation: {translation}\nPronunciation: {pronunciation}"
    )


translate_button = ttk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=20)


def random_word():
    language = language_var.get()
    word, translation, pronunciation = generate_random_word(language)
    messagebox.showinfo(
        "Random Word",
        f"Word: {word}\nTranslation: {translation}\nPronunciation: {pronunciation}",
    )


random_button = ttk.Button(root, text="Random Word", command=random_word)
random_button.pack(pady=20)


def learn_word():
    word = get_next_word()
    language = language_var.get()
    translation, pronunciation = translate_word(word, language)
    messagebox.showinfo(
        "Learn Word",
        f"Word: {word}\nTranslation: {translation}\nPronunciation: {pronunciation}",
    )


learn_button = ttk.Button(root, text="Learn Word", command=learn_word)
learn_button.pack(pady=20)

root.mainloop()
