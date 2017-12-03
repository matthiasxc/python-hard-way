# 30 year mortgage of $300,000 at 5%
print("A mortgage of $300,000 at 5 percent for 30 years")
print(300000.0*((.05/12.0)*(1.0 + .05/12.0)**(30.0*12.0)/(((1.0 + (.05/12.0))**(30.0*12.0)) -1.0)))
