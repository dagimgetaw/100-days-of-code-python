sentence = "what is the airspeed velocity of and unladen swallow?"
sentence_arr = sentence.split()
sentence_dict = {}

for word in sentence_arr:
    sentence_dict = {word: len(word) for word in sentence_arr}

print(sentence_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}

print(weather_f)
