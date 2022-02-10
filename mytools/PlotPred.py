import matplotlib.pyplot as plt
from .Color import ColorMap

def GetActionDict(mapping_path="/workspace/liukaiyuan/MS-TCN/PaddleVideo_Ms-tcn/data/gtea/mapping.txt"):
    file_ptr = open(mapping_path, 'r')
    actions = file_ptr.read().split('\n')[:-1]
    file_ptr.close()
    actions_dict = dict()
    for a in actions:
        actions_dict[a.split()[1]] = int(a.split()[0])
    return actions_dict

def GetSegmentClips(mat_1d, scale=1):
    """
    mat_1d(T)
    """
    label = [mat_1d[0]]
    start =[0]
    last_label = mat_1d[0]
    for i, _label in enumerate(mat_1d):
        if mat_1d[i] != last_label:
            label.append(mat_1d[i])
            start.append(i)
            last_label = mat_1d[i]
    idx = 0
    new_start = [0]
    for i in range(len(start[:-1])):
        idx += ((start[i+1] - start[i]) * scale)
        new_start.append(idx)
    end = new_start[1:] + [(len(mat_1d) - start[-1]) * scale + idx]
    return label, new_start, end

def PlotPred(mat_1d, ax=None, num_class=19, init_height=0, line_height=0, line_width=10,\
    scale=1, mapping_path="/workspace/liukaiyuan/MS-TCN/PaddleVideo_Ms-tcn/data/gtea/mapping.txt"):
    """
    mat_1d(T)
    """
    label, start, end = GetSegmentClips(mat_1d, scale=scale)
    rgb = ColorMap(num_class)

    if isinstance(label[0], str):
        actions_dict = GetActionDict(mapping_path)
        new_label = [actions_dict[l] for l in label]
        label = new_label

    for i in range(len(label)):
        if ax is not None:
            ax.plot([start[i] + init_height, end[i] + init_height], [line_height, line_height], linewidth=line_width, color=rgb[label[i]]) # , linewidth=10
        else:
            plt.plot([start[i] + init_height, end[i] + init_height], [line_height, line_height], linewidth=line_width, color=rgb[label[i]]) # , linewidth=10


if __name__ == '__main__':
    a = [1,1,2,2,3,3,4]
    print(GetSegmentClips(a, sacle=2))
    a = [1,1,1,1,2,2,2,2,3,3,3,3,4,4]
    print(GetSegmentClips(a))