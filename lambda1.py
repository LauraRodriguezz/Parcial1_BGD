import json
import boto3
import requests
import datetime
from bs4 import BeautifulSoup

client = boto3.client('s3')
BUCKET_NAME = 'parcial-bd-011'

def descargar_html():
    url = 'https://casas.mitula.com.co/searchRE/nivel2-Bogot%C3%A1/nivel1-Cundinamarca/op-1/tipo-Casa/q-Bogot%C3%A1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    html_file = "{}.html".format(datetime.datetime.now().strftime('%Y-%m-%d'))

    client.put_object(Bucket=BUCKET_NAME, Key=html_file, Body=response.content)
