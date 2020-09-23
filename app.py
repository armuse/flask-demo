from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html, components

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/bokehPlot', methods=['POST'])
def bokehPlot():
    # get data
    function = 'TIME_SERIES_DAILY_ADJUSTED'
    symbol = request.form['symbol']
    outputsize = 'compact'
    apikey = 'Q4Q8JUAPXYPNCYOF'
    address = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={apikey}'
    r = requests.get(address).json()
    dates =(r['Time Series (Daily)']) #why is this failing?
    #pd.DataFrame.from_dict(r['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
    data = pd.DataFrame.from_dict(r['Time Series (Daily)'])
    result = data.T
    result['Date'] = result.index.values.tolist()
    result = result.reset_index()
    #print(list(result.columns))
    result.columns = ['index', 'open', 'high', 'low', 'close', 'adjusted close', 'volume', 'dividend amount', 'split coefficient', 'Date']
    #result.columns = ['Date','open','high','low','close','adjusted close','volume','divident amount','split coefficient']
    result['Date'] = pd.to_datetime(result['Date'],format = '%Y-%m-%d')

    p = figure(tools = 'pan,box_zoom,reset,save', \
        y_axis_label = 'price (USD)', title = symbol, \
        x_axis_label = 'Date', x_axis_type='datetime',)
    #    y_range = [minY, maxY])
    if request.form.get('open'):
        p.line(result['Date'], result['open'], legend_label = 'open')
    if request.form.get('close'):
        p.line(result['Date'], result['close'], legend_label = 'close', color = 'firebrick')
    if request.form.get('adjusted close'):
        p.line(result['Date'], result['adjusted close'], legend_label = 'adjusted close', color = 'red')

    script, div = components(p)

    return render_template('bokehPlot.html', script=script, div=div)


if __name__ == '__main__':
  app.run(port=33507)

#what port is this?
