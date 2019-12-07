# in_principal

def in_principal(Acc_nm): # Acc_nm是输入文件的第一列
    if 'FAM GO PLUS FUND' in Acc_nm:
        return 'FGOPLUS'
    elif 'FAM GO FUND' in Acc_nm:
        return 'FGO'
    
# 在运行 in_book function 之前要在主体里有 currency 这一列


# in_book

def in_book(Acc_nm):
    for i in range(len(Acc_nm)):
        if 'S&R' in Acc_nm:
            return "_SNR_{}".format(currency[i])
        else:
            return "_BK"
            
# df['in_book']=df['in_principal'] + df_in['Account Name'].apply(in_book)  


# in_pay_rcv

def in_payrcv(inputStr):    
    for item in inputStr:
        if item=='Credit':
            return 'R'
        elif item=='Debit':
            return 'P'
        
        
# in_pay_rcv

def in_payrcv(inputStr):    
    for item in inputStr:
        if item=='Credit':
            return 'R'
        elif item=='Debit':
            return 'P'
        
        
# in_event_type

from collections import Counter
def event_type_map(inputStr, Event_type = Event_type):
    try:
        return [v for k, v in Event_type.items() if k.lower() in inputStr.lower()][0]
    except:
        return np.nan

def in_event_type(df_out, df_in):
    df_out['in_event_type'] = df_in["Transaction Details"].apply(event_type_map)
    
    # find the one with SSG0340 in it
    SSG_boo_list = df_out['in_event_type'] == Event_type['SSG0340']
    
    # find the SSG0340 corresponding Transaction Reference
    SSG = list(df_in[SSG_boo_list]["Transaction Reference"])
    
    # check Transaction Reference with exactly 2 occurrance
    SSG_double_list = [k for k, v in list(Counter(SSG).items()) if v == 2]
    
    # filter out the one which is not in the above 2-occurrance list
    for idx in df_out[SSG_boo_list].index:
        if df_in.loc[idx, 'Transaction Reference'] not in SSG_double_list:
            df_out.loc[idx, 'in_event_type'] = np.nan
    return df_out


# in_event_date

def get_bzday(inputDate, Pub_holiday = Pub_holiday):
    PH_dateobj = []
    for date in Pub_holiday:
        d,m,y = (int(i) for i in date.split('/'))
        PH_dateobj.append(datetime.datetime(y,m,d))

    if isinstance(inputDate, str):
        day, month, year = inputDate.split('/')
        dateobj = datetime.datetime(int(year), int(month), int(day))
    elif isinstance(inputDate, datetime.datetime):
        dateobj = inputDate
        
    while dateobj in PH_dateobj or dateobj.isoweekday()>5:    
        dateobj += datetime.timedelta(days=1)
        
    return dateobj.strftime("%d%/%m%/%Y")

