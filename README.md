# Akinator Diseases Repository
Code for predicting potential diseases using neural networks and Bayesian inference.

#### To execute the project remotely:
Tu run the emulator you can do it online using google collab wiht the link
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ycnoyPB0a7RiVS1p2Ras9o4CMigV_KSW?usp=sharing)


Tu run the Akinator you can do it online using google collab wiht the link
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BT3Zg_hp1K3Cfg407zbyh7G46566hzmg?usp=sharing)


- [Sadi Ramirez Solano](mailto:sadiramirez@estudiantes.fisica.unam.mx)


The code can be executed using the provided Google Colab link for Akinator_Sadi.ipynb. Alternatively, you can download the notebook, convert it to a Python file, and run it from the terminal.

The program will prompt you for various symptoms, starting with the most common ones. It will update the probabilities using Bayesian inference, construct a vector based on the symptoms, and finally use a neural network trained on the data to provide a prediction (this will be more accurate when adding more data of symptoms). Most of the time, the prediction will align with the most probable disease based on Bayesian inference. However, in cases of ties, the neural network will consider the most frequently occurring disease and will give an output with some recomendations.

If you want to use a different dataset, you can use the emulator code to train it on various data, such as personas with specific characteristics. The code will clean the data, convert it into binary form, and generate an emulator for you.

This Akinator Emulator uses disease data obtained from [Kaggle](https://www.kaggle.com/).
