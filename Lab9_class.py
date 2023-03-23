'''
Lab 9
Class in Python
3/23/2023
'''
#2
class my_stat():
    def cal_sigma(self,m,n):
        result = 0 
        for i in range(n,m+1):
            result = result + i
        return (result)
        
    def cal_pi(self,m,n):
        result = 1
        for i in range(n,m+1):
            result = result * i
        return (result)
        
    def cal_fac(self, m):
        if m == 0:
            return 1
        else:
            return m*self.cal_fac(m-1)
        
    def cal_p(self,m,n):
        return self.cal_fac(m)/self.cal_fac(m-n)
