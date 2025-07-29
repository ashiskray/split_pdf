import PyPDF2
# open the origional pdf in read-binary mode 
with open(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\split_pdf\merger_output.pdf","rb") as file:
    reader =PyPDF2.PdfReader(file)
    # create a new writter object 
    writer = PyPDF2.PdfWriter()
    # let's extract page 2
    for page_num in range (1,2):  # we will add page no. in range (a,b) || page number starts from 0
        writer.add_page(reader.pages[page_num])
    
    # write the selected pages into a new PDF
    with open ("split_output.pdf","wb") as output :
        writer.write(output)
    