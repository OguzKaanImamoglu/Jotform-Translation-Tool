There are 4 folders

Neural Machine Translation Folder:
Includes nmt_with_attention.ipnyb. This file contains Machine Learning part of the project.
It contains code for input preprocessing, composing of neural network model, training the
model, translate inputs and saving model.
The model was created based on the neural machine translation guide prepared by Tensorflow. 
Guide can be found here: https://www.tensorflow.org/text/tutorials/nmt_with_attention

*******************************************************************************************

Presentation Folder:
This folder includes my project presentation.

*******************************************************************************************

User Interface Folder:
The user interface of language translation tool. Flask and HTML were used for this part.
Also this folder includes all 14 language translation models.

*******************************************************************************************

Dataset Folder:
Includes necessary files for creating datasets.
Copy of Form Templates of All Languages.xlsx contains English form links and their
counterparts from 14 different languages.
Main.py is a web crawler. It crawls the forms of excel file and extracts their form ids'.
DatasetGenerator.ipnyb uses these ids and also Jotform API, extracts the texts of forms and 
creates datasets from these texts. Then it merges these datasets with datasets available at
http://www.manythings.org/anki/ and by merging them it prepares a final dataset for each 14
languages.
datasets folder contains these datasets and formid folder includes ids'of forms

*******************************************************************************************



