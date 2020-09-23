import requests
import simplejson as json
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

#heroku app named: young-coast-81847

def getData():

    #get data - future make adjustable
    function = 'TIME_SERIES_DAILY_ADJUSTED'
    symbol = 'QCOM'
    outputsize = 'compact'
    apikey = 'Q4Q8JUAPXYPNCYOF'
    address = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={apikey}'
    r = requests.get(address).json()
    dates =(r['Time Series (Daily)'])
    print(address)
    data = pd.DataFrame.from_dict(dates)
    result = data.T
    result = result.reset_index()
    print(list(result.columns))
    result.columns = ['Date','open','high','low','close','adjusted close',\
        'volume','divident amount','split coefficient']
    result['Date'] = pd.to_datetime(result['Date'],format = '%Y-%m-%d')
    print(result)
    #possibly adjust Date to datetime
    return result

    #result = json.loads(r.content.decode('utf-8'))


#plot data with bokeh

def plotData(data):
    output_file('test_graph.html',title='test_graph',mode='cdn')

    x = data['Date']
    y0 = data['open']
    y1 = data['close']
    y2 = data['adjusted close']

    #figure out y-range
    data['high'] = pd.to_numeric(data.high)
    maxY = data['high'].max()
    data['low'] = pd.to_numeric(data.low)
    minY = data['low'].min()

    p = figure(tools = 'pan,box_zoom,reset,save', \
        y_axis_label = 'price (USD)', title = 'Stocks', \
        x_axis_label = 'Date', x_axis_type='datetime', \
        y_range = [minY, maxY])
    p.line(x, y0, legend_label = 'open')
    p.line(x, y1, legend_label = 'close', color = 'firebrick')
    p.line(x, y2, legend_label = 'adjusted close', color = 'red')

    #show(p)
    html = file_html(p, CDN, "stock ticker")
    show(p)


def main():
    data = getData()
    #plotData(data)
    #pushToApp()

if __name__=="__main__":
    main()
