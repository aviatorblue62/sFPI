%% Plotting FSR

clear all; close all; clc;

pd = pdf('tLocationScale','mu',3,'sigma',1,'nu',1);

med = median(pd);
r = iqr(pd);
m = mean(pd);
s = std(pd);

figure('Color',[1 1 1]);
x = -20:1:20;
y = pdf(pd,x);
plot(x,y,'LineWidth',2);