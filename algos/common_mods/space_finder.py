def spacer_finder(pre_or_post,stuff):  #pre2\s?(target)\s?post
  if pre_or_post=="pre":
    splitted_stuff = stuff.lstrip().split(" ")

    if splitted_stuff[-1] == "":
      space_before = True
    else:
      space_before = False
    return space_before

  elif pre_or_post=="post":
    splitted_stuff = stuff.rstrip().split(" ")
    if splitted_stuff[0] == "":
      space_after = True
    else:
      space_after = False
    return space_after