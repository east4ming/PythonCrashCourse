import collections

# alphbet = {
#     'if': 'if condiction. ',
#     'elif': 'behind if , like as case',
#     'for': 'do cycles'
#     }
alphbet = collections.OrderedDict()
alphbet['if'] = 'if condiction. '
alphbet['elif'] = 'behind if , like as case'
alphbet['for'] = 'do cycles'
       
for k, v in alphbet.items():
    print("`{}`: \n\t {}".format(k, v))
