# Personal Income Analysis and Prediction
ECE180 Team2:
Kaiyu Zhang / Wenyu Zhang / Fengcan Zhu / Linqi Pan / Yucheng Huang / Woen Lee / Andrew (Dung) Luong

### PURPOSE

This project aims to predict whether a person’s income is above 50K or not, which is an important line to measure their living standards. Based on the adult data extracted from Census database, we want to design an optimized classifier, which will help employers consider the suitable salary for the new worker. Furthermore, we will analyze the influence of certain attributes and their correlations by data visualization. The outcome could be taken as reference for personal development. 

### DATA ACQUISITION AND ANALYSIS

We obtain the data from UC Irvine machine learning database, which including the samples’ different features and their annual income is above 50K or not.

*Dataset: 4 million adults’ features and salary statistics in 1994
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data*

The project should include several parts: To address our purpose using the data, we first need to have access to website document for data with __Urllib/Socket__;  After observing the data, we use __Numpy__ and __Pandas__ to extract features and do analysis; __Matplotlib__, __NetworkX__ can help with the visualization. __Basemap__, __Geoplotlib__ associate geometric data with networks when visualizing distribution of countries. __Scikit-learn__ will provide machine learning algorithms that we might use in classifier.

### EXPECTED TIMELINE
| Task  | Start/End Time | Assigned Member |
| ------------- | ------------- | ------------ |
| Data Acquisition/Assembly  | 2/9 - 2/11  | Fengcan & Linqi & Yucheng |
| Data Learning: Classifier Training  | 2/12 - 2/16  | Kaiyu & Wenyu & Woen |
| Data Analysis I: Prediction Accuracy | 2/17 - 2/24 | Kaiyu & Andrew & Woen |
| Data Analysis II: Impact Ranking | 2/17 - 2/24 | Andrew & Fengcan & Linqi |
| Data Analysis III: Attribute Correlation | 2/12 - 2/24 | Wenyu & Yucheng |
| Data Visualization: Plotting/Networking | 2/24 - 3/4 | All members |
| Conclusion and Report | 3/1 - 3/6 | All members |

#### Feature Responsibilities
| Responsibility | Feature |
| -------- | ------- |
| Jax | Race, Education |
| Kaiyu | Age, Working Year |
| Woen | Nationality, Marriage Status |
| Yucheng | Job Type, Gender |
