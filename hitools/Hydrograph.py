import matplotlib.pyplot as plt
import folium
import geopandas as gpd

def plot_hydrograph(time, flow_observed, flow_predicted):
    plt.figure()
    plt.plot(time, flow_observed, label='Observed')
    plt.plot(time, flow_predicted, label='Predicted')
    plt.xlabel('Time')
    plt.ylabel('Flow')
    plt.title('Hydrograph')
    plt.legend()
    plt.show()

def plot_error(time, error):
    plt.figure()
    plt.plot(time, error, label='Error')
    plt.xlabel('Time')
    plt.ylabel('Error')
    plt.title('Error Over Time')
    plt.legend()
    plt.show()

def plot_map_from_kml(kml_file):
    gdf = gpd.read_file(kml_file)
    m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=10)
    folium.GeoJson(gdf).add_to(m)
    m.save('map.html')
    print("Map saved to 'map.html'")