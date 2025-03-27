from transformers import pipeline

genrator = pipeline('text-generation')
res = genrator('Hello nice to meet you...', min_length=50, max_length=100)
print(res) 

""" 
# output:

[{'generated_text': 'Hello nice to meet you...I\'ll be seeing you soon...I hope you\'re back nice and relaxed."\n\n"Well?" 
Anna asked, staring at Anna.\n\n"Good. I have a little something in my office to do. Maybe the place has something to do with the 
fact that we\'re just having a break."\n\n"I don\'t know," Anna replied and opened the door. She then opened it and found Elsa standing next to her, 
looking down at the snow'}]
"""