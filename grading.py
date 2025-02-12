def grading(marks):
    if marks > 90:
      return "A"
    elif marks > 80:
      return "B"
    elif marks > 70:
      return "C"
    else: 
      return "Nahobo"
      
marks =int(input("Enter the marks: "))
grade = grading(marks)
    
print(f"Your grade is: {grade}")
