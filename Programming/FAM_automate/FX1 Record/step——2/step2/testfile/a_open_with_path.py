from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    if reader.isEncrypted:
        print('need password')
        reader.decrypt(password)
        print("Number of page: {reader.getNumPages()}")
#     reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

if __name__ == '__main__':
  # example usage:
  decrypt_pdf('pdf.pdf', 'decrypted.pdf', '123456')