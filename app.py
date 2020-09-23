from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

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
    print(address)
    r = requests.get(address).json()
#    dates =(r['Time Series (Daily)'])

#    data = pd.DataFrame.from_dict(dates)
#    result = data.T
    #result['Date'] = result.index.values.tolist()
#    result = result.reset_index()
#    result.columns = ['Date','open','high','low','close','adjusted close',\
#        'volume','divident amount','split coefficient']
#    result['Date'] = pd.to_datetime(result['Date'],format = '%Y-%m-%d')
    #print(result)
#    x = data['Date']
#    y0 = data['open']
#    y1 = data['close']
#    y2 = data['adjusted close']

#    data['high'] = pd.to_numeric(data.high)
#    maxY = data['high'].max()
#    data['low'] = pd.to_numeric(data.low)
#    minY = data['low'].min()

#    p = figure(tools = 'pan,box_zoom,reset,save', \
#        y_axis_label = 'price (USD)', title = 'Stocks', \
#        x_axis_label = 'Date', x_axis_type='datetime', \
#        y_range = [minY, maxY])
#    if request.form.get('open'):
#        p.line(data['Date'], data['open'], legend_label = 'open')
#    if request.form.get('close'):
#        p.line(data['Date'], data['close'], legend_label = 'close', color = 'firebrick')
#    if request.form.get('adjusted close'):
#        p.line(data['Date'], data['adjusted close'], legend_label = 'adjusted close', color = 'red')
#    html = render_template('bokehPlot.html',)
    return render_template('bokehPlot.html')

#open, close, adjusted close (high, low, volume)

#@app.route('/bokeh')
#def bokeh():
#    fig = figure(plot_width=600, plot_height=600)
#    fig.vbar(x=[1, 2, 3, 4],width=0.5,bottom=0,top=[1.7, 2.2, 4.6, 3.9])
#    js_resources = INLINE.render_js()
#    css_resources = INLINE.render_css()
#    script, div = components(fig)
#    html = render_template(
#        'index.html',
#        plot_script=script,
#        plot_div=div,
#        js_resources=js_resources,
#        css_resources=css_resources,)
#    return encode_utf8(html)

if __name__ == '__main__':
  app.run(port=33507)

#what port is this?
