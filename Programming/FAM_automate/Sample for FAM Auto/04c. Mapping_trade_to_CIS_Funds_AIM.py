def read_file_CIS(file):
    CIS = pd.read_excel(file)
    CIS_Buy = CIS[CIS["B/S"]=="B"]
    CIS_Buy = CIS_Buy[["ISIN Number","B/S","Currency","Settlement Amount","Account","Ticket"]]
    CIS_Sell = CIS[CIS["B/S"]=="S"]
    CIS_Sell = CIS_Sell[["ISIN Number","B/S","Currency","Full trade Amount","Account","Ticket"]]
    
    return CIS_Buy,CIS_Sell

def CIS_processing_Buy(CIS,date_time_uni):
    CIS["Sender BIC"] = "SCBLSG22XSTM"
    CIS["TxnType"] = CIS["B/S"].map(lambda x: TxnType_CIS_rebalancing_AIM[x])
    CIS["ClientRef"] =  [r"AIM" + str(list(CIS["Ticket"])[i]-1) for i in range(CIS.shape[0])]
    CIS["Func"] = "NEWM"
    CIS["PreviousRef"] = ""
    CIS["TxnTypeIndicator"] = "TRAD"
    CIS["OrderType"] = "MAKT"
    CIS["OrderValidity"] = "GTCA"
    CIS["ExpiryDate"] = "29991231"
    CIS["Settdate"] = date_time_uni[:8]
    CIS["DealPriceType"] = ""
    CIS["DealPriceTypeCode"] = ""
    CIS["DealPriceCCY"] = ""
    CIS["DealPrice"] = ""
    CIS["SecScheme"] = "ISIN"
    CIS["SecId"] = CIS["ISIN Number"]
    CIS["QtyQualifier"] = "ORDR"
    CIS["Quantity"] = ""
    CIS["AmountCCY"] = CIS["Currency"]
    CIS["Amount"] = np.absolute(CIS["Settlement Amount"])
    CIS["BuyrSell"] = "SCBLSG22STM"
    CIS["BuyrSellAcc"] = CIS["Account"].map(lambda x: Account_CIS[x])
    CIS["CANCQtyQualifier"] = ""
    CIS["CANCQuantity"] = ""
    CIS["CANCAmountCCY"] = ""
    CIS["CANCAmount"] = ""
    CIS["DENOCurrency"] = ""
    CIS["DealPriceSign"] = ""
    CIS["Suppress Message To Agent"] = ""
    
    CIS_columns = ['Sender BIC', 'TxnType', 'ClientRef', 'Func', 'PreviousRef',
       'TxnTypeIndicator', 'OrderType', 'OrderValidity', 'ExpiryDate',
       'Settdate', 'DealPriceType', 'DealPriceTypeCode', 'DealPriceCCY',
       'DealPrice', 'SecScheme', 'SecId', 'QtyQualifier', 'Quantity','AmountCCY',
       'Amount', 'BuyrSell', 'BuyrSellAcc', 'CANCQtyQualifier', 'CANCQuantity',
       'CANCAmountCCY', 'CANCAmount', 'DENOCurrency', 'DealPriceSign',
       'Suppress Message To Agent','Account','B/S']
    CIS = CIS[CIS_columns]#.set_index("Sender BIC")
    
    return CIS

def CIS_processing_Sell(CIS,date_time_uni):
    CIS["Sender BIC"] = "SCBLSG22XSTM"
    CIS["TxnType"] = CIS["B/S"].map(lambda x: TxnType_CIS_rebalancing_AIM[x])
    CIS["ClientRef"] = [r"AIM" + str(list(CIS["Ticket"])[i]-1) for i in range(CIS.shape[0])]
    CIS["Func"] = "NEWM"
    CIS["PreviousRef"] = ""
    CIS["TxnTypeIndicator"] = "TRAD"
    CIS["OrderType"] = "MAKT"
    CIS["OrderValidity"] = "GTCA"
    CIS["ExpiryDate"] = "29991231"
    CIS["Settdate"] = date_time_uni[:8]
    CIS["DealPriceType"] = ""
    CIS["DealPriceTypeCode"] = ""
    CIS["DealPriceCCY"] = ""
    CIS["DealPrice"] = ""
    CIS["SecScheme"] = "ISIN"
    CIS["SecId"] = CIS["ISIN Number"]
    CIS["QtyQualifier"] = "UNIT"
    CIS["Quantity"] = np.absolute(CIS["Full trade Amount"])
    CIS["AmountCCY"] = ""
    CIS["Amount"] = ""
    CIS["BuyrSell"] = "SCBLSG22STM"
    CIS["BuyrSellAcc"] = CIS["Account"].map(lambda x: Account_CIS[x])
    CIS["CANCQtyQualifier"] = ""
    CIS["CANCQuantity"] = ""
    CIS["CANCAmountCCY"] = ""
    CIS["CANCAmount"] = ""
    CIS["DENOCurrency"] = ""
    CIS["DealPriceSign"] = ""
    CIS["Suppress Message To Agent"] = ""
    
    CIS_columns = ['Sender BIC', 'TxnType', 'ClientRef', 'Func', 'PreviousRef',
       'TxnTypeIndicator', 'OrderType', 'OrderValidity', 'ExpiryDate',
       'Settdate', 'DealPriceType', 'DealPriceTypeCode', 'DealPriceCCY',
       'DealPrice', 'SecScheme', 'SecId', 'QtyQualifier', 'Quantity','AmountCCY',
       'Amount', 'BuyrSell', 'BuyrSellAcc', 'CANCQtyQualifier', 'CANCQuantity',
       'CANCAmountCCY', 'CANCAmount', 'DENOCurrency', 'DealPriceSign',
       'Suppress Message To Agent','Account','B/S']
    CIS = CIS[CIS_columns]#.set_index("Sender BIC")
    
    return CIS

def CIS_merge(CIS_Buy,CIS_Sell,date_time_uni):
    CIS = CIS_Buy.append(CIS_Sell)
    #CIS["ClientRef"] = CIS["Account"].str[-4:]+[date_time_uni[2:-2]+str("%03d" %i) for i in range(CIS.shape[0])]+CIS["B/S"].str[:1]
    #CIS["ClientRef"] = "AIM" + str(CIS["Ticket"])

    CIS_columns = ['Sender BIC', 'TxnType', 'ClientRef', 'Func', 'PreviousRef',
       'TxnTypeIndicator', 'OrderType', 'OrderValidity', 'ExpiryDate',
       'Settdate', 'DealPriceType', 'DealPriceTypeCode', 'DealPriceCCY',
       'DealPrice', 'SecScheme', 'SecId', 'QtyQualifier', 'Quantity','AmountCCY',
       'Amount', 'BuyrSell', 'BuyrSellAcc', 'CANCQtyQualifier', 'CANCQuantity',
       'CANCAmountCCY', 'CANCAmount', 'DENOCurrency', 'DealPriceSign',
       'Suppress Message To Agent']
    CIS = CIS[CIS_columns].set_index("Sender BIC")
    CIS_FGO = CIS[CIS["BuyrSellAcc"]=="134085100002"]
    CIS_FGOPLUS = CIS[CIS["BuyrSellAcc"]=="134085200002"]
    
    return CIS,CIS_FGO,CIS_FGOPLUS



def text_output_FGO(CIS,date_time_txt):
    text = "Attn: Securities Services, Singapore" + "\n" + "\n" \
        + "Re: Mutual Fund subscription and redemption orders" + "\n" + "\n" \
        + "Please process the following mutual Fund subscription and redemption orders"  + "\n" \
        + "Order Date: " + date_time_txt + "\n" + "\n" 
    for i in range(CIS.shape[0]):
        CIS_TEXT = pd.DataFrame(CIS.iloc[i,:]).T
        #################
        text = text + "Your Securities Account Number : " + str(CIS_TEXT["BuyrSellAcc"]["SCBLSG22XSTM"]) + "\n" \
            + "Your Order Reference : " + CIS_TEXT["ClientRef"]["SCBLSG22XSTM"] + "\n" \
            + "Transaction Type : " + CIS_TEXT["TxnType"]["SCBLSG22XSTM"] + "\n" \
            + "Fund ISIN Code : " + CIS_TEXT["SecId"]["SCBLSG22XSTM"] + "\n" \
            + "Quantity : " \
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="SUBS","-",str("UNIT "+str(CIS_TEXT["Quantity"]["SCBLSG22XSTM"]))))\
            + "\n" \
            + "Order Currency : "\
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="REDM","-",CIS_TEXT["AmountCCY"]["SCBLSG22XSTM"]))+ "\n" \
            + "Order Amount or UNIT : "\
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="REDM","-",str("ORDR " + str(CIS_TEXT["Amount"]["SCBLSG22XSTM"]))))\
            + "\n" + "\n"
            
    return text

def text_output_FGOPLUS(CIS,date_time_txt):
    text = "Attn: Securities Services, Singapore" + "\n" + "\n" \
        + "Re: Mutual Fund subscription and redemption orders" + "\n" + "\n" \
        + "Please process the following mutual Fund subscription and redemption orders"  + "\n" \
        + "Order Date: " + date_time_txt + "\n" + "\n" 
    for i in range(CIS.shape[0]):
        CIS_TEXT = pd.DataFrame(CIS.iloc[i,:]).T
        #################
        text = text + "Your Securities Account Number : " + str(CIS_TEXT["BuyrSellAcc"]["SCBLSG22XSTM"]) + "\n" \
            + "Your Order Reference : " + CIS_TEXT["ClientRef"]["SCBLSG22XSTM"] + "\n" \
            + "Transaction Type : " + CIS_TEXT["TxnType"]["SCBLSG22XSTM"] + "\n" \
            + "Fund ISIN Code : " + CIS_TEXT["SecId"]["SCBLSG22XSTM"] + "\n" \
            + "Quantity : " \
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="SUBS","-",str("UNIT "+str(CIS_TEXT["Quantity"]["SCBLSG22XSTM"]))))\
            + "\n" \
            + "Order Currency : "\
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="REDM","-",CIS_TEXT["AmountCCY"]["SCBLSG22XSTM"]))+ "\n" \
            + "Order Amount or UNIT : "\
            + str(np.where(CIS_TEXT["TxnType"]["SCBLSG22XSTM"]=="REDM","-",str("ORDR " + str(CIS_TEXT["Amount"]["SCBLSG22XSTM"]))))\
            + "\n" + "\n"
               
    return text
    
    