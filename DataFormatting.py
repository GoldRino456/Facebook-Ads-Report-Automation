##########################################
# DataFormatting.py
# Author: Ethan H. Eastwood
# Date Last Updated: 2/8/2024
##########################################


##########################################
#Actions, Values, and Cost Per Actions come bundled in a set of data with all other possible actions.
#Method takes an array of dictionaries in the form [{'action_type':'action', 'value':'number'}, ...]
#And the desired action type you want to retrieve. Only the corresponding value will be returned.
##########################################
def extractValueFromActionType(actionArray, actionType):

    for dict in actionArray:
        if(dict["action_type"] == actionType):
            return dict["value"]

##########################################       
#Removes all of the extra information found in the title of a given Ad campaign.
#Assumes Campaign follows company campaign naming conventions.
##########################################
def removeCampaignNamingConvention(str, final_char_of_naming_convention):

    return (str[str.rfind(final_char_of_naming_convention) 
                + len(final_char_of_naming_convention):])
