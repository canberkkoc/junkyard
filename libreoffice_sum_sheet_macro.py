# Libre office macro for showing summaries on multiple sheets and also show general summary in one excluded sheet.

def calculate_money(x):
    doc = XSCRIPTCONTEXT.getDocument()
    active_sheet_object = doc.getCurrentController().getActiveSheet()
    code_dict = make_dictionary(doc)
    general_summary = 0
    for sheet in doc.Sheets:
      summary = 0
      i = 2
      if sheet.Name != "Excluded Sheet":
        while True:
          if sheet['A'+str(i)].getType().value == "EMPTY":
            break
          current_value = code_dict.get(sheet['A'+str(i)].getString())
          if current_value:
            sheet['B'+str(i)].setString(current_value[0])
            sheet['C'+str(i)].setValue(current_value[1])
            summary += current_value[1]
          i += 1
        sheet["E19"].setString("Summary")
        sheet["E20"].setValue(summary)
        general_summary += summary
    active_sheet_object["E19"].setString("GENERAL SUMMARY")
    active_sheet_object["E20"].setValue(general_summary)
    return


def make_dictionary(doc):
    code_dict = {} 
    i = 2
    while True:
      if doc.getCurrentController().getActiveSheet()['A'+str(i)].getType().value == "EMPTY":
        break
      code_dict[doc.getCurrentController().getActiveSheet()['A'+str(i)].getString()] = [doc.getCurrentController().getActiveSheet()['B'+str(i)].getString(),doc.getCurrentController().getActiveSheet()['C'+str(i)].getValue()]  
      i += 1
    
    return code_dict
