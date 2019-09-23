from functions import *
from sklearn.preprocessing import LabelEncoder
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

infile = args.infile
pickle_model = r"model_transformation.joblib"
pickle_encoder = r"encoder.joblib"

X = genebank_to_numpyarr(infile, only_seqs)

with open(pickle_model, "rb") as input_file:
     model = pickle.load(input_file)
with open(pickle_encoder, "rb") as input_file:
     le = pickle.load(input_file)

y_pred = model.predict(X)
y_pred = le.inverse_transform(y_pred)

