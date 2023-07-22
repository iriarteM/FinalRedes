import timeit
import heapq


def dijkstra(grafo, origen):
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0
    cola_prioridad = [(0, origen)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, valor in grafo[nodo_actual].items():
            distancia = distancia_actual + valor
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias


def get_camino_optimo(grafo, origen, destino):
    distancias = dijkstra(grafo, origen)
    camino = [destino]
    nodo_actual = destino
    distancia_total = 0

    while nodo_actual != origen:
        vecinos = grafo[nodo_actual]
        distancia_optima = distancias[nodo_actual]

        for vecino, valor in vecinos.items():
            if distancias[vecino] + valor == distancia_optima:
                camino.append(vecino)
                nodo_actual = vecino
                distancia_total += valor
                break

    camino.reverse()
    return camino, distancia_total


grafo = {
    "A": {"B": 5, "D": 2, "E": 1},
    "B": {"A": 5, "C": 1, "E": 4},
    "C": {"B": 1, "F": 3},
    "D": {"A": 2, "E": 3},
    "E": {"A": 1, "B": 4, "D": 3, "F": 2},
    "F": {"C": 3, "E": 2, "G": 3},
    "G": {"F": 3, "H": 2, "I": 5},
    "H": {"G": 2, "I": 4, "J": 1},
    "I": {"G": 5, "H": 4, "J": 3, "K": 2},
    "J": {"H": 1, "I": 3, "K": 5, "L": 4},
    "K": {"I": 2, "J": 5, "L": 3},
    "L": {"J": 4, "K": 3},
}

nodo_origen = input("Ingrese el nodo de origen: ")
nodo_destino = input("Ingrese el nodo de destino: ")

camino_optimo, distancia_total = get_camino_optimo(grafo, nodo_origen, nodo_destino)

print("Camino más corto Dijkstra:", camino_optimo)
print("Distancia más corta Dijkstra:", distancia_total)


def medir_tiempo(grafo, origen, destino):
    return get_camino_optimo(grafo, origen, destino)


numero_de_ejecuciones = 10000
tiempo_promedio = (
    timeit.timeit(
        lambda: medir_tiempo(grafo, nodo_origen, nodo_destino),
        number=numero_de_ejecuciones,
    )
    / numero_de_ejecuciones
)
tiempo_en_microsegundos = tiempo_promedio * 1e6
print(
    "Tiempo promedio en ejecución Dijkstra:", tiempo_en_microsegundos, "microsegundos"
)
