from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))

class Post(Base):
    __tablename__ = 'posts'

    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String(40))
    content = Column(String(40))
    user_id = Column(Integer)

class ProcessData(Base):
    __tablename__ = 'process_data'

    tempo = Column("Tempo", DateTime,  primary_key=True, index=True)

    temperatura_entrada_multijato = Column("Temperatura de Entrada do Multijato", String)
    temperatura_saida_multijato = Column("Temperatura de saída no multijato", String)

    abertura_valvula_alimentacao = Column("Abertura da válvula de alimentação", String)
    nivel_cozedor = Column("Nível do cozedor", String)
    capacitancia_cozedor = Column("Capacitância do cozedor", String)
    pressao_cozedor = Column("Pressão do cozedor", String)

    abertura_valvula_alimentacao_0 = Column("Abertura da válvula de alimentação_[0]", String)
    nivel_cozedor_0 = Column("Nível do cozedor_[0]", String)
    capacitancia_cozedor_0 = Column("Capacitância do cozedor_[0]", String)
    pressao_cozedor_0 = Column("Pressão do cozedor_[0]", String)

    abertura_valvula_alimentacao_1 = Column("Abertura da válvula de alimentação_[1]", String)
    nivel_cozedor_1 = Column("Nível do cozedor_[1]", String)
    capacitancia_cozedor_1 = Column("Capacitância do cozedor_[1]", String)
    pressao_cozedor_1 = Column("Pressão do cozedor_[1]", String)

    abertura_valvula_alimentacao_2 = Column("Abertura da válvula de alimentação_[2]", String)
    nivel_cozedor_2 = Column("Nível do cozedor_[2]", String)
    capacitancia_cozedor_2 = Column("Capacitância do cozedor_[2]", String)
    pressao_cozedor_2 = Column("Pressão do cozedor_[2]", String)

    abertura_valvula_alimentacao_3 = Column("Abertura da válvula de alimentação_[3]", String)
    nivel_cozedor_3 = Column("Nível do cozedor_[3]", String)
    capacitancia_cozedor_3 = Column("Capacitância do cozedor_[3]", String)
    pressao_cozedor_3 = Column("Pressão do cozedor_[3]", String)

    abertura_valvula_alimentacao_4 = Column("Abertura da válvula de alimentação_[4]", String)
    nivel_cozedor_4 = Column("Nível do cozedor_[4]", String)
    capacitancia_cozedor_4 = Column("Capacitância do cozedor_[4]", String)
    pressao_cozedor_4 = Column("Pressão do cozedor_[4]", String)

    abertura_valvula_alimentacao_5 = Column("Abertura da válvula de alimentação_[5]", String)
    nivel_cozedor_5 = Column("Nível do cozedor_[5]", String)
    capacitancia_cozedor_5 = Column("Capacitância do cozedor_[5]", String)
    pressao_cozedor_5 = Column("Pressão do cozedor_[5]", String)

    abertura_valvula_alimentacao_6 = Column("Abertura da válvula de alimentação_[6]", String)
    nivel_cozedor_6 = Column("Nível do cozedor_[6]", String)
    capacitancia_cozedor_6 = Column("Capacitância do cozedor_[6]", String)
    pressao_cozedor_6 = Column("Pressão do cozedor_[6]", String)
