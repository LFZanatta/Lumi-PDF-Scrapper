from src.models.scrapper_model import ScrapperModel


def test_extract_energy_data():
    text = """
    Valores Faturados
    Itens da Fatura Unid. Quant. Preço Unit Valor  (R$)  PIS/COFINS Base Calc. Aliq. ICMS Tarifa Unit.
    ICMS ICMS
    Energia Elétrica kWh       50  0,86613683        43,28  0,67479161 
    Energia SCEE s/ ICMS kWh    1.007  0,64802788       652,55  0,61569129 
    Energia compensada GD I kWh    1.007  0,61569129      -620,00  0,61569129 
    Contrib Ilum Publica Municipal          49,43
    TOTAL         125,26
    Histórico de Consumo
    MÊS/ANO Cons. kWh Média kWh/Dia Dias
    JUN/23    1.057     34,09   31
    MAI/23    1.105     36,83   30
    ABR/23    1.383     44,61   31
    MAR/23    1.581     52,70   30
    FEV/23    1.114     38,41   29
    JAN/23    1.389     43,40   32
    DEZ/22    1.251     40,35   31
    NOV/22    1.439     49,62   29
    OUT/22    1.355     42,34   32
    SET/22    1.093     36,43   30
    AGO/22      686     23,65   29
    JUL/22      843     26,34   32
    JUN/22      898     29,93   30Reservado ao Fisco
    SEM VALOR FISCAL
    Base de cálculo (R$) Alíquota (%) Valor (R$)
    Fale com CEMIG: 116 - CEMIG Torpedo 29810 - Ouvidoria CEMIG: 0800 728 3838 - Agência Nacional de Energia Elétrica - ANEEL - Telefone: 167 - Ligação gratuita de telefones fixos e móveis.
    Código de Débito Automático Instalação Vencimento Total a pagar
    008046010818 3000055479 11/07/2023 R$125,26
    Junho/2023 83650000001-0 25260138007-1 11580954433-7 08046010818-8
    ATENÇÃO:NnNnWwNwNnWnNnNwWnWwNnNnNnNnWwWwNnNnNnWwWwNnNnNnWwWwNnWnNwNnNnWwWnNwWnNnNwNnWnWwNwNnWwNwNnNnWnWnNnNwWwNnNnNnWnWwNwWwNnNnNnWwWwNnWnNwNnNnNwWnWwNnWnNnWwNnNwNwNwWnNnWnWnWnNwNwNnWnNnNwWwNnNnNwWwNnWnNwNnWnWnNwNwNnWnWwNnWwNnNnNwWnWnN DÉBITO AUTOMÁTICOPLIM TELECOMUNICACOES LTDA ME"""

    result = ScrapperModel.extract_energy_data(text)

    assert result == [{'type': ' Energia Elétrica ', 'quantity': 50.0, 'price_unit': 0.86613683, 'total_value': 43.28},
                      {'type': ' Energia SCEE s/ ICMS ', 'quantity': 1007.0, 'price_unit': 0.64802788,
                       'total_value': 652.55},
                      {'type': ' Energia compensada GD I ', 'quantity': 1007.0, 'price_unit': 0.61569129,
                       'total_value': -620.0}]
