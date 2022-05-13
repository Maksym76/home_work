# ask user count of earth day and hour (type number through ",")
earth_day, earth_hour = map(int, input("write (earth_day, earth_hour): ").split(","))

# translate earth day to solo
solo = (earth_day + earth_hour / 24) * 1.02595675

print('count sol: ', round(sol, 2))
