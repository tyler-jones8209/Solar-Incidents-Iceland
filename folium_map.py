import folium
import pandas as pd


# All of the stations in Iceland I could find with useable 'sun' data
# The format is name, latitude, longitude, monthly solar average over 30 years (or less depending on the station), average from April to August and September to March for all the years, start year, and end year
stations = [
    {"name": "Akureyri", "lat": 65.6839, "lon": -18.1105, "solar_avg": 90, "apr-aug": 160, "sept-mar": 40, "start_year": 1995, "end_year": 2025},
    {"name": "Haganes", "lat": 65.5919, "lon": -17.0588, "solar_avg": 99, "apr-aug": 169, "sept-mar": 49, "start_year": 1989, "end_year": 2019},
    {"name": "Hallormsstadur", "lat": 65.09508, "lon": -14.74828, "solar_avg": 91, "apr-aug": 166, "sept-mar": 37, "start_year": 1960, "end_year": 1990},
    {"name": "Hofn I Hornafirdi", "lat": 64.26197, "lon": -15.20342, "solar_avg": 100, "apr-aug": 149, "sept-mar": 65, "start_year": 1965, "end_year": 1984},
    {"name": "Holar I Hornafirdi", "lat": 65.73318, "lon": -19.11243, "solar_avg": 100, "apr-aug": 148, "sept-mar": 65, "start_year": 1981, "end_year": 2011},
    {"name": "Hoskuldarnes", "lat": 66.45751, "lon": -15.93438, "solar_avg": 82, "apr-aug": 142, "sept-mar": 38, "start_year": 1958, "end_year": 1988},
    {"name": "Hveravellir", "lat": 64.8668, "lon": -19.5622, "solar_avg": 95, "apr-aug": 162, "sept-mar": 48, "start_year": 1974, "end_year": 2004},
    {"name": "Leirubakki", "lat": 63.987, "lon": -20.04967, "solar_avg": 101, "apr-aug": 154, "sept-mar": 61, "start_year": 1984, "end_year": 1991},
    {"name": "Reykholar", "lat": 65.44675, "lon": -22.20516, "solar_avg": 93, "apr-aug": 157, "sept-mar": 46, "start_year": 1961, "end_year": 1989},
    {"name": "Reykir I Olfusi", "lat": 65.64415, "lon": -19.06860, "solar_avg": 95, "apr-aug": 144, "sept-mar": 60, "start_year": 1972, "end_year": 2000},
    {"name": "Samsstadir", "lat": 63.7354, "lon": -20.1091, "solar_avg": 99, "apr-aug": 155, "sept-mar": 57, "start_year": 1989, "end_year": 2019},
]

# This creates the map that is centered around Iceland
iceland_map = folium.Map(location=[64.9631, -19.0208], zoom_start=6)

# Loop through stations and create markers with the all the data
for station in stations:

    # Only for Skalanes
    popup_skalanes = f"""
    <div style="width: 200px; min-width: 175px;">
        <b>Skalanes</b><br>
        This is homebase baby  
    </div>
    """

    # Define the content and css elements of the popups
    popup_content = f"""
    <div style="width: 200px; min-width: 175px;">
        <b>{station['name']}</b><br>
        <i>Years:</i> {station['start_year']}-{station['end_year']}<br>
        <i>Solar Avg:</i> {station['solar_avg']} hrs/month<br>
        <i>April-August:</i> {station['apr-aug']} hrs/month<br>
        <i>September-March:</i> {station['sept-mar']} hrs/month
        
    </div>
    """

    # Actually create the popup on the map using the coordinates, content, and color, then stick it on the map
    folium.Marker(
        location=[station["lat"], station["lon"]],
        popup=folium.Popup(popup_content, max_width=200),
        icon=folium.Icon(color="orange"),
    ).add_to(iceland_map)

    # Same thing but for Skalanes
    folium.Marker(
        location=(65.2944963410417, -13.705741037561193),
        popup=folium.Popup(popup_skalanes, max_width=200),
        icon=folium.Icon(color="red"),
    ).add_to(iceland_map)

# Save as html
iceland_map.save("iceland_solar_map.html")
