#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[8]:


def read_file(file):
    df_in = pd.read_excel(file)
    return df_in


# In[9]:


# in_principal

def in_principal(Acc_nm): # Acc_nm是输入文件的第一列
    if 'FAM GO PLUS FUND' in Acc_nm:
        return 'FGOPLUS'
    elif 'FAM GO FUND' in Acc_nm:
        return 'FGO'


# In[ ]:


# 在运行 in_book function 之前要在主体里有 currency 这一列


# In[10]:


# in_book

def in_book(Acc_nm):
    for i in range(len(Acc_nm)):
        if 'S&R' in Acc_nm:
            return "_SNR_{}".format(currency[i])
        else:
            return "_BK"
            
# df['in_book']=df['in_principal'] + df_in['Account Name'].apply(in_book)         


# In[11]:


# in_pay_rcv

def in_payrcv(inputStr):    
    for item in inputStr:
        if item=='Credit':
            return 'R'
        elif item=='Debit':
            return 'P'


# In[1]:


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


# In[27]:


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



# In[12]:


def df_output_process(df_out,df_in):
    df_out['#in_principal'] = df_in['Account Name'].apply(in_principal)
    currency=[i[-3:] for i in df_in['Account Name']]
    df_out['in_book'] = df_out['#in_principal'] + df_in['Account Name'].apply(in_book)
    df_out['in_strategy'] = 'NONE'
    df_out['in_prime_broker'] = 'SCB'
    df_out['in_pb_account'] = df_out['#in_principal'] + '_' + df_out['in_prime_broker'] + '_ACCTID' 
    df_out['in_pl_book_ccy_xrate'] = ''
    df_out['in_pl_book_ccy_xrate_mdiv'] = ''
    df_out['in_cpty'] = df_out['in_prime_broker']
    df_out['in_narrative'] = ''
    df_out['in_pay_rcv'] = df_in['Dr / Cr Indicator'].apply(in_payrcv)
    df_out['in_amt'] = df_in['Payment Amount']
    df_out['in_ccy'] = currency
    df_out[['in_ident_type',
       'in_ext_ident', 'in_inst_class', 'in_price_divisor', 'in_type',
       'in_sec_event_id', 'in_behaviour_type', 'in_realise_difference_ind',
       'in_logon', 'in_canc_amnd_ind', 'in_cnev_id']] = ''
    df_out = in_event_type(df_out = df_out, df_in = df_in)
    df_out['in_event_date'] = df_in['Business Date'].apply(get_bzday)
    df_out['in_value_date'] = df_out['in_event_date']

   # df_out.reset_index(inplace=True, drop = True)
    df_out_columns = ['#in_principal', 'in_book', 'in_strategy', 'in_prime_broker',
       'in_pb_account', 'in_pl_book_ccy_xrate', 'in_pl_book_ccy_xrate_mdiv',
       'in_cpty', 'in_event_type', 'in_narrative', 'in_pay_rcv', 'in_amt',
       'in_ccy', 'in_event_date', 'in_value_date', 'in_ident_type',
       'in_ext_ident', 'in_inst_class', 'in_price_divisor', 'in_type',
       'in_sec_event_id', 'in_behaviour_type', 'in_realise_difference_ind',
       'in_logon', 'in_canc_amnd_ind', 'in_cnev_id']
    
    df_out = df_out[df_out_columns]
    #df_out.reset_index(inplace=True, drop = True)
    
    return df_out


# In[20]:


import datetime
import time
date_time = datetime.datetime.now().strftime("%Y%m%d")
csv_name = 'cash_event_'+date_time +'.csv'
def add_data(book):
    book.write(0,0,'#!CONNECT=HK067_GNG/HK067_GNG@prod_ho3orc12_fm.world##')
    book.write(0,1,'Connected') 
    book.write(1,0,'#!MAX_ERROR=1000')
    book.write(2,0,'#!OPF=TDP_LOADER_2.insert_cash_event')
        # save file 
    new_book.save('new_book.xls')
    new_csv =pd.read_excel('new_book.xls')
    new_csv_file = pd.DataFrame.to_csv(new_csv, csv_name, index=False)
    return new_csv_file


# In[16]:


def merge(t,z):
    with open(t,'ab') as f:
        f.write(open(z,'rb').read())                                          
    return t


# In[ ]:




