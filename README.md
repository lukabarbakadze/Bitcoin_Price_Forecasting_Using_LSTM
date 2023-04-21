# Bitcoin Price Forcasting Using LSTM
---
The project is based on [Bitroin Historical Price data](https://www.kaggle.com/datasets/lukabarbakadze/bitcoin-historical-data) scrapped from [coinmarketcap.com](https://coinmarketcap.com/) and consists several experimets using several types of [LSTM Networks](https://www.bioinf.jku.at/publications/older/2604.pdf) (Simple LSTM, Double Reccurent-Layer LSTM, Bidirectional LSTM).

## Results
![Results](https://github.com/lukabarbakadze/Bitcoin_Price_Forecasting_Using_LSTM/blob/main/figure.png)

---
## Files Description
* weights - folder where model weights are saved
* code.ipynb - main working notebook
* data.csv - data used in project
* scrapper.py - The web-scraper I used to extract data
---
## Table of Contents
### Imports
### Data Preprocessing
* Generate X & y Matrices
* Define Dataset & Dataloader
### Modeling
* Experiment I: one layer simple LSTM
* Experiment II: double reccurent layer LSTM
* Experiment IIi: bidirectional LSTM
### Model Comparison
* Vizualization
* Metrics
---
## Acknowledgements
* [How to Develop LSTM Models for Time Series Forecasting](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)
