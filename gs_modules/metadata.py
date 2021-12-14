import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


class metadata_module():
    def get_meta_data(self):
        fileList = os.listdir('search_files/')
        return_array = []
        for i in range(len(fileList)):
            file_name = fileList[i]
            print(f'get metadata {file_name}...')
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
                    if value != '':
                        value_dict.update({keys_array[h]: value})
                    return_array.append([file_name, value_dict])
            elif file_name.endswith('docx'):
                pass
        return return_array


