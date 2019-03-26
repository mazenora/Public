import students_pkg.all_courses as courses

def enroll(course_name):
    if course_name in courses.ava_courses:
        print("You can enroll in",course_name)
    else:
        print("This course is not available!!",course_name)
