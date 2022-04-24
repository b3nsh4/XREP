from github import Github
import uuid,os,sys
sys.path.append('.logs')
g = Github('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')
repo = g.get_repo("b3nsh4/XREP_BUG_REPORTS")

def init_report(vars):

   entire_line=vars[0]
   string_selected=vars[1]
   pattern_1_result=vars[2]
   pattern_2_result=vars[3]
   pattern_3_result=vars[4]
   pattern_4_result=vars[5]
   pattern_5_result=vars[6]
   pattern_6_result=vars[7]
   if string_selected!="":
      #creating new hash for the report
      x=uuid.uuid1()
      rand_uuid = x.hex
      #rand_uuid has file name
      with open('../.logs'+rand_uuid,'a+') as new:
         new.write(entire_line[0]+"\t <--entire_line\n")
         new.write(string_selected+"\t  <--selected_text\n")
         new.write(pattern_1_result+"\t <--pattern_1\n")
         new.write(pattern_2_result+"\t <--pattern_2\n")
         new.write(pattern_3_result+"\t <--pattern_3\n")
         new.write(pattern_4_result+"\t <--pattern_4\n")
         new.write(pattern_5_result+"\t <--pattern_5\n")
         new.write(pattern_6_result+"\t <--pattern_6\n")
         new.seek(0) #pointer to start of line to read
         repo.create_file(rand_uuid, "NEW REPORT",new.read(), branch="main") #file creates
      
      report_status = "Report Sent"
      notes = "Thank you very much for submitting this report, this will help to improve 𝙓𝙍𝙀𝙋 RefID for this report is:  {}".format(rand_uuid)
      os.remove('../.logs'+rand_uuid) #removing file after use
      return { "status":report_status,"notes":notes,"Ref:ID":rand_uuid}
   else:
      report_status = "Report NOT sent"
      notes = "You have not choose anything!"
      print("report NOT sent")
      return { "status":report_status,"notes":notes}