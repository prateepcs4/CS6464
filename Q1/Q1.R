library(ggpubr)

data_sa1 = readRDS('/home/prateep/Documents/CS6464/SA1/Q1/Q1_data_02.Rda')
attach(data_sa1)

cor(data_sa1, use="complete.obs", method="pearson")

ggscatter(data_sa1, x = "x1", y = "x2", add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "X1", ylab = "X2")
