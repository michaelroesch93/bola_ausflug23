import pandas as pd # needed to read data from excel file
import os  # needed to create directories
from helper_functions import * #create_new_directory
#from PIL import Image #need to include the pictures

# needed to create pdfs
from reportlab.lib.pagesizes import *
from reportlab.pdfgen import canvas

################## Script Manipulation #########################

excel_file = "puzzle_data.xlsx"
output_directory = "pdf_gen"
flag_define_passwords_for_pdfs = False

# text pdf
pagesize_text_pdf = A4
font_size_text_pdf = 18
font_name = "Helvetica"

# picture pdf
pagesize_picture_pdf = A4
path_picture_original = "kreuzlinger_meisterwerk_original.jpg"
path_picture_fake = "kreuzlinger_meisterwerk_fake.jpg"
flag_generate_pdf_with_fake = True


################################################################

def main():

    # Read the passwords from the excel file and create a dictionary
    #  with the passwords for puzzle pds
    password_data = pd.read_excel(excel_file, sheet_name = "Passwörter")
    password_dict = {}

    for index, row in password_data.iterrows():

        password_dict[str(row["Station"])] = str(row["Passwort"])

    # read the puzzle data from the excel file 
    data = pd.read_excel(excel_file)

    # get the station headers to loop later over the stations
    stations = [s for s in data.columns if 'Station_' in s]

    for index, row in data.iterrows():

        directory_name = output_directory + "/" + str(row["Nummer"]) + "_" + str(row["Deckname"])

        create_new_directory(directory_name)

        #loop over stations

        for station in stations:

            # concatenate file path
            file_path = directory_name + "/" + station + ".pdf"

            # get pdf content from data frame
            pdf_content = str(row[station])
            # Create a canvas with the specified file path and page size (letter)
        
            if pdf_content != "Bild":
                
                # generate PDF with text content
                pdf_handle = generate_pdf_with_text_content(file_path, pdf_content, pagesize_text_pdf, font_name, font_size_text_pdf)

            else:
                
                # which picture shall be used for the pdf?
                if flag_generate_pdf_with_fake:
                    path_picture = path_picture_fake
                else:
                    path_picture = path_picture_original

                pdf_handle = generate_pdf_with_picture(file_path, path_picture, pagesize_picture_pdf)

            pdf_handle.showPage()

            # set up a password for the pdf
            if flag_define_passwords_for_pdfs:
                pdf_handle.setEncrypt(row["Passwort"])

            # save pdf
            pdf_handle.save()
        
if __name__ == "__main__":
    main()
