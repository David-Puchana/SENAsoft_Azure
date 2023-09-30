#importacion de liberias custom vision
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

class ConexionCustomVision:
    # variables para la conexion
    ENDPOINT = "https://senacalidavidsebastian-prediction.cognitiveservices.azure.com/"
    prediction_key = "b1e81542f271448db4f31264b66a46d4"        
    project_id = "45ab08a3-bc97-4680-8496-48e561d2be37"
    model = "classifyModel"
    
    #creación del método de conexión        
    def conn(self):        
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.prediction_key})
        predictorConn = CustomVisionPredictionClient(self.ENDPOINT, prediction_credentials)
        return predictorConn
    