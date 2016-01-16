%% Amplifier Setup
%-----------------------------

clear all
close all
clc
format shorteng

n = 1:16';
max_amp = 35/5;
Rin = 200e3;

Rt = Rin./n;
Ri = Rin/sum(n);
Rf = max_amp*Ri;

display(sprintf(['Feedback Resistance = ',num2str(Rf)]));

disp_table('\tn\tRin\n',[n;Rt]');

