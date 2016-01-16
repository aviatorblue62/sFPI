%% Data Simulation
%
% For analyzing the output of a photodetector using a python GUI a "live
% data set is necessary to determine the programs functionality.

freq = 3;
cycles = 5;
duration = cycles/freq;
bits_per_scan = 1024;

%% Sawtooth Function
%
% Current speed for this function is 3 Hz (a refresh rate of 1/3 s). The
% voltage of the ramp function will tranlate to calibrated values based on
% the current driver configuration. Range of 0-30V is the goal, however I
% have only achieved 0-10V with the current configuration. Other
% configuraitons are being examined.

function_time = linspace(0,duration,cycles*bits_per_scan);
ramp_function = 5*sawtooth(3*(2*pi*function_time),1);
sample_time = function_time;

ramp.time = sample_time;
ramp.output = ramp_function;

%% Photodetector Output
%
% Data collection will be Gaussian white noise along with two Sinc function
% which will pose as the modes of the laser.

bits = bits_per_scan;
noise = rand(1,length(ramp.time));
mode1 = sin(3*(2*pi*function_time))+0.5;

figure('Color',[1 1 1]);
plot(mode1)

photo.signal = mode1;
photo.time = ramp.time;

%% Plotting

figure('Color',[1 1 1]);
subplot(2,1,1);
plot(ramp.time,ramp.output);
subplot(2,1,2);
plot(photo.time,photo.signal);

M = [ramp.output;photo.signal];

csvwrite('photodiode_output',M);

