import sys
 
sys.setrecursionlimit(1000000000)
class D_per:
	def __init__(self,name,years_services,company,is_drone,zip_codes):
		self.name=name
		self.years_services=years_services
		self.company=company
		self.is_drone=is_drone
		self.zip_codes=zip_codes
	def get_company(self):
	 	return(self.company)
	def set_company(self,c):
	 	self.company=c
	def get_years_services(self):
	 	return(self.years_services)
	def set_years_services(self,y):
	 	self.years_services=y
	def get_zip_codes(self):
	 	return(zip_codes)
	def set_zip_codes(self,c):
	 	self.zip_codes=c
	def recur(self,l2):
	 	
	 	l2=[i for i in l2 if self.zip_codes in i]
	 	if (len(l2)==1):
	 		l2=l2[0]
	 		print(l2)
	 	else:
	 		m=len(l2)//2
	 		h1=l2[:m]
	 		h2=l2[m:]
	 		self.recur(h1)
	 		self.recur(h2)

	 		
def main():
	sys.setrecursionlimit(2000)
	d=D_per(name="sd",years_services=4,company="ups",is_drone=True,zip_codes='20013')
	d.recur(['20016','20015','20013'])
if __name__ == '__main__':
	main()


