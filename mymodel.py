# Importando algunas librerías

# Librerías estándar
import pandas as pd
# Librerías de scikit-learn
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
import joblib


def get_train_test(df, y, column):
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
    df[column], 
    y, 
    test_size=0.3, 
    stratify=y, 
    random_state=42
)
    X_train = X_train.fillna('')
    X_test = X_test.fillna('')
    return X_train, X_test, y_train, y_test


def predict_genres(sentence, model, mlb, vectorizer):
    sentence_tfidf = vectorizer.transform([sentence])
    predicted = model.predict(sentence_tfidf)
    return mlb.inverse_transform(predicted)

def set_df(root_path):
    df = pd.read_csv(root_path)
    df['genres'] = df['genres'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    return df

def save_model(model, mlb, vectorizer, model_path, mlb_path, vectorizer_path):
    joblib.dump(model, model_path)
    joblib.dump(mlb, mlb_path)
    joblib.dump(vectorizer, vectorizer_path)

def load_model(model_path, mlb_path, vectorizer_path):
    model = joblib.load(model_path)
    mlb = joblib.load(mlb_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, mlb, vectorizer

def train_model(df, column, mlb=MultiLabelBinarizer(), vectorizer=TfidfVectorizer()):
    model = OneVsRestClassifier(LogisticRegression(max_iter=1000))
    y = mlb.fit_transform(df['genres'])
    X_train, X_test, y_train, y_test = get_train_test(df, y, column)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    model.fit(X_train_tfidf, y_train)
    return model, mlb, vectorizer


# df = set_df('./df_final.csv')
# model = train_model(df, 'about_the_game', mlb, vectorizer)
# joblib.dump(model, 'model.pkl')
# model, mlb, vectorizer = train_model(df, 'about_the_game')  # Reemplaza 'text_column' con el nombre de la columna de texto

# Guardar el modelo, mlb y vectorizador
# save_model(model, mlb, vectorizer, 'model.pkl', 'mlb.pkl', 'vectorizer.pkl')

# Cargar el modelo, mlb y vectorizador guardados
# model, mlb, vectorizer = load_model('model.pkl', 'mlb.pkl', 'vectorizer.pkl')
# test_sentence = "Shooter and cars races."
# predicted_genres = predict_genres(test_sentence, model, mlb, vectorizer)

# print(f"Oración de prueba: {test_sentence}")
# print(f"Géneros predichos: {predicted_genres}")

# print("Modelo entrenado y guardado exitosamente.")

