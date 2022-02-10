import seaborn as sns
# https://blog.csdn.net/m0_38103546/article/details/79935671

def HeatMap(mat, vmin=None, vmax=None, annot=False, fmt='.3f', cbar=True):
    """
    mat(N, M)
    vmin, vmax: 最大最小
    annot, fmt: 显示数值
    cbar: 显示颜色图例
    """
    if (vmin is None) and (vmax is None):
        sns.heatmap(mat, annot=annot, fmt=fmt, cbar=cbar)
    else:
        sns.heatmap(mat, vmin=vmin, vmax=vmax, annot=annot, fmt=fmt, cbar=cbar)