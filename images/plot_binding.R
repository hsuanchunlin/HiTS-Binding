singleBinding <- function(conc, kd){
  fraction = (conc)/(kd+conc)
  return(fraction)
}
reversebinding <- function(frac,kd){
  conc = (frac*kd)/(1-frac)
  return(conc)
}

x = seq(0,10,by=0.1)
y = singleBinding(x, 1)
y1 = seq(0,.75, by=.25)
x1 = reversebinding(y1,1)
plot(x1,y1, xlab="Concentration (nM)", ylab="Binding Fraction")
lines(x,y)