##########################################
# CampaignDataCollector.py
# Author: Ethan H. Eastwood
# Date Last Updated: 2/18/2024
##########################################

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
import DataFormatting as format
import time

global ad_account_id
global fb_api

##########################################       
#Needed before any other functions in the Campaign Data Collector run. Connection must be established first.
##########################################
def InitializeFacebookAdsAPI(access_token):
    global fb_api
    fb_api = FacebookAdsApi.init(access_token=access_token, timeout=120)

##########################################       
#Switches the Ad Account ID from which to pull data.
##########################################
def changeAdAccountID(new_ID):
    global ad_account_id
    ad_account_id = new_ID

##########################################       
#Fetches Campaign Data from Facebook for a given range of time
#CRUD Object returned will iterate through campaigns in chunks of 25, so there may be a slight delay when iterating through the object
#if you have a large number of campaigns to sift through.
##########################################
def getCampaignData(fields, params):

    bulk_FB_Campaign_Data = AdAccount(ad_account_id).get_insights(fields=fields, params=params)
    return bulk_FB_Campaign_Data

##########################################       
#Creates an array of dictionaries, each holding data for a specific campaign.
    # NOTE: If you altered the fields in Main.py, alter the fields here as well.
##########################################
def formatCampaignData(campaignData, final_char_of_naming_convention):

    retrieved_campaigns = []

    for campaign in campaignData:
    
        

        try:
            dates = getCampaignStartStopTimes(campaign["campaign_id"])

            entryToAdd = {
            "campaign_name": format.removeCampaignNamingConvention(campaign["campaign_name"], final_char_of_naming_convention),
            "spend": campaign["spend"],
            "reach": campaign["reach"],
            "clicks": campaign["clicks"],
            "cpc": campaign["cpc"],
            "purchases": format.extractValueFromActionType(campaign["actions"], "purchase"),
            "purchase_value": format.extractValueFromActionType(campaign["action_values"], "purchase"),
            "cpp": format.extractValueFromActionType(campaign["cost_per_action_type"], "purchase"),
            "date_start": dates[0],
            "date_stop": dates[1]
            }

            print("Importing: " + entryToAdd["campaign_name"])
            retrieved_campaigns.append(entryToAdd)
            time.sleep(0.05)
    
        except:
            time.sleep(0.05)
            continue

    return retrieved_campaigns

##########################################       
#Gets the Campaign Object (not just the data) from the campaign's ID#.
    #Returns the Start and Stop time of a given campaign (this isn't included in Campaign Insights, so must be retrieved from the Campaign Object)
##########################################
def getCampaignStartStopTimes(campaign_id):
    
    try:
        response = (FacebookAdsApi.call(self= fb_api, method='GET',path= str("https://graph.facebook.com/v18.0/" + str(campaign_id) + "?fields=start_time,stop_time")))
        campaignDates = [response.json()['start_time'][:10], response.json()['stop_time'][:10]]
        return campaignDates
    except:
        return ["", ""]
    