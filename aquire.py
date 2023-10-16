def new_titanic_data(sql_query):
    """
    this function will :
    -take in a SQL query
    -create a connection url(get_db_url)
    -it will return a df of the given query from the titanic_db
     """
    #create conncetion url
    url = get_db_url('titanic_db')
    
    return pd.read_sql(sql_query, url)


def get_iris_data(sql_query):
    """
    this function will :
    -take in a SQL query
    -create a connection url(get_db_url)
    -it will return a df of the given query from the iris_db
     """
    #create conncetion url
    url = get_db_url('iris_db')
    
    return pd.read_sql(sql_query, url)


def get_telco_data(sql_query):
    """
    this function will :
    -take in a SQL query
    -create a connection url(get_db_url)
    -it will return a df of the given query from the telco_churn
     """
    #create conncetion url
    url = get_db_url('telco_churn')
    
    return pd.read_sql(sql_query, url)


def new_titanic_data(sql_query,directory, filename = 'titanic.csv'):
    """
    This function wll:
    -check local directory for csv file
    -return df if file exists
    -if csv does not exist:
    -it will create a df of the sql query 
    -and it will write the df to a csv file
    - output titanic df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = get_titanic_data(sql_query)
        
        df.to_csv(filename)
        return df
    
    def new_get_iris_data(sql_query, directory, filename ='iris.csv'):
    """
    This function wll:
    -check local directory for csv file
    -return df if file exists
    -if csv does not exist:
    -it will create a df of the sql query 
    -and it will write the df to a csv file
    - output iris df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = get_iris_data(sql_query)
        
        df.to_csv(filename)
        return df
    
    def new_telco_data(sql_query, directory, filename = 'telco.csv'):
    """
    This function wll:
    -check local directory for csv file
    -return df if file exists
    -if csv does not exist:
    -it will create a df of the sql query 
    -and it will write the df to a csv file
    - output telco df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = get_telco_data(sql_query)
        
        df.to_csv(filename)
        return df