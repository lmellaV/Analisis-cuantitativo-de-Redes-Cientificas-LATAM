import networkx as nx
import pandas as pd

def clean_address(address_str):
    address_list = address_str.split('; ')
    countries = []
    for address in address_list:
        country = address.split(', ')[-1]
        if country not in countries:
            countries.append(country)
    return countries

def es_diagonal_cero(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    for i in range(len(matriz)):
        if matriz[i][i] != 0:
            return False
    return True


def centralizacion(grafo):
    centralizacion_grado = nx.degree_centrality(grafo)
    grados = [val for (node, val) in centralizacion_grado.items()]
    k_max = max(grados)
    N = len(grados)
    C_grado = sum([k_max - k_i for k_i in grados]) / ((N - 1) * (N - 2))

    return C_grado

def propiedades(x):
    print(x)
    communities = nx.algorithms.community.greedy_modularity_communities(x)

    print("N de Nodos: ", x.number_of_nodes())
    print("N de aristas: ", x.number_of_edges())
    print("Es direccionado: " , nx.is_directed(x))
    print("Transitividad", nx.transitivity(x))
    print("Centralización ", centralizacion(x))
    print("Tiene: ", len(communities), 'comunidades')
    print(communities)
    print("Densidad:" ,nx.density(x))

def centralidades(grafo):
    metricas = {}

    # Centralidad de Grado
    grado_centralidad = nx.degree_centrality(grafo)
    centralidad = pd.DataFrame(list(grado_centralidad.items()), columns=['Institucion', 'Centralidad'])
    centralidad = centralidad.sort_values(by='Centralidad', ascending=False)
    metricas['centralidad'] = centralidad

    # Centralidad de Intermediación
    intermediacion = nx.betweenness_centrality(grafo)
    betweenness = pd.DataFrame(list(intermediacion.items()), columns=['Institucion', 'Centralidad'])
    betweenness = betweenness.sort_values(by='Centralidad', ascending=False)
    metricas["betweenness"] = betweenness

    # Centralidad de Cercanía
    cercania_centralidad = nx.closeness_centrality(grafo)
    cercania = pd.DataFrame(list(cercania_centralidad.items()), columns=['Institucion', 'Centralidad'])
    cercania = cercania.sort_values(by='Centralidad', ascending=False)
    metricas["cercania"] = cercania
    
    #Centralidad de Vector Propio
    eigen_cen = nx.eigenvector_centrality(grafo)
    eigen = pd.DataFrame(list(eigen_cen.items()), columns=['Institucion', 'Centralidad'])
    eigen = eigen.sort_values(by='Centralidad', ascending=False)
    metricas["eigen"] = eigen

    return metricas