from flask import Flask , redirect , render_template , url_for
import pandas as pd
from bs4 import BeautifulSoup
import pymysql
import requests

r = requests.get("")
