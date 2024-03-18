from num import Num
class NumExtended(Num):
    def least_square_line(self, x, y):
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum([i**2 for i in x])
        sum_xy = sum([x[i]*y[i] for i in range(len(x))])
        mean_x = self.mean(x)
        mean_y = self.mean(y)
        n = len(x)

        b1 = sum_xy - (sum_x*sum_y)/n
        b2 = sum_x2 = ((sum_x)**2)/n

        b = round(b1/b2,4)
        a = round(mean_y - b*mean_x,4)
        st = '+' + str(b)+'x' if b >0 else b+'x'
        return [a,b,f'y = {a}{st}']
    
    def linear(self,a,b,x):
        return [round(a+(b*i)+ (b*i),4) for i in x]
    def quadratic(self,a,b1,b2,x):
        return [round(a+(b1*i)+(b2*i**2),4) for i in x]
    def residual(self,y,y_hat):
        return [round((y[i]-y_hat[i]),4) for i in range(len(y))]
    def SSResid(self,y,y_hat):
        return sum([(y[i] - y_hat[i])**2 for i in range(len(y))])
    def SSTo(self,y):
        y_mean = self.mean(list(y))
        return sum([(y[i]-y_mean)**2 for i in range(len(y))])
    def r_square(self,y,y_hat):
        #SSResid sum((y-y_hat)^2)
        SSResid = sum([(y[i]-y_hat[i])**2 for i in range(len(y))])
        y_mean = self.mean(list(y))
        SSto = sum([(y[i] - y_mean)**2 for i in range(len(y))])
        return round((1-(SSResid/SSto))*100,2)