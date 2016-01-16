%% Resloution testing of a 12 bit DAC 
% With assumed max voltage values

clc
clear all
close all
% There are only 0 to 127 possible addresses for values.
% However the bit resolution 
clock_hz = 8; % in MHz
bits = 12; % amount of data bits
vmax = 5; % Volts
posbits = 2^bits; % bits/volt
vd = input('Enter Desired Peak Voltage: ');
freq = input('Enter Desired Frequency: ');
div = freq/clock_hz;
maxbs = vd*posbits/vmax; % bits
n = 0:(maxbs - 1); 
t = linspace(0,(maxbs-1),(div*clock_hz*maxbs)); % n in .125 us steps
t_out = t./(div*clock_hz*maxbs);
sh = 1/clock_hz; % for 8 Mhz clock
output = zeros(posbits,length(t));
t0 = t(1);

for k = 1:maxbs
    for y = 1:length(t)
        if t(y) < (sh + t0) && t(y) >= t0 
            output(k,y) = n(k)*vmax/posbits;
        else
            output(k,y) = 0;
        end
    end
    t0 = t0 + sh;
end

ramp = sum(output);

stairs(t_out,ramp,'b.');
xlabel('samples');
ylabel('Voltage (V)');
title('DAC Output Sampling');

