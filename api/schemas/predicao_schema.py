from pydantic import BaseModel

class PredicaoSchema(BaseModel):
    """ Define como a solicitação de uma predição deve ser representada
    """
    ccateg: str = "Arts"
    timesp: float = 54.58
    nvideo: int = 10
    nquizz: int = 29
    qscore: float = 50.36
    corate: float = 20.86
    device: int = 1
    
    
class PredicaoViewSchema(BaseModel):
    predicao: int