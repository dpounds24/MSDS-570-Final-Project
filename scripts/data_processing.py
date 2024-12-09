import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    label_encoder = LabelEncoder()
    data['Type'] = label_encoder.fit_transform(data['Type'])
    data['Total_Sensory_Symptoms'] = data[['Dysphasia', 'Dysarthria', 'Vertigo', 'Tinnitus', 
                                           'Hypoacusis', 'Diplopia', 'Visual_defect', 'Paresthesia']].sum(axis=1)
    return data, label_encoder
