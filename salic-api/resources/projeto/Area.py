from ..result_format import get_formated, to_json
from flask_restful import Api
from database.QueryHandler import QueryHandler
from flask import Response
from ..ResourceBase import *

class Area(ResourceBase):
    
    def __init__(self):
       pass
        
    
    def get(self):
        
        try:
            result = self.query_handler.get_area()
        except:
            result = {'message' : 'internal error',
                                 'message_code' : 13,
                      }
            
            return self.result_return(result, status_code = 503)   

        
       
     
        return self.result_return(result)
    
