# Let's examine how the different open AI parameters are tweaked based on the use case:


#Question Answering
temperature=0,
max_tokens=100,
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.0,
stop=["\n"]

#Grammar Correction
temperature=0,
max_tokens=60,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0


#Translation
temperature=0.3,
max_tokens=100,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0




#Summarization
temperature=0.7,
max_tokens=64,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0

#TLDR summarization
temperature=0.7,
max_tokens=60,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=1

#Q; why is presence_penalty=1 for TLDR summarization?

#Q: difference between frequency_penalty and presence_penalty?

#Product name generation
temperature=0.8,
max_tokens=60,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0

https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md
https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md#selection-inference-prompting
https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md#maieutic-prompting
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html



#Temperature:
#Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.
#We generally recommend altering this or top_p but not both.

#Top_p:
#An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
#We generally recommend altering this or temperature but not both.
