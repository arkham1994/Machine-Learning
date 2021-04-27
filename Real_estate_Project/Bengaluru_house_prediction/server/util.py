import json
import pickle
import numpy as np

__data_columns =None
__model = None


def get_estimated_price( sqft, bath, bhk,rank):
    x =np.zeros(4)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3] = rank

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print('loading saved artifacts..')

    #global __data_columns

    #with open('./artifacts/columns2.json','r') as f:
     #   __data_columns = json.load(f)['data_columns2']


    with open('./artifacts/banglore_home_prices_model_2.pickle', 'rb') as f:
        global __model
        __model = pickle.load(f)
        print('loading saved artifacts... done')


if __name__ =='__main__':
    load_saved_artifacts()
    print(get_estimated_price(1,1000,2,2))
