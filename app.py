from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
import plotly.utils
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_plot', methods=['POST'])
def update_plot():
    # Get the frequency from the slider
    freq = float(request.json['frequency'])
    
    # Create the data
    x = np.linspace(0, 10, 500)
    y = np.sin(freq * x)
    
    # Create a Plotly figure
    fig = go.Figure(data=[go.Scatter(x=x, y=y, line=dict(color='firebrick', width=3))])
    fig.update_layout(title=f'Sine Wave (Frequency: {freq})',
                      xaxis_title='Time', yaxis_title='Amplitude',
                      margin=dict(l=40, r=40, t=40, b=40))

    # Convert the figure to JSON to send to the frontend
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
