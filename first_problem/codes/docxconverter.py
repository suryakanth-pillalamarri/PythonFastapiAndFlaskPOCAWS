from pdf2docx import Converter

class PDFTODOCX:
    def convert(self, pdf_file_path, docx_file_path):
        try:
            cv=Converter(pdf_file_path)
            cv.convert(docx_file_path, start=0, end=None)
            cv.close()
            return True,"Conversion successfull"
        except Exception as e:
            return False, f"Error converting to docx {e}"
        



# pdf_path=r"D:\Surya files\pythonaws_poc_2024\first_problem\inputfile\IMT2018017_example_cv.pdf"
# docx_path=r"D:\Surya files\pythonaws_poc_2024\first_problem\inputfile\IMT2018017_example_cv.docx"


# pd=PDFTODOCX()

# print(pd.convert(pdf_path,docx_path))