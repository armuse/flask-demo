from flask import Flask, render_template, request, redirect
import bokeh

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

open, close, adjusted close (high, low, volume)

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
