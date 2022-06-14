import keras
import numpy as np
import pandas as pd
import tensorflow as tf

df = pd.read_csv('IowaHousingPrices.csv')

squareFeet = df[['SquareFeet']].values
salePrice = df[['SalePrice']].values

model = keras.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile(tf.keras.optimizers.Adam(lr=1), 'mean_squared_error')

model.fit(squareFeet, salePrice, epochs=30, batch_size=10)
