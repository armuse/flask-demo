import requests
import simplejson as json
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show

def getData():

    #get data - future make adjustable
    function = 'TIME_SERIES_DAILY_ADJUSTED'
    symbol = 'QCOM'
    outputsize = 'compact'
    apikey = 'Q4Q8JUAPXYPNCYOF'
    address = 'https://www.alphavantage.co/query?function=' + function + \
        '&symbol=' + symbol + '&outputsize=' + outputsize + '&apikey=' + apikey

    r = requests.get(address).json()
    dates =(r['Time Series (Daily)'])

    data = pd.DataFrame.from_dict(dates)
    result = data.T
    #result['Date'] = result.index.values.tolist()
    result = result.reset_index()
    result.columns = ['Date','open','high','low','close','adjusted close',\
        'volume','divident amount','split coefficient']
    print(result)
    return result

    #result = json.loads(r.content.decode('utf-8'))


#plot data with bokeh

def plotData(data):
    output_file('test_graph.html')


def main():
    data = getData()
    plotData(data)
    #pushToApp()

if __name__=="__main__":
    main()
