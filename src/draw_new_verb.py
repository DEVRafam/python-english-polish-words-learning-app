from random import choice


def draw_new_verb(words_list, already_drawn_words):
    temp_words = [verb for verb in words_list if verb not in already_drawn_words]
    chosen_verb = choice(temp_words)
    already_drawn_words.append(chosen_verb)
    return chosen_verb