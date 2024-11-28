import pandas as pd

def analyze_incidents(data):
    # Contar incidentes por tipo
    incident_counts = data['tipo_incidente'].value_counts()
    return incident_counts

def trends_over_time(data):
    # Agrupar incidentes por data
    trends = data.groupby(data['data'].dt.date).size()
    return trends