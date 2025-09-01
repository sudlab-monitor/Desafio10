import geopandas as gpd
import pandas as pd

print("Loading Shapefile...")

file1 = r"Limite_de_Bairros.shp"
file5 = r"Trajeto_VLT.shp"
admin = gpd.read_file(file1)
vlt = gpd.read_file(file5)
legend = gpd.read_file(file5)

ax = admin.plot(
    color="lightgrey", 
    edgecolor="lightgrey", 
    figsize=(20, 10))
vlt.nome = pd.to_numeric(vlt.nome, errors='coerce')
shapefile = gpd.read_file("Trajeto_VLT.shp")
vlt.plot(
    ax=ax,
    column="nome",
    cmap='viridis',
    figsize=(20, 10)
)
legend.plot(
    ax=ax,
    column="nome", 
    cmap="viridis",
    categorical=True,
    legend=True,
    legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5)}
)
ax.set_axis_off()
shapefile.head()