'''
Created on Sep 26, 2012

@author: Luis de Sousa [luis.desousa@tudor.lu]

Contains the WPS XML tags needed to parse the outputs of a WPS process. 
'''

###########################################################

class Tags:
    
    preRef  = "<wps:Reference"
    midRef  = "wps:Reference href=\""
    preId   = "<ows:Identifier>"
    sufId   = "</ows:Identifier>"
    preLit  = "<wps:LiteralData>"
    sufLit  = "</wps:LiteralData>"
    preCplx = "<wps:ComplexData"
    sufCplx = "</wps:ComplexData>"
    preAck  = "<wps:ProcessAccepted>"
    preFail = "<wps:ProcessFailed>"
    sufFail = "</wps:ProcessFailed>"
    preSucc = "<wps:ProcessSucceeded>"
    preOut  = "<wps:Output>"
    prStart = "</wps:ProcessStarted>"
