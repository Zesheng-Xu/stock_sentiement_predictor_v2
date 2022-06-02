def search_media(stock,date):
    date_in = datetime.datetime.strptime(date,"%Y-%m-%d")
    date_in = date_in.strftime("%m/%d/%Y")

    days = datetime.timedelta(14)
    date_start = datetime.datetime.strptime(date_in,"%m/%d/%Y") - days
    googlenews = GoogleNews(start=date_start.strftime("%m/%d/%Y"), end=date_in)
    googlenews.search("\""+stock.upper()+"\"")
    result = googlenews.result()
    for i in range(2, 3):
        googlenews.getpage(i)
        result += googlenews.result()

    df=pd.DataFrame(result)
    print(df)
    titles = df["title"].values.tolist()
    media = df["media"].values.tolist()
    return titles, media
