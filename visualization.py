import matplotlib.pyplot as plt
import seaborn as sns

def plot_incident_counts(incident_counts):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=incident_counts.index, y=incident_counts.values)
    plt.title('Contagem de Incidentes por Tipo')
    plt.xlabel('Tipo de Incidente')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45)
    plt.show()

def plot_trends(trends):
    plt.figure(figsize=(10, 6))
    trends.plot(kind='line')
    plt.title('Tendências de Incidentes ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Número de Incidentes')
    plt.xticks(rotation=45)
    plt.show()