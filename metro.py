import geopandas as gpd
import pandas as pd

print("Loading Shapefile...")

file1 = r"Limite_de_Bairros.shp"
file6 = r"Trajetos_Metro.shp"
file7 = r"Estacoes_Metro.shp"
admin = gpd.read_file(file1)
metro = gpd.read_file(file6)
legend = gpd.read_file(file6)
estacoesmetro = gpd.read_file(file7)

ax = admin.plot(
    color="lightgrey", 
    edgecolor="white", 
    figsize=(20, 10))
metro.tipo = pd.to_numeric(metro.tipo, errors='coerce')
shapefile = gpd.read_file("Trajetos_Metro.shp")
estacoesmetro.plot(
    ax=ax, 
    column="flg_linha2", 
    cmap="viridis", 
    markersize=100, 
    figsize=(20, 10))
metro.plot(
    ax=ax,
    column="tipo",
    cmap='viridis',
    figsize=(20, 10)
)
legend.plot(
    ax=ax,
    column="tipo", 
    cmap="viridis",
    categorical=True,
    legend=True,
    legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5)}
)
ax.set_axis_off()
shapefile.head()