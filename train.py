from functions import *
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import pickle

#input params
infile = "seq/Asparagales.gb"
outfile = "svn.txt"
log_folder ="logs"

#Get data from file
data_array = genebank_to_numpyarr(infile, process_function_return_string)

#Xy
X = data_array[:, 0]
y = data_array[:, 1]
le = LabelEncoder()
le.fit_transform(y)

#Learning
cv = CountVectorizer()
pca = TruncatedSVD(n_components=2)
clf = SVC(gamma='auto',probability=True)
clf2 = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(20, 10, 10), random_state=1)
T = Transformer()

model_transformation = Pipeline([("Transformer",T),
                                 ('CountVectorizer', cv),
                                 ("pca", pca),
                                 ('svc', clf)])

parameters = {"pca__n_components": [i for i in range(1,100,10)]}

model_transformation = GridSearchCV(model_transformation, parameters, cv=5, verbose=2, n_jobs=-1)
model_transformation.fit(X, y)

print("\n best_score: "+
      str(model_transformation.best_score_))

#Model persistance
pickle.dump(model_transformation, open('model_transformation.joblib', "wb" ))
pickle.dump(le, open('encoder.joblib', "wb" ))


