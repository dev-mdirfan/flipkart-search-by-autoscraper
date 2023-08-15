from flask import Flask, render_template, request, redirect, url_for, flash
from autoscraper import AutoScraper
import pandas as pd
import time
app = Flask(__name__)

#creating object and loading
flipkart_scraper = AutoScraper()
flipkart_scraper.load('search.json')    



@app.route('/', methods=['GET'])
def index():
    #when user search it
    if request.args.get('search'):
        #inputs
        search = request.args.get('search')
        sortby = request.args.get('sortby','relevanceblender')
        
        #call function to retrieve data
        search_data,original_url = searchquery(search, sortby)
        data_length = len(search_data)
        
        #show to user
        return render_template("index.html",data = {'original_url':original_url,'query':search, 'sortby':sortby,'searchData':search_data,'totalRecords':data_length}) 
    
    #default data_length when no search
    data_length = -1
    return render_template("index.html",data = {'query':"",'searchData':"d",'totalRecords':data_length}) 

def searchquery(search, sortby):
    #load library    

    #define url
    flipkart_url="https://www.flipkart.com/search?q={}&s={}".format(search, sortby)
    #get data
    data = flipkart_scraper.get_result_similar(flipkart_url, group_by_alias=True)

    #combine data into tuple to show it to user
    search_data = tuple(zip(data['Name'],data['Price'],data['Stars'],data['Ratings'], data['Reviews'], data['Info1'], 
                            data['Info2'], data['Info3'], data['Info4'], data['Info5'], data['Info6'], data['ImageURL']))

    #creating dataframe so that user can download it in csv format
    df = pd.DataFrame(columns=['Query','Name','Price', 'Stars', 'Ratings','Reviews', 'Info1', 'Info2', 'Info3', 'Info4', 'Info5', 'Info6',  'ImageURL'])
    for i in range(len(search_data)):
        df.loc[len(df)] = [search,search_data[i][0],search_data[i][1],search_data[i][2],search_data[i][3],
                        search_data[i][4],search_data[i][5],search_data[i][6],search_data[i][7],
                        search_data[i][8],search_data[i][9],search_data[i][10],search_data[i][11],]
    df.to_csv("data/searchedData.csv",index=False)

    #returing data
    return search_data, flipkart_url

if __name__ == '__main__':
    app.run(debug=True)

