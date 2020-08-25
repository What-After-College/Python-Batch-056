import pandas as pd
city_names = pd.Series(['San Fransisco', 'San jose', 'Texas'])
# print(type(city_names)) <class 'pandas.core.series.Series'>

population = pd.Series([100000, 200000, 300000])
pd.DataFrame = ({'City Names:': city_names, 'Population':population})

print(pd.DataFrame)