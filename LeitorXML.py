# Imports
import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Função para ler e extrair dados do XML
def ler_xml(arquivo_xml):
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()
    dados = []

    for record in root.findall('Test'):
        # Pegando os atributos da tag <Test>
        teste_id = record.get('TestId', '')
        teste_type = record.get('TestType', '')
        
        # Pegando os elementos filhos da tag <Test>
        nome = record.findtext('Name', '')
        command_line = record.findtext('CommandLine', '')
        input_ = record.findtext('Input', '')
        output = record.findtext('Output', '')
        
        # Adicionando ao dict
        dados.append((teste_id, teste_type, nome, command_line, input_, output))
    
    return dados

# Função para escrever dados em uma planilha do Excel
def escrever_planilha(dados, arquivo_excel):
    wb = Workbook()
    ws = wb.active
    ws.title = "Dados"

    ws.append(["TestId", "TestType", "Nome", "CommandLine", "Input", "Output"])

    for linha in dados:
        ws.append(linha)

    wb.save(arquivo_excel)

arquivo_xml = 'teste.xml'
arquivo_excel = 'dados.xlsx'

# Ler os dados do XML
dados = ler_xml(arquivo_xml)

# Escrever os dados na planilha do Excel
escrever_planilha(dados, arquivo_excel)

print(f"Dados extraídos do {arquivo_xml} e inseridos no {arquivo_excel} com sucesso!")
