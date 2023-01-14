
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import yfinance as yf
from bs4 import BeautifulSoup
import requests

tsla = yf.Ticker('TSLA')
tesla_share_price_data = tsla.history(period='max')
tesla_share_price_data.reset_index(inplace=True)

fig = px.scatter(tesla_share_price_data, x = "Date", y = "Open", title="Tesla Open Price By Year", template='ggplot2')

first_date = tesla_share_price_data['Date'][0].date()
last_date = tesla_share_price_data['Date'][tesla_share_price_data['Date'].size - 1].date()

tesla_revenue = pd.read_csv('tesla_revenue.csv')
avg_volume_by_year = pd.read_csv('avg_volume_by_year.csv')

fig2 = px.scatter(tesla_revenue, x="Year", y="Revenue (Millions of US $)", title="Tesla Revenue by Year")
fig2.update_yaxes(autorange='reversed')

fig3 = px.line(avg_volume_by_year, x="Year", y="Average Volume", title="Average Volume by Year", markers=True, template='seaborn')


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
yahoodata = "https://finance.yahoo.com/quote/TSLA/financials"
macrotrendsdata = "https://www.macrotrends.net/stocks/charts/tsla/tesla/revenue"


 
app.layout = html.Div([
                        html.H1("Stock and Revenue Data: Tesla (TSLA)"),
                        html.H2("Tesla Share Price Data"),
                        html.Ul([
                            html.Li(f"Time Period: {first_date} - {last_date}"),
                            html.Li([f"Data Source: ", html.A(yahoodata, href=yahoodata), " and ", html.A(macrotrendsdata, href=macrotrendsdata)])
                            ]),
                        dcc.Graph(figure = fig),
                        dcc.Graph(figure = fig2),
                        html.H3("Q: What is the average trading volume per year?"),
                        dcc.Graph(figure=fig3)
                        ], style={'display': 'block', 'width': '90%', 'margin' : '5%' 'auto'})




 
if __name__ == "__main__":
    app.run_server(debug=True)