"""
This is the start of the SentimentAnalysis component of the Stock Tool.
Currently just used as an example for creating a new Python backend component folder and structure

"""

import fasttext

model = fasttext.train_supervised(input="file_example.train")

model.save_model("model_example.bin")

model.predict("Test Text for Classification")

model.test("testing_example.valid")