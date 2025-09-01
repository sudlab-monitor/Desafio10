import geopandas as gpd
import pandas as pd

print("Loading Shapefile...")

file1 = r"Limite_de_Bairros.shp"
file4 = r"Itinerarios_de_Servicos_de_Onibus_Regulares.shp"
admin = gpd.read_file(file1)
sppo = gpd.read_file(file4)
legend = gpd.read_file(file4)

ax = admin.plot(
    color="lightgrey", 
    edgecolor="lightgrey", 
    figsize=(20, 10))
sppo.consorcio = pd.to_numeric(sppo.consorcio, errors='coerce')
shapefile = gpd.read_file("Itinerarios_de_Servicos_de_Onibus_Regulares.shp")
sppo.plot(
    ax=ax,
    column="consorcio",
    cmap='PuBu',
    figsize=(20, 10)
)
legend.plot(
    ax=ax,
    column="consorcio", 
    cmap="PuBu",
    categorical=True,
    legend=True,
    legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5)}
)
ax.set_axis_off()
shapefile.head()