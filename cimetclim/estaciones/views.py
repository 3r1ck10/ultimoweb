from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def estaciones(request):
    return render(request,"estaciones/estaciones.html")

import plotly
import plotly.graph_objs as go
import pandas as pd
class Plot2DView(TemplateView):

    template_name = "estaciones/estaciones.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot2DView, self).get_context_data(**kwargs)
        datos=pd.read_csv('datos.csv')
        uno=list(datos['uno'].values)
        dos=list(datos['dos'].values)
        datos=[go.Scatter(x=uno, y=dos)]
        layouts=go.Layout(title="Temperatura de los ultimos 7 días")
        figura=go.Figure(data=datos,layout=layouts)
        div=plotly.offline.plot(figura,auto_open=False,output_type='div',config={'displaylogo':False},show_link=False)

        datos=[go.Scatter(x=list(pd.date_range(start='21-11-11',freq='d',periods=7).strftime('%Y-%m-%d')), y=[13, 14, 11, 13,15,16,15])]
        layouts=go.Layout(title="Temperatura de los ultimos 7 días")
        figura=go.Figure(data=datos,layout=layouts)
        div2=plotly.offline.plot(figura,auto_open=False,output_type='div',config={'displaylogo':False},show_link=False)

        datos=[go.Scatter(x=list(pd.date_range(start='21-11-11',freq='d',periods=7).strftime('%Y-%m-%d')), y=[21, 23, 24, 21,22,24,21])]
        layouts=go.Layout(title="Temperatura de los ultimos 7 días")
        figura=go.Figure(data=datos,layout=layouts)
        div3=plotly.offline.plot(figura,auto_open=False,output_type='div',config={'displaylogo':False},show_link=False)

        datos=[go.Scatter(x=list(pd.date_range(start='21-11-11',freq='d',periods=7).strftime('%Y-%m-%d')), y=[17, 16, 15, 17,15,17,18])]
        layouts=go.Layout(title="Temperatura de los ultimos 7 días")
        figura=go.Figure(data=datos,layout=layouts)
        div4=plotly.offline.plot(figura,auto_open=False,output_type='div',config={'displaylogo':False},show_link=False)

        context['graph'] = div
        context['graph2']= div2
        context['graph3']= div3
        context['graph4']= div4
        return context
