def validStartingCity(distances, fuel, mpg):
    
    def mapping(x):
        return x*mpg
    
    new = list(map(mapping, fuel))
    
    i = 0
    fuel_left = 0
    while True:
        starting = distances[i]
        distance = distances[0]
        fuels = fuel[0]
        fuel_left += fuels - distance
        if  
    
validStartingCity([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10)