women_100m_final = [
   {"athlete": "Emma McKeon", "country": "Australia", "time": 51.96},
   {"athlete": "Siobhan Haughey", "country": "Hong Kong", "time": 52.27},
   {"athlete": "Cate Campbell", "country": "Australia", "time": 52.52},
   {"athlete": "Abbey Weitzeil", "country": "United States", "time": 52.59},
   {"athlete": "Marie Wattel", "country": "France", "time": 52.72},
   {"athlete": "Penny Oleksiak", "country": "Canada", "time": 52.89},
   {"athlete": "Sarah Sjöström", "country": "Sweden", "time": 53.08},
   {"athlete": "Simone Manuel", "country": "United States", "time": 53.23}
 ]

avg = 0
for item in women_100m_final:
    avg  += item['time']

avg /= len(women_100m_final)