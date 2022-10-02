import pickle
import pandas as pd # library for data manipulation
from sklearn.ensemble import RandomForestClassifier



class Prediction:
    def __init__(self, mod):
        self.clf  = pickle.load(open('./models/'+mod, 'rb'))
        print("Data init Done")

    def prediect(self,data):
        data = [float(x) for x in data] 
        df = pd.DataFrame(data).T
        #df.columns(["Mean of the integrated profile","Standard deviation of the integrated profile",
        #"Skewness of the integrated profile","Mean of the DM-SNR curve","Excess kurtosis of the DM-SNR curve"])
        ans = self.clf.predict(df)
        #print(ans)
        return ans
