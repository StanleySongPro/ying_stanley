lagged_day = {"HK":2,
              "AU":2,
              "AT":2,
              "CH":2,
              "JP":2,
              "NZ":2,
              "SP":3,
              "TB":2,
              "PM":2,
              "MK":2,
              "US":2,
              "UK":2,
              "LN":2,
              "TW":2,
              "KR":2,
              "ID":2,
              "FP":2,
              "KY":2
}

week_lag  =  {"Mon":0,
              "Tue":0,
              "Wed":0,
              "Thu":0,
              "Fri":0,
              "Sat":2,
              "Sun":1
}

total_lag = {1:1,
 2:2,
 3:3,
 4:4,
 5:5,
 6:6,
 7:7,
 8:8,
 9:9    
}

# Trade Confirmation
Buy_Sell = {"Subscription":"SUBS",
            "Redemption":"REDM"}


Fund_name = {2188:"FGOPLUS",
             2191:"FGO"}

Fund_name_AIM_str = {"134085200002":"FGOPLUS",
             "134085100002":"FGO"}

Fund_name_AIM = {134085200002:"FGOPLUS",
             134085100002:"FGO"}

Pb_account = {"FGOPLUS": "134085200002",
              "FGO": "134085100002"}

Pb_account_AIM = {"FGOPLUS": "FGOPLUS_SCB_ACCT_ID",
              "FGO": "FGO_SCB_ACCT_ID"}

Buy_Sell_EMSX = {"Buy":"B",
                 "Sell":"S"}

Broker_EMSX = {"SCB":"SCB",
               "IBKR":"IB",
               "DBS":"DBS",
               "APEX":"APEX",
               "BDSK":"TB",
               "OCBC":"OCBC",
               "TEST_PB":"TEST_PB"}

Account_EMSX = {"FAMASVFD":"FAF"}

############ 04. CIS
TxnType_CIS = {"B":"SUBS",
               "S":"REDM"}

Account_CIS = {"FGOPLUS": "134085200002",
              "FGO": "134085100002"}

TxnType_CIS_rebalancing = {"BUY":"SUBS",
               "SELL":"REDM"}

TxnType_CIS_rebalancing_AIM = {"B":"SUBS",
               "S":"REDM"}