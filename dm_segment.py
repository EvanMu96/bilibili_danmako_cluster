import jieba

# danmaku word segmentation
def seg_word(dm, ouput_mode='list'):
    seg_list = jieba.cut(dm, cut_all=False)
    if ouput_mode == 'list':
        return seg_list
    elif ouput_mode == 'str':
        return ','.join(seg_list)
    else:
        raise ValueError('Invalid value of output_mode ', ouput_mode)



