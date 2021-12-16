import os
import zipfile
import xmltodict
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)


class metadata_module():
    def get_meta_data(self):
        fileList = os.listdir('search_files/')
        return_array = []
        for i in range(len(fileList)):
            file_name = fileList[i]
            print(Fore.LIGHTYELLOW_EX + f'[#] get metadata {file_name}...')
            if file_name.endswith('pdf'):
                pdf_file = open(f'search_files/{file_name}', 'rb')
                pdf_data = PDFParser(pdf_file)
                doc = PDFDocument(parser=pdf_data)
                metadata_dict = doc.info[0]
                keys_array = list(metadata_dict.keys())
                value_dict = {}
                for h in range(len(keys_array)):
                    codes = ['utf-8', 'utf-16', 'windows-1251']
                    for g in range(len(codes)):
                        try:
                            value = metadata_dict[keys_array[h]].decode(codes[g])
                            break
                        except:
                            pass
                    value_dict.update({keys_array[h]: value})
                return_array.append([file_name, value_dict])
            elif file_name.endswith('docx') or file_name.endswith('pptx'):
                dict_for_return = {}
                docx_file = zipfile.ZipFile(f'search_files/{file_name}', 'r')
                core_file_xml = docx_file.read('docProps/core.xml')
                core_file_dic = xmltodict.parse(core_file_xml, encoding='utf-8')
                keys_core_file_dict = list(core_file_dic['cp:coreProperties'].keys())
                for g in range(len(keys_core_file_dict)):
                    value = core_file_dic["cp:coreProperties"][keys_core_file_dict[g]]
                    key = keys_core_file_dict[g]
                    if value is not None and str(type(value)) != "<class 'collections.OrderedDict'>" and value[0] != 'h':
                        dict_for_return.update({f'{key[key.find(":") + 1:]}': f'{value}'})

                app_file_xml = docx_file.read('docProps/app.xml')
                docx_file.close()
                app_file_dic = xmltodict.parse(app_file_xml, encoding='utf-8')
                keys_app_file_dict = list(app_file_dic['Properties'].keys())
                for g in range(len(keys_app_file_dict)):
                    value = app_file_dic["Properties"][keys_app_file_dict[g]]
                    key = keys_app_file_dict[g]
                    if value is not None and str(type(value)) != "<class 'collections.OrderedDict'>" and value[0] != 'h':
                        dict_for_return.update({f'{key[key.find(":") + 1:]}': f'{value}'})

                return_array.append([file_name, dict_for_return])
        return return_array
