sentence = "fshdgffititsfdhfsdghfdkjghdfgititititititititiititiitiititiiiti"

occurances = len(sentence.split("iti")) - 1
occurances_v2 = sentence.count('iti')  # more cleaner approach

print(f"iti occurances in sentence are {occurances} ")
print(f"iti occurances in sentence are {occurances_v2} ")
