class student():
    faculty="CSIT" #Class attribute
    def fac(self):
        print(f"Faculty = {self.faculty}")
    def subj(self):
        print(f"Subject = {self.subject}")

detail=student()
detail.fac()

detail.faculty='BSc. CSIT' #Instance attribute
detail.subject='python'
detail.fac()
detail.subj()