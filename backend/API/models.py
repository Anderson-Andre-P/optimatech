from sqlalchemy import Column, Float, DateTime
from database import Base

class ProcessData(Base):
    __tablename__ = 'process_data'

    tempo = Column("Tempo", DateTime, primary_key=True, index=True)

    temperatura_entrada_multijato = Column("Temperatura de Entrada do Multijato", Float)
    temperatura_saida_multijato = Column("Temperatura de saída no multijato", Float)

    abertura_valvula_alimentacao = Column("Abertura da válvula de alimentação", Float)
    nivel_cozedor = Column("Nível do cozedor", Float)
    capacitancia_cozedor = Column("Capacitância do cozedor", Float)
    pressao_cozedor = Column("Pressão do cozedor", Float)

    abertura_valvula_alimentacao_0 = Column("Abertura da válvula de alimentação.1", Float)
    nivel_cozedor_0 = Column("Nível do cozedor.1", Float)
    capacitancia_cozedor_0 = Column("Capacitância do cozedor.1", Float)
    pressao_cozedor_0 = Column("Pressão do cozedor.1", Float)

    abertura_valvula_alimentacao_1 = Column("Abertura da válvula de alimentação.2", Float)
    nivel_cozedor_1 = Column("Nível do cozedor.2", Float)
    capacitancia_cozedor_1 = Column("Capacitância do cozedor.2", Float)
    pressao_cozedor_1 = Column("Pressão do cozedor.2", Float)

    abertura_valvula_alimentacao_2 = Column("Abertura da válvula de alimentação.3", Float)
    nivel_cozedor_2 = Column("Nível do cozedor.3", Float)
    capacitancia_cozedor_2 = Column("Capacitância do cozedor.3", Float)
    pressao_cozedor_2 = Column("Pressão do cozedor.3", Float)

    abertura_valvula_alimentacao_3 = Column("Abertura da válvula de alimentação.4", Float)
    nivel_cozedor_3 = Column("Nível do cozedor.4", Float)
    capacitancia_cozedor_3 = Column("Capacitância do cozedor.4", Float)
    pressao_cozedor_3 = Column("Pressão do cozedor.4", Float)

    abertura_valvula_alimentacao_4 = Column("Abertura da válvula de alimentação.5", Float)
    nivel_cozedor_4 = Column("Nível do cozedor.5", Float)
    capacitancia_cozedor_4 = Column("Capacitância do cozedor.5", Float)
    pressao_cozedor_4 = Column("Pressão do cozedor.5", Float)

    abertura_valvula_alimentacao_5 = Column("Abertura da válvula de alimentação.6", Float)
    nivel_cozedor_5 = Column("Nível do cozedor.6", Float)
    capacitancia_cozedor_5 = Column("Capacitância do cozedor.6", Float)
    pressao_cozedor_5 = Column("Pressão do cozedor.6", Float)

    abertura_valvula_alimentacao_6 = Column("Abertura da válvula de alimentação.7", Float)
    nivel_cozedor_6 = Column("Nível do cozedor.7", Float)
    capacitancia_cozedor_6 = Column("Capacitância do cozedor.7", Float)
    pressao_cozedor_6 = Column("Pressão do cozedor.7", Float)
