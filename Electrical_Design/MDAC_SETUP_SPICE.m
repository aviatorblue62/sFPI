%% MDAC Model for LTSPICEIV

clear all;
close all;
clc;

t = 0:0.0001:0.1;
vpp = 5;
Tp = 0.01;

signal = ramp(t,vpp,Tp);

% Lets make some noise!

noise = rand(1,length(signal));

MDAC = signal + 2*noise;

save('mdac_data','t','MDAC','-ascii')



plot(MDAC)
