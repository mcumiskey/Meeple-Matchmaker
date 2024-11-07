def un_hot_encode(row):
    '''Turn one-hot-encoded data into a list'''
    return row[row == 1].index.tolist()


