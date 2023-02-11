import time

def typing_test(sentence):
    start_time = time.time()
    typed_sentence = input(f"Type the following sentence: {sentence}\n")
    end_time = time.time()
    time_elapsed = end_time - start_time
    words_typed = len(typed_sentence.split())
    words_per_minute = int(words_typed / (time_elapsed / 60))
    return words_per_minute

sentence = "The quick brown fox jumps over the lazy dog."
wpm = typing_test(sentence)
print(f"You typed at {wpm} words per minute.")
