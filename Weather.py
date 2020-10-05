def get_data_from_url(url):
    data_json = urllib.request.urlopen(url).read()
    data_dict = json.loads(data_json)
    return data_dict


app_id = '90dcc46f'
app_key = 'e16e576ca2c39bdbb28ccac2bdf6ce5a'

location = get_data_from_url("http://ip-api.com/json/")

lat = location['lat']
lon = location['lon']

url = f"http://api.weatherunlocked.com/api/current/{lat},{lon}" \
      f"?app_id={app_id}&app_key={app_key}"

weather = get_data_from_url(url)

result = f"""
