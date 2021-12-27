def does_pre_post_exist(whatever):
	splitted = whatever.split()

	if len(splitted)>=1:
		exist = True
	else:
		exist= False
	return exist

print(does_pre_post_exist("cu"))