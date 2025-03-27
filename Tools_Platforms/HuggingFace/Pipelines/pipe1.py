from transformers import pipeline


# here we specify tasks, there are more tasks available also
classifier = pipeline('sentiment-analysis') # in pipeline 2nd param we can pass model name that we wanna use for task, if not give it use default one

# in object we can pass any data we wanna test
res = classifier('Hello nice to meet you')
print(res)


