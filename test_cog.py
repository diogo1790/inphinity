from configuration.configuration_api import ConfigurationAPI
from rest_client.AuthenticationRest import AuthenticationAPI


from objects_API.ProteinPFAMJ import ProteinPFAMJson

from objects_API.CogScoreJ import CogScoreJson

conf_obj = ConfigurationAPI()
conf_obj.load_data_from_ini()
AuthenticationAPI().createAutenthicationToken()


list_cog_score = CogScoreJson.getAllAPI()
print(len(list_cog_score))


print(list_cog_score[2])

cog_score_obj = CogScoreJson(score=23.4, cog_method_score=1, cog_interaction_source=1)
cog_score_obj = cog_score_obj.setCogScore()
print(cog_score_obj)