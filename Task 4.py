exam_st_date = (11, 12, 2014)

# Print the exam start date using string formatting
# The '%i' placeholders are filled with the values from the 'exam_st_date' tuple
print("The examination will start from : %i / %i / %i" % exam_st_date)
a = int(input("write a number:"))
n1 = int("%s"% a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" %(a,a,a))
print(n1 + n2 + n3)

