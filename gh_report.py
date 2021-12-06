import uuid
from github import Github
g = Github('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')
repo = g.get_repo("b3nsh4/EXrep_BUG_REPORT")

x=uuid.uuid1()
rand_uuid = x.hex
#creating new report file
repo.create_file(rand_uuid, "NEW REPORT", "VALUE", branch="main")