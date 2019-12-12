#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import datetime
import time
from datetime import date, timedelta
from collections import Counter
import datetime
import xlwt
import xlrd
import xdrlib, sys
import inspect, os
from collections import Counter
import re

from collections import Counter

#%%
class Mapping:
    def __init__(self, BASE=None):
        self.BASE = BASE

    # in_event_type
    Event_type = {
        "CASH FEES": "CASH_FEES_BANK",
        "CFINV": "CUST_FEE_MAN",
        "FSINV": "FUND_SVCES_FEE",
        # "MGMTFEE": "MAN_FEE_MAN",
        "TRUSTEE": "TRUSTEE_FEE",
        "CREDIT INTEREST": "INT",
    }

    # Public holiday
    Pub_holiday = [
        "01/01/2019",
        "05/02/2019",
        "06/03/2019",
        "19/04/2019",
        "01/05/2019",
        "20/05/2019",
        "05/06/2019",
        "09/08/2019",
        "12/08/2019",
        "28/10/2019",
        "25/12/2019",
    ]

    # in_principal
    def in_principal(self, Acc_nm=None):  # Acc_nm是输入文件的第一列
        if "FAM GO PLUS FUND" in Acc_nm:
            return "FGOPLUS"
        elif "FAM GO FUND" in Acc_nm:
            return "FGO"

    # in_book
    def in_book(self, Acc_nm=None, currency=None):
        for i in range(len(Acc_nm)):
            if "S&R" in Acc_nm:
                return "_SNR_{}".format(currency[i])
            else:
                return "_BK"

    # in_pay_rcv
    def in_payrcv(self, inputStr=None):
        for item in inputStr:
            if item == "Credit":
                return "R"
            elif item == "Debit":
                return "P"

    # in_event_type
    def event_type_map(self, trans_detail=None, trans_ref=None, trans_ref_dic=None):
        """
        1. 以SSG+数字开头，或者前面有空格
            - transaction reference double : cash transfer
            - if not double
                - 里面有mgmtfee
                - 舍弃
        2. in
        """
        ssg_regx_start = re.compile(r"^ssg\d+", re.IGNORECASE)
        ssg_regx_middle = re.compile(r"\sssg\d+", re.IGNORECASE)
        match = re.search(ssg_regx_start, trans_detail)
        if match:
            if trans_ref_dic[trans_ref] >= 2:
                return "CASH_TFR"
            else:
                if "MGMTFEE" in trans_detail:
                    return "MAN_FEE_MAN"
                else:
                    ""
        else:
            match = re.search(ssg_regx_middle, trans_detail)
            if match:
                if trans_ref_dic[trans_ref] >= 2:
                    return "CASH_TFR"
                else:
                    if "MGMTFEE" in trans_detail:
                        return "MAN_FEE_MAN"
                    else:
                        ""
            else:
                try:
                    return [
                        v
                        for k, v in self.Event_type.items()
                        if k.lower() in trans_detail.lower()
                    ][0]
                except:
                    return ""

    def in_event_type(self, df_out=None, df_in=None):
        event_type_list = df_in["Transaction Reference"]
        trans_ref_dic = Counter(event_type_list)

        for idx in df_in.index:
            trans_detail = df_in.loc[idx, "Transaction Details"]
            trans_ref = df_in.loc[idx, "Transaction Reference"]
            df_out.loc[idx, "in_event_type"] = self.event_type_map(
                trans_detail=trans_detail,
                trans_ref=trans_ref,
                trans_ref_dic=trans_ref_dic,
            )
        return df_out

    # in_event_date
    def get_bzday(self, inputDate=None, save_format="%d/%m/%Y"):
        """
        寻找inputDate前一个工作日
        """
        PH_dateobj = []
        for dt in self.Pub_holiday:
            d, m, y = (int(i) for i in dt.split("/"))
            PH_dateobj.append(datetime.datetime(y, m, d))

        if isinstance(inputDate, str):
            day, month, year = inputDate.split("/")
            dateobj = datetime.datetime(int(year), int(month), int(day))
        elif isinstance(inputDate, datetime.datetime):
            dateobj = inputDate

        while dateobj in PH_dateobj or dateobj.isoweekday() > 5:
            dateobj += datetime.timedelta(days=1)

        # return dateobj.strftime("%d/%m/%Y")
        return dateobj.strftime(save_format)

    def processing(self, input_file=None, output_file=None, tmpt_file=None):
        df_tmpt = pd.read_csv(tmpt_file, skiprows=3)
        df_in = pd.read_excel(input_file)
        df_in = df_in.dropna(subset=["Dr / Cr Indicator"])
        df_out = pd.DataFrame(columns=df_tmpt.columns)
        # #in_principal
        df_out["#in_principal"] = df_in["Account Name"].apply(MP.in_principal)

        # in_book
        currency = [i[-3:] for i in df_in["Account Name"]]
        df_out["in_book"] = df_out["#in_principal"] + df_in["Account Name"].apply(
            MP.in_book, args=(currency,)
        )

        # in_strategy
        df_out["in_strategy"] = "NONE"

        # in_prime_broker
        df_out["in_prime_broker"] = "SCB"

        # in_pb_account
        df_out["in_pb_account"] = (
            df_out["#in_principal"] + "_" + df_out["in_prime_broker"] + "_ACCTID"
        )

        # in_pl_book_ccy_xrate
        df_out["in_pl_book_ccy_xrate"] = ""

        # in_pl_book_ccy_xrate_mdiv
        df_out["in_pl_book_ccy_xrate_mdiv"] = ""

        # in_cpty
        df_out["in_cpty"] = df_out["in_prime_broker"]

        # in_narrative
        df_out["in_narrative"] = ""

        # in_pay_rcv
        df_out["in_pay_rcv"] = df_in["Dr / Cr Indicator"].apply(self.in_payrcv)

        # in_amt
        df_out["in_amt"] = df_in["Payment Amount"]

        # in_ccy
        df_out["in_ccy"] = currency

        #
        df_out[
            [
                "in_ident_type",
                "in_ext_ident",
                "in_inst_class",
                "in_price_divisor",
                "in_type",
                "in_sec_event_id",
                "in_behaviour_type",
                "in_realise_difference_ind",
                "in_logon",
                "in_canc_amnd_ind",
                "in_cnev_id",
            ]
        ] = ""

        # in_event_type
        df_out = self.in_event_type(df_out=df_out, df_in=df_in)

        df_out["in_event_date"] = df_in["Business Date"].apply(self.get_bzday)
        df_out["in_value_date"] = df_out["in_event_date"]

        df_out.reset_index(inplace=True, drop=True)

        # a new excel
        file = xlwt.Workbook()
        # new sheet
        sheet0 = file.add_sheet("info", cell_overwrite_ok=True)
        # write data into sheet: sheet_name.write(r,col,value)
        sheet0.write(0, 0, "#!CONNECT=HK067_GNG/HK067_GNG@prod_ho3orc12_fm.world##")
        sheet0.write(0, 1, "Connected")
        sheet0.write(1, 0, "#!MAX_ERROR=1000")
        sheet0.write(2, 0, "#!OPF=TDP_LOADER_2.insert_cash_event")

        for i, col in enumerate(df_out.columns):
            sheet0.write(3, i, col)

        for i in df_out.index:
            print("-------------------------------- {}".format(i))
            for j in range(len(df_out.columns)):
                temp_value = df_out.iloc[i, j]
                print("# {} - {} - {}".format(j, temp_value, type(temp_value)))
                try:
                    if isinstance(temp_value, str):
                        sheet0.write(int(i) + 4, j, temp_value)
                    elif isinstance(temp_value, float):
                        sheet0.write(int(i) + 4, j, "")
                    elif isinstance(temp_value, type(None)):
                        sheet0.write(int(i) + 4, j, "")
                except Exception as e:
                    print(e)

        # save file
        file.save(output_file)


#%%
if __name__ == "__main__":

    BASE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    MP = Mapping(BASE=BASE)

    # yesterday = date.today() - timedelta(days=1)
#    previous_workday = MP.get_bzday(inputDate=date.today(), save_format="%d%m%Y")
#    print(previous_workday)
    # timestamp = yesterday.strftime('%Y%m%d')

    # pdf_from_email = os.path.join(BASE, "att_folder", "pdf_from_email")
    # pdf_from_email_dcrpt = os.path.join(BASE, "att_folder", "pdf_decrypt")
    # pdf_to = os.path.join(BASE, "att_folder", "pdf_to")
    # input_file = os.path.join(pdf_from_email_dcrpt, "DailyBAL_211391500.xls")

    # output_file = os.path.join(destination_folder,"DailyBAL_"+timestamp+".csv")

    input_file = os.path.join(BASE, "config_files", "DailyBAL_221034674.xls")

    # # Customize save mechanism
    output_file = os.path.join(BASE, "config_files", "output.csv")
    tmpt_file = os.path.join(
            BASE, "config_files", "cash_event_20190430interest(out).csv"
            )

    MP.processing(input_file=input_file, output_file=output_file, tmpt_file=tmpt_file)

