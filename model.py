from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(data):
    # Converter categorias em variáveis numéricas
    data_encoded = pd.get_dummies(data, columns=['tipo_incidente', 'localizacao'], drop_first=True)
    
    X = data_encoded.drop(['gravidade'], axis=1)
    y = data_encoded['gravidade']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))