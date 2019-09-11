import ephem


mars = ephem.Mars('2019/09/12')
const = ephem.constellation(mars)
print(const)