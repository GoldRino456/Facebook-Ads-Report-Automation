##########################################
# Main.py
# Author: Ethan H. Eastwood
# Date Last Updated: 2/18/2024
##########################################

##########################################
#
# Required Fields
#
# This information is vital to using this application. Fill these fields before running.
# You should be able to find most of this information on Facebook's developer page.
# Ad Account IDs can be found by navigating to the ads manager, switch to the desired Ad Account, click the URL, and copy the string of text from the URL that is in this format: act_################
#
##########################################

# REQUIRED FIELDS BEFORE RUNNING
    # NOTE: You must enter your Access Token and at least one Ad Account ID before running this application.
access_token = 'Your Access Token Here'
ad_accounts = {"First Ad Account Name":'act_################'}

##########################################
#
# Additional Fields & Parameters
#
# Only edit these fields to alter search query for Campaign Data, update app information, or excel doc path.
# Altering function in imported files or further down this document could break functionality.
# Change those functions at your own risk.
#
##########################################

# Date Search - dates entered must be in 'YYYY-MM-DD' Format. 
    # NOTE: Max time range FB allows is 37 months at time of writing.
start_date = '2023-01-01' 
end_date = '2024-01-01'

#Campaign Naming Convention
    # NOTE: Used to remove extraneous text from Campaign names. If not needed, leave this field empty.
final_char_of_naming_convention = "" #EX: If Campaigns are named "EX - John Doe", put the string before "John Doe" (" - ") here to remove text before "John Doe".

#Excel
excel_document_file_path = "Sheet.xlsx"
columns_to_format = {"integer":[], "float":[]} #Data auto formats to TEXT. Insert Execl Sheet Column Number (A = 1, B = 2, etc) in either list to format data to that type.

##########################################
#
# Imports
#
##########################################

import CampaignDataCollector as dataCollector
import ExcelManager as xl

##########################################
#
# Functions
#
##########################################

#Global Variables
ad_account_id = '' #Used to rotate through the list of ad accounts, changing this variable's value here will have no effect.

##########################################
#Fetches Facebook Data and returns a list of campaigns for the given date range
##########################################
def RetrieveAndFormatFacebookData(fields, params):
    retrieved_campaigns = dataCollector.formatCampaignData(
    dataCollector.getCampaignData(fields, params), final_char_of_naming_convention)
        
    return retrieved_campaigns

##########################################
#Loads a list of campaign data into an excel document.
##########################################
def ExportToExcel(retrieved_campaigns, sheetName):
    wb = xl.OpenWorkbook(excel_document_file_path)
    ws = xl.OpenSpecificSheet(sheetName)
    xl.LoadDataToSheet(ws, retrieved_campaigns)

    if(len(columns_to_format.get("integer"))):
        print("Formatting Integer Columns...")
        
        for col in columns_to_format.get("integer"):
            xl.ConvertColumnToInt(ws, col)
    
    if(len(columns_to_format.get("float"))):
        print("Formatting Float Columns...")
        
        for col in columns_to_format.get("float"):
            xl.ConvertColumnToFloat(ws, col)

##########################################
#Switches to the Next Ad Account Data needs to be extracted from
##########################################
def SwitchAdAccountID(adAccountName):
    global ad_account_id
    ad_account_id = ad_accounts.get(adAccountName)
    dataCollector.changeAdAccountID(ad_account_id)

##########################################
#
# Main Function
#   
##########################################

if __name__ == "__main__":

    #Setup Facebook Fields / Params to Retrieve
        # NOTE: Valid fields can be found HERE: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/insights
        # Currently, if you alter these fields, you must also alter the fields stored in CampaignDataCollector.formatCampaignData()
    fields = ['campaign_id','campaign_name','spend','reach','clicks','cpc','action_values',
            'actions','cost_per_action_type']

        # NOTE: Parameters are used to limit your search. Not recommended to edit these unless you have more experience with Facebook's Graph API as this can effect which fields are available to you.
    params = {'time_range': {'since':start_date,'until':end_date},
            'level': 'campaign',}

    #Initialize and Startup
    dataCollector.InitializeFacebookAdsAPI(access_token)

    #Display Warning for User
    print("If you've input a large date range, this may take a while.")
    print("-------------------------")

    ad_account_names = ad_accounts.keys()

    for AdAccount in ad_account_names:
        print("Switching to Ad Account: " + AdAccount)
        SwitchAdAccountID(AdAccount)

        #Retrieve & Format Data
        print("Retrieving and formatting data...")
        retrieved_campaigns = RetrieveAndFormatFacebookData(fields, params)
        print("Complete!")

        #Insert Into Excel Doc
        print("Adding to Excel Document...")
        ExportToExcel(retrieved_campaigns, AdAccount)
        print("Complete!")

