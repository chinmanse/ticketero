from fastapi.responses import Response
from starlette.status import HTTP_200_OK
import json
import inspect


@staticmethod
def dprint(*args):
  method = inspect.currentframe().f_back.f_code.co_name
  file_name = inspect.getframeinfo(inspect.stack()[1][0]).filename
  print(f'{file_name} -- {method}')
  for element in args:
    print(f" { element } ")
          

def success(data, message):
  return {
    "status_code" : HTTP_200_OK,
    "response" : data,
    "message": message        
    }
        

def error(message, code):
  response = {
    "status_code" : code,
    "response" : [],
    "message": message
  }
  return Response(
    status_code=code, 
    content=json.dumps(response), 
    headers={"Content-Type": "application/json"}
  )