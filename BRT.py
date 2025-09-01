import geopandas as gpd

file1 = r"Limite_de_Bairros.shp"
file2 = r"Trajetos_BRT.shp"
file3 = r"Estações_BRT_Corredores.shp"
file4 = r"Trajetos_BRT.shp"

admin = gpd.read_file(file1)
set_asides = gpd.read_file(file2)
estacoes = gpd.read_file(file3)
legend = gpd.read_file(file4)

ax = admin.plot(
    color="lightgrey", 
    edgecolor="white", 
    figsize=(20, 10))
set_asides.plot(
    ax=ax, 
    column="objectid_1", 
    cmap="viridis", 
    marker='•', 
    markersize=20000, 
    figsize=(20, 10))
estacoes.plot(
    ax=ax, 
    column="fid", 
    cmap="viridis",
    categorical=True,
    legend=False,
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