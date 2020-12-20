from flask import Flask, render_template,request, redirect, url_for
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import datetime
from datetime import datetime 
import numpy as np
import pandas as pd
from decimal import *
from fbprophet import Prophet
from fbprophet.plot import plot_plotly

app=Flask(__name__)
@app.route('/')
def FER():
    return render_template('FER.html')

@app.route('/FER',methods=['GET','POST'])
def index():
    extra_line1=''
    extra_line2=''
    if request.method == 'POST':
        From=request.form['From']
        To=request.form['To']
        Amount=request.form['Amount']
        amt = Decimal(Amount)
        Date=request.form['Date']
        #dt = datetime.strptime (Date, "% Y ,% m ,% d")
        dt = pd.datetime.strptime(Date, '%d%b%y')
        c = CurrencyRates(force_decimal=True)
        result = c.convert(From, To, amt,dt)
        c = CurrencyCodes()
        code = c.get_symbol(To)
        extra_line1 = f'The Currency Converted is :{code}'
        extra_line2 = f'{result}'
    return render_template("FER.html",cd = extra_line1,new = extra_line2)

@app.route('/Japan')
def Japan():
    pd.set_option('display.max_columns', None)
    df=pd.read_csv('Japan1.csv')
    df1 = df.iloc[1:3000]
    df2 = df1[['Date' , 'Value']]
    #Renaming column names according to fb prophet
    df2.columns = ['ds' , 'y']
    m = Prophet()
    m.fit(df2)
    future = m.make_future_dataframe(periods= 10) 
    forecast = m.predict(future)
    fig = plot_plotly(m, forecast)  # This returns a plotly Figure
    fig.update_layout(
        title_text='<b>Japan Currency Exchange Rate<b>',
        title_x=0.5,
        paper_bgcolor='LightBlue',
        plot_bgcolor = "LightBlue",)
    fig.show()
    return render_template("FER.html")

@app.route('/Britain')
def Britain():
    br=pd.read_csv('Britain1.csv')
    br1 = br.iloc[1:3000]
    br2 = br1[['Date' , 'Value']]
    #Renaming column names according to fb prophet
    br2.columns = ['ds' , 'y']
    m = Prophet()
    m.fit(br2)
    future = m.make_future_dataframe(periods= 10) 
    forecast = m.predict(future)
    fig = plot_plotly(m, forecast)  # This returns a plotly Figure
    fig.update_layout(
        title_text='<b>Great Britain Currency Exchange Rate<b>',
        title_x=0.5,
        paper_bgcolor='LightPink',
        plot_bgcolor = "LightPink",)
    fig.show()
    return render_template("FER.html")

@app.route('/Canada')
def Canada():
    cn=pd.read_csv('Canada1.csv')
    cn1 = cn.iloc[1:3000]
    cn2 = cn1[['Date' , 'Value']]
    #Renaming column names according to fb prophet
    cn2.columns = ['ds' , 'y']
    m = Prophet()
    m.fit(cn2)
    future = m.make_future_dataframe(periods= 10) 
    forecast = m.predict(future)
    fig = plot_plotly(m, forecast)  # This returns a plotly Figure
    fig.update_layout(
        title_text='<b>Canada Currency Exchange Rate<b>',
        title_x=0.5,
        paper_bgcolor='palevioletred',
        plot_bgcolor = "palevioletred",)
    fig.show()
    return render_template("FER.html")

@app.route('/India')
def India():
    cn=pd.read_csv('India1.csv')
    ind1 = ind.iloc[1:3000]
    ind2 = ind1[['Date' , 'Value']]
    #Renaming column names according to fb prophet
    ind2.columns = ['ds' , 'y']
    m = Prophet()
    m.fit(ind2)
    future = m.make_future_dataframe(periods= 10) 
    forecast = m.predict(future)
    fig = plot_plotly(m, forecast)  # This returns a plotly Figure
    fig.update_layout(
        title_text='<b>Canada Currency Exchange Rate<b>',
        title_x=0.5,
        paper_bgcolor='palevioletred',
        plot_bgcolor = "palevioletred",)
    fig.show()
    return render_template("FER.html")

if __name__ == "__main__":
    app.run(debug=True)